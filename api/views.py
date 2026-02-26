from core.models import blog
from rest_framework import viewsets
from core.serializers import blogserializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class BlogAPI(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = blog.objects.all()
    serializer_class = blogserializer
    filterset_fields = ['status', 'is_featured', 'category']
