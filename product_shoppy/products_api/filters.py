from django_filters import FilterSet, RangeFilter
from .models import Laptop

class LaptopFilter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = Laptop
        fields = {
            'price': ['lt','gt'],
            'website': ['exact'],
            'is_refurbished': ['exact']
        }