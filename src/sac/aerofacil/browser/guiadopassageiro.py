# -*- coding: utf-8 -*-
from five import grok
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.ATContentTypes.interface import IATFolder
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.memoize.view import memoize
from sac.aerofacil import MessageFactory as _

grok.templatedir('templates')


class GuiaDoPassageiro(grok.View):
    """BrowserView para apresentação das Pastas e Páginas da seção
    Guia do Passageiro.
    """

    grok.context(IATFolder)
    grok.require('zope2.View')

    @memoize
    def subsecoes(self):
        """Devolve mapeamento entre subseções e suas abas internas.
        """
        context = aq_inner(self.context)
        portal = context.restrictedTraverse('@@plone_portal_state').portal()
        path = portal['guia-do-passageiro'].getPhysicalPath()
        if not 'guia-do-passageiro' in getNavigationRootObject(context, portal).objectIds():
            return None
        catalog = getToolByName(context, 'portal_catalog')
        subsecoes = catalog(portal_type='Folder',
                            review_state='published',
                            path={'query': '/'.join(path),
                                  'depth': 1},
                            sort_on='getObjPositionInParent',
                            sort_limit=4)[:4]
        return [(subsecao, self.abas(subsecao)) for subsecao in subsecoes]

    @memoize
    def abas(self, subsecao):
        """Devolve abas internas de uma subseção do Guia do passageiro.
        """
        context = aq_inner(self.context)
        portal = context.restrictedTraverse('@@plone_portal_state').portal()
        path = portal['guia-do-passageiro'][subsecao.id].getPhysicalPath()
        catalog = getToolByName(context, 'portal_catalog')
        abas = catalog(portal_type='Document',
                       review_state='published',
                       path={'query': '/'.join(path),
                             'depth': 1},
                       sort_on='getObjPositionInParent',
                       sort_limit=12)[:12]
        return abas
