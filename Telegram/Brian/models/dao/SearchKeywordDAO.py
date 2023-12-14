import sqlite3
from Telegram.Brian.models.dto.SearchKeyworkDTO import SearchKeywordDTO

class SearchKeywordDAO:

    def __init__(self, db_file):
        self.db_file = db_file

    def selectSearchKeyword(self):
        try:

            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute("")

            keywords = []

            for row in cursor.fetchall():
                keyword_id, keyword = row
                search_keyword = SearchKeywordDTO(keyword_id, keyword)
                keywords.append(search_keyword)

            return keywords

        except Exception as e:

            print("Error:", e)

        finally:

            connection.close()


    def registerSearchKeyword(self, keyword):
        try:

            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute("")
            connection.commit()
            return True

        except Exception as e:

            print("Error:", e)
            return False

        finally:

            connection.close()


    def updateForKeywordNotUse(self, searchKeyword):
        try:

            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute("")
            connection.commit()
            return True

        except Exception as e:

            print("Error:", e)
            return False

        finally:

            connection.close()