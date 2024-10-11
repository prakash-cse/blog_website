from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import table1,aboutus
import logging
from django.http import Http404
from django.core.paginator import Paginator
from .forms import contactform

# Create your views here.
# static demo data in list
# lis = [
#         {'id':1,'title':'post1','content':'content of post1'},
#         {'id':2,'title':'post2','content':'content of post2'},
#         {'id':3,'title':'post3','content':'content of post3'},
#         {'id':4,'title':'post4','content':'content of post4'},
#         {'id':5,'title':'post5','content':'content of post5'}
#     ]

def home(request):
    blog_value = 'Latest Posts'
    #getting data from post model
    lis = table1.objects.all()

    #paginate
    paginator = Paginator(lis,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request,'home.html',{'blog_value': blog_value,'page':page_obj})

def product_detail(request,slug):
    #static data
    #post = next((item for item in lis if item['id'] == int(pk)), None)

    #get model data by post id 
    try:
        post = table1.objects.get(slug=slug)
        related_post = table1.objects.filter(category = post.category).exclude(pk = post.id)

    except table1.DoesNotExist:
        raise Http404("post does not exist!")

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    return render(request,'product_detail.html',{'tit':post,'list_post':related_post})

def old_url(request):
    return redirect(reverse("blog:new_page_url"))

def new_url(request):
    return HttpResponse("this is the new url")

def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger=logging.getLogger('testing')
        if form.is_valid():
            logger.debug(f"post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = "your email has been sent!"
            return render(request,'contact.html',{'form':form, 'success_message':success_message})
        else:
            logger.debug("form validation failure")
        return render(request,'contact.html',{'form':form, 'name':name, 'email':email, 'message':message})
    return render(request,'contact.html')

def about(request):
    about_us = aboutus.objects.first().content
    return render(request,'about.html',{'about_us':about_us})

