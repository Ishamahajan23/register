from django.urls import path
from . import views
urlpatterns = [
    path('',views.FrontPage,name='frontpage'),
    path('test/', views.test, name="test"),
]