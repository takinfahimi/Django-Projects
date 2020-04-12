from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from .models import user, course
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django import forms

# Create your views here.

def index(request):
    course_list = course.objects.all()
    args = {'courses': course_list}
    return render(request, 'main_page/index.html', args)


@csrf_protect
def register(request):
    # registered = False
    # if request.method=='POST':

    reg_form = RegisterForm(request.POST)
    if reg_form.is_valid():
        reg_form.save()
        print("Valid")
    # registered=True

    # else:
    # 	reg_form = RegisterForm()
    if not reg_form.is_valid():
        print("Not valid")

    return render(request, 'main_page/Registration.html', {'reg_form': reg_form})

def about(request):
    return render(request, 'main_page/about.html')


def whatsapp_redirect(request):
    return HttpResponseRedirect('https://wa.me/00994513557271')
