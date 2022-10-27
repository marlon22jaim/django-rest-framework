from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    # con esta configuracion cualquier cliente podra solicitar datos al server
    # se puede reemplazar por IsAuthenticated
    permission_classes = [permissions.AllowAny]
    serializer_class =  ProjectSerializer
