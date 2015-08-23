from django.db import models
class ResearchGrant(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	eligibility = models.TextField()
	how_to_apply = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):							
		return	self.title

class TravelGrant(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	eligibility = models.TextField()
	how_to_apply = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):						
		return	self.title
class ConferenceGrant(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	eligibility = models.TextField()
	how_to_apply = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):							
		return	self.title
class Fellowship(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):						
		return	self.title
class Scholarship(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):						
		return	self.title
class Message(models.Model):
	Post = models.CharField(max_length=200)
	text = models.TextField()
	def	__str__(self):						
		return	self.Post
	
# Create your models here.
