from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductsViewSet, basename='products')
router.register('collections', CollectionViewSet, basename='collections')
router.register('customers', CustomerViewSet)
router.register('carts', CartViewSet)
router.register('orders', OrderViewSet, basename='orders')

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, 'product-reviews')


carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + products_router.urls + carts_router.urls



