from django.db import models
from mptt.models import TreeForeignKey, MPTTModel, raise_if_unsaved
from django.db.models import permalink


class Tiles(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(verbose_name='content', null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    view_content = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ("tile-detail", (self.pk,))



class Menu(MPTTModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    '''
    TreeForeignKey basic ForeignKey, but uses mptt's
    I used this to generat a ModelForm with correct widget
    '''

    def __str__(self):
        return self.name
