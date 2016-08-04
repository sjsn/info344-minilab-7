from django.db import models

# Author object
class Author(models.Model):
	fname = models.CharField(max_length = 200)
	lname = models.CharField(max_length = 200)

	def __string__(self):
		return self.fname + " " + self.lname

# Publisher object
class Publisher(models.Model):
	name = models.CharField(max_length = 200)

	def __string__(self):
		return self.name

# Book object
class Book(models.Model):
	title = models.CharField(max_length = 100)
	pub_date = models.DateField()
	summary = models.TextField(max_length = 5000)
	price = models.DecimalField(max_digits = 65, decimal_places = 2)
	link = models.URLField(max_length = 300)
	img = models.URLField(max_length = 300)
	author = models.ManyToManyField(Author)
	publisher = models.ManyToManyField(Publisher)

	def __string__(self):
		return self.title
