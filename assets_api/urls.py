from django.urls import path, include
from . import views
from rest_framework import routers




# Create separate routers for the all View

# CompanyViewSet
company_router = routers.DefaultRouter()
company_router.register(r'', views.CompanyViewSet)

# EmployeeViewSet
employee_router = routers.DefaultRouter()
employee_router.register(r'', views.EmployeeViewSet)

# EmployeeViewSet
employee_router = routers.DefaultRouter()
employee_router.register(r'', views.EmployeeViewSet)

# CategoryTypeViewSet
category_router = routers.DefaultRouter()
category_router.register(r'', views.CategoryTypeViewSet)

# SupplierViewSet
supplier_router = routers.DefaultRouter()
supplier_router.register(r'', views.SupplierViewSet)

# AssetsViewSet
asset_router = routers.DefaultRouter()
asset_router.register(r'', views.AssetsViewSet)

# AssetAllocationViewSet
asset_allocation_router = routers.DefaultRouter()
asset_allocation_router.register(r'', views.AssetAllocationViewSet)


urlpatterns = [
     # Include the URLs for all ViewSet
    path('company', include(company_router.urls)),
    path('employee', include(employee_router.urls)),
    path('category', include(category_router.urls)),
    path('supplier', include(supplier_router.urls)),
    path('asset', include(asset_router.urls)),
    path('asset-allocation', include(asset_allocation_router.urls)),
   
]