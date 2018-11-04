from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_app import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r'categories', views.CategoryViewSet)
ROUTER.register(r'users', views.UserViewSet)
ROUTER.register(r'belongings', views.BelongingViewSet)
ROUTER.register(r'posts', views.PostViewSet)
ROUTER.register(r'offers', views.OfferViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(ROUTER.urls)),
    path('token-auth/', obtain_jwt_token),
]
