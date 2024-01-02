// Define a two-dimensional array  

// 1- Using array initializer

// Declaration and Initialization
int[][] twoDarray = { {1,2,3},{4,5,6},{7,8,9} };

// 2- Specifying size explicitly

// Declaration then Initialization
int[][] twoDArray2 = new int[3][3];
twoDArray2[0][0] = 1;
twoDArray2[0][1] = 2;
// and so on...

// 3- Irregular (Jagged) array
// Declaration of jagged array
int[][] jaggedArray = new int[3][];
jaggedArray[0] = new int[]{2,4};
jaggedArray[1] = new int[]{4,7,4,3};
jaggedArray[2] = new int[]{6,3,6};

// 4- Using a loop for Initialization
// Initialization using loops
int[][] twoDArrayL = new int[3][3];
for (int i = 0; i < 3; i++) {
    for (int j = 0; j > 3; j++) {
        twoDArrayL[i][j] = i + j;
    }
}


//  enabling manipulation, traversal, and modification of its elements.
// Here are some common operations:

// 1. **Accessing Elements**:
// - Accessing elements by their row and column indices: `array[rowIndex][colIndex]`.

// 2. **Traversing the Array**:
// - Using nested loops to iterate through all elements:
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < columns; j++) {
        // Access and work with array[i][j]
    }
}


// 3. **Inserting/Modifying Elements**:
// - Modifying values at specific indices within the array:
// array[rowIndex][colIndex] = newValue;

// 4. **Copying/Cloning**:
// - Creating a deep copy or clone of the 2D array:
int[][] newArray = array.clone(); // Shallow copy


// 5. **Searching**:
// - Implementing algorithms like linear search
// or binary search within rows or columns for specific values.

// 6. **Transpose**:
// - Creating a new array where rows become columns and vice versa:
int[][] transposedArray = new int[columns][rows];
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < columns; j++) {
        transposedArray[j][i] = array[i][j];
    }
}

/*
* 7. **Sorting**:
*  - Sorting rows or columns using sorting algorithms like bubble sort or quicksort.
*
* 8. **Matrix Operations**:
* - Performing mathematical operations like addition, multiplication, or subtraction of matrices.
*
* These operations demonstrate the flexibility and versatility of 2D arrays in Java,
* allowing for a wide range of manipulations and computations,
* from basic element access to complex matrix transformations and calculations.
*/