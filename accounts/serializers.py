from . models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password"]
        
class CustomUserLoginSerializer(serializers.ModelSerializer):
    username = serializers.EmailField()
    password = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ("username", "password")
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = CustomUser.objects.filter(username=username).first()

            if user and user.check_password(password):
                data['user'] = user
                return data

        raise serializers.ValidationError('Invalid credentials')

class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name', 'middle_name', 'last_name', 'phone_number', 'adress')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user