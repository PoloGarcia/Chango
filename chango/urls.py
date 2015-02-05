from django.conf.urls import patterns, include, url
from django.contrib import admin

import views
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^all/$', views.all_render_view, name='login'),
    url(r'^detail/(?P<chango_id>\d*)/$', views.detail_render_view, name='projects'),
)
