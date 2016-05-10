from django.db import connection
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append('../../tryAng')


c = connection.cursor()
c.execute("""DELETE FROM PiParse_postcontents
WHERE post_id IN (SELECT id
                  FROM PiParse_piposts
                  WHERE p_id IN (SELECT p_id
                                 FROM PiParse_piposts
                                 GROUP BY p_id
                                 HAVING count(p_id) > 1))""")
c.fetchall()
c.execute("""DELETE FROM PiParse_piposts
                  WHERE p_id IN (SELECT p_id
                                 FROM PiParse_piposts
                                 GROUP BY p_id
                                 HAVING count(p_id) > 1)""")
c.fetchall()
c.close()
