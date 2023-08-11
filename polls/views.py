from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(request):
    # return HttpResponse("HELLO WORLD")
    myname = "Python"
    taisan = ["Điện thoại", "Máy tính", "Máy bay"]
    context = {'name': myname, "taisan": taisan}
    return render(request, "polls/index.html", context)


def viewlist(request):
    # list_question = get_object_or_404(Question, pk=1): tìm xem có khóa chính là 1 ko, nếu ko có thì trả về lỗi 404
    list_question = Question.objects.all()
    context = {'dsquest': list_question}
    return render(request, "polls/question_list.html", context)


def abc(request):
    return HttpResponse("PYTHON DJANGO")
