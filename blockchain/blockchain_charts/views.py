from unicodedata import name
from django.shortcuts import redirect, render
from .models import Top
from .forms import TopForm





def index(request):
    top = Top.objects.all()
    if request.method =='POST':
        form = TopForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TopForm()

    context= {
        "top": top,
        "form": form,
    }

    return render(request,'chartapp/index.html',context)


def delete(request,user_id):
    delete = Top.objects.get(id=user_id)
    delete.delete()
    return redirect('http://127.0.0.1:8000/')