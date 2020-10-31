from django.shortcuts import render
# Create your views here.


posts = [
    {
        'author':'Rohit Sav',
        'title':'Blog title 1',
        'content':'First post content',
        'date_posted':'October 31 2020'
    },
    {
        'author':'James',
        'title':'Blog title 2',
        'content':'Second post content',
        'date_posted':'October 30 2020'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title':'About Page'})
