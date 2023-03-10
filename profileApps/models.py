from django.db import models

# Create your models here.

class Product:
    def __init__(self, id, name, brand, color, price, amount):
        self.productId = id
        self.productName = name
        self.productBrand = brand
        self.productColor = color
        self.productPrice = price
        self.productAmount = amount


    def __str__(self):
        return "ID : {}, NAME : {}, BRAND : {}, COLOR : {}, PRICE : {}, AMOUNT : {}"\
            .format(self.productId, self.productName, self.productBrand, self.productColor, self.productPrice, self.productAmount)
