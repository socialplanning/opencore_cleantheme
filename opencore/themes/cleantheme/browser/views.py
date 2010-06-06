from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.viewlet.viewlet import ViewletBase
from opencore.nui.main.view import GetStarted as GetStartedBase

class GetStarted(GetStartedBase):
    render = ViewPageTemplateFile('get-started.pt')

class TermsOfUseViewlet(ViewletBase):

    render = ViewPageTemplateFile('termsofuse.pt')

    def validate(self):
        view = self.__parent__
        request = self.request

        if not request.form.has_key('termsofuse'):
            return {"termsofuse": "You must agree to the terms of use"}

        if not request.form['termsofuse']:
            return {"termsofuse": "You must agree to the terms of use"}

        return {}
