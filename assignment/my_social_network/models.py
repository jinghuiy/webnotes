from django.db import models
from django.contrib.auth.models import User

class UserLink(models.Model):
  from_user = models.ForeignKey(User,related_name="from_user")
  to_user = models.ForeignKey(User,related_name="to_user")
  date_added = models.DateField()
  
  def __unicode__(self):
    return self.from_user.username + " is following " + self.to_user.username
   
  def save(self,*args,**kwargs):
    if (self.to_user==self.from_user):
      return
    else:
      super(UserLink,self).save(*args,**kwargs)
      
  class Meta:
    unique_together=('from_user','to_user')
