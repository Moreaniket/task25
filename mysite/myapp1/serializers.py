from rest_framework import serializers

class shubham_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=50)