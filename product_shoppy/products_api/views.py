from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Laptop
from .serializers import LaptopSerializer
from .filters import LaptopFilter
from .pagination import ProductPagination


# Create your views here.
class LaptopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Laptop.objects.all().order_by('-total_review_count')    # Highest rated laptops first
    serializer_class = LaptopSerializer
    pagination_class = ProductPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    filterset_class = LaptopFilter
    search_fields = ['title']
    ordering_fields = ['price', 'rating', 'total_review_count']

    @method_decorator(cache_page(60*15))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)