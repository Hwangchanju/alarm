
from Telegram.Brian.models.dao.ExceptUrlDAO import ExceptUrlDAO

class ExceptUrlService:

    def __init__(self):
        self.dao = ExceptUrlDAO()    

    def retrieveExceptUrl(self):
        ExceptUrlList = []
        # ExceptUrlList = self.dao.selectExceptUrl()

        return ExceptUrlList

    def registerExceptUrl(self, ExceptUrl):
        # self.dao.registerExceptUrl()

        return 0

    def deleteExceptUrl(self):
        return 0