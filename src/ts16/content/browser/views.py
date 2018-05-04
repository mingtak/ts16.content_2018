# -*- coding: utf-8 -*- 
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class Vote(BrowserView):

    def __call__(self):
        request = self.request
        portal = api.portal.get()
        voteUIDs = request.form.get('vote').split(',')
        email = request.form.get('email')

        voteObj = portal['vote']
        if email in voteObj.description.split('\n'):
            return 'err1'
        voteObj.description += '\n%s' % email

        for uid in voteUIDs:
            pollObj = api.content.find(UID=uid)[0].getObject()
            pollObj.vote += 1
            if not pollObj.voteEmail:
                pollObj.voteEmail = email
            else:
                pollObj.voteEmail += '\n%s' % email
        return 'ok'


class PostEnView(BrowserView):
    template = ViewPageTemplateFile('template/post_en_view.pt')

    def __call__(self):
        portal = api.portal.get()
        request = self.request
        postId = request.form.get('id')
        self.post = portal['zh-tw']['award'][postId]
        return self.template()


class CoverView(BrowserView):
    template_zh = ViewPageTemplateFile('template/cover_view_zh.pt')
    template_en = ViewPageTemplateFile('template/cover_view_en.pt')

    def getNews(self):
        return api.content.find(context=self.portal[self.lang]['news'], Type=['News Item', 'Link'], sort_on='created', sort_order='reverse')

    def getAward(self):
        return api.content.find(context=self.portal[self.lang]['award'], Type='Page')

    def get_en_Award(self):
        return api.content.find(context=self.portal['zh-tw']['award'], Type='Page')

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
        if self.lang == 'en-us':
            return self.template_en()
        else:
            return self.template_zh()
