
from django.contrib import admin
from django.urls import path, include
from demoapp import urls as newurls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(newurls)),

]
