from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm, BookingForm
from .models import Property, Booking, Payment
from django.db.models import Q
from django.contrib import messages
import razorpay
from django.conf import settings


@login_required
def add_property(request):

    if not request.user.is_staff:

        messages.error(
            request,
            'Only property owners can add listings.'
        )

        return redirect('dashboard')

    if request.method == 'POST':

        form = PropertyForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            property = form.save(commit=False)

            property.owner = request.user

            property.save()

            messages.success(
                request,
                'Property Added Successfully'
            )

            return redirect('dashboard')

    else:

        form = PropertyForm()

    context = {
        'form': form
    }

    return render(
        request,
        'properties/add_property.html',
        context
    )


@login_required
def edit_property(request, property_id):

    property = get_object_or_404(
        Property,
        id=property_id,
        owner=request.user
    )

    form = PropertyForm(
        request.POST or None,
        request.FILES or None,
        instance=property
    )

    if form.is_valid():

        form.save()

        return redirect(
            'owner_dashboard'
        )

    context = {

        'form': form

    }

    return render(
        request,
        'properties/edit_property.html',
        context
    )


@login_required
def delete_property(request, property_id):

    property = get_object_or_404(
        Property,
        id=property_id,
        owner=request.user
    )

    property.delete()

    return redirect(
        'owner_dashboard'
    )


@login_required
def my_properties(request):

    properties = Property.objects.filter(
        owner=request.user
    )

    context = {
        'properties': properties
    }

    return render(request,
                  'properties/my_properties.html',
                  context)


def property_detail(request, id):

    property = get_object_or_404(
        Property,
        id=id
    )

    context = {
        'property': property
    }

    return render(request,
                  'properties/property_detail.html',
                  context)




def search(request):

    query = request.GET.get('q')

    properties = Property.objects.filter(

        Q(title__icontains=query) |

        Q(city__icontains=query) |

        Q(category__icontains=query)

    )

    context = {
        'properties': properties,
        'query': query
    }

    return render(request,
                  'home/search.html',
                  context)


@login_required
def book_property(request, id):

    property = Property.objects.get(id=id)

    if request.method == 'POST':

        form = BookingForm(
            request.POST
        )

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user

            booking.property = property

            booking.save()

            return redirect('dashboard')

    else:

        form = BookingForm()

    context = {
        'form': form,
        'property': property
    }

    return render(
        request,
        'properties/book_property.html',
        context
    )


@login_required
def owner_bookings(request):

    bookings = Booking.objects.filter(
        property__owner=request.user
    )

    context = {
        'bookings': bookings
    }

    return render(
        request,
        'properties/owner_bookings.html',
        context
    )


@login_required
def accept_booking(request, id):

    booking = Booking.objects.get(id=id)

    booking.status = 'Accepted'

    booking.save()

    return redirect('owner_bookings')


@login_required
def reject_booking(request, id):

    booking = Booking.objects.get(id=id)

    booking.status = 'Rejected'

    booking.save()

    return redirect('owner_bookings')


@login_required
def owner_dashboard(request):

    properties = Property.objects.filter(
        owner=request.user
    )

    total_properties = properties.count()

    total_bookings = Booking.objects.filter(
        property__owner=request.user
    ).count()

    pending_bookings = Booking.objects.filter(
        property__owner=request.user,
        status='Pending'
    ).count()

    context = {

        'properties': properties,

        'total_properties': total_properties,

        'total_bookings': total_bookings,

        'pending_bookings': pending_bookings,

    }

    return render(
        request,
        'properties/owner_dashboard.html',
        context
    )


@login_required
def payment_page(request, booking_id):

    booking = Booking.objects.get(id=booking_id)

    amount = 500 * 100

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({

        'amount': amount,

        'currency': 'INR',

        'payment_capture': '1'

    })

    context = {

        'booking': booking,

        'payment': payment,

        'razorpay_key': settings.RAZORPAY_KEY_ID,

        'amount': amount

    }

    return render(
        request,
        'properties/payment.html',
        context
    )


@login_required
def payment_success(request):

    if request.method == "POST":

        order_id = request.POST.get(
            'razorpay_order_id'
        )

        payment_id = request.POST.get(
            'razorpay_payment_id'
        )

        signature = request.POST.get(
            'razorpay_signature'
        )

        booking_id = request.POST.get(
            'booking_id'
        )

        booking = Booking.objects.get(
            id=booking_id
        )

        client = razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            )
        )

        params_dict = {

            'razorpay_order_id': order_id,

            'razorpay_payment_id': payment_id,

            'razorpay_signature': signature

        }

        try:

            client.utility.verify_payment_signature(
                params_dict
            )

            Payment.objects.create(

                booking=booking,

                razorpay_order_id=order_id,

                razorpay_payment_id=payment_id,

                razorpay_signature=signature,

                amount=500,

                paid=True

            )

            return render(
                request,
                'properties/payment_success.html'
            )

        except:

            return render(
                request,
                'properties/payment_failed.html'
            )