from django.contrib import admin
from . import models

# Register the All models here.

# Customized the CompanyAdmin
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company_name']
    list_display = ['company_name', 'company_mail', 'contact_info']

admin.site.register(models.Company, CompanyAdmin)

# Customized the EmployeeAdmin
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['full_name', 'company__company_name']
    list_display = ['company' ,'full_name', 'contact_info', 'address']

admin.site.register(models.Employee, EmployeeAdmin)

# Customized the CategoryTypeAdmin
class CategoryTypeAdmin(admin.ModelAdmin):
    search_fields = ['category_type']
    list_display = ['category_type']

admin.site.register(models.CategoryType, CategoryTypeAdmin)


# Customized the SupplierAdmin
class SupplierAdmin(admin.ModelAdmin):
    search_fields = ['supplier_name', 'contact_name']
    list_display = ['supplier_name', 'contact_name','contact_info', 'status']

admin.site.register(models.Supplier, SupplierAdmin)


# Customized the AssetAdmin
class AssetAdmin(admin.ModelAdmin):
    search_fields = ['title', 'model', 'category__category_type', 'condition', 'supplier__supplier_name']
    list_display = ['asset_id', 'title', 'model', 'category', 'qty', 'price', 'condition', 'supplier']

admin.site.register(models.Asset, AssetAdmin)

# Customized the AssetAllocationAdmin
class AssetAllocationAdmin(admin.ModelAdmin):
    search_fields = ['device', 'employee']
    list_display = ['device',  'employee', 'checkout_time', 'return_time', 'condition_on_checkout', 'condition_on_return']

admin.site.register(models.AssetAllocation, AssetAllocationAdmin)


