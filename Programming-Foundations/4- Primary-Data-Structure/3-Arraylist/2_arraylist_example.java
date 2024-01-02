import java.util.ArrayList;
import java.util.Arrays;

public class ArrayListExample {
    public static void main(String[] args) {
        // Creating an ArrayList of strings
        ArrayList<String> fruitList = new ArrayList<>();

        // Adding elements
        fruitList.add("Apple"); // Appends the specified element at the end of the list
        fruitList.add("Banana");
        fruitList.add("Orange");
        fruitList.add(3, "Mango"); // Inserts the element at the specified index, shifting the subsequent elements to the right.

        // Updating elements
        fruitList.set(1, "Watermelon"); // Replaces the element at the specified index with the new element

        // Accessing Elements
        System.out.println("First Fruit: " + fruitList.get(0)); // Retrieves the element at the specified index.

        // Removing an element
        fruitList.remove(2); // Removes the element at the specified index and shifts subsequent elements to the left.
        fruitList.remove("Apple"); // Removes the first occurrence of the specified element

        // Size and Capacity
        System.out.println(fruitList.size()); // Returns the number of elements in the list.
        System.out.println(fruitList.isEmpty()); // Checks if the list is empty, returning a boolean.

        // Iterating through elements
        for (String fruit : fruitList) {
            System.out.println(fruit);
        }
        fruitList.forEach(item -> System.out.println(item));

        // Shallow copy using clone() method
        ArrayList<String> copiedList = (ArrayList<String>) fruitList.clone();
        // subList(fromIndex, toIndex): Returns a view of the portion of the list between the specified fromIndex (inclusive) and toIndex (exclusive)

        // Modifying the original list
        fruitList.add(4, "Strawberry");

        // Modifying the original list
        System.out.println("The Original List: " + fruitList);
        System.out.println("The Copied List: " + copiedList);

        // Converting ArrayList to an array
        String[] array = fruitList.toArray(new String[fruitList.size()]);

        // Displaying the converted array
        System.out.println("Converted Array: " + Arrays.toString(array));
    }
}