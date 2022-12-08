from django.contrib import admin
from mainapp.models import News, Courses, Lesson, CourseTeachers
from django.utils.html import format_html


admin.site.register(Courses)
admin.site.register(Lesson)
admin.site.register(CourseTeachers)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted', 'slug')
    list_filter = ('deleted',)
    ordering = ('pk',)
    list_per_page = 1
    search_fields = ('title',)
    actions = ('mark as delete',)
    

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            obj.title.lower().replace(' ','-'),
            obj.title
            )

    
    slug.short_dscription = 'Clug!'

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Mark deleted'