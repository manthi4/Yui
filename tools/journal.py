from datetime import date
import logging
import os
from pathlib import Path

class Journal:
    def __init__(self, base_path = "./workspaces/Yui/world"):
        self._base_path = base_path
        self.logger = logging.getLogger(__name__)   
        if not os.path.exists(base_path):
            self.logger.warning(f"Journal base path does not exist: {base_path}, \n Creating now...")
            Path(base_path).mkdir(parents=True, exist_ok=True)


    def put(self, content) -> str:
        self.write(content)
    def write(self, content) -> str:
        today = str(date.today())
        f_path = self._base_path+today+".txt"
        # if not os.path.isfile(f_path):
        #     with open(f_path, "x") as f:
        #         f.write(content)
        #     return
        with open(f_path, "a+") as f:
            f.write(content)
            f.write("\n")

    def get (self, fname) -> str:
        return self.read(fname)

    def read(self, fname) -> str:
        fname = str(fname)
        if not fname.endswith("txt"):
            fname = fname + ".txt"
        f_path = self._base_path+fname

        if not os.path.isfile(f_path):
            return "sorry, could not find journal entry from " + fname
        with open(f_path) as f:
            ans = f.read()
        return ans
    
def main():
    j = Journal()
    j.write("Hello there this is a test\n")
    print(j.read("boop"))
    print(j.read(date.today()))
    print(j.read(str(date.today())))

if __name__ == '__main__':
    main()