import datetime
from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User



class Hacker(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
		return self.question

    def was_published_recently(self):
        now = timezone.now()
        return (now - datetime.timedelta(days=1)) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
	#def was_published_recently(self):
		#return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))
	


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
		return self.choice_text
