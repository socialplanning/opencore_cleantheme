from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.viewlet.viewlet import ViewletBase
from opencore.nui.main.view import GetStarted as GetStartedBase

class GetStarted(GetStartedBase):
    render = ViewPageTemplateFile('get-started.pt')

