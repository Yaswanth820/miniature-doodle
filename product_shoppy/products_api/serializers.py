from rest_framework.serializers import ModelSerializer

from .models import Laptop

class LaptopSerializer(ModelSerializer):
    class Meta:
        model = Laptop
        fields = ('title', 'price', 'rating', 'total_review_count', 'website', 'is_refurbished', 'url')
