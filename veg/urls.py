"""
URL configuration for veg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from veg import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
# from veg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show,name="home"),
    path('recipe/', views.recipedata,name="recipe"), #recipe/
    path('delete/<id>',views.delete ,name="delete"),
    path('update/<id>',views.updateresipe, name="update"),
    # path('do_update/<id>',views.do_update, name="do_update")
    path('login/',views.login_page, name="login"),
    path('register/',views.register, name="register"),
    path('logout/', views.logout_page, name="logout")

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()