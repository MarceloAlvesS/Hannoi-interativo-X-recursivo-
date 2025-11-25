from time import perf_counter


def hanoi_r(n, i, a, o, show=True):
    if n > 0:
        hanoi_r(n-1, i, o, a, show=show)

        jogo[o].append(jogo[i].pop())
        if show:
            print(jogo)

        hanoi_r(n-1, a, i, o, show=show)

n = 30

print(f'{"Hanoi recursivo":-^40}')
print()
t = perf_counter()

jogo = [list(range(n, 0, -1)), [], []]
hanoi_r(n, 0, 1, 2, show=False)

print(f'Tempo: {perf_counter() - t}')
print()