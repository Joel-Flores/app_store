from flask import request
def resquiest_form (names):
    _list = list()
    _dict = dict()
    for name in names:
        data = request.form[name]
        if data == '':
            data = 0
        _dict[name] = int(data)
        _list.append(int(data))
    return _dict, _list