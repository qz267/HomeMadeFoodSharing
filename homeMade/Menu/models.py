from django.db import models

class Cooker(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField('e-mail',blank=True)
	
	def __unicode__(self):
		return u'%s %s' %(self.first_name, self.last_name)

class Menu(models.Model):
	title = models.CharField(max_length=100)
	cookers = models.ManyToManyField(Cooker)
	publication_date = models.DateField(blank=True,null=True)
	
	def __unicode__(self):
		return u'%s %s' %(self.title, self.cookers)