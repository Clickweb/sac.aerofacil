# -*- coding: utf-8 -*-
import logging
from zope.component.hooks import getSite
from Products.CMFCore.utils import getToolByName


def doUpgrades(context):
    """ If exists, run migrations
    """
    if context.readDataFile('sac.aerofacil.txt') is None:
        return
    logger = logging.getLogger('sac.aerofacil')
    portal = getSite()
    _delete_example_content(portal)
    _publish_structure(portal)
    _excludeFromNav(portal)
    _applyInterfaces(portal)
    _updateCatalog(portal)
    _setDefaultPage(portal)

def _delete_example_content(portal):
    all_content = portal.portal_catalog()
    if all_content:
        expected = [
            'front-page',
            'news',
            'aggregator',
            'events',
            'aggregator',
            'Members'
        ]
        if not [i.id for i in all_content] == expected:
            return
        to_delete = ['front-page', 'news', 'events']
        portal.manage_delObjects(to_delete)

def _publish_structure(portal):
    pass

def _excludeFromNav(portal):
    to_exclude = ['destaques', 'Members']
    pass

def _applyInterfaces(portal):
    to_apply = ['home',
                'aeroportos-brasileiros',
                'aplicativos-e-ferramentas',
                'guia-do-viajante'
    ]
    pass

def _updateCatalog(portal, clear=True):
    logger = portal.getLogger('sac.aerofacil updateCatalog')
    logger.info('Updating catalog (with clear=%s) so items in profiles/default/structure are indexed...' % clear)
    catalog = getToolByName(portal, 'portal_catalog')
    err = catalog.refreshCatalog(clear=clear)
    if not err:
        logger.info('...done.')
    else:
        logger.warn('Could not update catalog.')

def _setDefaultPage(portal):
    if portal.readDataFile('sac.aerofacil.txt') is None:
        return
    logger = portal.getLogger('sac.aerofacil setDefaultPage')
    obj = 'home'
    if obj in portal:
        obj = portal[obj]
        logger.info('Configurando item padrão para %s...' % obj)
        obj.saveDefaultPage('%s_view' % obj)
        logger.info('Configurando visão padrão para %s...' % obj)
        obj.setLayout(pd)
        logger.info('...Feito.')
        return
