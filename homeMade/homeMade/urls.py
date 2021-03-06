from django.conf.urls import patterns, include, url
# from django.conf.urls.defaults import *
# from homeMade.views import hello, current_datetime, hours_ahead
# from homeMade.books import views
# from homeMade.contact import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from homeMade import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homeMade.views.home', name='home'),
    # url(r'^homeMade/', include('homeMade.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ('^hello/$', views.hello), 
    ('^time/$', views.current_datetime),
    (r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    # (r'^search_form/$', views.search_form),
    (r'^display_meta/$',views.display_meta),
    # (r'^search/$', views.search),
    # (r'^contact/$', views.contact),
    # (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    )
