import java.util.*;

/*
 * Reverse an array in place
 * 
 * Given an array A of size N, reverse the array in place.
 * You must change the original array. Do not create a new array
 * 
 * 
 * Example 1:
 * 
 * Input:
 * N = 4
 * A[] = {1, 2, 3, 4}
 * Output:
 * A[] will be changed to{4, 3, 2, 1}
 * 
 * This is a variation of the problem
 * https://practice.geeksforgeeks.org/problems/reverse-an-array/0
 */

class Main {
    public static void main(String[] args) {
        // DO NOT CHANGE THIS CODE
        // TEST CASES
        int[][] inputs = {
            {3,4,5,6,7},
            {1,2,3,4},
            {1},
            {1,10},
            {}
        };
        int[][] expected = {
            {7,6,5,4,3},
            {4,3,2,1},
            {1},
            {10,1},
            {}
        };
        for(int i = 0; i < inputs.length; i++) {
            int[] actual = inputs[i];
            reverseArray(actual);
            if (Arrays.equals(actual, expected[i])) {
                System.out.printf("Test case %d passed! \n", i + 1);
            } else {
                System.out.printf("Test case %d failed! ", i + 1);
                System.out.printf("Expected result %s, actual result %s \n",
                    Arrays.toString(expected[i]), Arrays.toString(actual));
            }
            System.out.println();
        }
    }

    private static int[] reverseArray(int a[]) {
        int start = 0;
        int end = a.length - 1;

        for (int i = 0; i < a.length / 2; i++) {
            int temp = a[start];
            a[start] = a[end];
            a[end] = a[temp];
            start++;
            end--;
        }
        int[] reversedArray = reverseArray(a);
        return reversedArray;
    }
}
