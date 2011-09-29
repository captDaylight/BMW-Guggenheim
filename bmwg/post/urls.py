from django.conf.urls.defaults import *
from post.views import *

urlpatterns = patterns('',
	(r'^(?P<lecture_id>\d+)/$', lecture_display),
	(r'^(?P<lecture_id>\d+)/add', add_word),
	(r'^(?P<lecture_id>\d+)/increment/(?P<post_id>\d+)/$', increment_word)
)