from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def view1(request):
    print(request.method)
    return HttpResponse("hello i am from view1")
def view2(request):
    return HttpResponse("hello i am from view2.")
def view3(request):
    return JsonResponse({"name":"satya","age":"21"})
def view4(reuest):
    return JsonResponse({"status":"success","message":"hello"})
def dynamicview(request):
    qp1=request.GET.get("name")
    return HttpResponse(f"hello{qp1}")
def personinfo(request):
    name=request.GET.get("name","durgabavani")
    city=request.GET.get("city","hyd")
    role=request.GET.get("role","it")
    info=({"name":name,"role":role,"city":city})
    return JsonResponse({"status":"sucess","data":info})
def temp1(request):
    return render(request,"./simple.html")