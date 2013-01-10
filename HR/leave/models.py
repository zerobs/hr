from django.db import models

# Create your models here.
class departments(models.Model):
    description=models.CharField(max_length=30)
    def __unicode__(self):
        return self.description
    
   

class employees(models.Model):
    firstname=models.CharField(max_length=30)
    familyName=models.CharField(max_length=30)
    dateJoined=models.DateTimeField('Date Joined')
    department=models.ForeignKey(departments)
    
    def __unicode__(self):
        return self.firstname
