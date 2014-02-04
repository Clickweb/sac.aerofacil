# -*- coding: utf-8 -*-
from five import grok
from plone.memoize.view import memoize
from Products.ATContentTypes.interface import IATFolder
from sac.aerofacil import MessageFactory as _


grok.templatedir('templates')

class GuiaDoPassageiro(grok.View):
    """BrowserView para apresentação das Pastas e Páginas da seção
    Guia do Passageiro.
    """

    grok.context(IATFolder)
    grok.name('@@guia')
    grok.require('zope2.View')
    # grok.template('guia_do_passageiro.pt')

    @memoize
    def guias(self):
        """Devolve mapeamento entre guias e abas
        """
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        if not 'guia-do-passageiro' in getNavigationRootObject(context, portal).objectIds():
            return None
        catalog = getToolByName(self.context, 'portal_catalog')
        guias = catalog(portal_type='Folder',
                        review_state='published',
                        path='/'.join(portal['guia-do-passageiro'].getPhysicalPath()),
                        sort_on='getObjPositionInParent',
                        sort_limit=4)[:4]
        return {guia: self.abas(guia) for guia in guias}

    @memoize
    def abas(self, guia=None):
        """Devolve abas a partir das guias da seção Guia do passageiro.
        """
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        path = portal['guia-do-passageiro'][guia.id].getPhysicalPath()
        catalog = getToolByName(self.context, 'portal_catalog')
        abas = catalog(portal_type='Document',
                       review_state='published',
                       path='/'.join(path),
                       sort_on='getObjPositionInParent',
                       sort_limit=12)[:12]
        return abas
