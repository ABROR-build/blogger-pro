from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'first_name', 'last_name', 'email', 'age', 'gender', 'adress']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'gender', 'adress',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'gender', 'adress',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# superuser: abror
# pass: abror2005

# testuser1: Test
# pass: Testing1234

# testuser2: Testeressa
# pass: Testere$$a1234

# testuser3: Ann
# pass: ahann12345