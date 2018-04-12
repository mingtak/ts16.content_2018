# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class CoverView(BrowserView):
    template = ViewPageTemplateFile('template/cover_view.pt')

    def getNews(self):
        return api.content.find(context=self.portal[self.lang]['news'], Type='News Item')

    def getAward(self):
        return api.content.find(context=self.portal[self.lang]['award'], Type='Page')

    def getDocumentShow(self):
        return api.content.find(context=self.portal[self.lang]['document_show'], Type='Page')

    def getMeetingRoom(self):
        return api.content.find(context=self.portal[self.lang]['meeting_room'], Type='Page')

    def getAbout(self):
        return api.content.find(context=self.portal[self.lang]['about'], Type='Page')

    def getForThis(self):
        return api.content.find(context=self.portal[self.lang]['for_this'], Type='Page')

    def __call__(self):
        self.portal = api.portal.get()
        self.lang = api.portal.get_current_language()
        return self.template()
