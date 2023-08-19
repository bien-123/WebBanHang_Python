from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm


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


class ViewUser(LoginRequiredMixin, View):
    login_url = '/demo/login/'

    def get(self, request):
        # if not request.user.is_authenticated:
        #     return HttpResponse('Ban vui long dang nhap')
        # else:
        #     return HttpResponse('<h1>Day la view user</h1>')
        return HttpResponse('<h1>Day la view user</h1>')

    def post(self, request):
        pass


@decorators.login_required(login_url='/demo/login/')
def view_product(request):
    return HttpResponse('Xem san pham')


class AddPost(LoginRequiredMixin, View):
    login_url = '/demo/login/'

    def get(self, request):
        f = PostForm()
        context = {'f': f}
        return render(request, 'demo/add_post.html', context)

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('Ban nhap sai du lieu roi') #nếu nhập vào ko đúng kiểu dl trong model
        print(request.user.get_all_permissions) #xem các quyen cua user
        if request.user.has_perm('loginDemo.add_bai_viet'):#viet thuong ten model
            f.save()
        else:
            return HttpResponse('Ban khong co quyen')
        return HttpResponse('OK')
