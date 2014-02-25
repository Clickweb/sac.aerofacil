# -*- coding: utf-8 -*-
from collections import deque
from collections import OrderedDict
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
        brains = catalog(portal_type='Folder',
                            review_state='published',
                            path={'query': '/'.join(path),
                                  'depth': 1},
                            sort_on='getObjPositionInParent',
                            sort_limit=4)[:4]
        brains = deque(brains)
        ids = [brain.id for brain in brains]
        steps = -ids.index(context.id)
        brains.rotate(steps)
        return [(brain, self.abas(brain)) for brain in brains]

    @memoize
    def abas(self, subsecao):
        """Devolve abas internas de uma subseção do Guia do passageiro.
        """
        context = aq_inner(self.context)
        portal = context.restrictedTraverse('@@plone_portal_state').portal()
        path = portal['guia-do-passageiro'][subsecao.id].getPhysicalPath()
        catalog = getToolByName(context, 'portal_catalog')
        brains = catalog(portal_type='Document',
                         review_state='published',
                         path={'query': '/'.join(path),
                               'depth': 1},
                         sort_on='getObjPositionInParent',
                         sort_limit=12)[:12]
        return brains

    @memoize
    def depoimentos(self):
        context = aq_inner(self.context)
        portal = context.restrictedTraverse('@@plone_portal_state').portal()
        path = portal['guia-do-passageiro']['depoimentos'].getPhysicalPath()
        catalog = getToolByName(context, 'portal_catalog')
        brains = catalog(portal_type='sc.embedder',
                         review_state='published',
                         path={'query': '/'.join(path),
                               'depth': 1},
                         sort_on='getObjPositionInParent',
                         sort_limit=18)[:18]
        depoimentos = OrderedDict()
        for b in brains:
            video_obj = b.getObject()
            depoimentos[b] = {'video_id': video_obj.url.split('v=')[1].split('&')[0],
                              'thumb': video_obj.tag(scale='tile', css_class='', alt=b.Title)}
        return depoimentos

    @memoize
    def thumbs(self):
        """ Reagrupa um dicionário em uma lista de dicionários de 3 elementos.
        """
        thumbs = []
        depoimentos = self.depoimentos().copy()
        while depoimentos:
            group = OrderedDict()
            for i, brain in enumerate(depoimentos):
                if i < 3:
                    group[brain] = depoimentos.pop(brain)
            thumbs.append(group)
        return thumbs