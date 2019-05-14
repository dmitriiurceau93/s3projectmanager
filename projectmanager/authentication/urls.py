from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ( 
            login,
            signup,
            UserViewSet
        )

router = DefaultRouter()
router.register(r'users', UserViewSet)

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_create = UserViewSet.as_view({
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    # path('', include(router.urls)),
    path('login/', login),
    path('join/', signup),
    path('users/', user_list, name='user-list'),
    path('user/', user_create, name='user-create'),
    path('user/<pk>', user_detail, name='user-detail'),

]