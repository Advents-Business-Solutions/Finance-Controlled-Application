from django.db import models

# Create your models here.

class ProductEngine(models.Model):
    class Meta:
        db_table = "engine_metadata"

    product_engine_code = models.CharField(max_length=255, verbose_name="Product Engine Code", null=False)
