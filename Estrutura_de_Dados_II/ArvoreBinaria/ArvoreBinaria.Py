class NodoArvore:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.esq = None
        self.dir = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    # --- INSERIR ---
    def inserir(self, valor):
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, nodo, valor):
        if nodo is None:
            return NodoArvore(valor)
        if valor < nodo.conteudo:
            nodo.esq = self._inserir_rec(nodo.esq, valor)
        elif valor > nodo.conteudo:
            nodo.dir = self._inserir_rec(nodo.dir, valor)
        return nodo

    # --- REMOVER ---
    def remover(self, valor):
        self.raiz = self._remover_rec(self.raiz, valor)

    def _remover_rec(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.conteudo:
            nodo.esq = self._remover_rec(nodo.esq, valor)
        elif valor > nodo.conteudo:
            nodo.dir = self._remover_rec(nodo.dir, valor)
        else:
            if nodo.esq is None:
                return nodo.dir
            elif nodo.dir is None:
                return nodo.esq
            sucessor = self._minimo(nodo.dir)
            nodo.conteudo = sucessor.conteudo
            nodo.dir = self._remover_rec(nodo.dir, sucessor.conteudo)
        return nodo

    def _minimo(self, nodo):
        while nodo.esq is not None:
            nodo = nodo.esq
        return nodo

    # --- VISUALIZAÇÃO ---
    def mostrar(self, nodo=None, nivel=0, interno=False):
        """Exibe a árvore com indentação hierárquica."""
        # Se for a primeira chamada, começa pela raiz
        if not interno:
            nodo = self.raiz
        if nodo is None:
            return
        # imprime primeiro o lado direito (topo visual)
        if nodo.dir:
            self.mostrar(nodo.dir, nivel + 1, True)
        print("   " * nivel + f"-> {nodo.conteudo}")
        if nodo.esq:
            self.mostrar(nodo.esq, nivel + 1, True)

    # --- MOSTRAR NÓS FOLHAS ---
    def mostrar_folhas(self, nodo=None, interno=False):
        if not interno:
            nodo = self.raiz
        if nodo:
            if nodo.esq is None and nodo.dir is None:
                print(nodo.conteudo, end=' ')
            if nodo.esq:
                self.mostrar_folhas(nodo.esq, True)
            if nodo.dir:
                self.mostrar_folhas(nodo.dir, True)


# --------------------------------------
if __name__ == "__main__":
    arv = ArvoreBinaria()
    for valor in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        arv.inserir(valor)

    print("\n🌿 Árvore inicial:")
    arv.mostrar()

    print("\nRemovendo 3...")
    arv.remover(3)
    arv.mostrar()

    print("\nRemovendo 10...")
    arv.remover(10)
    arv.mostrar()

    print("\nNós folhas:")
    arv.mostrar_folhas()
    print()
