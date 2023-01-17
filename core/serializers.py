from rest_framework import serializers, status
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from phonenumber_field.serializerfields import PhoneNumberField
from .models import User


class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40, allow_blank=True)
    email = serializers.EmailField(max_length=80, allow_blank=False)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(allow_blank=False, write_only=True)
    confirm_password = serializers.CharField(allow_blank=False, write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "password",
            "confirm_password",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise ValidationError(
                detail="Password not match", code=status.HTTP_409_CONFLICT
            )

        email = User.objects.filter(username=attrs.get("username")).exists()
        if email:
            raise ValidationError(
                detail="User with email exists", code=status.HTTP_403_FORBIDDEN
            )

        username = User.objects.filter(username=attrs.get("username")).exists()
        if username:
            raise ValidationError(
                detail="User with username exists", code=status.HTTP_403_FORBIDDEN
            )

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        new_user = User(**validated_data)
        new_user.password = make_password(validated_data.get("password"))
        new_user.save()
        return new_user
