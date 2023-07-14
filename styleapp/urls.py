from django.urls import path
from . import views

app_name = 'styleapp'

urlpatterns = [
    path("", views.index, name="index"),
    # path('myview/', views.myview, name='myview')
]