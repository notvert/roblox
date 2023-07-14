from django.db import models

class Items(models.Model):
    productId = models.IntegerField()
    itemType = models.CharField(max_length=200)
    assetType = models.IntegerField() 
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300) 
    devproductId = models.IntegerField()
    genres = models.CharField(max_length=200)
    itemStatus = models.CharField(max_length=200)
    itemRestrictions = models.CharField(max_length=200)
    creatorHasVerifiedBadge = models.CharField(max_length=200)
    creatorType = models.CharField(max_length=200)
    creatorTargetId = models.IntegerField() 
    creatorName = models.CharField(max_length=200)
    price = models.IntegerField() 
    favoriteCount = models.IntegerField() 
    offSaleDeadline = models.CharField(max_length=200)
    saleLocationType = models.CharField(max_length=200)

    def __str__(self):
        return self.name
