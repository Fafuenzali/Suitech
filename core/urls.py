from django.urls import path
from .views import home, blake, fireflyxl, fireflym, lc30, helios, new, popular, allp, about

urlpatterns = [
    path('', home, name="home"),
    path('blake/', blake, name="blake"),
    path('fireflyxl/', fireflyxl, name="fireflyxl"),
    path('fireflym/', fireflym, name="fireflym"),
    path('lc30/', lc30, name="lc30"),
    path('helios/', helios, name="helios"),
    path('new/', new, name="new"),
    path('popular', popular, name="popular"),
    path('allp', allp, name="allp"),
    path('about', about, name="about"),
    ]
    
