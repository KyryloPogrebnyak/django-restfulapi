from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    #path('', include(router.urls)),
    path('', views.index, name="home"),
    path('all/', views.all, name="all_books"),
    path('api-auth/', include('rest_framework.urls')),
]