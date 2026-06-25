from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['business', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'business']
    search_fields = ['comment', 'user__username', 'business__name']
    ordering = ['-created_at']