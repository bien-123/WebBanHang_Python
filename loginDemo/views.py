from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Xin chào</h1>')


class LoginClass(View):
    def get(self, request):
        return render(request, 'demo/login.html')

    def post(self, request):
        user_name = request.POST.get('tendangnhap')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse('Dang nhap that bai! User khong ton tai')

        login(request, my_user)
        return render(request, 'demo/success.html')

class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('Ban vui long dang nhap')
        else:
            return HttpResponse('<h1>Day la view user</h1>')