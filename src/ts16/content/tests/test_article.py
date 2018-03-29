# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from ts16.content.interfaces import IArticle
from ts16.content.testing import TS16_CONTENT_INTEGRATION_TESTING  # noqa
from zope.component import createObject
from zope.component import queryUtility

import unittest


class ArticleIntegrationTest(unittest.TestCase):

    layer = TS16_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Article')
        schema = fti.lookupSchema()
        self.assertEqual(IArticle, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Article')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Article')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IArticle.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type='Article',
            id='Article',
        )
        self.assertTrue(IArticle.providedBy(obj))
