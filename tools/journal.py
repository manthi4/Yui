import os
from datetime import date

class Journal:
    def __init__(self):
        self._base_path = "/workspaces/Yui/world/"

    def write(self, content):
        today = str(date.today())
        f_path = self._base_path+today+".txt"
        if not os.path.isfile(f_path):
            with open(f_path, "x") as f:
                f.write(content)
            return
        with open(f_path, "w") as f:
            f.write(content)

    def get(self, date):
        f_path = self._base_path+date+".txt"
        if not os.path.isfile(f_path):
            return "sorry, could not find journal entry from " + date
        with open(f_path) as f:
            ans = f.read()
        return ans