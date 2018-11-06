from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from users import views as userViews
from posts import views as postViews
from offers import views as offerViews
from categories import views as categoryViews
from belongings import views as belongingViews

ROUTER = routers.DefaultRouter()
ROUTER.register(r'categories', categoryViews.CategoryViewSet)
ROUTER.register(r'users', userViews.UserViewSet)
ROUTER.register(r'belongings', belongingViews.BelongingViewSet)
ROUTER.register(r'posts', postViews.PostViewSet)
ROUTER.register(r'offers', offerViews.OfferViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(ROUTER.urls)),
    path('token-auth/', obtain_jwt_token),
]
