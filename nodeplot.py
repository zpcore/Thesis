import plotly
import plotly.plotly as py
from plotly.graph_objs import *

import networkx as nx

#G=nx.random_geometric_graph(10,0.125)


G=nx.Graph()
G.add_node(1, 
  pos=[1,2], 
  ref='paper name', 
  focus='Embedded Computer Architecture for Trajectory Generation under Dynamic Conditions')
G.add_node(2, 
  pos=[0.5,1],
  focus='Trajectory Generation')
G.add_node(3, 
  pos=[1.5,1],
  focus='System Adjustable w.r.t. Dynamic Conditions')
G.add_node(4, 
  pos=[-1.0,-1],
  focus='Bellman\'s Dynamic Programming')
G.add_node(5, 
  pos=[0.5,-1],
  focus='Pontryagin\'s Maximum Principal')
G.add_node(6,
  pos=[2.5,1],
  focus='Trajectory Tracking')
G.add_node(7,
  pos=[-1.5,0],
  focus='Local Trajectory(online)')
G.add_node(8,
  pos=[-0.5,0],
  focus='Global Trajectory(offline)')
G.add_node(9,
  pos=[-2.5,-1],
  focus='A Star')
G.add_node(10,
  pos=[-1.8,-1],
  focus='D Star')
G.add_node(11,
  pos=[-3.8,-1],
  focus='Potential Field')
G.add_node(12,
  pos=[-3.0,-1],
  focus='Dynamic Window')
#G.add_edge(1,2)
G.add_edges_from([(1,2),(1,3),(2,7),(2,8),(8,4),(8,5),(1,6),(8,10),(8,9),(7,11),(7,12)])
# G.add_node(1)
# G.add_edge(1,2)
pos=nx.get_node_attributes(G,'pos')

# dmin=1
# ncenter=0
# for n in pos:
#     x,y=pos[n]
#     d=(x-0.5)**2+(y-0.5)**2
#     if d<dmin:
#         ncenter=n
#         dmin=d

#p=nx.single_source_shortest_path_length(G,ncenter)

edge_trace = Scatter(
    x=[],
    y=[],
    line=Line(width=0.5,color='#888'),
    hoverinfo='none',
    mode='lines')

for edge in G.edges():
    x0, y0 = G.node[edge[0]]['pos']
    x1, y1 = G.node[edge[1]]['pos']
    edge_trace['x'] += [x0, x1, None]
    edge_trace['y'] += [y0, y1, None]

node_trace = Scatter(
    x=[],
    y=[],
    text=[],
    textposition='bottom center',
    mode='markers+text',
    #hoverinfo='text',
    hoverinfo=['x','y'],
    marker=Marker(
        showscale=True,
        # colorscale options
        # 'Greys' | 'Greens' | 'Bluered' | 'Hot' | 'Picnic' | 'Portland' |
        # Jet' | 'RdBu' | 'Blackbody' | 'Earth' | 'Electric' | 'YIOrRd' | 'YIGnBu'
        colorscale='YIGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line=dict(width=2)))
for node in G.nodes():
    x, y = G.node[node]['pos']
    node_trace['x'].append(x)
    node_trace['y'].append(y)
    node_trace['text'].append(G.node[node]['focus'])

for node, adjacencies in enumerate(G.adjacency_list()):
  node_trace['marker']['color'].append(len(adjacencies))
  node_info = '# of connections: '+str(len(adjacencies))
  node_trace['text'].append(node_info+"jidoccdi")

fig = Figure(data=Data([edge_trace, node_trace]),
             layout=Layout(
                title='<br>Network graph for Ph.D. Thesis',
                titlefont=dict(size=16),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    #text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                    text="Pei Zhang ISU",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=-0.005, y=-0.002 ) ],
                xaxis=XAxis(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=YAxis(showgrid=False, zeroline=False, showticklabels=False)))

plotly.offline.plot(fig, filename='networkx.html')
#py.plot(fig, filename='networkx.html')