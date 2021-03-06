from django.urls import path

from . import views

urlpatterns = [
    path('user/create', views.user_create, name='user_create'),
    path('user/add_twitter_id', views.user_add_twitter_id,
         name='user_add_twitter_id'),
    path('line/push', views.push_room_id_to_line, name='push_room_id_to_line'),
    path('topic/register_text', views.topic_register_text,
         name='topic_register_text'),
    path('topic/relaxing_topics', views.calculate, name='calculate')
]
