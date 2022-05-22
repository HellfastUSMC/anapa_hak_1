from datetime import datetime as dt

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.tokens import RefreshToken

from add_services.models import Activity
from users.models import Kid, Parent, Shift, Team

user_m = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователей."""

    full_name = serializers.SerializerMethodField('get_full_name')

    def get_full_name(self, obj):
        return obj.get_full_name()

    class Meta:
        model = user_m
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    """Сериализатор детей."""
    user = serializers.SlugRelatedField('id', queryset=user_m.objects.all())
    activities = serializers.SlugRelatedField('id', queryset=Activity.objects.all())

    class Meta:
        model = Parent
        fields = '__all__'

class KidSerializer(serializers.ModelSerializer):
    """Сериализатор детей."""
    user = serializers.SlugRelatedField('id', queryset=user_m.objects.all())
    parent = serializers.SlugRelatedField('id', queryset=Parent.objects.all())
    shift = serializers.SlugRelatedField('id', queryset=Shift.objects.all())
    team = serializers.SlugRelatedField('id', queryset=Team.objects.all())
    activities = serializers.SlugRelatedField('id', queryset=Activity.objects.all())

    class Meta:
        model = Kid
        fields = (
            'pk',
            'user',
            'shift',
            'team',
            'parent',
            'birth_date',
            'bio',
            'med_info',
            'food_info',
            'building_number',
            'qr_code',
            'room',
            'activities',
            'menus',
        )


class ShiftSerializer(serializers.ModelSerializer):
    """Сериализатор смен."""

    class Meta:
        model = Shift
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор смен."""

    class Meta:
        model = Team
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    """Сериализатор смен."""
    responsible = serializers.SlugRelatedField('id', queryset=user_m.objects.all())

    class Meta:
        model = Activity
        fields = '__all__'