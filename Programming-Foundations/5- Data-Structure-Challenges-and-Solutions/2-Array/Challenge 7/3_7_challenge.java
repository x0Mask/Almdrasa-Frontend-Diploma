/*
 * Missing number in array
 * 
 * Given an array of size N-1 such that it only contains
 * distinct integers in the range of 1 to N.
 * Find the missing element.
 * 
 * 
 * Example 1:
 * Input:
 * N = 5
 * A[] = {1, 2, 3, 5}
 * Output:
 * 4
 * 
 * Example 2:
 * Input:
 * N = 10
 * A[] = {6,1,2,8,3,4,7,10,5}
 * Output:
 * 9
 * 
 * 1 <= A[i] <= 10^6
 * 
 * Original problem
 * https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1
 */

class Main {
    public static void main(String[] args) {
        // DO NOT CHANGE THIS CODE
        // TEST CASES
        int[][] inputs = {
            {1, 2, 3, 5},
            {6,1,2,8,3,4,7,10,5},
            {1},
            {2,3},
            {}
        };
        int[] N = {5, 10, 2, 3, 1};
        int[] expected = {4, 9, 2, 1, 1};
        for(int i = 0; i < inputs.length; i++) {
            int actual = missingNumber(inputs[i], N[i]);
            if (actual == expected[i]) {
                System.out.printf("Test case %d passed! \n", i + 1);
            } else {
                System.out.printf("Test case %d failed! ", i + 1);
                System.out.printf("Expected result %s, actual result %s \n",
                    expected[i], actual);
            }
            System.out.println();
        }
    }


/**
 * Finds the missing number in a sorted array of integers.
 * 
 * @param arr The sorted array of integers.
 * @param n The number of elements in the array.
 * @return The missing number.
 */
private static int missingNumber(int[] arr, int n) {
    // Calculate the expected sum of the numbers in the array
    int expectedSum = (n * (n + 1) / 2); // n = 10 => (10 * (10 + 1) / 2) = 55
    
    // Calculate the actual sum of the numbers in the array
    int actualSum = 0;
    for (int num : arr) {
        actualSum += num;
    }
    
    // Return the difference between the expected sum and the actual sum
    return expectedSum - actualSum;
}
}

// Another solution
// int expectedSum = (n * (n + 1) / 2); // n = 10 => (10 * (10 + 1) / 2) = 55
// int actualSum = Arrays.stream(arr).sum();
// return expectedSum - actualSum;