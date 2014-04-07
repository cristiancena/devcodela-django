from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaDiscusiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('apps.home.urls')), #incluimos las urls de la aplicacion home
    url(r'^admin/', include(admin.site.urls)),
)