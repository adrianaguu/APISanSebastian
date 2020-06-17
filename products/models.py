from django.db import models

class Category (models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Line(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=250)
	type = models.CharField(max_length=50, null=True, blank=True)
	measure = models.CharField(max_length=50, null=True, blank=True)
	image = models.ImageField(upload_to='images/')
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
	line = models.ForeignKey(Line, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
