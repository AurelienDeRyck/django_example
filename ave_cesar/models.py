from django.core.validators import MinValueValidator
from django.db import models
from django.urls.base import reverse


class Product(models.Model):

    name = models.CharField(max_length=255)
    number = models.CharField(max_length=5)
    price = models.FloatField(validators=[MinValueValidator(0)])
    create_at = models.DateTimeField(auto_now_add=True, editable=True)
    given_at = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField('Category')
    borrower = models.ForeignKey('auth.User', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return u'%s-%s'% (self.name, self.number)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return u'%s'% self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})

