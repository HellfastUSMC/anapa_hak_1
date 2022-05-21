from datetime import datetime as dt

import api.exceptions as api_exceptions
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import Kid

user = get_user_model()

class KidSerializer(serializers.ModelSerializer):
    """Сериализатор детей."""

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Kid
        fields = ("id", "user__first_name", "shift__name", "team__name")
        read_only_fields = ("user",)