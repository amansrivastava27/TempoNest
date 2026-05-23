from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm
from .models import Property
from django.db.models import Q
from django.contrib import messages


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