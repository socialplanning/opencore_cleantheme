from Acquisition import aq_inner, aq_parent
from zope import component
from zope import interface
from zope.traversing.interfaces import IPathAdapter

def static_root_for_domain(environ):
    domain = environ['HTTP_X_FORWARDED_SERVER']
    return "/++static++/%s" % domain

class Tales(object):
    component.adapts(interface.Interface)
    interface.implements(IPathAdapter)

    def __init__(self, context):
        self.request = context.request

    def static_root(self):
        return static_root_for_domain(self.request.environ)

