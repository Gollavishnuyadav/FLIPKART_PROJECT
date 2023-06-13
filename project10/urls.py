
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import *
import app1,app2
urlpatterns = [
    path("admin/", admin.site.urls),
    path("app1/",include("app1.urls")),

    
    path("app2/",include("app2.urls")),
    path("registration/",registration,name="registration"),
    path("home/",home,name="home"),
    path('user_login/',user_login,name='user_login'),
    path('user_logout/',user_logout,name='user_logout'),
    path("eight/",eight,name="eight"),
    path("payment/",payment,name="payment"),
    path('display_profile/',display_profile,name='display_profile'),
    path('change_password/',change_password,name='change_password'),
    path('reset_password/',reset_password,name='reset_password'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    