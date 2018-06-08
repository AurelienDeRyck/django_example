"""fifi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from ave_cesar import views


urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^product/$', views.ProductListView.as_view(), name='product_list'),
    url(r'^product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^product/create/$', views.ProductCreate.as_view(), name='product_form'),
    url(r'^product/(?P<pk>\d+)/update/$', views.ProductUpdate.as_view(), name='product_update_form'),
    url(r'^product/(?P<pk>\d+)/delete/$', views.ProductDelete.as_view(), name='product_confirm_delete'),

    url(r'^category/$', views.CategoryListView.as_view(), name='category_list'),
    url(r'^category/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name='category_detail'),
    url(r'^category/create/$', views.CategoryCreate.as_view(), name='category_form'),
    url(r'^category/(?P<pk>\d+)/update/$', views.CategoryUpdate.as_view(), name='category_update_form'),
    url(r'^category/formset/$', views.CategoryFormSetView.as_view(), name='category_formset'),
    url(r'^category/(?P<pk>\d+)/delete/$', views.CategoryDelete.as_view(), name='category_confirm_delete'),
]
