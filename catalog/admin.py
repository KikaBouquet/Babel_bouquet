from django.contrib import admin
from .models import Author, Dewey, Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'reference', 'type_publication', 'genre', 'author', 'dewey_number', 'label_editor')


admin.site.register(Author)
admin.site.register(Dewey)
admin.site.register(Publication, PublicationAdmin)
