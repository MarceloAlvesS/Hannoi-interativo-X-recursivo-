from time import perf_counter


class Hanoi_i:
    jogo = [[], [], []]

    def __init__(self, n):
        self.jogo = [list(range(n, 0, -1)), [], []]
        self.dificuldade = n
        if n % 2 == 0:
            self.movimento = lambda x: (x+1)%3 
        else:
            self.movimento = lambda x: (x-1)%3
        self.ultimo = -1

    def pilha_get(self, pilha):
        if pilha:
            return pilha[-1]
        return self.dificuldade + 1

    def passo(self):
        topo = [self.pilha_get(self.jogo[0]), self.pilha_get(self.jogo[1]), self.pilha_get(self.jogo[2])]

        for index in range(3):
            move = index
            if index != self.ultimo and topo[index] != 0:
                for _ in range(2):
                    move = self.movimento(move)
                    if topo[index] < topo[move]:
                        self.jogo[move].append(self.jogo[index].pop())
                        self.ultimo = move
                        return

    def resolver(self, show=True):
        fim = [[], [], list(range(self.dificuldade, 0, -1))]
        if show:
            print(self.jogo)
        while self.jogo != fim:
            self.passo()
            if show:
                print(self.jogo)


            

    def __str__(self):
        return str(self.jogo)


if __name__ == '__main__':
    n = 30

    print(f'{"Hanoi interativo":-^40}')
    print()
    t = perf_counter()
    Hanoi_i(n).resolver(show=False)
    print(f'Tempo: {perf_counter() - t}')
    print()
