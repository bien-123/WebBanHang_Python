from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Xin chào</h1>')


class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

    def post(self, request):
        user_name = request.POST.get('tendangnhap')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse('User khong ton tai')
        return HttpResponse('Ban vua bam dang nhap %s %s'%(user_name, pass_word))