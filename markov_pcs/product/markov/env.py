from markov import *

def get_graph():
  r = StdRandom()
  g = Graph(2, r)
  g.add(Link.from_s('abc'))
  g.add(Link.from_s('abc'))
  g.add(Link.from_s('abc'))
  g.add(Link.from_s('abd'))
  g.add(Link.from_s('abe'))
  return g

def get_markov(lengths):
  m = TextMarkov(lengths)
  add_names(m)
  return m

def add_names(m):
  m.add_text_block('humberto velez')
  m.add_text_block('homer simpson')
  m.add_text_block('diego veralli')

  m.add_text_block('moneymate')
  m.add_text_block('dev day')
  m.add_text_block('team')

m = get_markov([3,2,1])

for i in range(0,18):
  value = m.build_seq(17)
  print str(value) + "\n"
  m.add_text_block(str(value))

print '---- Done ---- '

