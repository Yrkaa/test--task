from rest_framework.serializers import ModelSerializer

from .models import Book_Model


class Book_Serializer(ModelSerializer):
    class Meta:
        model = Book_Model
        fields = '__all__'
