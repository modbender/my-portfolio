from django.contrib import admin

from .models import Skill, Profile, Category, Post, Work, Service

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    autocomplete_fields = ('skills',)
    save_on_top = True

    class Media:
        from django.conf import settings

        css = {
            'all' : (settings.STATIC_URL + 'css/profileAdmin.css', )
        }

    def changelist_view(self, request, extra_context=None):
        p = Profile.objects.all().order_by('added_at').first()
        return self.change_view(request, object_id=str(p.id) if p else None)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
