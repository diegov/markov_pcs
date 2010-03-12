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
  m.add_text_block('changing from recursion to stack data structures has allowed me to generate very large sequences')
  m.add_text_block('of course the same could have been achieved with tail call optimisation, although I\'m not sure that would have been possible here')

  f = open('usher10.txt', 'r')
  for line in f:
    m.add_text_block(line)

  m.add_text_block('moneymate')
  m.add_text_block('dev day')
  m.add_text_block('team')

m = get_markov([7,6,8,5,4])

for i in range(0,5):
  value = m.build_seq(1500)
  print str(value) + "\n"
  m.add_text_block(str(value))

print '---- Done ---- '

