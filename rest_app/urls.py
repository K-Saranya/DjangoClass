from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('productsViewset', ProductsAPIViewset)



urlpatterns = [
    path('products/', ProductsCRUDAPI.as_view()),
    path('products/<int:productId>/', ProductsCRUDAPI.as_view()),
    path('productsFunction/', ProductsCRUDAPIFunction),
    path('productsFunction/<int:productId>/', ProductsCRUDAPIFunction),
    path('productsGenerics/', ProductsPOSTAPIGenerics.as_view()),
    path('productsGenerics/<int:pk>/', ProductsUPDATEAPIGenerics.as_view()),
    path('', include(router.urls))

    

]
