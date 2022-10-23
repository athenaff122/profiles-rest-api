from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) #这里不需要有base_name是因为views.py这个UserProfileViewSet里面有queryset这种东西


urlpatterns=[
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]
