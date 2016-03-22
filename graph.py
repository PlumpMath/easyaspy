import networkx as _nx
import matplotlib.pyplot as _plt
from mpl_toolkits.mplot3d import Axes3D as _axes
from matplotlib.animation import FuncAnimation as _animation
from numpy import array as _array

def is_graph(g):
	return type(g) is _nx.Graph

def uses_graph_to(do_this):
	def fn(g,*args,**kwargs):
		if not is_graph(g):
			g = of(g)
		return do_this(g,*args,**kwargs)
	return fn

def lists_nodes(attr,otherwise_get):
	def attrs(g):
		return g.node[next(g.nodes_iter())]
	
	def get_attr(g,*args,**kwargs):
		if not attr in attrs(g):
			result = otherwise_get(g,*args,**kwargs)
			_nx.set_node_attributes(g, attr, result)
		return _nx.get_node_attributes(g,attr)

	return uses_graph_to(get_attr)

def plotter(dim=3):
	fig = _plt.figure()
	
	if dim is 2:
		ax = fig.add_subplot(111)
	else:
		ax = _axes(fig)

	return fig, ax

def lines_and_labels(g):
	verts = xyz(g)
	labels = [(str(n),verts[n]) for n in g]
	line = lambda edge: (verts[edge[0]],verts[edge[1]])
	lines = _array(list(map(line,g.edges())))

	return lines, labels

def axis_colors(ax,colors):
	bg, *lines = colors

	_plt.axis('off')
	ax.set_axis_bgcolor(bg)

def plot3D(ax, g):
	ax_plot = ax.plot

	lines,labels = lines_and_labels(g)

	for line in lines:
		ax_plot(line[:,0], line[:,1], line[:,2])
	
	return ax

def plot2D(ax, line):
	ax.plot(line)
	return ax

def plot_to(format):
	def run(x):
		if is_graph(x):
			fig, ax = plotter()
			plot3D(ax,x)
		else:
			fig, ax = plotter(dim=2)
			plot2D(ax,x)
		format()
		return ax
	return run

# exports ->

def of(edges):
	g = _nx.Graph()
	g.add_edges_from(edges)
	return g

subgraphs = uses_graph_to(lambda g: _nx.connected_components(g))

def find_3d_layout(g, dim=3, k=None):
	k=k or 1/len(g)**0.5
	xyz = _nx.spring_layout(g, dim=3, k=k)
	return xyz

xyz = lists_nodes('position',find_3d_layout)
degrees = lists_nodes('degree',lambda g: g.degree())
betweeness = lists_nodes('betweeness',lambda g: _nx.betweeness_centrality(g,g.nodes()))

def rotator(g, ax, frames):
	plot3D(ax, g)
	def rotate(i):
		ax.view_init(elev=0.0,azim=(i % 360))
	return rotate

def chunk(i, g):
	degs = degrees(g).items()
	max_deg = max([v for k,v in degs]) - 1
	i = i*max_deg
	ccs = subgraphs(
		g.subgraph(
			[node for node, deg in degs if deg > i]))
	ccs = sorted(ccs,key=len)
	return g.subgraph(ccs[-1])

def accumulator(g, ax, frames):
	seq = (chunk(i/(frames + 2.0),g) for i in reversed(range(frames + 2)))
	def accumulate(i):
		plot3D(ax, next(seq))
	return accumulate

def combine(*animators):
	def combiner(g, ax, frames):
		animations = [x(g, ax, frames) for x in animators]
		def run_multiple(i):
			for animate in animations:
				animate(i)
		return run_multiple
	return combiner

def make_video(g, filename=None, animator=rotator):
	fig, ax = plotter()
	filename = filename or 'graph.mp4'
	frames=360
	anim = _animation(fig, animator(g, ax, frames), frames=frames, interval=20)
	anim.save(filename, fps=30, extra_args=['-vcodec','libx264'])

mp4=uses_graph_to(make_video)

def image(filename=None):
	filename = filename or 'graph.png'
	_plt.savefig(filename)

png = plot_to(image)

def window():
	plt.show()

gui = plot_to(window)

# going green
del uses_graph_to,lists_nodes, \
	plot_to,find_3d_layout, \
	image, window, make_video

