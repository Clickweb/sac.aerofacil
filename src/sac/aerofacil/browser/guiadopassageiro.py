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
    def guias(self):
        """Devolve mapeamento entre guias e abas.
        """
        context = aq_inner(self.context)
        portal = context.restrictedTraverse('@@plone_portal_state').portal()
        path = portal['guia-do-passageiro'].getPhysicalPath()
        if not 'guia-do-passageiro' in getNavigationRootObject(context, portal).objectIds():
            return None
        catalog = getToolByName(context, 'portal_catalog')
        guias = catalog(portal_type='Folder',
                        review_state='published',
                        path={'query': '/'.join(path),
                              'depth': 1},
                        sort_on='getObjPositionInParent',
                        sort_limit=4)[:4]
        return {guia: self.abas(guia) for guia in guias}

    @memoize
    def abas(self, guia=None):
        """Devolve abas a partir das guias da seção Guia do passageiro.
        """
        context = aq_inner(self.context)
        portal = context.restrictedTraverse('@@plone_portal_state').portal()
        path = portal['guia-do-passageiro'][guia.id].getPhysicalPath()
        catalog = getToolByName(context, 'portal_catalog')
        abas = catalog(portal_type='Document',
                       review_state='published',
                       path={'query': '/'.join(path),
                             'depth': 1},
                       sort_on='getObjPositionInParent',
                       sort_limit=12)[:12]
        # import pdb; pdb.set_trace()
        return abas

    def is_current(self):
        return True