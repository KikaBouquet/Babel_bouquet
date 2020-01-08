from django.contrib import admin
from .models import Author, Dewey, Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        # Affichage des infos lors de la liste de toutes les publication
        "name",
        "reference",
        "type_publication",
        "genre",
        "author",
        "dewey_number",
        "label_editor",
        "isbn",
        "content",
    )
    radio_fields = {"type_publication": admin.HORIZONTAL}
    list_publication = ("type_publication", ("isbn", "dewey_number"))
    fieldsets = (
        # quels champs seront affichés et sous quelles catégories (Rérérences, Publications, Détails)
        ("Référence", {"fields": list_publication}),
        ("Publications", {"fields": ("name", "author", "label_editor")}),
        ("Détails", {"classes": ("collapse",), "fields": ("content", "genre"),},),
    )


class DeweyAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        'century_birth',
        "date_birth",
        "content",
        "place_birth",
    )
    fieldsets = (
        ("Identité", {"fields": (("first_name", "last_name"), "date_birth"),},),
        ("Biographie", {"classes": ("collapse",), "fields": ("content", 'place_birth'),},),
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Dewey)
admin.site.register(Publication, PublicationAdmin)
