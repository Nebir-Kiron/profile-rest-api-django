from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm,UserCreationForm
# Register your models here.
user  = get_user_model()
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name','last_name','is_active', 'is_admin','is_staff')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email','first_name','last_name', 'password')}),
        ('Permissions', {'fields': ('is_admin','is_staff',)}),
    )

    add_fieldsets = (
        (
            None, {
            'fields': ('email', 'first_name','last_name', 'password1', 'password2'),
        }
      ),
      ('Permissions', {'fields': ('is_admin','is_staff',)}),
    )

    ordering = ('email',)
    search_fields = ('email',)
    filter_horizontal=()


admin.site.register(user, UserAdmin)