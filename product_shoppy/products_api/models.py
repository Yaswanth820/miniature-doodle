from django.db import models

# Create your models here.
class Laptop(models.Model):

    WEBSITE_CHOICES = (
        ('shopclues', 'SHOPCLUES'),
        ('flipkart', 'FLIPKART'),
        ('croma', 'CROMA'),
        ('vijay_sales', 'VIJAY_SALES'),
        ('reliance', 'RELIANCE'),
    )

    title = models.CharField(max_length=300)
    price = models.FloatField()
    rating = models.FloatField(null=True)
    total_review_count = models.IntegerField()
    is_refurbished = models.BooleanField(default=False)
    url = models.CharField(max_length=500)
    website = models.CharField(max_length=20, choices=WEBSITE_CHOICES, default='shopclues')

    def __str__(self):
        return self.title

    # create index on price, rating, total_review_count, website as these are most frequently used fields for filtering
    class Meta:
        indexes = [
            models.Index(fields=['price', 'rating', 'total_review_count', 'website'])
        ]