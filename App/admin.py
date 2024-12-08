from django.contrib import admin
from .models import (GeneralInfo, 
                     Services,
                       Testemonail, 
                       FrequentlyAskedQuestions, 
                       ContactFormLog, 
                       Blog,
                       Authur
                       )


# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    
    list_display = [
        'company_name',
        'location',
        'email',
        'phone',
        'open_hours',
    ]

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
    ]

    search_fields = [
        'title','description'
    ]


@admin.register(Testemonail)
class TestemonialAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'user_job_title',
        'display_rating',
    ]

    def display_rating(self, obj):
        return "*" * obj.rating_count
    
    display_rating.short_description = "Rating"

@admin.register(FrequentlyAskedQuestions)
class FrquentlyAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'anwser',
    ]

@admin.register(ContactFormLog)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'is_success',
        'is_error',
        'action_time',
    ]
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'authur',
        'blog_image',
        'category',
        'title',
        'created',
    ]

@admin.register(Authur)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'firstname',
        'lastname',
        'country',
        'join_date'
    ]