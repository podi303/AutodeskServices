from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('new_item', views.add_new_item, name="new_item"),
]
