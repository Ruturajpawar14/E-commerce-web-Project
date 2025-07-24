
from django.contrib import admin
from django.urls import path

from learning import views
from django.conf import settings  # for media url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Homepage ,name="home" ),
    path('About', views.Aboutpage, name="about" ),
    path('saveenquiry', views.saveEnquiry, name="saveenquiry" ),
    path('Blogpage', views.Blogpage, name="blog" ),
    path('Chartpage', views.Chartpage, name="chart" ),
    path('Contactpage', views.Contactpage, name="contact" ),
    path('shop', views.shop, name="shop" ),
    path('sproduct', views.sproduct, name="sproduct" ),
    path('userform',views.userform, name="userform"),
                                                  
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    