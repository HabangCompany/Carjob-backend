from rest_framework import serializers
from .models import User , Store
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'nickname', 'phonenumber', 'password')
        extra_kwargs = {'password': {'write_only': True}}  # 비밀번호 필드를 쓰기 전용으로 설정

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            phonenumber=validated_data.get('phonenumber')  # phonenumber는 null 허용이므로 get 메서드 사용
        )
        user.set_password(validated_data['password'])  # set_password 메서드로 비밀번호 해시 처리
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                data['refresh_token'] = str(refresh)
                data['access_token'] = str(refresh.access_token)
            else:
                raise serializers.ValidationError("잘못된 자격 증명. 다시 시도해 주세요.")
        return data
    

#업체폼
# class StoreRegister(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = '__all__'

#     def create(self, validated_data):
#         store =Store(
#             storeName = validated_data['storeName'],
#             storenTel = validated_data['storeTel'],
#             storeDescription = validated_data['storeDescription'],
#             storeImage = validated_data['storeImage'],
#             storeSkill = validated_data['storeSkill'],
#         )

#         return store


# #업체폼
# class StoreRegister(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = '__all__'
#     def create(self,validated_data):
#         store = Store(
#             user = 
#         )