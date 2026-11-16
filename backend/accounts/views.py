from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from accounts.serializer import UserSerializer
from accounts.models import User

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all().order_by("id")
        return User.objects.filter(id=user.id)
