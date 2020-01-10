from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Author, Dewey, Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        # Affichage des infos lors de la liste de toutes les publication
        "name",
        "reference",
        "type_publication",
        "author",
        "dewey_number",
        "isbn",
    )
    radio_fields = {"type_publication": admin.HORIZONTAL}
    list_publication = ("type_publication", ("isbn", "dewey_number"))
    fieldsets = (
        # quels champs seront affichés et sous quelles catégories (Rérérences, Publications, Détails)
        (_("Référence"), {"fields": list_publication}),
        (_("Publication"), {"fields": ("name", "author", "label_editor")}),
        (_("Détails"), {"classes": ("collapse",), "fields": ("content", 'image_url_publication'),},),
    )
    readonly_fields = ('reference',)
    autocomplete_fields = ['author', 'dewey_number', ]
    # Fait une liste de filtre du champ number de dewey -> Fait une requette
    list_filter = ('dewey_number__number', 'author__last_name',)


class DeweyAdmin(admin.ModelAdmin):
    list_display = ("number", "name", "colored_number")
    search_fields = ['name', 'number', ]
    list_filter = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "century_birth",
        "date_birth",
        "place_birth",
    )
    fieldsets = (
        ("Identité", {"fields": (("first_name", "last_name"), "date_birth"),},),
        (
            "Biographie",
            {"classes": ("collapse",), "fields": ("image_file", "content", "place_birth", ),},
        ),
    )
    readonly_fields = ('century_birth',)
    search_fields = ('first_name', 'last_name', )
    list_filter = ('first_name', 'last_name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Dewey, DeweyAdmin)
admin.site.register(Publication, PublicationAdmin)
