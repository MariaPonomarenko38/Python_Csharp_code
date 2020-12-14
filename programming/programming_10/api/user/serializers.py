from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


def valid_name(dob):
    if dob.isalpha() is False:
        raise serializers.ValidationError("Name and surname must contain only letters")
    return dob


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
    )
    first_name = serializers.CharField(validators=[valid_name])
    last_name = serializers.CharField(validators=[valid_name])
    token = serializers.CharField(max_length=255, read_only=True)
    role = serializers.CharField(max_length=5)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'role', 'password', 'token',)

    def create(self, validated_data):
        if validated_data.get('role') == 'admin':
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'token': user.token,
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
