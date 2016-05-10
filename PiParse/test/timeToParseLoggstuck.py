import datetime
from timeit import Timer

import pytz

tryes=1000

def toStuck():
    loggs = {'title': 'trying date=, tillPage=None, tillRating=None',
             'logs': [{'error': '', 'type': 'info', 'message': 'Post was created: Коллекторы ищут людей через пикабу'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Однажды в ресторане'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Любителям метро на заметку'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Кровавый ЖЭК или будни юриста.'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Когда кафедра с чувством юмора'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Про мемы и взаимоотношения'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Потерял 100000 рублей'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Восстание машин обречено на провал.'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Чудеса случаются!'},
                      {'error': '', 'type': 'info',
                       'message': 'Post was created: Пожарные, которые не покладая рук работали всю ночь, наконец, получили столь необходимый отдых"'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Теперь проживем'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Въезд в город'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Селфи на игровом табло'},
                      {'error': '', 'type': 'info',
                       'message': 'Post was created: В Казахстане сняли короткометражку к 9 мая'},
                      {'error': '', 'type': 'info',
                       'message': 'Post was created: В России появится организация для защиты атеистов'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Дух общаги :3'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Смотрите как я могу'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Поступок...'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Сквозь время'},
                      {'error': '', 'type': 'info', 'message': 'Post was created: Ой как тесно!'}, {
                          'error': 'TypeError\n\'NoneType\' object is not subscriptable\n  File "C:\\Users\\Tidjei\\PycharmProjects\\tryAng\\myLogger\\rawLoggertry.py", line 12, in wrapper\n    return fn(*args, **kwargs)\n  File "C:\\Users\\Tidjei\\PycharmProjects\\tryAng\\PiParse\\scripts\\rawParseScript.py", line 51, in setPost\n    link = story_link[\'href\']\n',
                          'type': 'error', 'message': 'setPost fail to set a post date'}]}

    stuckLoggs = []
    for log in loggs['logs']:
        now = str(datetime.datetime.now(pytz.UTC))
        stuckLog = (log['type'], log['message'], log['error'], 1111, now)
        stuckLoggs.append(stuckLog)

def timetoStuck():
    t = Timer(lambda: toStuck())
    return t.timeit(number=tryes)

if __name__ == "__main__":
    print(timetoStuck()/tryes)