from opencore.browser.topnav.topnav import TopNavView as TopNavBase

class TopNavView(TopNavBase):

    def contextmenu(self):
        listitems = TopNavBase.contextmenu(self)
        area = self.area

        url = area['absolute_url']
        if url == self.portal.absolute_url():
            return listitems

        listitems = """<li><a href="%s">%s &raquo;</a></li>""" % (
            url, area['Title']) + listitems
        return listitems
