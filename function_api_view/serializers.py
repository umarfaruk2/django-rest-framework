from rest_framework import serializers
from .models import StudentApiViewModel

class StudentApiViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentApiViewModel

        fields = ['id', 'name', 'roll', 'city']


