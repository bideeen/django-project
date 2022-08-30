from re import template
from django.template import loader
from django.http import *
from django.urls import *
from .models import Posts
import datetime

# Create your views here.
def index(request):
    posts = Posts.objects.all().values()
    template = loader.get_template('post.html')
    context = {
        'allposts': posts,
    }
    return HttpResponse(template.render(context, request))

def add_post(request):
    name = request.POST['name']
    post = request.POST['post']
    time = datetime.datetime.now()
    
    feeds = Posts(name=name, post=post, time=time)
    feeds.save()
    
    return HttpResponseRedirect(reverse('index'))
