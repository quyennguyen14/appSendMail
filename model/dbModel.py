from config import config
from Ultils.Log import nlogger
import traceback  # debug
import pymssql
import pandas as pd

class getData:

    def __init__(self, filename='config/config.ini', section='mssql'):
        self.filename = filename
        self.section = section

    # Lấy dữ liệu trả ra Pandas Dataframe
    def SP_Articles_getInfo_byArticleId_Pandas(self, articleId):
        configParam = config.config()
        data_checkInVN = configParam.config_mssql_db(filename=self.filename, section=self.section)

        try:
            conn = pymssql.connect(
                server=data_checkInVN['host'],
                database=data_checkInVN['database'],
                user=data_checkInVN['user'],
                password=data_checkInVN['password']
            )

            cursor = conn.cursor()

            sql_text = """
                        SET NOCOUNT ON
                        EXEC	[dbo].[SP_Articles_getInfo_byArticleId]
                                @Article_Id = %s
                        """
            params = (articleId,)

            # Exec query
            cursor.execute(sql_text, params)
            column_names = [col[0] for col in cursor.description] # Get column names from SQL

            df_data = []
            for row in cursor.fetchall():
                df_data.append({name: row[i] for i, name in enumerate(column_names)})

            df = pd.DataFrame(df_data)

            return df

        except Exception as e:
            nlogger(string="!!!!!!!!!! EXCEPTION !!!!!!!!!", filename='getdata', log_type='error')
            nlogger(string=str(e), filename='getdata', log_type='error')
            nlogger(string=traceback.format_exc(), filename='getdata', log_type='error')
            return []

