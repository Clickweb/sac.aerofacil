# -*- coding: utf-8 -*-
from zope.interface import implements
from Products.Archetypes.atapi import RichWidget
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from sac.aerofacil.interfaces import ISACAerofacilLayer


class DestaquesExtender(object):
    implements(IBrowserLayerAwareExtender, ISchemaModifier)
    layer = ISACAerofacilLayer
    # _fields = []

    def __init__(self, context):
        self.context = context

    # def getFields(self):
    #     return self._fields

    def fiddle(self, schema):
        schema['description'].default_content_type = 'text/html'
        schema['description'].allowable_content_types = ('text/html',)
        schema['description'].widget = RichWidget(
            label=u'Sumário',
            description='Utilizado na página inicial, nas listagens de itens e resultado de buscas',
            allow_file_upload=False
        )
        schema['description'].default_output_type = 'text/html'
        # schema['description'].validators = ('isTidyHtmlWithCleanup',)
        # schema['description'].validators = ('isTidyHtml',)
        return schema
