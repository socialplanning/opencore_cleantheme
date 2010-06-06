from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.viewlet.viewlet import ViewletBase
from opencore.nui.main.view import GetStarted as GetStartedBase

class GetStarted(GetStartedBase):
    render = ViewPageTemplateFile('get-started.pt')

class TermsOfUseViewlet(ViewletBase):

    render = ViewPageTemplateFile('termsofuse.pt')

    def validate(self):
        self.errors = {}

        view = self.__parent__
        request = self.request

        if not request.form.has_key('termsofuse'):
            self.errors = {"termsofuse": "You must agree to the terms of use"}
            return self.errors

        if not request.form['termsofuse']:
            self.errors = {"termsofuse": "You must agree to the terms of use"}
            return self.errors

        return self.errors
