from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
     path('about',views.about,name='about'),
     path('courses',views.index,name='courses'),
      path('contact',views.contact,name='contact'),
       path('blog',views.blog,name='blog'),
        path('elements',views.element,name='element'),
         path('login',views.login,name='login'),
         path('ebooks',views.ebooks,name='ebooks'),
         path('post',views.post,name='post'),
         path('blog_details',views.blog_detail,name='blog_detail'),
         path('ads_page',views.ads,name='ads'),
         path('register',views.register,name='register'),
         path('listings',views.listings,name='listings'),
         

]
