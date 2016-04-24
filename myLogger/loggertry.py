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
                exc = str(error_type.__name__) + "\n" + str(error_message) + "\n" + error_traceback
                toLogger = myLogger(group=newLogger, type=type, message=message, error=exc)
                toLogger.save()
                return None

        return wrapper

    return wwrapper


def logger_write(group, type, message):
    toLogger = myLogger(group=group, type=type, message=message)
    toLogger.save()