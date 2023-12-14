
from Telegram.Brian.service import SearchKeywordService
from Telegram.Brian.service import ExceptKeywordService
from Telegram.Brian.service import ExceptUrlService

class TelegramAlarmSetKeywordService:

    def __init__(self):
        self.searchKeywordService = SearchKeywordService()
        self.exceptKeywordService = ExceptKeywordService()
        self.exceptUrlService = ExceptUrlService()

    