# -*- coding: utf-8 -*-
from ts16.content import _
# from plone.autoform import directives
#from plone.supermodel import directives
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope.component import adapts
from zope.interface import alsoProvides, implements
from zope.interface import provider
#from z3c.relationfield.schema import RelationList, RelationChoice
#from plone.app.vocabularies.catalog import CatalogSource
from plone.dexterity.interfaces import IDexterityContent
#from plone.directives import dexterity
from plone.app.textfield import RichText
#from plone.app.content.interfaces import INameFromTitle
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
#from DateTime import DateTime
#import random
#from plone.directives import form


class IBigImage(model.Schema):
    """ Add bigImage_* field """

    model.fieldset(
        'bigImage',
        label=_(u"bigImage"),
        fields=['bigImage_1', 'photoer_1', 'bigImage_2', 'photoer_2', 'bigImage_3', 'photoer_3',
                'bigImage_4', 'photoer_4', 'bigImage_5', 'photoer_5', ]
    )

    model.fieldset(
        'english',
        label=_(u"English"),
        fields=['en_title', 'en_description', 'en_text', ]
    )

    en_title = schema.Text(
        title=_(u"English Title"),
        required=False,
    )

    en_description = schema.Text(
        title=_(u"English Description"),
        description=u"英文摘要，與中文摘要格式同",
        required=False,
    )

    en_text = RichText(
        title=_(u"English text"),
        required=False,
    )

    bigImage_1 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page. Size:1900 X 950"),
        required=False,
    )

    bigImage_2 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page. Size:1900 X 950"),
        required=False,
    )

    bigImage_3 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page. Size:1900 X 950"),
        required=False,
    )

    bigImage_4 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page. Size:1900 X 950"),
        required=False,
    )

    bigImage_5 = NamedBlobImage(
        title=_(u"Big Image"),
        description=_(u"Big image for page. Size:1900 X 950"),
        required=False,
    )

    photoer_1 = schema.TextLine(
        title=_(u"Photographer"),
        required=False,
    )

    photoer_2 = schema.TextLine(
        title=_(u"Photographer"),
        required=False,
    )

    photoer_3 = schema.TextLine(
        title=_(u"Photographer"),
        required=False,
    )

    photoer_4 = schema.TextLine(
        title=_(u"Photographer"),
        required=False,
    )

    photoer_5 = schema.TextLine(
        title=_(u"Photographer"),
        required=False,
    )


alsoProvides(IBigImage, IFormFieldProvider)


def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class BigImage(object):
    implements(IBigImage)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    bigImage_1 = context_property("bigImage_1")
    bigImage_2 = context_property("bigImage_2")
    bigImage_3 = context_property("bigImage_3")
    bigImage_4 = context_property("bigImage_4")
    bigImage_5 = context_property("bigImage_5")
    photoer_1 = context_property("photoer_1")
    photoer_2 = context_property("photoer_2")
    photoer_3 = context_property("photoer_3")
    photoer_4 = context_property("photoer_4")
    photoer_5 = context_property("photoer_5")
    en_title = context_property("en_title")
    en_description = context_property("en_description")
    en_text = context_property("en_text")
