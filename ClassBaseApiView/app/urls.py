from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.StudentApi.as_view()),
    path('api/<int:id>',views.StudentApi.as_view()),
]
