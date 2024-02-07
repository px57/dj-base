from django.contrib import admin
from sites.models import Site
from django.http.request import HttpRequest


@admin.register(Site)
class SitesModelsAdmin(admin.ModelAdmin):
    list_display = [
        'host'
    ]

    def save_model(self, 
        request: HttpRequest, 
        obj, 
        form, 
        change
    ):
        """
            @description:
            @param.request -> Request
            @param.obj -> Site
            @param.form -> ModelForm
            @param.change -> bool
        """
        obj.save()