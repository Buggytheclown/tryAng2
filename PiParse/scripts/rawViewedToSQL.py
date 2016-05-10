from django.db import connection

def ViewedToDB(userid, viewed):
    cursor = connection.cursor()
    sql = """INSERT OR IGNORE INTO PiParse_piposts_viewed (piposts_id, user_id)  VALUES """
    for i in viewed:
        sql += "({}, {}), ".format(i, userid)
    cursor.execute(sql[:-2])
    cursor.fetchall()
    connection.close()