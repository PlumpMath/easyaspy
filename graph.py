import networkx as _nx
import matplotlib.pyplot as _plt
from mpl_toolkits.mplot3d import Axes3D as _axes
from numpy import array as _array

# Higher order functions
# ** These are not exposed **

def _uses_graph_to(do_this):
	"Ensures g is a NetworkX Graph, and calls do_this with g."
	def _as_networkx(g,*args,**kwargs):
		if not type(g) is _nx.Graph:
			g = of(g)
		return do_this(g,*args,**kwargs)
	return _as_networkx

def _lists_nodes(attr,otherwise_get):
	"Ensures g has attribute attr, otherwise adds attribute to all nodes with otherwise_get."
	# lists node's <x> uses graph to get each node's <x>
	def _attrs(g):
		"List attributes available in g."
		return g.node[next(g.nodes_iter())]
	
	def _get_attr(g,*args,**kwargs):
		"Get attribute attr from g, or add attr."
		if not attr in _attrs(g):
			result = otherwise_get(g,*args,**kwargs)
			_nx.set_node_attributes(g, attr, result)
		return _nx.get_node_attributes(g,attr)

	return _uses_graph_to(_get_attr)

def _plots_to(format):
	"Plots with matplotlib ending plot with procedure."
	# plots to <x> uses a graph and plots it to <x>
	def _lines(g):
		"List lines in g as pairs of 3d vectors ((x,y,z),(x,y,z))."
		verts = xyz(g)
		return _array(list(map(lambda edge: (verts[edge[0]],verts[edge[1]]), g.edges())))

	def _plot(g, *args, **kwargs):
		"Plot g."
		fig = _plt.figure()
		ax = _axes(fig)
		ax_plot = ax.plot

		for line in _lines(g):
			ax_plot(line[:,0],line[:,1],line[:,2])

		return format(fig,ax,*args,**kwargs)

	return _uses_graph_to(_plot)

# main functions

def of(edges):
	"Graph of adjacency list."
	# graph.of([(1,2),(2,3)])
	# wrapper for nx.Graph.add_edges_from
	g = _nx.Graph()
	g.add_edges_from(edges)
	return g

def 

subgraphs = uses_graph_to(lambda g: nx.connected_components(g))
subgraphs.__doc__ = 'Yield connected components of graph.'
# graph.subgraphs([(1,2),(2,3),(4,5)]) -> [{1,2,3},{4,5}]

def _find_3d_layout(g, dim=3, k=None):
	"Graph nodes are assigned an (x,y,z)."
	# exclusively for graph.xyz
	# wrapper for nx.spring_layout
	k=k or 1/len(g)**0.5
	xyz = _nx.spring_layout(g, dim=3, k=k)
	return xyz

xyz = _lists_node('position',_find_3d_layout)
xyz.__doc__ = '[0,1,...] -> {0:(x,y,z),1:(x,y,z),...}'
# graph.xyz([(1,2),(2,3)]) will associate
# the graphs nodes (ie [1,2,3]) with
# 3 dimensional vectors (x,y,z)

degrees = _lists_node('degree',lambda g: g.degree())
degrees.__doc__ = '[(1,2),(2,3)] -> {1:1,2:2,3:1}'
# graph.degrees([(1,2),(2,3)]) will associate
# the graphs nodes (ie [1,2,3]) with
# its degree

def _file(fig,ax,filename=None):
	"Save matplotlib figure to file."
	# exclusively for graph.png
	# wrapper for matplotlib.pyplot.savefig
	filename = filename or 'graph.png'
	_plt.savefig(filename)

png = _plots_to(_file)
png.__doc__ = 'Export graph to PNG file.'
# graph.png([(1,2),(2,3)]) will save
# a file named graph.png

def _gui(fig,ax):
	"Show matplotlib gui."
	# exclusively for gui
	# wrapper for matplotlib.pyplot.show
	_plt.show()

gui = _plots_to(_gui)
gui.__doc__ = 'Show graph in matplotlib gui.'
# graph.gui([(1,2),(2,3)]) will show
# the graph in a matplotlib window

# going green
del _uses_graph_to,_lists_nodes, \
	_plots_to,_find_3d_layout,_file

