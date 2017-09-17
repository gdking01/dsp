# Matrix Algebra

A=np.matrix([[1,2,3],[2,7,4]])
B=np.matrix([[1,-1],[0,1]])
C=np.matrix([[5,-1],[9,1],[6,0]])
D=np.matrix([[3,-2,-1],[1,2,3]])
u=np.matrix([[6,2,-3,5]])
v=np.matrix([[3,5,-1,4]])
w=np.matrix([[1],[8],[0],[5]])

print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(v.shape)
print(w.shape)

# (2, 3)
# (2, 2)
# (3, 2)
# (2, 3)
# (1, 4)
# (1, 4)
# (4, 1)


print(u+v)
print(u-v)
print(6*u)
print(np.dot(u,v.T))
print(sqrt(sum([x**2 for x in u.tolist()[0]])))

# [[ 9  7 -4  9]]
# [[ 3 -3 -2  1]]
# [[ 36  12 -18  30]]
# [[51]]
# 8.602325267042627


print('A+C undefined')
print(A-C.T)
print(C.T+3*D)
print(B.dot(A))
print('B*A^T undefined')

# A+C undefined
# [[-4 -7 -3]
#  [ 3  6  4]]
# [[14  3  3]
#  [ 2  7  9]]
# [[-1 -5 -1]
#  [ 2  7  4]]
# B*A^T undefined
