# -*- coding: utf-8 -*-
from five import grok
from plone.supermodel import model
from sac.aerofacil import interfaces

grok.templatedir('templates')


def has_image(content):
    image = content.image
    return (image and image.getSize())


class IAplicativo(model.Schema):
    """Um aplicativo contendo título, chamada, corpo de texto e campos
    para URLs de download.
    """

    model.load("models/sac.aerofacil.aplicativo.xml")


class Aplicativo(grok.View):
    grok.name('view')
    grok.context(IAplicativo)
    grok.require('zope2.View')
    grok.implements(interfaces.IAplicativo)

    def image_thumb(self):
        ''' Return a thumbnail '''
        if not has_image(self):
            return None
        view = self.unrestrictedTraverse('@@images')
        return view.scale(fieldname='image',
                          scale='thumb').index_html()

    def tag(self, scale='thumb', css_class='tileImage', **kw):
        ''' Return a tag to the image '''
        if not (has_image(self)):
            return ''
        view = self.unrestrictedTraverse('@@images')
        return view.tag(fieldname='image',
                        scale=scale,
                        css_class=css_class,
                        **kw)
