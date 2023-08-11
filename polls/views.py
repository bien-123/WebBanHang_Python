from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("HELLO WORLD")
    myname = "Python"
    taisan = ["Điện thoại", "Máy tính", "Máy bay"]
    context = {'name': myname, "taisan": taisan}
    return render(request, "polls/index.html", context)


def abc(request):
    return HttpResponse("PYTHON DJANGO")
