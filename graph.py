import networkx as _nx
import matplotlib.pyplot as _plt
from mpl_toolkits.mplot3d import Axes3D as _axes
from matplotlib import animation as _anim
import numpy as _np

def of(edges):
	"Shorthand for NetworkX graph from adjacency list."
	g = _nx.Graph()
	g.add_edges_from(edges)
	return g

def subgraphs(g):
	"List connected components in graph."
	return _nx.connected_components(g)

def attributer(attr,get):
	"Build a function to add an attribute to a graph."
	def _attrs(g):
		"Attributes for each node."
		return g.node[next(g.nodes_iter())]
	
	def _get_attr(g,*args,**kwargs):
		"Get an attr from graph."
		if not attr in _attrs(g):
			result = get(g,*args,**kwargs)
			_nx.set_node_attributes(g, attr, result)
		return _nx.get_node_attributes(g,attr)
	return _get_attr

def layout(g, dim=3, k=None):
	"Graph nodes are assigned an (x,y,z)."
	k=k or 1/len(g)**0.5
	xyz = _nx.spring_layout(g, dim=3, k=k)
	return xyz

xyz=attributer('position',layout)
xyz.__doc__="Set of nodes with (x,y,z)."

degrees=attributer('degree',lambda g: g.degree())
degrees.__doc__="Set of nodes with degree."

# going green
del attributer, layout

"""
def view(edges,labels=True,filename='graph.png'):
	"Draw edges to file."
	g = nx.Graph()
	g.add_edges_from(edges)

	q=255.0
	colors=[(0,48,86),(4,81,140),(0,161,217),(71,217,191),(242,208,59)]
	colors=[(x/q,y/q,z/q) for x,y,z in colors]

	xyz = nx.spring_layout(g, dim=3, k=1/len(g)**0.5)

	vertices = [(str(n),xyz[n]) for n in g]
	values = g.degree().values()
	min_degree = min(values)
	max_degree = max(values)-min_degree
	n_colors = len(colors)
	lines = np.array([(xyz[a],xyz[b]) for a,b in g.edges()])
	line_color = []
	fontsizes=[]
	
	for n in g:
		a = (g.degree(n)-min_degree)/max_degree
		fontsizes.append(a*3+1)

	for a,b in g.edges():
		ad = (g.degree(a)-min_degree)/max_degree
		bd = (g.degree(b)-min_degree)/max_degree
		avg = (ad+bd)/2.0
		line_color.append(colors[math.floor(avg*n_colors)])

	fontsizes=iter(fontsizes)
	line_color = iter(line_color)
	f = plt.figure()
	ax = Axes3D(f)

	ax.set_axis_bgcolor('black')

	text = ax.text
	plot = ax.plot
	fontdict={'fontsize':3,'color':'white'}
	def init():
		if labels:
			for label, (x, y, z) in vertices:
				text(x, y, z, label, fontdict={'fontsize':next(fontsizes),'color':'white'})
	
		lineops={'marker':'o','lw':'0.1','ms':'0.25'}
		
		for line in lines:
			color=next(line_color)
			plot(line[:,0],
				 line[:,1],
				 line[:,2],
				 mfc=color,
				 color=color,
				 **lineops)
	
	plt.axis('off')
	animate = lambda x: ax.view_init(elev=0.0,azim=x)
	anim = animation.FuncAnimation(f,animate,init_func=init,frames=360,interval=20)
	anim.save('anim.mp4',fps=30,extra_args=['-vcodec','libx264'])
#	for i in range(0,360):
#		ax.view_init(30,i)	
#		plt.savefig('graph{0}.png'.format(i),
#				bbox_inches=None,
#				pad_inches=0,
#				transparent=False,
#				format=None,
#				papertype=None,
#				edgecolor='black',
#				facecolor='black')
"""
