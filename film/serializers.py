from rest_framework import serializers
from django.contrib.auth.models import User
from film.models import Movies,Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"
        read_only_fields=["id","user","movies"]

class MovieSerializer(serializers.ModelSerializer):
    genres=serializers.StringRelatedField(many=True)
    language=serializers.StringRelatedField()
    actors=serializers.StringRelatedField(many=True)
    reviews=ReviewSerializer(read_only=True,many=True)
    review_count=serializers.CharField(read_only=True)
    class Meta:
        model=Movies
        fields="__all__"