from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt import views as jwt_views


router=routers.DefaultRouter()
router.register(r'users',views.UserModelViewset)
router.register(r'blog',views.BlogViewsets)
urlpatterns =[
    path('',include(router.urls)),
    path('login/',views.signin,name='signin'),
    path('token-auth/', obtain_jwt_token),

    path('logout/<slug:id>/',views.signout,name='singout'),
    path('api-auth/', include('rest_framework.urls')),  
    path('validate/token/<slug:id>/<slug:token>/',views.validate_token,name='validate_token'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('forgot/',views.forgot,name='forgot')
]