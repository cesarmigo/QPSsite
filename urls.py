from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('book/<int:book_id>',views.book_by_id, name='book_by_id'),
    path('reviews/',views.reviews, name='Reviews'),
    path('contact_us/',views.contact_us, name='Contact Us'),
    path('gallery/', views.gallery, name='gallery'),
    path('home/', views.index, name = 'home'),
    path('gallery/newmain',views.newmain, name='newmain'),
    path('next/', views.next, name='next'),
    path('next2/',views.ske, name='next2'),
    path('next3/',views.skeleton2,name='next3')

]
