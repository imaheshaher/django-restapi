from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'users',views.UserModelViewset)
router.register(r'blog',views.BlogViewsets)
urlpatterns =[
    path('',include(router.urls)),
    path('login/',views.signin,name='signin'),
    path('logout/<slug:id>/',views.signout,name='singout'),
    path('api-auth/', include('rest_framework.urls')),

]