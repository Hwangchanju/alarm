
from Telegram.Brian.models.dao.ExceptKeywordDAO import ExceptKeywordDAO

class ExceptKeywordService:

    def __init__(self):
        self.dao = ExceptKeywordDAO()    

    def retrieveExceptKeyword(self):
        ExceptKeywordList = []
        # ExceptKeywordList = self.dao.selectExceptKeyword()

        return ExceptKeywordList

    def registerExceptKeyword(self, ExceptKeyword):
        # self.dao.registerExceptKeyword()

        return 0

    def deleteExceptKeyword(self):
        return 0