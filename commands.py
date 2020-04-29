import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher


class Commander:
    def __init__(self):
        self.confirm = ["yes","affirmative","si","sure","do it","yeah","confirm"]
        self.cancel=["no","negative","negative soldier","don't","wait","cancel"]

    def discover(self, command):
        if "what" in command and " name" in command:
            if "my" in command:
                self.respond("You haven't told me your name.")
            else:
                self.respond("My name is Python Commander. How are you?")
        else:
            f = Fetcher("https://www.google.co.in/search?source=hp&ei=k9e2XeP2JrfTz7sP-LaigAY&q="+command)
            answer = f.lookup()
            self.respond(answer)

    def respond(self, answer):
        print(answer)
        subprocess.call('cscript say.vbs '+answer+"'", shell=True)


