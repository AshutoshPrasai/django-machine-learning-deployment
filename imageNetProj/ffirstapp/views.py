from django.shortcuts import render

# Create your views here.
from django.core.files.storage import FileSystemStorage


def index(request):
    context={'a':1}
    return render(request,'index.html',context)


def predictImage(request):
    print (request)
    print (request.POST.dict())
    fileObj=request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileObj.name,fileObj)
    filePathName=fs.url(filePathName)

    context={'filePathName':filePathName}
    return render(request,'index.html',context)     
