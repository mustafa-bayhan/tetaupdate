from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .models import *
import requests



"""               captcha                 """

def recaptcha_check(recaptcha_response): #2
    verify_url = 'https://www.google.com/recaptcha/api/siteverify' #3
    value = { #4
        'secret': '6Lc_NoQkAAAAAFwDxzVnetlEpqhLnQ4wQMS5jBL4',
        'response': recaptcha_response
    }
    response = requests.post(verify_url, value) #5
    result = response.json() #6
    if result['success'] is True: #7
        return True
    else: #8
        return {'status': result['success'], 'reason': result['error-codes']} #


"""               captcha                 """


def index(request):
    query2=request.GET.get('s')
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    context = {}
    web = Website.objects.all().order_by('-publishing_date','-id').distinct()
    context['website']=web
    context['all_web'] = web[:9]
    context['customer_comments']= CustomerComments.objects.all().order_by('-created_date').distinct()
    context['last_posts']=Post.objects.all().filter(Q(completed__iexact='completed')).order_by('-publishing_date').distinct()[:5]
    context['duyurular']=Duyuru.objects.all().order_by('-publishing_date').distinct()
    context['instagram']=Instagram.objects.all().order_by('-date_num').distinct()
    return render(request, 'index.html', context)
   

# Create your views here.
def blog(request):
    
    context1 = {}
    
    all_posts=Post.objects.all().filter(Q(completed__iexact='completed')).distinct()
    cat_request=request.GET.get('q')
    if cat_request:
        all_posts= all_posts.filter(
            Q(category__name__iexact=cat_request)
        ).distinct()
    query2=request.GET.get('s')
    if query2:
        all_posts= all_posts.filter(
            Q(category__name__icontains=query2)|Q(body__icontains=query2)|Q(title__icontains=query2)|Q(title__icontains=query2)|Q(summary__icontains=query2)
        ).distinct()
        
        
    
    paginator = Paginator(all_posts, 6) # bir sayfada kaç tane görünmesi gerek
    context1['filter_count']=paginator.count
    page_num = request.GET.get('page')
    page=paginator.get_page(page_num)
    
    context1['count']=paginator.count
    context1['page'] = page  
    page_number=page.number

    if page_number !=None:
        fark=int(paginator.num_pages) - int(page_number)
       
        if fark >= 2:
            context1['last'] = ('last')
            if fark > 2:
                context1['last_three'] = ('last_three')
                
            
        if int(page_number) >= 3:
            context1['first'] = ('first')
            
            if int(page_number) > 3:
                context1['three_dot'] = ('three_dot')
            
    else:

        
        if paginator.num_pages-1 >= 2:
            context1['last_true'] = ('last')
            if paginator.num_pages-1 >2:
                
                context1['last_three'] = ('last_three')
  


    
    context1['all_posts']=all_posts
    context1['all_cats']=Category.objects.all().distinct()
    context1['most_read']=Post.objects.all().filter(Q(completed__iexact='completed')).order_by('-read').distinct()[:5]
    context1['website']=Website.objects.all().distinct()[::-1]
    return render(request, 'blog.html', context1)

def about(request):
    query2=request.GET.get('s')
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    context2 = {}
    context2['website']=Website.objects.all().distinct()[::-1]
    context2['about']=About.objects.all().distinct()[0]
    context2['duyurular']=Duyuru.objects.all().order_by('-publishing_date').distinct()
    return render(request, 'about-us.html', context2)

def contact(request):
    query2=request.GET.get('s')
    context3 = {}
    
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    
    context3['website']=Website.objects.all().distinct()[::-1]
    if request.method=="POST":
        
        recaptcha_response = request.POST.get('g-recaptcha-response') #8
        recaptcha_response_result = recaptcha_check(recaptcha_response) #9
        username=request.POST.get('name')
        mail=request.POST.get('email')
        number=request.POST.get('phone')
        comment=request.POST.get('comment')
        
        if recaptcha_response_result is True:
            make_comment = Usermessage.objects.create(name=username,mail=mail, telefon=number, content=comment)
            make_comment.save()
            
            return redirect(request.META['HTTP_REFERER'])
            
        else:
        
           
            context3['username']=request.POST.get('name')
            context3['mail']=request.POST.get('email')
            context3['number']=request.POST.get('phone')
            context3['comment']=request.POST.get('comment')
            context3['error'] = 'Lütfen robot olmadığınızı doğrulayınız!'
            return render(request,'contact-us.html',context3)
    
    
    return render(request, 'contact-us.html', context3)

def career(request):
    query2=request.GET.get('s')
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    context4 = {}
    context4['website']=Website.objects.all().distinct()[::-1]
    context4['jobs']=Job.objects.all().distinct()[::-1]
    return render(request, 'career.html', context4)

def services(request):
    query2=request.GET.get('s')
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    context5 = {}
    context5['website']=Website.objects.all().order_by('-publishing_date','-id').distinct()
    return render(request, 'services.html', context5)

def post_detail(request, slug):
    context6={}
    query2=request.GET.get('s')
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    post11=get_object_or_404(Post, slug=slug)
  
    
    read = post11.read
    read += 1
    degıs = Post.objects.filter(slug=slug).update(read=read)
    context6['website']=Website.objects.all().distinct()[::-1]
    context6['post11'] = post11
    context6['most_read']=Post.objects.all().filter(Q(completed__iexact='completed')).order_by('-read').distinct()[:5]
   
   
    return render(request, 'blog-detail.html', context6)


def gizlilik(request):
    query2=request.GET.get('s')
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    context8 = {}
    context8['website']=Website.objects.all().order_by('-publishing_date','-id').distinct()
    return render(request, 'gizlilik-politikasi.html', context8)




def handle_not_found(request, exception):
    context7={}
    context7['website']=Website.objects.all().distinct()[::-1]
    query2=request.GET.get('s')
    if query2:
        return HttpResponseRedirect('/blog?s={}'.format(query2))
    return render(request, '404.html',context7)