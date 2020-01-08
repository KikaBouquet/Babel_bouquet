from django.db import models
from .utils import get_century


class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    name = models.CharField(max_length=61, editable=False, blank=True, null=True)
    century_birth = models.IntegerField()
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
        # Ici, classer les autheurs par ordre alphabétique du nom de famille
        ordering = ['last_name']

    def __str__(self):
        # __str__ -> This method returns the string representation of the object.
        if self.first_name:
            return f"{self.last_name}, {self.first_name}"
        else:
            return self.last_name
    
    def clean(self):
        if self.last_name and self.first_name:
            self.nom = f"{self.first_name} {self.last_name}"
        else:
            self.nom = self.last_name

        if self.date_birth:
            year = self.date_birth.year
            self.century_birth = get_century(year)  
                    
    
class Dewey(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    bg_color = models.CharField(max_length=7, blank=True, null=True)
    text_color = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return f"{self.number} - {self.name}"


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
