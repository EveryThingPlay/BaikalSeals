from django.contrib import admin
from api.forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

from .models import *

admin.site.register(position)


class FinRequestInlineAdmin(admin.StackedInline):
    model = finance_request

class LongSickInlineAdmin(admin.StackedInline):
    model = long_sick_request

class VacInlineAdmin(admin.StackedInline):
    model = vacation_request

class SickInlineAdmin(admin.StackedInline):
    model = sick_request


class TaskInlineAdmin(admin.StackedInline):
    model = task

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    inlines = [TaskInlineAdmin, FinRequestInlineAdmin, VacInlineAdmin, SickInlineAdmin, LongSickInlineAdmin]
    list_display = ('email', 'role', 'is_staff', 'is_active',)
    list_filter = ('role', 'is_staff', 'is_active', 'gender', 'remote', 'workStart')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'father_Name', 'position', 'phone', 'extraPhone', 'vacationName', 'vacationRole', 'spentaimes', 'remote', 'skype', 'telegram', 'birthday', 'office', 'division', 'entity', 'status', 'employment', 'workStart', 'gender')}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(finance_request)
class RequesstAdmin(admin.ModelAdmin):
    model = finance_request
    list_display = ('approved','text', 'price', 'owner')
    list_filter = ('approved',)
    
@admin.register(vacation_request)
class VacationAdmin(admin.ModelAdmin):
    model = vacation_request
    list_display = ('approved', 'first_date', 'last_date', 'owner', 'paid')
    list_filter = ('approved', 'paid')    

@admin.register(sick_request)
class SickAdmin(admin.ModelAdmin):
    model = sick_request
    list_display = ('approved', 'first_date', 'last_date', 'owner')
    list_filter = ('approved', )

@admin.register(long_sick_request)
class LongSickAdmin(admin.ModelAdmin):
    model = long_sick_request
    list_display = ('approved', 'first_date', 'last_date', 'owner')
    list_filter = ('approved', )