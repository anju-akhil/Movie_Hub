from django.urls import path
from film import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("movies",views.MoviesView,basename="movies")
router.register("reviews",views.ReviewView,basename="reviews")
urlpatterns = [
    path("register/",views.SignupView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    
    
]+router.urls