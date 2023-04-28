from django.urls import path
from . import views


urlpatterns = [
    path('html/', views.article_html),
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('json-3/', views.article_json_3),
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('article_list_create/', views.article_list_create),
    path('comment/<int:article_pk>/', views.comment),
]
