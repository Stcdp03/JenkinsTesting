
def func(f):
    if(f == 'Hello'):
        return "World"
    else:
        return 'Hello'


def test_answer():
    assert func('Hello') == 'World'

def test_wrong():
    assert func('World') == 'Hello'








'''
def test_answer():
    assert func(**) == **
    '''
