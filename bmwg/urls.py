from django.conf.urls.defaults import *
from bmwg.views import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^lecture/', include('post.urls')),
	(r'^$', landing),
	(r'^get/$', get),
	#do I need to take out the last '/' ??
	(r'^get/(?P<last_update>[-.:\w]+)/$', get),
	url(r'^admin/', include(admin.site.urls)),
)
