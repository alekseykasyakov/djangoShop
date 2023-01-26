from django.contrib import admin
from .models import Categories, CategoriesDescription
# Register your models here.


# admin.site.register(Categories)
# admin.site.register(CategoriesDescription)

class CategoriesInline(admin.TabularInline):
    model = CategoriesDescription


# Register the Admin classes for Book using the decorator

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('categories_image', 'parent_id', 'sort_order', 'date_added', 'last_modified', 'categories_status')
    fields = ['categories_image', 'parent_id', 'sort_order', 'categories_status']
    inlines = [
            CategoriesInline,
        ]
# Register the Admin classes for BookInstance using the decorator



@admin.register(CategoriesDescription)
class CategoriesDescriptionAdmin(admin.ModelAdmin):
    list_display = ('categories_name',)
    list_fields = ['categories', 'language_id', 'categories_name', 'categories_heading_title', 'categories_description', 'categories_meta_title', 'categories_meta_description', 'categories_meta_keywords', 'categories_seo_url']



