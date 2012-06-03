from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from pygeocoder import Geocoder
from django.conf import settings
from .models import Image, Shape
import simplejson

def arbor_index(request):
    pass


def arbor_api_geocode(request):
    """
    Returns coordinates of a given address
    """
    address = request.GET.get('address')
    address_city = address.split(' ')[-1]
    if address_city.lower() is not 'toronto':
        address += " Toronto"
    coordinates = Geocoder.geocode(address)
    coordinates = coordinates[0].coordinates
    return HttpResponse(
        simplejson.dumps({
            'lat': coordinates[0],
            'lon': coordinates[1],
        })
    )


def arbor_api_botanical_image(request):
    """
    Returns a botanical description
    """
    botanical_name = request.GET.get('botanical')
    image = Image.objects.get(botanical_name=botanical_name)
    return HttpResponse(settings.STATIC_URL+image.file.name)


def arbor_comments_list(request):
    gid = request.GET.get('gid')
    tree = Shape.objects.get(gid=gid)
    return render_to_response('arbor/comments_list.html', {'tree': tree,},
        context_instance=RequestContext(request))

def arbor_comments_add(request):
    gid = request.GET.get('gid')
    tree = Shape.objects.get(gid=gid)
    return render_to_response('arbor/comments_add.html', {'tree': tree,},
        context_instance=RequestContext(request))
    pass
