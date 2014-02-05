# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class ISACAerofacilLayer(IDefaultPloneLayer):
    """Interface de marcação que define um Zope 3 browser layer."""


class IAeroporto(Interface):
    """Interface de marcação para seção Aeroporto.
    """


class IAplicativo(Interface):
    """Interface de marcação para seção Aplicativo.
    """


class IGuiaDoPassageiro(Interface):
    """Interface de marcação para seção Guia do Passageiro.
    """
