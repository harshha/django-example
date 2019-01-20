from django.urls import path
from second_app import views
app_name='second_app'
urlpatterns = [
    path('',views.index2),
    path('form',views.form_name),
    path('index',views.index,name="index")
]
