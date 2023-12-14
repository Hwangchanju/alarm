import sqlite3
from Telegram.Brian.models.dto.ExceptUrlDTO import ExceptUrlDTO

class ExceptUrlDAO:

    def __init__(self, db_file):
        self.db_file = db_file


    def selectSearchKeyword(self):
        try:

            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            cursor.execute("")

            urls = []

            for row in cursor.fetchall():
                url_id, url_address = row
                except_url = ExceptUrlDTO(url_id, url_address)
                urls.append(except_url)

            return urls

        except Exception as e:

            print("Error:", e)

        finally:

            connection.close()


    def registerExceptUrl(self, keyword):
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


    def updateForUrlNotUse(self, url_id):
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