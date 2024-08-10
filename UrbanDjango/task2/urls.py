from django.urls import path
from .views import function_view, class_view

urlpatterns = [
    path('function/', function_view, name='function_view'),
    path('class/', class_view, name='class_view'),
]
