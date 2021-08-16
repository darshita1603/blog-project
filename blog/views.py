# from django_project.blog.models import Post
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.urls.base import reverse
from django.views.generic.edit import UpdateView
from . models import Post
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import  ListView,DetailView,CreateView,DeleteView
from django.http import HttpRequest,HttpResponse
# Create your views here.

# posts=['1','2','3','4','5']

# p=Paginator(posts,3)
# p.num_pages

# for page in p.page_range:
#     print(page)

# p1=p.page(1)
# print(p1)
# print(p1.object_list)


# print(p1.has_previous())
# print(p1.has_next())
# print(p1.next_page_number())
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

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['date_posted']
    paginate_by=2

class UserPostListView(ListView):
    model=Post
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        print(user)
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model=Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    print("wefw")
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        # print("sdf",form)
        form.instance.author=self.request.user
        print(form.instance.author)
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    print("wefw")
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        # print("sdf",form)
        form.instance.author=self.request.user
        print(form.instance.author)
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        print(post)
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url="/blog/"

    def test_func(self):
        post=self.get_object()
        print(post)
        if self.request.user==post.author:
            return True
        return False
def about(request):
   return render(request,"blog/about.html",{'titile':'About'})
