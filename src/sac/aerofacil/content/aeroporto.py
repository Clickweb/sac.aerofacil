# -*- coding: utf-8 -*-
from sac.aerofacil import MessageFactory as _
from five import grok
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


grok.templatedir('templates')

class IAeroporto(model.Schema):
    """Um aeroporto contendo título, descrição e campos para facilidades:
    Restaurantes, Lojas, Localização e Estacionamento.
    """

    model.load("models/sac.aerofacil.aeroporto.xml")

    # title = schema.TextLine(
    #         title=_(u"Nome do aeroporto"),
    #         required=True,
    #     )

    # body = RichText(
    #         title=_(u"Corpo de texto"),
    #         description=_(u"Descrição detalhada do aeroporto"),
    #         required=True,
    #     )

    # restaurantes = RichText(
    #         title=_(u"Restaurantes"),
    #         description=_(u"Lista de restaurantes do aeroporto"),
    #         required=False
    #     )

    # lojas = RichText(
    #         title=_(u"Lojas"),
    #         description=_(u"Lista de lojas do aeroporto"),
    #         required=False
    #     )

    # localizacao = schema.Text(
    #         title=_(u"Localização"),
    #         description=_(u"Código HTML de incorporação do mapa de localização do aeroporto"),
    #         required=False
    #     )

    # estacionamento = RichText(
    #         title=_(u"Estacionamento"),
    #         description=_(u"Informações sobre o estacionamento do aeroporto"),
    #         required=False  
    #     )


class AeroportoView(grok.View):
    grok.context(IAeroporto)
    grok.require('zope2.View')
    grok.template('aeroportoview')
