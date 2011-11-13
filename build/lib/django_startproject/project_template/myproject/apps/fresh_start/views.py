from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import media

def index(request):
	return render(request, 'fresh_start/index.html', locals(), context_instance=RequestContext(request))
	
def login(request):
	return render(request, 'fresh_start/login.html', locals(), context_instance=RequestContext(request))
	
def signup(request):
	return render(request, 'fresh_start/signup.html', locals(), context_instance=RequestContext(request))
	
def features(request):
	return render(request, 'fresh_start/features.html', locals(), context_instance=RequestContext(request))
	
def learn(request):
	return render(request, 'fresh_start/learn.html', locals(), context_instance=RequestContext(request))
	
def faqs(request):
	return render(request, 'fresh_start/faqs.html', locals(), context_instance=RequestContext(request))
	
def support(request):
	return render(request, 'fresh_start/support.html', locals(), context_instance=RequestContext(request))