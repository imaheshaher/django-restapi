
from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser,Blog
from .serializers import UserSerializer,BlogSerializer
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from .permission_helper import IsOwner
UserModel=get_user_model()
# Create your views here.
from django.http import JsonResponse
class UserModelViewset(viewsets.ModelViewSet):
    permission_classes_by_action ={'create':[AllowAny]}
    

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]

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
    print(request.POST)
    username=request.POST["email"]
    password = request.POST["password"]
    print(password)
    UserModel = get_user_model()    

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            token = generate_token()

            if user.session_token != "t":
                user.session_token = "t"
                user.save()
                return JsonResponse({"token":token})

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



class BlogViewsets(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticated]
    
    serializer_class=BlogSerializer
    queryset = Blog.objects.all()
    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



def validate_token(request,id,token):
    user = UserModel.objects.get(id=id)
    if user.session_token == token:
        return JsonResponse({'LoggedIn':True})
    return JsonResponse({"err":"error"})




class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        print(self.request.user)
        content = {'message': 'Hello, World!'}
        return Response(content)


@csrf_exempt

def forgot(request):
    if request.method == 'POST':
        name=request.POST["email"]
        print(name)
        return JsonResponse({"msg":"hello"})