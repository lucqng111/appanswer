from django.urls import path
from . import views

urlpatterns = [
    path('first_page', views.first_page, name="first_page"),
    path('first_page/get_choice', views.post_first_page, name="post_first_page"),
    path('second_page', views.second_page, name="second_page"),
    path('second_page/get_answer', views.post_second_page, name="post_first_page"),
    path('', views.inputs, name="input"),
    path('input_password', views.get_inputs, name="get_input"),
    path('thank_you', views.thank)
]

