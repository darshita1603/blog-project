# from django_project.blog.models import Post
from django.shortcuts import render
from . models import Post
from django.http import HttpRequest,HttpResponse
# Create your views here.

# posts=[
#     {
#         'author':'a',
#         'title':'Blog 1',
#         'content':'first contetnt',
#         'date_posted':'Auguest 27,2021'
#     },
#     {
#         'author':'b',
#         'title':'Blog 2',
#         'content':'second contetnt',
#         'date_posted':'Auguest 28,2021'
#     }
# ]
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request,"blog/home.html",context)


def about(request):
   return render(request,"blog/about.html",{'titile':'About'})
