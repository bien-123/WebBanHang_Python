from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail


# Create your views here.

def index(request):
    return HttpResponse("Xin chao")


def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})


def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('Lưu thành công')
        else:
            return HttpResponse('Không được validate')
    else:
        return HttpResponse('Không phải POST request')


def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})


def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            # Lấy từng phần tử
            tieude = m.cleaned_data['title']
            email = m.cleaned_data['email']
            content = m.cleaned_data['content']
            cc = m.cleaned_data['cc']
            context = {'td': tieude, 'b': content, 'd': email, 'c': cc}

            # Lấy nhiều phần tử
            context2 = {'email_data': m}
            return render(request, 'news/print_email.html', context)
        else:
            return HttpResponse('Form not validate')
    else:
        return HttpResponse('Không phải POST method')
