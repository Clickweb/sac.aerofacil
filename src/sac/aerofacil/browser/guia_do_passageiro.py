# -*- coding: utf-8 -*-
from five import grok
from Products.ATContentTypes.interface import IATFolder
from sac.aerofacil import MessageFactory as _


grok.templatedir('templates')

class GuiaDoPassageiro(grok.View):
    """BrowserView para apresentação das Pastas e Páginas da seção
    Guia do Passageiro.
    """

    grok.context(IATFolder)
    grok.require('zope2.View')
    # grok.template('guia_do_passageiro.pt')
