from django.shortcuts import render
from testapp.models import Post

from django.views.generic import DetailView
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def post_view(request):
    post_list=Post.objects.all()
    my_dict={'post_list':post_list}
    return render(request,'html/home.html',my_dict)



class post_detail_view(DetailView):
    model=Post
    #post_detail.html
    #post or object

def email_view(request):
    if request.method=='POST':
        email=request.POST['email']
        message=request.POST['body']
        print(email,message)
        send_mail('First Email',
        message,
        settings.EMAIL_HOST_USER,
        [email],
        )



    return render(request,"html/email.html")
