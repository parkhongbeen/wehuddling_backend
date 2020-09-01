from rest_framework import serializers

from info.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        models = UserInfo
        fields = [
            'name',
            'phone_number',
            'old_address',
            'new_address',
        ]
