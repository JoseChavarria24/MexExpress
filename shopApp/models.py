from django.db import models

# Create your models here.
class Product(models.Model):
    #Definir campos de la tabla
    product_name = models.CharField(max_length=100, unique=True)
    product_description = models.CharField(max_length=255)
    product_full_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_is_offer = models.BooleanField()
    product_offer_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.product_name

class HistoricalCost(models.Model):
    #Definir campos de la tabla
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_date = models.DateTimeField()
    product_cost = models.DecimalField(max_digits=10, decimal_places=2)
    product_is_offer = models.BooleanField()

    def __str__(self):
        return self.product.product_name + " " + self.change_date.strftime("%Y-%M-%D %H:%M") 
    
class Contact(models.Model):
    #Campos de la tabla contact
    contact_full_name = models.CharField(max_length = 60, unique=True)
    contact_address = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField(unique = True, max_length=255)
    contact_active = models.BooleanField()

    def __str__(self):
        return self.contact_full_name