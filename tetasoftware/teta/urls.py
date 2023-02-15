from django.urls import path


from . import views

urlpatterns=[
  
    path('',views.index, name='index'),
    path('blog',views.blog, name='blog'),    
    path('about-us',views.about, name='about-us'),  
    path('contact-us',views.contact, name='contact-us'),
    path('career',views.career, name='career'),
    path('services',views.services, name='services'),
    path('blog/<slug:slug>',views.post_detail, name='post_detail'),
    path('privacy-policy',views.gizlilik, name='gizlilik-politikasi'),
    
   
]


