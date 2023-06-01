from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    image = serializers.ImageField(
        max_length=None, allow_empty_file=True, required=False
    )

    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created_at", "image")

    def create(self, validated_data):
        image = validated_data.pop("image", None)
        post = Post.objects.create(**validated_data)
        if image:
            post.image = image
            post.save()
        return post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")
