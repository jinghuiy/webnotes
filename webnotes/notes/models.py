from django.db import models 

class Notes(models.Model): 
  title = models.CharField(max_length=255) 
  content = models.TextField() 
  author = models.CharField(max_length=255)
def __unicode__(self): #note: 2 underscores on each side
  return self.title

