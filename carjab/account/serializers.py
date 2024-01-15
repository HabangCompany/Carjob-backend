from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'address', 'phonenumber', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드를 쓰기 전용으로 설정

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            address=validated_data['address'],
            phonenumber=validated_data.get('phonenumber')  # phonenumber는 null 허용이므로 get 메서드 사용
        )
        user.set_password(validated_data['password'])  # set_password 메서드로 비밀번호 해시 처리
        user.save()
        return user
