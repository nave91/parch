class E:
  def __init__(i,name):
    i.name = name
  def __repr__(i):
    return i.name

e = E('wow')
print dir(e)
