from assets.models import *
from rest_framework import serializers


# Create CompanyModelSerializer
class CompanyModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Company
    fields = '__all__'


# Create EmployeeModelSerializer
class EmployeeModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Employee
    fields = '__all__'


# Create CategoryTypeModelSerializer
class CategoryTypeModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=CategoryType
    fields = '__all__'


# Create SupplierModelSerializer
class SupplierModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Supplier
    fields = '__all__'


# Create AssetModelSerializer
class AssetModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Asset
    fields = '__all__'


# Create AssetAllocationModelSerializer
class AssetAllocationModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=AssetAllocation
    fields = '__all__'