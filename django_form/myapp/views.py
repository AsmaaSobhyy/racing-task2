from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm 
from .forms import SnippetForm



def contact (request):
    if request.method =='POST':
        form = ContactForm(request.POST)
    form = ContactForm()    
    if form.is_valid() :
        name = form.cleaned_data['name']
        email =form.cleaned_data['email']
        print(name,email)

    
    return render(request,'form/form.html',{'form': form})

def Snippet_detail (request) :  
    if request.method =='POST':
        form = SnippetForm(request.POST)
    form = SnippetForm()    
    if form.is_valid():
        form.save(commit=False)

    
    return render(request,'form/form.html',{'form': form})