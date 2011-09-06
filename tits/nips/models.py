from django.db import models
from django.contrib.auth.models import User

class Nipple(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='nipples/')
    interests = models.CharField(max_length=300, null=True, blank=True)
    hometown = models.CharField(max_length=60, null=True, blank=True)
    high_school = models.CharField(max_length=60, null=True, blank=True)
    score = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    
    def avg(self):
        if self.votes > 0:
            return float(self.score)/self.votes
        else:
            return 0.0
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ["-votes"]
        
class DayFour(models.Model):
    nipple = models.ForeignKey(Nipple)
        
class NippleOpinion(models.Model):
    user = models.ForeignKey(User)
    nipple = models.ForeignKey(Nipple)
    score = models.IntegerField()
    comment = models.TextField()
    
    def __unicode__(self):
        return self.user.get_full_name() + " gave " + self.nipple.first_name+" "+self.nipple.last_name+" a "+str(self.score)
