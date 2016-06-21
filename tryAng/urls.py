"""tryAng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from PiParse.views import PiPostsViewSet, saveViewed, Comments, Friendlist
from Angular2 import views as Angular2View
from rest_framework_jwt.views import obtain_jwt_token

from myLogger.views import myLoggerGroupViewSet

router = routers.DefaultRouter()
router.register(r'PiParse', PiPostsViewSet, base_name="PiPosts")
router.register(r'logger', myLoggerGroupViewSet, base_name='Logger')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jasmine/', Angular2View.AngJasmine),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-register/$', Angular2View.Register),
    url(r'^api/viewed/$', saveViewed.as_view()),
    url(r'^api/comments/$', Comments.as_view()),
    url(r'^api/friendlist/$', Friendlist.as_view()),
    url(r'^', Angular2View.AngIndex),
]
