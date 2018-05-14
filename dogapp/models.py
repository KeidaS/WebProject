from django.contrib.auth.models import User
from django.db import models
from django.urls.base import reverse


# Create your models here.

class Refuge(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('dogapp:refuge_detail', kwargs={'pk': self.pk})


class Vaccine(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name


'''
class Race(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name
'''


class Dog(models.Model):
    name = models.TextField()
    race = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    refuge = models.ForeignKey(Refuge, null=True, related_name='dogs')
    vaccine = models.ForeignKey(Vaccine, null=True, related_name='dogs')
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('dogapp:dog_detail', kwargs={'pkr': self.refuge.pk, 'pk': self.pk})


class Adoption(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, null=True, related_name='adoption')
    dog = models.ForeignKey(Dog, null=True, related_name='adoption')
