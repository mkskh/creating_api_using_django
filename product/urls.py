from django.urls import path
from . import views


app_name = "product"

urlpatterns = [
    path("all/", views.ProductList.as_view(), name="all"),
    path("create/", views.ProductCreate.as_view(), name="create"),
    path("delete/<int:pk>/", views.ProductDelete.as_view(), name="delete"),
    path("<str:name>/", views.ProductDetail.as_view(), name="detail"),
]
