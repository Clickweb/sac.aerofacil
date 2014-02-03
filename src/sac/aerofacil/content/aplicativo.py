# -*- coding: utf-8 -*-
from sac.aerofacil import MessageFactory as _
from five import grok
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema


# grok.templatedir('templates')

class IAplicativo(model.Schema):
    """Um aplicativo contendo título, chamada, corpo de texto e campos
    para URLs de download.
    """

    model.load("models/sac.aerofacil.aplicativo.xml")

    # title = schema.TextLine(
    #         title=_(u"Nome do aplicativo"),
    #         required=True,
    #     )

    # description = schema.Text(
    #         title=_(u"Chamada"),
    #         description=_(u"Sumário do aplicativo, exibido na página inicial."),
    #         required=True,
    #     )

    # body = RichText(
    #         title=_(u"Corpo de texto"),
    #         description=_(u"Descrição detalhada do aplicativo."),
    #         required=True,
    #     )

    # android = schema.URI(
    #         title=_(u"Android"),
    #         description=_(u"URL para download"),
    #         required=False
    #     )

    # ios = schema.URI(
    #         title=_(u"IOS"),
    #         description=_(u"URL para download"),
    #         required=False
    #     )

    # windows = schema.URI(
    #         title=_(u"Windows"),
    #         description=_(u"URL para download"),
    #         required=False
    #     )

    # web = schema.URI(
    #         title=_(u"Voos Online Web"),
    #         description=_(u"URL para acesso"),
    #         required=False
    #     )


# class View(grok.View):
#     grok.context(IAplicativo)
#     grok.require('zope2.View')
