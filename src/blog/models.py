from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title      = models.CharField(max_length = 100)
    content    = models.TextField()
    post_date  = models.DateTimeField(default=timezone.now)
    post_update= models.DateTimeField(auto_now = True)
    author     = models.ForeignKey(User ,on_delete =models.CASCADE)
   
      #fontion for display title in adminPanel
    def __str__(self):
        return self.title

    class Meta :
        ordering = ('-post_date',)   



class Comment(models.Model) :
  name         = models.CharField( max_length = 50,  verbose_name= 'الاسم')   
  email        = models.EmailField(verbose_name= 'الايميل')
  body         = models.TextField(verbose_name= 'التعليق')
  comment_date = models.DateTimeField(auto_now_add =True)
  active       = models.BooleanField(default = False)
  post         = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')   
 
  def __str__ (self):
    return 'علق {} على {}.'.format(self.name,self.post)

  class Meta:
    ordering =('-comment_date',)  