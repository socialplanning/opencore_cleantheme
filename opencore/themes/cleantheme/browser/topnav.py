from opencore.browser.topnav.topnav import TopNavView as TopNavBase

class TopNavView(TopNavBase):

    def contextmenu(self):
        listitems = TopNavBase.contextmenu(self)
        area = self.area
        listitems = """<li><a href="%s">%s &raquo;</a></li>""" % (
            area['absolute_url'], area['Title']) + listitems
        return listitems
