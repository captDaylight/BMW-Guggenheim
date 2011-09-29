from django.db import models

class Lecture(models.Model):
	title = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.title
	

class Post(models.Model):
	lecture = models.ForeignKey(Lecture)
	word = models.CharField(max_length = 100)
	count = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.word