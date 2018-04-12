# -*- coding: utf-8 -*-
from plone import api
from ts16.content import _


def userLogin(event):
    portal = api.portal.get()
    request = portal.REQUEST
    request.response.redirect('%s/folder_contents' % portal.absolute_url())

