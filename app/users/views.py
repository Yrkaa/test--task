from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import UserModel
from .serializers import UserSerializer


# Create your views here.
class UserView(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        obj = UserModel.objects.all()
        l = []
        for i in obj:
            l.append({'id':i.id, 'name': i.name, 'email': i.email, 'date': i.date})

        return Response(l)