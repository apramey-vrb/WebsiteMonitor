import json

class url:
    def __init__(self, link, content):
        self.link = link
        self.content = content

    @staticmethod
    def from_json(json_dct):
      return url(json_dct['link'], json_dct['content'])
    
class urlResponse(url):
    def __init__(self, link, content, responseTime = 0, isValidContent = False, response = ""):
        super().__init__(link, content)
        self.responseTime = responseTime
        self.isValidContent = isValidContent
        self.response = response

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)