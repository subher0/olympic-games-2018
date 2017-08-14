from django.db import models
from django.utils.timezone import now
from .utils import make_filepath


class IndexTileManager(models.Manager):
    def getAllTiles(self):
        try:
            result = self.order_by('date').reverse()
        except Exception:
            result = None
        return result

    def getSomeTiles(self, amount):
        try:
            result = self.order_by('date').reverse()[:amount]
        except Exception:
            result = None
        return result


class IndexTile(models.Model):
    date = models.DateTimeField(verbose_name='Creation date', default=now)
    title = models.CharField(verbose_name='Tile title', max_length=64)
    icon = models.ImageField(verbose_name='Tile icon', default='no_icon.jpg', upload_to=make_filepath)
    iconOnHover = models.ImageField(verbose_name='Icon on hover', default='no_icon-reversed.jpg',
                                    upload_to=make_filepath)
    link = models.CharField(verbose_name='Link to follow on click', max_length=1024)
    objects = IndexTileManager()

    def __str__(self):
        return self.title
