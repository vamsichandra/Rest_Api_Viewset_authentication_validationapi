from django.db import models

# Create your models here.
class Product(models.Model):

    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    title=models.CharField( max_length=50)
    content=models.TextField()
    price=models.DecimalField( max_digits=15, decimal_places=2,default=1024.00)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    def get_discount(self):
        return "122"

    
