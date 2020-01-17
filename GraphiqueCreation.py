# Dependances pour tracer le graphique
from graphviz import Digraph
from graphviz import Source

graph = Digraph()

# Creation des noeuds symbolisant les lieux dits
graph.node(name='A', label='Boston')
graph.node(name='B', label='Providence')
graph.node(name='C', label='New Orleans')
graph.node(name='D', label='Paterson')
graph.node(name='E', label='San Francisco')
graph.node(name='F', label='Dunedin')
graph.node(name='G', label='Auckland')
graph.node(name='H', label='Sydney')
graph.node(name='I', label='London')
graph.node(name='J', label='Oslo')

# Creation des aretes du graphique
graph.edge(tail_name='A', head_name='B', label='1')
graph.edge(tail_name='B', head_name='C', label='2')
graph.edge(tail_name='C', head_name='A', label='3')
graph.edge(tail_name='A', head_name='D', label='4')
graph.edge(tail_name='D', head_name='E', label='5')
graph.edge(tail_name='E', head_name='F', label='6')
graph.edge(tail_name='F', head_name='G', label='7')
graph.edge(tail_name='G', head_name='H', label='8')
graph.edge(tail_name='H', head_name='I', label='9')
graph.edge(tail_name='I', head_name='J', label='10')
graph.edge(tail_name='J', head_name='I', label='11')
graph.edge(tail_name='I', head_name='A', label='12')

# Creation du fichier de resultat
graph.save(filename='cthulhu.gv')

# Affichage du resultat
graph.render('cthulu.gv', view=True)
