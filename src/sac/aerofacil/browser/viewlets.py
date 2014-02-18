# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.memoize.view import memoize


class DestaquesHomeViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/destaques_home.pt')

    @memoize
    def destaques(self):
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        path = tuple()
        if 'destaques' in getNavigationRootObject(context, portal).objectIds():
            path = portal['destaques'].getPhysicalPath()
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='News Item',
                         review_state='published',
                         path='/'.join(path),
                         sort_on='Date',
                         sort_order='reverse',
                         sort_limit=1)[:1]
        return brains


class NoticiasHomeViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/noticias_home.pt')

    @memoize
    def noticias(self):
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        if 'noticias' in getNavigationRootObject(context, portal).objectIds():
            path = portal['noticias'].getPhysicalPath()
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='News Item',
                         review_state='published',
                         path='/'.join(path),
                         sort_on='Date',
                         sort_order='reverse',
                         sort_limit=5)[:5]
        return brains


class OutrasNoticiasViewlet(NoticiasHomeViewlet):
    render = ViewPageTemplateFile('templates/outras_noticias.pt')

    @memoize
    def noticias(self):
        """ Exclui a notícia corrente da listagem.
        """
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        path = tuple()
        if 'noticias' in getNavigationRootObject(context, portal).objectIds():
            path = portal['noticias'].getPhysicalPath()
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='News Item',
                         review_state='published',
                         path='/'.join(path),
                         sort_on='Date',
                         sort_order='reverse',
                         sort_limit=6)[:6]
        brains = [b for b in brains if not b.id == context.id][:5]
        return brains


class EBookViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/ebook.pt')


class AppsHomeViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/apps_home.pt')

    @memoize
    def apps(self):
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        if 'aplicativos-e-ferramentas' in getNavigationRootObject(context, portal).objectIds():
            path = portal['aplicativos-e-ferramentas'].getPhysicalPath()
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='sac.aerofacil.aplicativo',
                         review_state='published',
                         path='/'.join(path),
                         sort_on='getObjPositionInParent',
                         sort_limit=3)[:3]
        return brains


class AppsAplicativoViewlet(AppsHomeViewlet):
    render = ViewPageTemplateFile('templates/apps_aplicativo.pt')


class AppsAeroportoViewlet(AppsHomeViewlet):
    render = ViewPageTemplateFile('templates/apps_aeroporto.pt')


class SelectAeroportoViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/select_aeroporto.pt')

    @memoize
    def aeroportos(self):
        context = aq_inner(self.context)
        portal = self.portal_state.portal()
        path = tuple()
        if 'aeroportos-brasileiros' in getNavigationRootObject(context, portal).objectIds():
            path = portal['aeroportos-brasileiros'].getPhysicalPath()
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(portal_type='sac.aerofacil.aeroporto',
                         review_state='published',
                         path='/'.join(path),
                         sort_on='sortable_title')
        return brains

    @memoize
    def klass(self):
        if self.context.restrictedTraverse('plone_context_state').is_portal_root():
            return 'select-aeroporto-home'
        return 'select-aeroporto'


class ShareViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/share.pt')

    @memoize
    def section(self):
        context = aq_inner(self.context)
        self.portal = self.portal_state.portal()
        return context.getPhysicalPath()[len(self.portal.getPhysicalPath()):][0]


def search_catalog(context=None,
                   portal=None,
                   portal_type='',
                   review_state='',
                   path='',
                   sort_on='',
                   sort_order='',
                   sort_limit=None):
    portal_type = portal_type or 'News Item'
    review_state = review_state or 'published'
    sort_on = sort_on or 'Date',
    sort_order = sort_order or 'reverse',
    sort_limit = sort_limit or 5
    if path in getNavigationRootObject(context, portal).objectIds():
        path = portal[path].getPhysicalPath()
    catalog = getToolByName(context, 'portal_catalog')
    brains = catalog(portal_type=portal_type,
                     review_state=review_state,
                     path='/'.join(path),
                     sort_on=sort_on,
                     sort_order=sort_order,
                     sort_limit=sort_limit)
    return brains
