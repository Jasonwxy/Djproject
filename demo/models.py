from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=60)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='E-mail')

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class City(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    province_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'city'


class Area(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    city_code = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'area'


class Province(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'province'
