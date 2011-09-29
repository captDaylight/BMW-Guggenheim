from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from post.models import Lecture, Post

def lecture_display(request, lecture_id):
	l = get_object_or_404(Lecture, pk=lecture_id)
	return render_to_response('post/post.html', {'lecture': l}, context_instance=RequestContext(request))

def increment_word(request, lecture_id, post_id):
	l = get_object_or_404(Lecture, pk=lecture_id)
	p = get_object_or_404(Post, pk=post_id)
	p.count += 1
	p.save()
	return HttpResponseRedirect(reverse('post.views.lecture_display', args=(l.id,)))

def add_word(request, lecture_id):
	l = get_object_or_404(Lecture, pk=lecture_id)
	if request.method == "POST":
		p = request.POST.copy()
		print p
		#see if there is a value with p
		if p.has_key('word') and p['word'] != "":
			try:
				oldWord = l.post_set.get(word = p['word'])
			except:
				newWord = l.post_set.create(word=p['word'], count = 1)
			else:
				oldWord.count += 1
				oldWord.save()
			return HttpResponseRedirect(reverse('post.views.lecture_display', args=(l.id,)))
	return HttpResponseRedirect(reverse('post.views.lecture_display', args=(l.id,)))