from django.contrib import admin
from . models import *



admin.autodiscover()
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'role_id')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role_id',)
    autocomplete_fields = ['role_id']

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'work_time_start', 'work_time_end', 'user')
    search_fields = ('name', 'address')
    list_filter = ('user',)
    autocomplete_fields = ['user']

@admin.register(ClubsComputer)
class ClubsComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'computer_number', 'gpu', 'cpu', 'ram', 'club', 'is_active')
    list_filter = ('club', 'is_active')
    search_fields = ('computer_number', 'gpu', 'cpu', 'ram')
    autocomplete_fields = ['club', 'instance']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_date', 'end_date', 'is_active', 'club_computer', 'user')
    list_filter = ('is_active', 'club_computer', 'user')
    search_fields = ('club_computer__computer_number', 'user__email')
    autocomplete_fields = ['club_computer', 'user']

@admin.register(UserMainTransaction)
class UserMainTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'transaction_type', 'user', 'club')
    list_filter = ('transaction_type', 'club')
    search_fields = ('user__email', 'club__name')
    autocomplete_fields = ['user', 'club']

@admin.register(UserBonusTransaction)
class UserBonusTransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'transaction_type', 'user', 'club')
    list_filter = ('transaction_type', 'club')
    search_fields = ('user__email', 'club__name')
    autocomplete_fields = ['user', 'club']

@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon_url')
    search_fields = ('name',)

