/*
 * performance evaluation in Java typically involves measuring how fast or efficient your code runs. 
 * Two common ways to evaluate performance are through time complexity and space complexity.
 * 
 * **Time Complexity**: It measures how the execution time of an algorithm grows with the input size. 
 * For instance, if you have a list of numbers and want to find a specific number in that list, 
 * some algorithms might take longer as the list gets larger. 
 * 
 * Let's say you have an array of numbers and want to find if a specific number exists in that array. 
 * You might use a linear search algorithm that checks each number in the array one by one until 
 * it finds the desired number. If the array has ten numbers, the algorithm might take fewer steps compared to 
 * finding the number in an array with a thousand numbers.
 */

// Linear Search Example
/**
 * Performs a linear search on the given array to find the target number.
 * @param array the array of numbers to search
 * @param target the number to find
 * @return true if the target number is found in the array, false otherwise
 */
public boolean linearSearch(int[] array, int target) {
    for (int num : array) {
        if (num == target) {
            return true;
        }
    }
    return false;
}


/*
* **Space Complexity**: This evaluates how much memory your algorithm uses concerning the input size. 
* For instance, some algorithms might create additional data structures that occupy memory proportional to the input.
*
* Consider sorting algorithms. Bubble sort might rearrange elements directly within an array, 
* while merge sort might create additional arrays to help with sorting. As the array gets larger, 
* the additional arrays in merge sort might take up more memory space.
*/

// Bubble Sort Example
/**
 * Sorts the given array using the bubble sort algorithm.
 * @param array the array of numbers to sort
 */
public void bubbleSort(int[] array) {
    int length = array.length;
    for (int i = 0; i < length - 1; i++) {
        for (int j = 0; j < length - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
}}


/*
 * Evaluating performance helps in choosing the most efficient algorithms or data structures for specific tasks, 
 * ensuring your code runs optimally, especially when dealing with large amounts of data.
 */