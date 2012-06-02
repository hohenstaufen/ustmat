from django.conf.urls import patterns, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('arbor.views',
    url(r'^$', 'arbor_index', name='arbor_index'),
    url(r'api/geocode/$', 'arbor_api_geocode', name='arbor_api_geocode'),
    url(r'api/test_view/$', 'arbor_test_view', name='arbor_test_view'),
)
