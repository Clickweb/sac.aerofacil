# -*- coding: utf-8 -*-
from five import grok
from plone.supermodel import model

grok.templatedir('templates')


class IAplicativo(model.Schema):
    """Um aplicativo contendo título, chamada, corpo de texto e campos
    para URLs de download.
    """

    model.load("models/sac.aerofacil.aplicativo.xml")


class Aplicativo(grok.View):
    grok.name('view')
    grok.context(IAplicativo)
    grok.require('zope2.View')
