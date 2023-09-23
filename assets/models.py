from django.db import models
import uuid

# Create the all models here.

# Company Model
class Company(models.Model):
    company_name = models.CharField(max_length=100)
    company_mail = models.EmailField(max_length=50)
    contact_info = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name


# Employee Model
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=50)
    address = models.TextField()

    class Meta:
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.full_name
    
# CategoryType Model
class CategoryType(models.Model):
    category_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_type

# Supplier Model
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=20)
    status = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.supplier_name  

# Asset Model
class Asset(models.Model):
    asset_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    qty = models.FloatField()
    price = models.FloatField()
    condition = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="AssetIMG/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Assets'

    def __str__(self):
        return f"{self.title}  {self.model} - ({self.condition}) - {self.category} "
    


# Asset Allocation Model
class AssetAllocation(models.Model):
    device = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateField()
    return_time = models.DateField()
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_return = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Assets Allocation'

    def __str__(self):
        return f"{self.device} - {self.employee}"