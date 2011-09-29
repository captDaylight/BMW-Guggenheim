from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from post.models import Lecture

def landing(request):
	lecture_listing = Lecture.objects.all()
	return render_to_response('post/index.html', {'lecture_listing': lecture_listing})