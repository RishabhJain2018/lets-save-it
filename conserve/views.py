from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from django.views import generic
from conserve.models import UserData
from conserve.forms import *
from django.template import Context
from django.views.generic import View
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def Login(request):
	context = RequestContext(request,
							{'request':request,
							'user':request.user})
	return render_to_response('index.html',context_instance = context)



def profile(request):
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/bill')
		else:
			form=UserForm()
			return render(request,'detail.html',{'form':form})
	elif request.method=="GET":
		form=UserForm()
		return render(request,'detail.html',{'form':form})

	return render(request,'detail.html',{'form':form})

def thanks(request):
	return render_to_response("thank_you.html")

def mailer(request):
	if request.method=='POST':
		form=BillForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/thanks')
	elif request.method=="GET":
		form = BillForm()
		return render(request,'Bill details.html',{'form':form})

	return render(request,'Bill details .html',{'form':form})


def about(request):
	return render_to_response("About us.html")

def mission(request):
	return render_to_response("Our mission.html")

def works(request):
	return render_to_response("How it works.html")

def approach(request):
	return render_to_response("approach.html")