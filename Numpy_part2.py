# -*- coding: utf-8 -*-
"""
"""## NumPy for Linear Algebra


Numpy includes several tools for working with linear algebra problems, including functions for performing matrix calculations, such as determinants, inverses, eigenvalues, eigenvectors, and the singular value decomposition.

Consider the system of linear equations below:

\begin{cases}
  2x_1 + 3x_2 &= 7 \\
  4x_1 - 2x_2 &= 4 \\
\end{cases}

We are going to:
- write the system in matrix product:

\begin{equation*}
AX=b
\end{equation*}
- use the matrix inverse and determinant to solve the system

#### 1. write the system in matrix product

\begin{equation}
\begin{bmatrix}
  2 & 3 \\
  4 & -2
\end{bmatrix}
\begin{bmatrix}
  x_1 \\
  x_2
\end{bmatrix}
=
\begin{bmatrix}
  7 \\
  4
\end{bmatrix}
\end{equation}

i.e
\begin{equation*}
AX=b
\end{equation*}
 With: \\
 \begin{equation*}
 A=
 \begin{bmatrix}
  2 & 3 \\
  4 & -2
\end{bmatrix}, \ \
X = \begin{bmatrix}
  x_1 \\
  x_2
\end{bmatrix}, \ \
b = \begin{bmatrix}
  7 \\
  4
\end{bmatrix}
\end{equation*}

#### 2. Solve the system using matrix inverse and determinant


\begin{equation*}
X=A^{-1}b
\end{equation*}
"""

import numpy as np

A = np.array([[2,3],[4,-2]])
b = np.array([7,4])

#Compute and check if A is non-singular matrix (|A|!=0)
A_det = np.linalg.det(A)
print(A_det)

A_inv = np.linalg.inv(A)

X = A_inv@b
print(X)

"""#### Solve the system using directly `linalg.solve`"""

X = np.linalg.solve(A,b)
print(X)

"""### Eigenvectors and eigenvalues

- To get the both eigenvalues and the cooresponding eingenvectors of a matrix, use `linalg.eig`.
"""

eig_vals, eig_vec = np.linalg.eig(A)
print(eig_vals, '\n\n')
print(eig_vec)

"""### Exercise 1

Let A a matrix. Check if A is an orthogonal matrix.

Hint: compute $A^{-1}$ and $A^{T}$
"""

A = np.array([[0,1],[-1,0]])

## START YOUR CODE HERE ##
np.array_equal(np.linalg.inv(A),A.T)

"""### Norm of a matrix"""

np.linalg.norm(A)

"""#### Exercise

Consider the two vectors below, compute the cosine of the angle between them
"""

A = np.array([1,0])
B = np.array([1,1])

##  START YOUR CODE HERE##
dot_prod= A @ B
length_A= np.sqrt(A @ A)
length_B= np.sqrt(B @ B)
Cosine_angle=dot_prod/(length_A*length_B)
Cosine_angle

A = np.array([1,0])
B = np.array([1,1])

cos_angle= (A.T @ B)/(np.linalg.norm(A,2)*np.linalg.norm(B,2))
print(cos_angle)
np.arccos(cos_angle)

