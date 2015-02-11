from django.shortcuts import render_to_response
from django.template import RequestContext

def index_view(request):
    return  render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
    return render_to_response('home/about.html',context_instance=RequestContext(request))

