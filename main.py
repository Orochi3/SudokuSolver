# checa quadrado por numero, se for valido colocar o numero la retorna true

class Sudoku:

    def __init__(self, matriz):
        # copia os valores da matriz
        self.matriz = []
        for i in range(0, 9):
            temp = []
            for j in range(0, 9):
                temp.append(matriz[i][j])
            self.matriz.append(temp)

    def checar_quad(self, linha, coluna, num):
        inicioL = (linha//3) * 3
        inicioC = (coluna//3) * 3
        for i in range(inicioL, inicioL + 3):
            for j in range(inicioC, inicioC + 3):
                if self.matriz[i][j] == num:
                    return False
        return True

    def checar_linha(self, linha, num):
        for j in range(0, 9):
            if self.matriz[linha][j] == num:
                return False
        return True

    def checar_coluna(self, coluna, num):
        for i in range(0, 9):
            if self.matriz[i][coluna] == num:
                return False
        return True

    def solve_rec(self, num_res):
        if num_res == 0:
            return True
        # loop por todas as casas
        for i in range(0, 9):
            for j in range(0, 9):
                # se ta vazia, verifica se poder fazer o moviment oe faz
                if self.matriz[i][j] == 0:
                    for n in range(1, 10):
                        if self.checar_linha(i, n) and self.checar_coluna(j, n) and self.checar_quad(i, j, n):
                            self.matriz[i][j] = n
                            if self.solve_rec(num_res - 1):
                                return True
                            else:
                                self.matriz[i][j] = 0
                    # se nao fez movimento, a solucao nao pode ser construida por esse caminho
                    return False

    def calc_res(self):
        res = 0
        for i in range(0, 9):
            for j in range(0,9):
                if self.matriz[i][j] == 0:
                    res +=1
        return res

    def solve(self):
        res = self.calc_res()
        self.solve_rec(res)
        return

    def print(self):
        for i in range(0, 9):
            print(self.matriz[i])


exemplo = [[0, 0, 0, 5, 6, 0, 0, 2, 0],
           [0, 0, 7, 3, 0, 2, 9, 0, 0],
           [0, 0, 4, 0, 9, 0, 0, 8, 3],
           [0, 0, 9, 0, 0, 0, 1, 0, 0],
           [0, 0, 0, 7, 0, 0, 0, 0, 0],
           [0, 5, 0, 0, 0, 0, 0, 0, 4],
           [9, 8, 0, 0, 0, 0, 0, 0, 0],
           [2, 0, 0, 0, 5, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 1]]
tab = Sudoku(exemplo)
tab.print()
print("-"*27)
tab.solve()
tab.print()
