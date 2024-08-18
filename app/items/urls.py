from django.urls import include, path
from rest_framework import routers

from items import views

app_name = "items"

router = routers.DefaultRouter()

router.register("items", views.ItemViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
