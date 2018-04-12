# -*- coding: utf-8 -*-
from plone import api
from ts16.content import _


def toFolderContents(object, event):
    try:
        portal = api.portal.get()
        lang = api.portal.get_current_language()
        request = portal.REQUEST
        request.response.redirect('%s/%s/folder_contents' % (portal.absolute_url(), lang))
    except:
        pass


def userLogin(event):
    portal = api.portal.get()
    request = portal.REQUEST
    request.response.redirect('%s/folder_contents' % portal.absolute_url())
