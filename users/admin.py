from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from common.admin import DjangoGamesAdmin
from common.utils.admin import append_fields, move_fields, remove_fields


CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(DjangoGamesAdmin, UserAdmin):
    model = CustomUser
    list_display = UserAdmin.list_display + ('is_superuser', 'id')
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    new_fields = ('dob', 'avatar')
    append_fields(UserAdmin.fieldsets, 'Personal info', new_fields)
    move_fields(UserAdmin.fieldsets, 'Personal info', None, ('email',))
    remove_fields(UserAdmin.fieldsets, None, ('password',))

    new_fields = ('email', )
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, None, new_fields)

    optional_fields = ('first_name', 'last_name', 'dob')
    add_fieldsets = append_fields(UserAdmin.add_fieldsets,
                                  'Optional Fields', optional_fields)

    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)
