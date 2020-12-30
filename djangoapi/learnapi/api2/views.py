from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from rest_framework.permissions import AllowAny
# Create your views here.
from django.http import JsonResponse
class UserModelViewset(viewsets.ModelViewSet):
    permission_classes_by_action ={'create':[AllowAny]}


    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes  ]

def generate_token():
    return "token"
@csrf_exempt
def signin(request):
    if request.method != "POST":
        return JsonResponse({"msg":"send post request"})

    username=request.POST["email"]
    password = request.POST["password"]
    print(password)
    UserModel = get_user_model()    

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            
            if user.session_token != "t":
                user.session_token = "t"
                user.save()
                return JsonResponse({"error":"alreasdy"})

            token = generate_token()
            user.session_token=token
            user.save()
            login(request,user)
            return JsonResponse({"msg":"user is logged in ","token":token})
        
        else:
            return JsonResponse({"error":"invalid password"})
    except UserModel.DoesNotExist:
        return JsonResponse({"msg":"invalid email"})

def signout(request,id):
    logout(request)
    UserModel = get_user_model()
    user=UserModel.objects.get(id=id)
    user.session_token='t'
    user.save()
    return JsonResponse({"msg":"User is Logged out"})