import sys
import traceback

from myLogger.models import myLogger


# decorator
def logger_try_or_none(type, message):
    def wwrapper(fn):
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except:
                newLogger = args[0]._newLogger
                error_type, error_message, error_traceback = sys.exc_info()
                error_traceback = ''.join(traceback.format_tb(error_traceback))
                # for future insert into " "
                error_traceback = error_traceback.replace('"', "\'")
                # exept advertising post
                if error_traceback.find('story_rating') == -1:
                    # exc = str(error_type.__name__) + "\n" + str(error_message) + "\n" + error_traceback
                    exc = '{} \n {} \n {}'.format(error_type.__name__, error_message, error_traceback)
                    newLogger['logs'].append({'type': type, 'message': message, 'error': exc})
                return None

        return wrapper

    return wwrapper


def logger_write(group, type, message):
    # Due to save() changed to raw sql...
    group['logs'].append({'type': type, 'message': message, 'error': ''})