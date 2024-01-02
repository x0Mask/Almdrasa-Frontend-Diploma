import java.util.ArrayList;
import java.util.Collections;

public class arraylist_collections {
    /**
     * This class demonstrates sorting an ArrayList of cars in alphabetical order.
     */
    
    public static void main (String[] args) {
        // Create an ArrayList to store the cars
        ArrayList<String> carList = new ArrayList<String>();
        
        // Add cars to the ArrayList
        carList.add("BMW");
        carList.add("Mazda");
        carList.add("Mercedes");
        carList.add("KIA");

        // Sort the ArrayList in alphabetical order
        Collections.sort(carList);
        
        // Print the sorted list of cars
        for(String car : carList) {
            System.out.println(car);
        }
    }
}