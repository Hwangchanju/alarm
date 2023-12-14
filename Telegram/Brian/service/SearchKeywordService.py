

from Telegram.Brian.models.dao.SearchKeywordDAO import SearchKeywordDAO

class SearchKeywordService:
    def __init__(self, db_file):
        self.dao = SearchKeywordDAO(db_file)

    def retrieveSearchKeyword(self):
        return self.dao.selectSearchKeyword()

    def registerSearchKeyword(self, searchKeyword):
        return self.dao.registerSearchKeyword(searchKeyword)

    def updateForKeywordNotUse(self, searchKeyword):
        return self.dao.updateForKeywordNotUse(searchKeyword)