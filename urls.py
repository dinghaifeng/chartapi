from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chartapi.views.home', name='home'),
    # url(r'^chartapi/', include('chartapi.foo.urls')),
    url(r'^api/$', 'chartapi.views.api', name='api'),
    url(r'^playground/$', 'chartapi.views.playground', name='playground'),
    url(r'^examples/$', 'chartapi.views.examples', name='examples'),
    url(r'^examples.js$', 'chartapi.views.examples_js', name='examples_js'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
