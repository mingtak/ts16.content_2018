# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class CoverView(BrowserView):
    template = ViewPageTemplateFile('template/cover_view.pt')
    
    def __call__(self):
        return self.template()
