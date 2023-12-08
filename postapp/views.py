from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def posts(request):
    posts = Post.objects.all()
    return render(request, "posts.html", {'posts':posts})

def post(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, "post.html", context={"post":post})
def bookCreate(request):  
    if request.method == "POST":  
        form = PostForm(request.POST)  
        if form.is_valid():   
            form.save() 
            model = form.instance
            return redirect('book-list')  
    else:  
        form = PostForm()  
    return render(request,'book-create.html',{'form':form})  

def postdelete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('/posts')

def updatepost(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostForm(initial={"title":post.title, "short_desc":post.short_desc, "body":post.body})

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/posts')
    return render(request, "update.html", context={'form':form})
    