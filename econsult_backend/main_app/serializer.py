from rest_framework import serializers
from .models import SchoolFormModel, StudentModel

# Serializers define the API representation.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"

class SchoolFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFormModel
        fields = "__all__"