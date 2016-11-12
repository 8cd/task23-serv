from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
	def new():
		pass
	def popular():
		pass


class Question(models.Model):
	objects=QuestionManager()
	title = models.CharField(max_length=255)
	text = models.TextField()
	rating = models.IntegerField( default=0) 
	added_at = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User,blank=True, related_name="question_author")
	likes = models.ManyToManyField(User,blank=True)

	def __unicode__(self):
		return self.title

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User, related_name="answer_author")

	def __unicode__(self):
		return self.text
