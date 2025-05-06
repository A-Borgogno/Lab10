import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self._view._btnRaggiungibili.disabled = False
        anno = self._view._txtAnno.value
        self._model.buildGraph(anno)
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente", size=18))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {len(list(nx.connected_components(self._model._grafo)))} componenti connesse"))
        for node in self._model._grafo.nodes:
            self._view._txt_result.controls.append(ft.Text(f"{node} -- {self._model._grafo.degree(node)} vicini"))
            self._view._ddStato.options.append(ft.dropdown.Option(text=node, data=node, on_click=self.readNode))
        self._view.update_page()


    def handleRaggiungibili(self, e):
        country = self._node
        if country is None:
            self._view.create_alert("Selezionare uno stato di partenza")
            return
        self._view._txt_result.controls.clear()
        res = self._model.trovaRaggiungibili(country)



    def readNode(self, e):
        self._node = e.control.data
