from django.urls import path
from . import views
from simple_chatbot.views import SimpleChatbot
urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('ulogin/',views.ulogin,name='ulogin'),
    path('home/',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('myblog/',views.myblog,name='myblog'),
    path('<int:id>/viewblog/',views.viewblog,name='viewblog'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('status/',views.status,name='status'),
    path('logout/',views.ulogout,name='ulogout'),
    path('botist/',views.botist,name='botist'),
    path("simple_chatbot/", SimpleChatbot.as_view()),
]