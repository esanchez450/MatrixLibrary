class Matrix2:
    def __init__(self,M,scalar):
        self.M=M
        self.n=len(M)    ## columns
        self.m=len(M[0]) ## rows
        self.k_vals=[]
        self.scalar=scalar
        
    def mtx_Eq(self, other):
        ## check if matrices are of same dimension for rows and columns
        Meq = (self.m==other.m) and (self.n==other.n)
        if Meq:
            return Meq,True
        else:
            return False

    def scalar_mul(self):
        scalMulM = [[elements * self.scalar for elements in each_col] for each_col in self.M]
        return scalMulM

    def add_mtx(self,other):
        ## adds matrix of same dimensions
        if self.mtx_Eq(other):
            sumOfM = [[sum(each) for each in zip(*both)] for both in zip(self.M,other.M)]
            return sumOfM
        else:
            noDim='Dimensions are not equal'
            return noDim

    def is_Multiplied(self,other):
        ## checks is matrices can be multipied
        mtxMul = self.n==other.m
        if mtxMul:
            mtxOut=("Will give us a {}x{} matrix".format(self.m,other.n))
            return ('Matrix Multiplication Possible: {}\n\t    {}'.format(mtxMul,mtxOut))
        else:
            return 'Matrices cannot be multipied. Try checking your rows and columns'

    def mtx_mul(self,other):
        ## multiply matrices of m*n by n*p to get m*p 
        if self.is_Multiplied(other):
            mtxMul=[[self.M[j][i]*other.M[j] for j in i] for i in zip(self.M[][i],other.M[]i[])]
            return mtxMul
        M[j][i]



k=Matrix2([[1,2,-1,7],[5,7,4,5],[234,5,3,-345]],2) #,2,3,-30]

h=Matrix2([[3,2,3],[2,7,23],[2,5,42]],1) #,2,1,30+2],[3,2,1,30+2],[3,2,1,30+2],[3,2,1,30+2]

print('M1:', k.M)
print('M2:', h.M,'\n')
k.add_mtx(h)
k.is_Multiplied(h)
print('Added matrix: {}'.format(k.add_mtx(h)),'\n')

print('Scalar Mul: {}'.format(k.scalar_mul()),'\n')

print('Matrix Mul: {}'.format(k.is_Multiplied(h)),'\n')

print('Matrix Mul: {}'.format(k.mtx_mul(h)),'\n')


x=input("enter with commas, no space:")
print(x)
print()
xs=x.split(',')
print(xs)

xl=[[int(i) for i in xs]]

print(xl)
xM=Matrix2(xl,1)
print('\n'+'Your Matrix is:',xM.M)
