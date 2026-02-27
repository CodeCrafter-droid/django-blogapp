from rest_framework import serializers
from .models import blog, category, comment


class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = "__all__"

class categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = "__all__"

class commentserializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
        read_only_fields = [
            'user',
            'blogg',
            'likes',
            'created_at',
            'updated_at'
        ]