from django import template
from blog.models import Post,Comment


register= template.Library()
@register.inclusion_tag('blog/lastest_post.html')
def lastest_posts():
    context = {
        'l_post' : Post.objects.all()[0:5]
    }
    return context


@register.inclusion_tag('blog/lastest_comments.html')
def lastest_comments():
    context={
        'l_comment' : Comment.objects.filter(active = True)[0:5]
    } 
    return context