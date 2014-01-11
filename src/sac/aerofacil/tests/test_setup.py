# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from sac.aerofacil.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of sac.aerofacil into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if sac.aerofacil is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('sac.aerofacil'))

    def test_uninstall(self):
        """Test if sac.aerofacil is cleanly uninstalled."""
        self.installer.uninstallProducts(['sac.aerofacil'])
        self.assertFalse(self.installer.isProductInstalled('sac.aerofacil'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ISacAerofacilLayer is registered."""
        from sac.aerofacil.interfaces import ISacAerofacilLayer
        from plone.browserlayer import utils
        self.failUnless(ISacAerofacilLayer in utils.registered_layers())
