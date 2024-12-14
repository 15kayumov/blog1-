from django.urls import path
from .views import HomeListViev,AbautListViev,Post_detail,Abaut_detail,signup,login,PostCreateView,HomeDeleteView,AbautDeleteView,PostUpdetView
urlpatterns=[
    path('',HomeListViev.as_view(),name='home'),
    path('abaut/',AbautListViev.as_view(),name='abaut'),
    path('post/<int:pk>/',Post_detail.as_view(),name='post_detail'),
    path('abaut/<int:pk>/',Abaut_detail.as_view(),name='abaut_detail'),
    path('',signup.as_view(),name='signup'),
    path('',login.as_view(),name='login'),
    path('post/new/',PostCreateView.as_view(),name='post_new'),
    path('post/<int:pk>delete/',HomeDeleteView.as_view(),name='post_delete'),
    path('abaut/<int:pk>delete/',AbautDeleteView.as_view(),name='abaut_delete'),
    path('post/<int:pk>edit/',PostUpdetView.as_view(),name='post_edit')
    ]