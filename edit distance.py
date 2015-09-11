import numpy as np

# Calculate the edit distance for all potential pairwise matches
def EditDistance(X, Y):
# these first 2 loops set the "null alignment" spots in the begining of the sequences, as well as the cost values for each first character in both sequences for aligning with this "null" (gap) spot.
    for i in range(0, len(X)+1):
        A[i,0] = i * gap

    for j in range(0, len(Y)+1):
        A[0,j] = j * gap

    for i in range(1, len(X)+1):
        for j in range(1, len(Y)+1):
            Diag = cost(X[i-1], Y[j-1]) + A[i-1, j-1]
            Down = gap + A[i-1, j]
            Left = gap + A[i, j-1]
            A[i,j] = min(Diag, Left, Down)

            if A[i,j] == Diag:
                B[i,j] = (i-1, j-1, "Diag")

            if A[i,j] == Down:
                B[i,j] = (i-1, j, "Down")  # I guess these loops aren't taking into account if any of the directions are equal in cost.

            if A[i,j] == Left:
                B[i,j] = (i, j-1, "Left")

    for j in range(1, A.shape[1]):  # These loops works to fill in the first row and column of the direction matrix B.
        B[0,j] = (0, j-1, "Left")
    for i in range(1, A.shape[0]):
        B[i,0] = (i-1, 0, "Down")



# Returns the final string alignment. Uses len(X) & len(Y) as initial parameters.
def parse(x, y):
    xChar = X[x-1]
    yChar = Y[y-1]

    if (B[x,y] == 0):
        return "",""

    if B[x,y][2] == "Down":
        yChar = "-"

    if B[x,y][2] == "Left":
        xChar = "-"

    str1, str2 = parse(B[x,y][0], B[x,y][1])
    return str1+xChar, str2+yChar


# Returns the shortest path taken by the algorithm. Uses len(X) & len(Y) as initial parameters. BigOh is presumably O(n).
def path(x, y):
# cost of this cell
    curCost = A[x,y]

    # base case
    if (B[x,y] == 0):
        return curCost

    #print A[x,y], B[x,y]  # useful to see what it is choosing each time

    #recursive case
    return str(curCost) + " -> " + str(path(B[x,y][0], B[x,y][1]))


# Cost of alignment
def cost(X, Y):
    if X == Y:
        return 0
    if X != Y:
        return 1


# Sequences
Y = "AAGGTATGAATC"
X = "AACGTTGAC"

gap = 3  # Gap cost.

#A = []  # This is another way to make the empty matrix
#for i in range(0, len(X)):
#    A.append([0]*len(Y))

# Create empty matrices
# The A matrix stores the cost values for all possible alignments
# The B matrix stores the coordinates of the path taken through the A matrix in order to obtain the alignment with the minimum total cost
A = np.zeros((len(X)+1,len(Y)+1))
B = np.zeros((len(X)+1,len(Y)+1), dtype=tuple)
#print(A.shape)  # This shows the number of rows and columns in a matrix.

EditDistance(X, Y)
print A[::-1]  # this prints the matrix in the correct way for human-viewing

print path(len(X), len(Y))
print parse(len(X), len(Y))
