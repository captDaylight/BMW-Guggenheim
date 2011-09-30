from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from post.models import Lecture
from datetime import datetime
import time
import os, json

def landing(request):
	lecture_listing = Lecture.objects.all()
	return render_to_response('post/index.html', {'lecture_listing': lecture_listing})


def get(request, last_update = None):		
	timestamp = time.time() 
	print timestamp
	if last_update:
		last_update = datetime.fromtimestamp(float(last_update))
		lecs = Lecture.objects.all().filter(last_modified__gt=last_update)
		lectures = format(lecs)
	else:
		lectures = format(Lecture.objects.all())
	updates = {'timestamp': timestamp, 'lectures': lectures}
	return HttpResponse(json.dumps(updates), mimetype="application/json")



#Put the objects in the correct format for JSON
def format(objs):
	ls = []
	for l in objs:
		posts = []
		ls.append({'title': l.title, 'posts': posts})
		for p in l.post_set.all():
			posts.append({'post': p.word, 'count': p.count})
	return ls