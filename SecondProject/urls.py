from django.contrib import admin
from django.urls import path, include
from SecondApp import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    # path('', views.home_view, name='display'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_views, name='contact'),
    path('post/', views.post, name='post'),
    path('admin/', admin.site.urls),
    #path('signup/', views.signup_view, name='signup'),
    #path('signin/', views.login_view, name='signin'),
    # path('signout/', views.signout_view, name='signout'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('display/', views.display_blog_posts, name='display'),
    path('update_blog/<int:pk>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('search/', views.search_results, name='search_results'),
    path('users/', include("users.urls"))

  
      
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
