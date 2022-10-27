from rest_framework import serializers
from .models import Project


# para convertir un modelo en datos que pueden ser consultados
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "technology", "create_at")
        read_only_fields = ("create_at",)
