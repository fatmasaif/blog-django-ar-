from re import I
from django.shortcuts import render, get_object_or_404
from . models import Post
from . forms import NewComment

def home(request):
    context = {
        'title' : 'الصفحة الرئيسية',
        'posts'  : Post.objects.all(),
    }
    return render(request, 'blog/index.html',context)



def about(request):
    context = {
        'title' : 'من أنــا ',
      
      }
    return render(request, 'blog/about.html',context)    

def post_detail(request, post_id):
    post     = get_object_or_404(Post, pk=post_id)
    comments = post.comment.filter(active =True)
    # comments معناها جيب جميع التعليقات المتعلقة بالمدونة 
    comment_form = NewComment()
    context  ={
        'title' : 'تفاصيل التدوينة',
        'post'  :  post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render (request, 'blog/post_detail.html',context)    