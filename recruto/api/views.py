from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello(request):
    if request.method != "GET":
        return HttpResponse("Wrong method")
    
    name = request.GET.get('name', '')
    message = request.GET.get('message', '')
    
    html_content = f"<h1> Hello {name}! {message}!</h1>"
    return HttpResponse(html_content)