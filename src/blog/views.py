from django.shortcuts import render

posts =[
    {
        'title' :'التدوينة 1',
        'content': '  1نص التدوينة',
        'post_date': '15-3-2019',
        'auther' : '1فاطمة',
    },
    {
        'title' :'2 التدوينة',
        'content': ' 2نص التدوينة',
        'post_date': '15-3-2019',
        'auther' : '2فاطمة',
    },
    {
        'title' :'التدوينة 3',
        'content': ' 3نص التدوينة',
        'post_date': '15-3-2019',
        'auther' : ' 3فاطمة',
    },

]

def home(request):
    context = {
        'title' : 'الصفحة الرئيسية',
        'posts'  : posts,
    }
    return render(request, 'blog/index.html',context)