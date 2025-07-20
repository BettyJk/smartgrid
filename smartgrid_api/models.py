from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

class User(AbstractUser):
    ROLE_CHOICES = (
        ('operator', 'Operator'),
        ('supervisor', 'Supervisor'),
    )
    SHIFT_CHOICES = (
        ('A', 'Shift A'),
        ('B', 'Shift B'),
        ('Night', 'Night'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='operator')
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, blank=True, null=True)

class Audit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    usine = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    global_remark = models.TextField(blank=True, null=True)
    operator_signature = models.CharField(max_length=255, blank=True, null=True)  # Changed from ImageField
    supervisor_signature = models.CharField(max_length=255, blank=True, null=True)  # Changed from ImageField
    code_route = models.CharField(max_length=100, blank=True, null=True)
    cofor_audite = models.CharField(max_length=100, blank=True, null=True)
    el_bl = models.CharField(max_length=100, blank=True, null=True)

class NonConformite(models.Model):
    audit = models.ForeignKey('Audit', related_name='nonconformites', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    code_anomalie = models.CharField(max_length=50)
    chapitre_mlp = models.CharField(max_length=50, blank=True, null=True)
    um = models.BooleanField(default=False)
    uc = models.BooleanField(default=False)
    ugs = models.BooleanField(default=False)
    avexp = models.BooleanField(default=False)
    remark = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

class GridRow(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    anomalie = models.CharField(max_length=255)
    chapitre = models.CharField(max_length=255, blank=True, null=True)
    code_anomalie = models.CharField(max_length=50, blank=True, null=True)
    um = models.CharField(max_length=50, blank=True, null=True)
    uc = models.CharField(max_length=50, blank=True, null=True)
    ums = models.CharField(max_length=50, blank=True, null=True)
    bl = models.CharField(max_length=50, blank=True, null=True)
    aviexp = models.CharField(max_length=50, blank=True, null=True)
    info_sup = models.TextField(blank=True, null=True)
    um_enabled = models.BooleanField(default=True)
    uc_enabled = models.BooleanField(default=True)
    ugs_enabled = models.BooleanField(default=True)  # changed from ums_enabled
    bl_enabled = models.BooleanField(default=True)
    avexp_enabled = models.BooleanField(default=True)  # changed from aviexp_enabled

    def __str__(self):
        return f"{self.anomalie} - {self.chapitre}"

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Role', {'fields': ('role',)}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'user', 'usine', 'reference')
    search_fields = ('usine', 'reference', 'user__username')
    list_filter = ('usine', 'user')

@admin.register(NonConformite)
class NonConformiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'audit', 'category', 'label', 'code_anomalie', 'um', 'uc', 'ugs', 'avexp')
    search_fields = ('category', 'label', 'code_anomalie')
    list_filter = ('category', 'um', 'uc', 'ugs', 'avexp')
