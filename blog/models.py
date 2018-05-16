from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
	title=models.CharField(max_length=200)
	pubdate=models.DateTimeField(default=datetime.now, blank=True)
	body=models.TextField()
	image=models.ImageField(upload_to='images/')

	def summary(self):
		return self.body[:30]+'...'

	def pub_date_pretty(self):
		return self.pubdate.strftime('%b %e %Y')
	def __str__(self):
		return self.title