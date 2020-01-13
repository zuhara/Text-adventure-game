import game
def test_navigate_north():
    map = {1:{'n':2,'s':3,'e':0,'w':0,'room':'Hall'},2:{'n':0,'s':1,'e':3,'w':0,'room':'Kitchen'},3:{'n':1,'s':0,'e':0,'w':2,'room':'Garden'}}
    a = game.navigate(map,direction = 'n',current_position = 1)
    e = 2
    assert a == e

def test_navigate_south():
    map = {1:{'n':2,'s':3,'e':0,'w':0,'room':'Hall'},2:{'n':0,'s':1,'e':3,'w':0,'room':'Kitchen'},3:{'n':1,'s':0,'e':0,'w':2,'room':'Garden'}}
    a = game.navigate(map,direction = 's',current_position = 1)
    e = 3
    assert a == e

def test_navigate_east():
    map = {1:{'n':2,'s':3,'e':0,'w':0,'room':'Hall'},2:{'n':0,'s':1,'e':3,'w':0,'room':'Kitchen'},3:{'n':1,'s':0,'e':0,'w':2,'room':'Garden'}}
    a = game.navigate(map,direction = 'e',current_position = 2)
    e = 3
    assert a == e

def test_navigate_west():
    map = {1:{'n':2,'s':3,'e':0,'w':0,'room':'Hall'},2:{'n':0,'s':1,'e':3,'w':0,'room':'Kitchen'},3:{'n':1,'s':0,'e':0,'w':2,'room':'Garden'}}
    a = game.navigate(map,direction = 'w',current_position = 3)
    e = 2
    assert a == e

def test_navigate_no_where():
    map = {1:{'n':2,'s':3,'e':0,'w':0,'room':'Hall'},2:{'n':0,'s':1,'e':3,'w':0,'room':'Kitchen'},3:{'n':1,'s':0,'e':0,'w':2,'room':'Garden'}}
    a = game.navigate(map,direction = 'w',current_position = 2)
    e = 2
    assert a == e
