from django.db import models

# Create your models here.
class Work(models.Model):
    class Meta:
        db_table="tbl_work"
        verbose_name_plural="Works"
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    image=models.ImageField(upload_to="images",null=True)
