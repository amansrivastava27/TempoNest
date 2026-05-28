from django.shortcuts import render
from properties.models import Property
from django.db.models import Q


from django.shortcuts import render

from properties.models import Property


def dashboard(request):

    properties = Property.objects.filter(
        available=True
    )

    search = request.GET.get('search')

    category = request.GET.get('category')

    # SEARCH BY CITY OR LOCATION

    if search:

        properties = properties.filter(
            city__icontains=search
        )

    # FILTER BY CATEGORY

    if category:

        properties = properties.filter(
            category=category
        )

    context = {

        'properties': properties

    }

    return render(
        request,
        'home/dashboard.html',
        context
    )


def about(request):

    return render(request,
                  'home/about.html')


def contact(request):

    return render(request,
                  'home/contact.html')


def services(request, category):

    properties = Property.objects.filter(
        category__iexact=category
    )

    context = {
        'properties': properties,
        'category': category
    }

    return render(request,
                  'home/services.html',
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

    return render(
        request,
        'home/search.html',
        context
    )