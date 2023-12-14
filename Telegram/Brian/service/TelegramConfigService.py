
from Telegram.Brian.models.dao.TelegramConfigDAO import TelegramConfigDAO

class TelegramConfigService:

    def __init__(self):
        self.dao = TelegramConfigDAO()

    def retreiveExBotToken(self):
        
        return self.dao.selectExBotToken()

    def retreiveAlarmBotToken(self):

        return self.dao.selectAlarmBotToken()

    def retreiveChatId(self, chatName):
        
        return self.dao.selectChatIdByChatName(chatName)