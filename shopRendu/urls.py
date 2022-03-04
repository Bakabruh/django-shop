"""shopRendu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, delete_product
from django.conf.urls.static import static
from shopRendu import settings
from login.views import signup, logout_user, login_user
from messagerie.views import messagerie

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('product/<str:slug>', product_detail, name="product"),
    path('delete/<int:id>', delete_product, name="delete_product"),
    path('messagerie/', messagerie, name="messagerie")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
