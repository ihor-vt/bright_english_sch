from rest_framework import serializers

from .models import (
    Category,
    Course,
    Comment,
    MainPage,
    Contact,
    Subscrabe_email
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id", "category", "name", "slug", "image", "model", "group",
            "format", "price_total", "price_mounth", "message"
            ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "author"]


class MainPageSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = MainPage
        fields = ["id", "image", "video"]

    def get_video(self, obj):
        if obj.video:
            return obj.video.url
        return None


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "name", "email", "mobile_phone",
            "description"]


class Subscrabe_emailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscrabe_email
        fields = ["email"]
