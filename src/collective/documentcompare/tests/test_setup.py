# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.documentcompare.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.documentcompare into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.documentcompare is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.documentcompare'))

    def test_uninstall(self):
        """Test if collective.documentcompare is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.documentcompare'])
        self.assertFalse(self.installer.isProductInstalled('collective.documentcompare'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollectiveDocumentcompareLayer is registered."""
        from collective.documentcompare.interfaces import ICollectiveDocumentcompareLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveDocumentcompareLayer, utils.registered_layers())
