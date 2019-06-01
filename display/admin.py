from django.contrib import admin

# Register your models here.
from .models import Link, Node, Colour, Shape


class BaseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'order',
        'modified',
        'created'
    ]


class NodeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'shape',
        'colour',
        'x',
        'y',
        'z'
    ]


class LinkAdmin(BaseAdmin):
    pass


class ColourAdmin(BaseAdmin):
    pass

class ShapeAdmin(BaseAdmin):
    pass


admin.site.register(Link, LinkAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Colour, ColourAdmin)
admin.site.register(Shape, ShapeAdmin)