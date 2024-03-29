from rest_framework import fields, serializers

# from api.ratings.serializers import RatingSerializer

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "id",
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "state",
            "city",
            "is_employer",
            "is_employee",
            "rating",
            "num_reviews",
            "reviews",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_reviews(self, obj):
        pass

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_employer:
            representation["top_employer"] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "state",
            "city",
            "is_employer",
            "is_employee",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.top_employer:
            representation["top_employer"] = True
        return representation
