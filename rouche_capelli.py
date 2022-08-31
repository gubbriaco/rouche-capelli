import numpy as np
import matplotlib.pyplot as plt


def solve(A, b):
    # m is the number of rows of the incomplete matrix A
    mA = len(A)
    # n is the number of columns of the incomplete matrix A
    nA = len(A[1])

    # computation of the rank of the incomplete matrix A
    rankA = np.linalg.matrix_rank(A)

    # concatenation of the incomplete matrix A with the vector of known terms b
    Ab = np.column_stack((A, b))
    # calculation of the rank of the matrix just obtained
    rankAb = np.linalg.matrix_rank(Ab)

    # application of Rouche-Capelli theorem
    if rankA < rankAb:
        print("The system is impossible, that is, it does not admit solutions.")
    elif rankA == rankAb:
        print("The system is compatible, that is, it admits one or infinite solutions.")
    elif rankA == rankAb and rankA == nA:
        print("The system admits one and only one solution.")
    elif rankA == rankAb and rankA < nA:
        nrk = nA - rankA
        print("The system admits " + str(np.inf) + "^" + nrk + " solutions.")

    # graphic representation of the planes corresponding to the equations obtained
    # by considering the rows of the matrix Ab
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_axis, y_axis = np.linspace(-10, 10, 100), np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x_axis, y_axis)

    x, y, z, d = 0, 0, 0, 0
    Z = 0
    for i in range(len(Ab)):
        for j in range(len(Ab[i])):
            if j == 1:
                x = Ab[i][j]
            elif j == 2:
                y = Ab[i][j]
            elif j == 3:
                z = Ab[i][j]
            elif j == 4:
                d = Ab[i][j]
        Z = (d - x * X - y * Y) / z
        ax.plot_surface(X, Y, Z)

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()


def main():
    A = [[1, -1, 1], [1, 1, 0], [2, 2, 2]]
    b = [1, 4, 9]
    solve(A, b)


if __name__ == "__main__":
    main()
