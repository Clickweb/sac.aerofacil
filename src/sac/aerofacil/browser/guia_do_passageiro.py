# -*- coding: utf-8 -*-
from sac.aerofacil import MessageFactory as _
from five import grok


class GuiaDoPassageiro(grok.View):
    """BrowserView para exibir as Pastas e Páginas do Guia do Passageiro.
    """

    grok.context(IATFolder)
    grok.require('zope2.View')
