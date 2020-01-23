from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created at',)
        model = Post