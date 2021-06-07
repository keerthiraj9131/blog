from django.shortcuts import render, get_object_or_404
from blogapp.models import Post
from . forms import commentForm
from taggit.models import Tag



# Create your views here.
def post_view(request,tag_slug=None):
    post_list = Post.objects.filter(status='published')
    tag=None
    if(tag_slug):
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    return render(request, 'index.html', {'post_list': post_list,'tag':tag})


def listdetailview(request,post,year,month,day):
    post = get_object_or_404(Post,status = 'published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             slug=post)
    comments = post.comments.filter(active=True)
    csubmit = False
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            csubmit = True
    else:
        form = commentForm()
    return render(request,'detailview.html',{'post': post,'form':form,'csubmit':csubmit,'comments':comments})

from django.core.mail import send_mail
from .forms import EmailSendForm

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent= False
    if request.method == 'POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{}({}) is recommends you to read this {}'.format(cd['name'],cd['email'],post.title)
            message = 'Read post at {} \n\n {}\'s comments: {}'.format(url,cd['name'],cd['comments'])
            send_mail(subject,message,'raj@gmail.com',[cd['to']])
            sent= True
    else:
        form = EmailSendForm()
    return render(request,'sharebyemail.html',{'form':form,'post':post,'sent':sent})

