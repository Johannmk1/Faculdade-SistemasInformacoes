class NodoArvore:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.esq = None
        self.dir = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    # --- PERTENCE ---
    def pertence(self, valor):
        return self._pertence_rec(self.raiz, valor)

    def _pertence_rec(self, nodo, valor):
        if nodo is None:
            return False
        if valor < nodo.conteudo:
            return self._pertence_rec(nodo.esq, valor)
        elif valor > nodo.conteudo:
            return self._pertence_rec(nodo.dir, valor)
        else:
            return True

    # --- INSERIR ---
    def inserir(self, valor):
        if self.pertence(valor):
            print(valor , " já pertence à árvore.")
        else:
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
        if self.pertence(valor):
            self.raiz = self._remover_rec(self.raiz, valor)
        else:
            print(valor , " não esta na árvore.")

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

    # --- COMPLETA ---
    def completa(self, nodo=None, interno=False):
        if not interno:
            nodo = self.raiz
        if nodo is None:
            return
        if nodo.esq is None and nodo.dir is None:
            return True
        if nodo.esq is None or nodo.dir is None:
            return False
        return self.completa(nodo.esq, True) and self.completa(nodo.dir, True)
            

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
    
    def mostrarPreOrdem(self, nodo=None, interno=False):
        if not interno:
            nodo = self.raiz
        if nodo:
            print(nodo.conteudo, end=" - ")
            self.mostrarPreOrdem(nodo.esq, True)
            self.mostrarPreOrdem(nodo.dir, True)
        else:
            return

    def mostrarOrdem(self, nodo=None, interno=False):
        if not interno:
            nodo = self.raiz
        if nodo:
            self.mostrarOrdem(nodo.esq, True)
            print(nodo.conteudo, end=" - ")
            self.mostrarOrdem(nodo.dir, True)
        else:
            return

    def mostrarPosOrdem(self, nodo=None, interno=False):
        if not interno:
            nodo = self.raiz
        if nodo:
            self.mostrarPosOrdem(nodo.esq, True)
            self.mostrarPosOrdem(nodo.dir, True)
            print(nodo.conteudo, end=" - ")
        else:
            return

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
    for valor in [8, 3, 10, 1, 6, 14, 4, 16, 17]:
        arv.inserir(valor)

    print("\nÁrvore inicial:")
    arv.mostrar()

    print("\nÁrvore inicial pre ordem:")
    arv.mostrarPreOrdem()

    print("\nÁrvore inicial ordem:")
    arv.mostrarOrdem()

    print("\nÁrvore inicial pos ordem:")
    arv.mostrarPosOrdem()

    print("\nRemovendo 3...")
    arv.remover(3)
    arv.mostrar()

    print("\nRemovendo 10...")
    arv.remover(10)
    arv.remover(999)
    arv.mostrar()

    print("\nNós folhas:")
    arv.mostrar_folhas()
    print()

    if arv.completa():
        print("Completa")
    else:
        print("Não completa")
