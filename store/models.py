from django.db import models

from django.urls import reverse

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length = 250, db_index = True)

    slug = models.SlugField(max_length = 250, unique = True)


    class Meta:

        verbose_name_plural = 'categories'
    #Category (1), Category (2)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # create custom url to redirect to the slug page
        # return the URL for the detail view of the product
        return reverse('list-category', args =[self.slug])


class Product(models.Model):
    #FK

    category = models.ForeignKey(Category, related_name = 'product', on_delete = models.CASCADE, null = True )

    title = models.CharField(max_length = 250)

    brand = models.CharField(max_length = 250, default = 'un-branded')

    description = models.TextField(blank = True)

    slug = models.SlugField(max_length = 255)

    price = models.DecimalField(max_digits = 4, decimal_places = 2)

    image = models.ImageField(upload_to = 'images/')

    class Meta:

        verbose_name_plural = 'Products'
    #pRODUCT (1), Product (2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # create custom url to redirect to the slug page
        # return the URL for the detail view of the product
        return reverse('product-info', args =[self.slug])


