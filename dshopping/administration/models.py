from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField('Title',max_length=150)
    description = models.TextField('Descripcion')
    status=models.BooleanField(default=True)
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.title

class Country(models.Model):
    id= models.AutoField(primary_key=True)
    title=models.CharField('Title',max_length=150)
    abbreviation=models.CharField('Abbreviation',max_length=150)
    status=models.BooleanField(default=True)
    class Meta:
        verbose_name='Country'
        verbose_name_plural='Contries'
    def __str__(self):
        return self.title

class Product(models.Model):
    id= models.AutoField(primary_key=True)
    title=models.CharField('Title',max_length=150)
    description= models.TextField('Descripcion')
    id_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    id_country=models.ForeignKey(Country,on_delete=models.CASCADE)
    quantity=models.IntegerField('Quantity')
    status =models.BooleanField(default=True)
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'
    def __str__(self):
        return self.title