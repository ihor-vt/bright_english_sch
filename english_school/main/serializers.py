from rest_framework import serializers

from .models import (
    Category,
    Course,
    Comment,
    MainPage,
    Contact,
    SubscriptionEmail,
    Teacher,
    TeacherCertificate,
    TeacherEducation,
    TeacherNote
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
            "format", "price_total", "price_mounth", "message", "description"
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


class SubscriptionEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionEmail
        fields = ["email"]


class TeacherEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherEducation
        fields = ["education"]


class TeacherNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherNote
        fields = ["notes"]


class TeacherCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherCertificate
        fields = ["image"]


class TeacherSerializer(serializers.ModelSerializer):
    educations = TeacherEducationSerializer(many=True, read_only=True)
    notes = TeacherNoteSerializer(many=True, read_only=True)
    certificates = TeacherCertificateSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = [
            "name", "position", "slug", "image",
            "educations", "notes", "certificates"
            ]
