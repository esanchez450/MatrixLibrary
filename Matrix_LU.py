"""

FINDING THE LU FACTORIZATION OF A MATRIX, A

"""

class Matrix:
    def __init__(self, M, n):
        self.M = M
        self.rank = n
        self.k_vals = list()
        self.In = [[1,0,0],
                   [0,1,0],
                   [0,0,1]]

    def getCol(self, c):
        return self.M[c]

    def getRow(self, r):
        row = []
        for i in self.M:
            row.append(i[r])
        return row

    def testFacts(self):
        if self.M[0][0] == 0:
            return False

        d = self.M[0][0] * self.M[1][1] - self.M[1][0] * self.M[0][1]

        if d == 0:
            return False

        d = self.M[0][0] * (self.M[1][1] * self.M[2][2] - self.M[2][1] * self.M[1][2]) - \
            self.M[1][0] * (self.M[0][1] * self.M[2][2] - self.M[2][1] * self.M[0][2]) + \
            self.M[2][0] * (self.M[0][1] * self.M[1][2] - self.M[1][1] * self.M[0][2])

        if d == 0:
            return False

        else:
            return True

    def row_reduce(self, c, r):
        row = r
        j = c

        if self.M.index(self.M[j]) == len(self.M) - 1 and self.M[j][row] != 0:
            self.M[j][row+1] -= round(float(self.M[j][row] * \
                                              self.M[j][row+1]/self.M[j][row]))
        elif self.M[j][row+1] == 0:
            self.k_vals.append(0)

        else:
            while self.M[j][row] == 0:
                row -= 1
                
            k = self.M[j][r+1]/M[j][row]
            self.k_vals.append(k)
        
            while j != self.rank:
                print("{} - {} * {} = {}".format(M[j][r+1], M[j][row], k, (M[j][r+1] - M[j][row] * k)))

                if M[j][r+1] == 0:
                    M[j][r+1] -= M[j][row] * k
                    j += 1
                else:
                    M[j][r+1] = round(float(M[j][r+1])) - round(float(M[j][row] * k))
                    j += 1
        return self.M

    def get_L(self):

        L = self.In
        A0 = list(map(list, self.M))
        
        A.row_reduce(0,0)
        A.row_reduce(0,1)
        A.row_reduce(1,1)

        L[0][1] = A.k_vals[0]
        L[0][2] = A.k_vals[1]
        L[1][2] = A.k_vals[2]



        return Matrix(L,3), A, A0

    def __mul__(self, B):
        if type(B) is not Matrix:
            return "{} is not a Matrix".format(B)
        elif self.rank != B.rank:
            return "This program does not currently work for nxn * pxp matrices..."
        else:
            C = self.In
            count = -1

            for i in range(self.rank):
                count += 1
                for j in range(self.rank):
                    for k in range(self.rank):
                        C[j][count] += self.M[count][j] * B.M[count][j]
        return Matrix(C,3)
                
                

    def __str__(self):
        count = 1
        sn = '[M]{}x{} \n'.format(self.rank, self.rank)
        for a in self.M:
            sn += "column {} = {}\n".format(count, a)
            count += 1
        return sn


M = [[1,-8,6],
     [-7,9,-4],
     [2,1,0]]

A = Matrix(M, 3)

print("Matrix A:", A)

if A.testFacts() == False:
    print("Not factorable")

else:
    
    L, U, A0 = A.get_L()
    A = Matrix(A0, 3)

    print("\n")
    print("Matrix A:", A)
    print("Matrix L =", L)
    print("Matrix U =", U)

    print("Have a nice day...")

print(L.getRow(2))
print(L * U)
