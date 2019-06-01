import uuid
from django.db import models
from thing.models import Base

SHAPES_CHOICE = (
    'rect','Rectangle',
    'circle', 'Circle',
    'ellipse', 'Ellipse',
    'line', 'Line',
    'polyline','Polylone',
    'polygon','Polygon'
)


class DisplayBase(Base):
    def random(self, seed, range):
        return

    class Meta:
        abstract = True


class Colour(DisplayBase):
    r = models.IntegerField(
        default=0,
        help_text='Red Value'
    )
    g = models.IntegerField(
        default=0,
        help_text='Green Value'
    )
    b = models.IntegerField(
        default=0,
        help_text='Blue Value'
    )
    a = models.IntegerField(
        default=0,
        help_text='Alpha Value'
    )


class Shape(DisplayBase):
    name = models.CharField(
        max_length=8,
        choices=SHAPES_CHOICE,
        help_text="""The DisplayBase name field"""
    )


class Position(DisplayBase):
    x = models.FloatField(
        default=0,
        help_text='XPos Value'
    )
    y = models.FloatField(
        default=0,
        help_text='YPos Value'
    )
    z = models.FloatField(
        default=0,
        help_text='Zpos Value'
    )


class Rotation(DisplayBase):
    x = models.FloatField(
        default=0,
        help_text='XRot Value'
    )
    y = models.FloatField(
        default=0,
        help_text='YRot Value'
    )
    z = models.FloatField(
        default=0,
        help_text='ZRot Value'
    )


class Size(DisplayBase):
    size = models.FloatField(
        help_text="""The DisplayBase name field""",
        default = 1.0
    )


class DisplayObject(DisplayBase):
    class Meta:
        abstract = True

    shape = models.ForeignKey('Shape')
    colour= models.ForeignKey('Colour')
    position = models.ForeignKey('Position')
    rotation = models.ForeignKey('Rotation')
    size = models.ForeignKey('Size')


class Node(DisplayObject):
    pass


class Link(DisplayObject):
    node1 = models.ForeignKey(
        'Node',
        related_name='LinkNode1'
    )
    node2 = models.ForeignKey(
        'Node',
        related_name='LinkNode2'
    )




class BackGround(DisplayBase):
    colour= models.ForeignKey('Colour')
