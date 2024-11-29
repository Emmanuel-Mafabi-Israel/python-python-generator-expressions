# GLORY BE TO GOD,
# RUNNING PYTHON CODE, 
# CREATING A PYTHON APPLICATION - LIST COMPREHENSIONS,
# BY ISRAEL MAFABI EMMANUEL

def return_evens(_list_:list)->list:
    return [n for n in _list_ if n % 2 == 0]

def make_exclamation(_list_:list)->list:
    return [n + "!" for n in _list_ if n]