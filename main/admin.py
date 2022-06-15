from django.contrib import admin

from . models import * 

# Register your models here.

admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','timestamp' ,'name')

admin.site.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')

admin.site.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_field = ('slug')

admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_field = ('slug')

admin.site.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')