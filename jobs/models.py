from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.

class Job(models.Model):
	image=models.ImageField(upload_to='images/')
	summary=models.CharField(max_length=250)


	def __str__(self):
		return self.summary