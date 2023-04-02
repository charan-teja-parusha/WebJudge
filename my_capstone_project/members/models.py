from django.db import models

# Create your models here.
class Member(models.Model):
  productname = models.TextField(null=True)
  brandname = models.TextField(null=True)
  price=models.FloatField(null=True,blank=True,default=0.0)
  reviews = models.TextField(null=True)
  ratings=models.IntegerField(null=True,blank=True,default=0)
  reviewvotes=models.IntegerField(null=True,blank=True,default=0)
  def __str__(self):
        return self.brandname
  