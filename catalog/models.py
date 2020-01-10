from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import format_html
from .utils import get_century
# d'abord les import django, ensuite les miens


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=61, editable=False, blank=True, null=True)
    century_birth = models.IntegerField(blank=True, null=True, editable=False)
    date_birth = models.DateField(blank=True, null=True)
    place_birth = models.CharField(max_length=50, blank=True, null=True)

    date_died = models.DateField(blank=True, null=True)
    place_died = models.CharField(max_length=50, blank=True, null=True)

    content = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    image_file = models.ImageField(blank=True, null=True)

    class Meta:
        # Définition : "This is just a class container with some options (metadata) attached to the model. 
        # It defines such things as available permissions, associated database table name, whether the model is abstract or not, singular and plural versions of the name etc."
        # Ici, classer les auteurs par ordre alphabétique du nom de famille
        ordering = ['last_name']
        verbose_name = _('Auteur')

    def __str__(self):
        # __str__ -> This method returns the string representation of the object.
        if self.first_name:
            return f"{self.last_name}, {self.first_name}"
        else:
            return self.last_name
    
    def clean(self):
        if self.last_name and self.first_name:
            self.name = f"{self.first_name} {self.last_name}"
        else:
            self.name = self.last_name

        if self.date_birth:
            self.century_birth = get_century(self.date_birth)
                    
    
class Dewey(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    bg_color = models.CharField(max_length=7, blank=True, null=True, editable=False)
    text_color = models.CharField(max_length=7, blank=True, null=True, editable=False)

    def __str__(self):
        return f"{self.number} - {self.name}"

    def clean(self):
        COLORS = [    
            ('0', "#000000", "#FFFFFF"),  
            ('1', "#8B4513", "#FFFFFF"), 
            ('2', "#FF0000", "#FFFFFF"),
            ('3', "#FF4500", "#FFFFFF"), 
            ('4', "#FFFF00", "#000000"),
            ('5', "#32CD32", "#FFFFFF"), 
            ('6', "#1E90FF", "#FFFFFF"),
            ('7', "#8B008B", "#FFFFFF"),  
            ('8', "#A9A9A9", "#000000"),
            ('9', "#FFFFFF", "#000000"),  
        ]

        if self.number:
            first_number = str(self.number)
            first_number = first_number[0]

            for c in COLORS:
                i = c[0]
                if i == first_number:
                    self.bg_color = c[1]
                    self.text_color = c[2]

    class Meta:
        ordering = ['number']
        verbose_name = _('Classement Dewey')
        
    def colored_number(self):                
        return format_html(
            '<div class="dewey_color p-2" style="background-color: {}; color: {};">{}</div>',
            self.bg_color,
            self.text_color,
            self.number,
        )
    

class Publication(models.Model):

    TYPE_PUBLICATION_CHOICES = [
        ('-', 'Indéfini'),
        ('B', 'Livre'),
        ('M', 'Musique'),
        ('F', 'Film')
    ]
    
    name = models.CharField(max_length=30, blank=True, null=True)
    type_publication = models.CharField(max_length=1, choices=TYPE_PUBLICATION_CHOICES, default='-')
    genre = models.CharField(max_length=35, blank=True, null=True)

    author = models.ForeignKey(Author, models.PROTECT, null=True)
    reference = models.CharField(max_length=61, blank=True, null=True, editable=False)
    dewey_number = models.ForeignKey(Dewey, models.PROTECT, null=True)
    isbn = models.CharField(max_length=15, blank=True)

    date_publication = models.DateField(blank=True, null=True)
    nb_tracks_pages = models.IntegerField(blank=True, null=True)
    label_editor = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_url_publication = models.URLField(blank=True, null=True)

    def __str__(self):
        if self.reference:
            return f"{self.reference} - {self.name}"
        else:
            return f"{self.name}"

    def clean(self):
        # Création de la référence pour chaque publication
        # pk = primary key
        if self.dewey_number and self.author:
            self.reference = f"{self.dewey_number.number}.{self.author.last_name[:3].upper()}.{self.pk}"
        else:
            self.reference = ""
