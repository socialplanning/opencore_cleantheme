from opencore.browser.base import BaseView

from opencore.themes.cleantheme.utils import static_base
import os

class BecomingAMemberView(BaseView):
    def __call__(self):
        path = os.path.join(static_base(), 'member-agreement.html')
        file = open(path)
        text = file.read()
        file.close()
        return text
