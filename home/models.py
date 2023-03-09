from django.db import models

# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Companies'

class job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirement =  models.TextField()
    policy = models.TextField()
    payment = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True)