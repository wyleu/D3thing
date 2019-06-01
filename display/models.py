from django.db import models
from thing.models import Base

SHAPES_CHOICE = (
    ('rect', 'Rectangle', ),
    ('circle', 'Circle', ),
    ('ellipse', 'Ellipse', ),
    ('line', 'Line',),
    ('polyline', 'Polylone', ),
    ('polygon', 'Polygon', ),
)

INITIAL_COLOUR_CHOICE = (
    ('red', 'Red', ),
    ('green', 'Green', ),
    ('blue', 'Blue', ),
    ('white', 'White',),
    ('black', 'Black', ),
    ('grey', 'Grey', ),
)


class DisplayBase(Base):
    def random(self, seed, range):
        return

    class Meta:
        abstract = True


class Colour(DisplayBase):
    name = models.CharField(
        max_length=8,
        choices=INITIAL_COLOUR_CHOICE,
        unique=True,
        default='red',
        help_text="""The DisplayBase name field"""
    )
    r = models.IntegerField(
        default=128,
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
        default=255,
        help_text='Alpha Value'
    )


def get_default_colour():
    return Shape.objects.get_or_create(name=INITIAL_COLOUR_CHOICE[0][0])[0]


class Shape(DisplayBase):
    name = models.CharField(
        max_length=8,
        choices=SHAPES_CHOICE,
        unique=True,
        default='circle',
        help_text="""The DisplayBase name field"""
    )


def get_default_shape():
    return Shape.objects.get_or_create(name=SHAPES_CHOICE[0][0])[0]


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


def get_default_position():
    return Shape.objects.get_or_create()[0]


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
        default=1.0
    )


class DisplayObject(DisplayBase):
    class Meta:
        abstract = True

    shape = models.ForeignKey(
        'Shape',
        to_field='name',
        on_delete=models.SET(get_default_shape),
    )
    colour = models.ForeignKey(
        'Colour',
        on_delete=models.SET(get_default_colour),
        to_field='name'
    )
    # position = models.ForeignKey(
    #     'Position',
    #     on_delete=models.SET(get_default_position),
    #
    # )
    # rotation = models.ForeignKey('Rotation')
    # size = models.ForeignKey('Size')


class Node(DisplayObject):
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
#
#
class Link(DisplayObject):
    node1 = models.ForeignKey(
        'Node',
        related_name='LinkNode1',
        on_delete=models.CASCADE
    )
    node2 = models.ForeignKey(
        'Node',
        related_name='LinkNode2',
        on_delete=models.CASCADE
    )
#
#
#
#
# class BackGround(DisplayBase):
#     colour= models.ForeignKey('Colour')
