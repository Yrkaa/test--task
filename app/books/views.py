from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import Book_Serializer


# Create your views here.
class Book_View(ModelViewSet):
    queryset = Book_Model.objects.all()
    serializer_class = Book_Serializer
    permission_classes = [IsAuthenticatedOrReadOnly]


