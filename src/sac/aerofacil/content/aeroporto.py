# -*- coding: utf-8 -*-
from five import grok
from plone.supermodel import model
from sac.aerofacil import interfaces

grok.templatedir('templates')


class IAeroporto(model.Schema):
    """Um aeroporto contendo título, descrição e campos para facilidades:
    Restaurantes, Lojas, Localização e Estacionamento.
    """

    model.load("models/sac.aerofacil.aeroporto.xml")


class Aeroporto(grok.View):
    grok.name('view')
    grok.context(IAeroporto)
    grok.require('zope2.View')
    grok.implements(interfaces.IAeroporto)
