
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#sys.path.insert(0, '/Users/adiop.PC-CLEGE/Documents/cloudsen/blog/ftp')
from  .views import UserViewSet, GroupViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ftp.urls')),
    path('myaccount/', include('myaccount.urls')),
    path('emailusers/', include('ldap.urls')),
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
