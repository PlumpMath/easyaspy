import networkx as _nx
import matplotlib.pyplot as _plt
from mpl_toolkits.mplot3d import Axes3D as _axes
from numpy import array as _array

def converter(procedure):
	"Convert adjacency list to graph before passing to procedure."
	def _convert(g,*args,**kwargs):
		if not type(g) is _nx.Graph:
			g = of(g)
		return procedure(g,*args,**kwargs)
	return _convert

def of(edges):
	"Graph from adjacency list."
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
	return converter(_get_attr)

def layout(g, dim=3, k=None):
	"Graph nodes are assigned an (x,y,z)."
	k=k or 1/len(g)**0.5
	xyz = _nx.spring_layout(g, dim=3, k=k)
	return xyz

xyz = attributer('position',layout)
xyz.__doc__ = '[0,1,...] -> {0:(x,y,z),1:(x,y,z),...}'

degrees = attributer('degree',lambda g: g.degree())
degrees.__doc__ = '[(1,2),(2,3)] -> {1:1,2:2,3:1}'

def plotter(finish):
	def _lines(g):
		"Graph -> [((x,y,z),(x,y,z)),...]"
		verts = xyz(g)
		return _array(list(map(lambda edge: (verts[edge[0]],verts[edge[1]]), g.edges())))

	def _plot(g, *args, **kwargs):
		"Plot a graph."
		fig = _plt.figure()
		ax = _axes(fig)
		ax_plot = ax.plot

		for line in _lines(g):
			ax_plot(line[:,0],line[:,1],line[:,2])

		return finish(fig,ax,*args,**kwargs)

	return converter(_plot)

def savefig(fig,ax,filename=None):
	filename = filename or 'graph.png'
	_plt.savefig(filename)
png = plotter(savefig)
png.__doc__ = 'Export graph to PNG file.'

# going green
del converter,attributer,layout,plotter,savefig

