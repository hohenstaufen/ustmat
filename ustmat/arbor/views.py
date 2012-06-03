from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from pygeocoder import Geocoder
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

def arbor_test_view(request):
    from .helpers import *
    bananas()
    return HttpResponse('1')
