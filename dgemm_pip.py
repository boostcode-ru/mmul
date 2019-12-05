
import numpy as np
#import scipy.linalg.blas as slb
import time

M = 10000
N = 10000
matrix_list = [1024, 2048, 4096, 8192, 10000]

for K in matrix_list:

    a = np.array(np.random.random((M, K)), dtype=np.double, order='F')
    b = np.array(np.random.random((K, N)), dtype=np.double, order='F')

    A = np.matrix(a, dtype=np.double, copy=False)
    B = np.matrix(b, dtype=np.double, copy=False)

    start = time.time()

    C = np.matmul(A,B)

    end = time.time()

    texec = end - start
    print ( 'M x N x K == ', M, N, K, '.. pip numpy Execution Time == ', texec, 'sec' )
