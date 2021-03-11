from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World, My name is Canh!")


def cal_page(request):
    return render(request, "calculator.html")


def do_cal_total(request):
    print(str(request.POST['number_a']))
    a = request.POST['number_a']
    b = request.POST['number_b']
    context = {
        'cal': {
            "a": a,
            "b": b,
            "result": int(a) + int(b),
        }
    }
    print(str(context))
    return render(request, "result.html", context)
