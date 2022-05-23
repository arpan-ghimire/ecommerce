from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views 
from . import models

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)


urlpatterns = [
    path('register/', views.RegisterUser.as_view()),
    path('login/', views.LoginUser.as_view()),
    path('allproducts/', views.AllProductsViews.as_view()),
    path('vendor-product/', views.LoogedInVendorOrderedProducts.as_view()),
]

urlpatterns += router.urls


