from django.conf.urls.defaults import *
from bmw.views import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^lecture/', include('post.urls')),
	(r'^$', landing),
	url(r'^admin/', include(admin.site.urls)),
)
