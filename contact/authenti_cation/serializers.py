from rest_framework import serializers
from django.contrib.auth.models import User #Importing In-Built model User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type': 'password'},write_only=True, required=True)
    

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password']

        extra_kwargs =  {
            'first_name':{'required':True},
            'last_name':{'required':True},
            }

    def validate(self, attrs):
        email=attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':"An account already exists with given email."})
        return attrs
      
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

        