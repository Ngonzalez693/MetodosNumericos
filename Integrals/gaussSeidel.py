import numpy as np

def gaussSeidel(A, b, iter, p, tol= 0.001):
    print("-------------------------Gauss Seidel-------------------------")
    print('{:s} \t {:<10} \t {:<10} \t {:<10} \t {:s}'.format('Iter', 'x', 'y', 'z', 'error'))
    
    D = np.diag(np.diag(A))
    L = np.tril(A) - D
    U = np.triu(A) - D

    T = - np.dot(np.linalg.inv(D + L), U)
    c = np.dot(np.linalg.inv(D + L), b)

    # Change array's lenth depending of matrix lenght
    x0 = np.array([0, 0, 0, 0])

    for i in range(iter):
        x1 = np.dot(T, x0,) + c
        error = (np.linalg.norm(x1 - x0, p) / np.linalg.norm(x1, p))

        if error <= tol:
            break
        else:
            x0 = x1

        print('{:d} \t {:.4f} \t {:.4f} \t {:.4f} \t {:.4f}'.format(i + 1, x1[0], x1[1], x1[2], error))