from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import authentication,permissions
from rest_framework.decorators import action
from rest_framework import serializers

from film.serializers import UserSerializer,MovieSerializer,ReviewSerializer
from film.models import Movies,Review

#----------------------Register------------------------
class SignupView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
class MoviesView(viewsets.ModelViewSet):
    serializer_class=MovieSerializer
    queryset=Movies.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

#adding review for a movie
#url:localhost:8000/api/movies/{4}/add_review/
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_object=Movies.objects.get(id=kwargs.get("pk"))
        user_object=request.user.profile
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user_object,movies=movie_object)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    # def create(self,request,*args,**kwargs):
    #     raise serializers.ValidationError("Permission denied")
    
    def update(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission denied")
    
    def destroy(self, request, *args, **kwargs):
        raise serializers.ValidationError("Permission denied")

class ReviewView(viewsets.ModelViewSet):
    serializer_class=ReviewSerializer
    queryset=Review.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    

