from django.contrib import admin
from django.forms import TextInput, ModelForm

from rango.models import Category, Page, UserProfile

from suit.widgets import NumberInput
from suit_redactor.widgets import RedactorWidget
from suit_ckeditor.widgets import CKEditorWidget


class PageForm(ModelForm):
    class Meta:
        widgets = {
            'title': CKEditorWidget(),
            'views': NumberInput,
        }


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    search_fields = ('title',)
    list_display = ('title', 'category', 'url')

    fieldsets = [
        ('Title', {
            'classes': ('suit-tab', 'suit-tab-title',),
            'fields': ['title']
        }),
        ('Category', {
            'classes': ('suit-tab', 'suit-tab-category',),
            'fields': ['category']}),
        ('Info', {
            'classes': ('suit-tab', 'suit-tab-info',),
            'fields': ['url', 'views']}),
    ]

    suit_form_tabs = (
        ('title', 'Title'), ('category', 'Category'), ('info', 'Info'),
    )


class CategoryForm(ModelForm):
    class Meta:
        widgets = {
            'name': RedactorWidget(editor_options={'lang': 'en'})
        }


class CategoryAdmin(admin.ModelAdmin):

    form = CategoryForm

    list_display = ('name', 'views', 'likes', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)