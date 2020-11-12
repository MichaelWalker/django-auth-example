from django.contrib import admin
from django.urls import path, include
from .myApp import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('items', views.ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('items', views.ItemListView.as_view(), name='items'),
    path('accounts/', include('django.contrib.auth.urls')),
]
