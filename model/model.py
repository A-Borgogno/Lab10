import networkx as nx
from networkx.algorithms.traversal import dfs_successors

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, anno):
        self._grafo.clear()
        nodes = DAO.getAllNodes(anno)
        for node in nodes:
            self._idMap[node.CCode] = node
        self._grafo.add_nodes_from(nodes)
        self.addEdges(anno)

    def addEdges(self, anno):
        edges = DAO.getEdges(anno)
        for edge in edges:
            self._grafo.add_edge(self._idMap[edge[0]], self._idMap[edge[1]])


    def trovaRaggiungibili(self, country):
        successori = dfs_successors(self._grafo, country)
        return list(successori)[1:]