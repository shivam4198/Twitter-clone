from doctest import OutputChecker
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):

    # if the methode is POST
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)

     # if the form is valid
        if form.is_valid():
            # yes, save
            form.save()
        # Redirect to home
            return HttpResponseRedirect('/')
        else:

            # no, show Error
            return HttpResponseRedirect(form.errors.as_json())
    # Get sll posts, limit=20

    posts = Post.objects.all().order_by('-created_at')[:20]
    # show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")
   
def edit(request,post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.erros.as_json())
    return render(request,"edit.html",{"post":post})

    
def LikeView(request,post_id):
    post= Post.objects.get(id=post_id)
    new_value = post.likes +1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
