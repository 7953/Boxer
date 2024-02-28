from django.http import HttpResponse
from django.shortcuts import render


from . models import boxer
  
  
def demo(request):
    obj=boxer.objects.all()
  
    return render(request,"index.html",{'result':obj})
 

