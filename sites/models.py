from kernel.models.base_metadata_model import BaseMetadataModel
from django.db import models

class Site(models.Model):
    """
        @description: 
    """
    host = models.CharField(
        max_length=250, 
        default='',
        unique=True,
        blank=True,
    )
    
    title = models.CharField(
        max_length=250, 
        default='...'
    )

    logo_color_version = models.ImageField(
        'logo_color_version',
        upload_to='profile/%Y/%m/%d/',
        default='',
    )

    logo_white_version = models.ImageField(
        'logo_white_version',
        upload_to='profile/%Y/%m/%d/',
        default='',
    )    
    logo_height = models.IntegerField(default=60)
