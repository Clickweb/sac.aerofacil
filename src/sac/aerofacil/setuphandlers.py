# -*- coding: utf-8 -*-
import logging
from five.localsitemanager import make_objectmanager_site
from zope.component.interfaces import ISite
from zope.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException
from Products.CMFCore.interfaces import IContentish
from Products.Five.utilities.marker import mark
from interfaces import IAplicativo, IAeroporto, IGuiaDoPassageiro

from Products.ATContentTypes.interface import IATNewsItem
from archetypes.schemaextender.interfaces import ISchemaModifier
from sac.aerofacil.browser.extender import DestaquesExtender


def do_upgrades(context):
    """ If exists, run migrations
    """
    if context.readDataFile('sac.aerofacil.txt') is None:
        return
    portal = getSite()
    _delete_example_content(portal)
    _exclude_from_nav(portal)
    _apply_interfaces(portal)
    _publish_structure(portal)
    _update_catalog(portal)
    _set_layout(portal)
    _extend_destaques(portal)


def _delete_example_content(portal):
    to_delete = ['front-page', 'news', 'events']
    to_delete = [i for i in to_delete if hasattr(portal, i)]
    portal.manage_delObjects(to_delete)


def _exclude_from_nav(portal):
    to_exclude = ['destaques', 'Members']
    to_exclude = [portal[i] for i in to_exclude if hasattr(portal, i)]
    for obj in to_exclude:
        obj.setExcludeFromNav(True)


def _apply_interfaces(portal):
    to_apply = {'aeroportos-brasileiros': IAeroporto,
                'aplicativos-e-ferramentas': IAplicativo,
                'guia-do-passageiro': IGuiaDoPassageiro}
    to_apply = {k: v for k, v in to_apply.iteritems() if hasattr(portal, k)}
    for i in to_apply:
        mark(portal[i], to_apply[i])


def _publish_structure(portal):
    wtool = getToolByName(portal, 'portal_workflow')
    logger = logging.getLogger('sac.aerofacil _publish_structure')
    to_publish = [i for i in portal.keys() if IContentish.providedBy(portal[i])]
    for i in to_publish:
        try:
            wtool.doActionFor(portal[i], "publish")
        except WorkflowException:
            logger.info("Could not publish: %s. Already published?" % i)
            pass


def _update_catalog(portal, clear=True):
    logger = logging.getLogger('sac.aerofacil _update_catalog')
    logger.info('Updating catalog so items in profiles/default/structure are indexed...')
    catalog = getToolByName(portal, 'portal_catalog')
    err = catalog.refreshCatalog(clear=clear)
    if not err:
        logger.info('...done.')
    else:
        logger.warn('Could not update catalog.')


def _set_layout(portal):
    logger = logging.getLogger('sac.aerofacil _set_default_page')
    logger.info('Configurando visão padrão para %s...' % portal)
    portal.setLayout('folder_tabular_view')
    logger.info('...Feito.')


def _extend_destaques(portal):
    folder = portal['destaques']
    if not ISite.providedBy(folder):
        make_objectmanager_site(folder)
    sm = folder.getSiteManager()
    sm.registerAdapter(
        DestaquesExtender,
        (IATNewsItem,),
        ISchemaModifier,
        name=u'DestaqueExtended'
    )
