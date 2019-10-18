from django.shortcuts import render
from test_app.models import TestModel
from test_app.forms import TestModelForm

# Create your views here.
def index(request):
    data_set = {}
    return render(request,"test_app/index.html",data_set)

def getall(request):
    objects = TestModel.objects.all()
    data_set = {'objects':objects}
    return render(request,"test_app/getall.html",data_set)

def addnew(request):
    form = TestModelForm()
    if request.method == "POST":
        form = TestModelForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return getall(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'test_app/addnew.html',{'form':form})
