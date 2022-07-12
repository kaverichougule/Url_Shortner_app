from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from .models import Url

# Create your views here.
def url_shortner(request):
    if request.method == "POST":
        full_url = request.POST.get('full_url')
        obj = Url.create(full_url)
        return render(request,'url_shortner/url_shortner.html',{'full_url':obj.full_url,'short_url': request.get_host() +'/'+obj.short_url})

    
    return render(request,'url_shortner/url_shortner.html')

def routToURL(request,key):
    try:
        obj = Url.objects.get('short_url=key')
        return redirect(obj.full_url)
    except:
        return redirect('url_shortner')

    #return redirect('')