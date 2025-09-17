from django.contrib import admin
from .models import About, Trainer, Expertise, Testimonial
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    summernote_fields = ('content',)


@admin.register(Trainer)
class TrainerAdmin(SummernoteModelAdmin):
    list_display = ('name', 'role', 'updated_at')
    search_fields = ('name', 'role')
    summernote_fields = ('bio',)


@admin.register(Expertise)
class ExpertiseAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    summernote_fields = ('content',)


@admin.register(Testimonial)
class TestimonialAdmin(SummernoteModelAdmin):
    list_display = ('client_name', 'updated_at')
    search_fields = ('client_name',)
    summernote_fields = ('feedback',)
