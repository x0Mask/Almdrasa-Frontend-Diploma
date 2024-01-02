import java.util.Queue;
import java.util.LinkedList;


public class QueueExample {
    public static void main(String[] xargs){
        Queue<String> queue = new LinkedList<>();

        // Enqueuing items - Return Excepetion
        queue.add("Apple");
        queue.add("Banana");
        queue.add("Strewparry");


        // Returning Null
        queue.offer("Crapes");
        queue.offer("Watermelan");

        // Peeking at the front item - Return Null
        String peek = queue.peek();
        System.out.println(peek);

        String element = queue.element(); // Return Excepetion
        System.out.println(element);

        // Dequeuing an item
        String dequeuedItem = queue.remove(); // Return Excepetion
        System.out.println(dequeuedItem);

        // Return Null
        queue.poll();

        // Iterate through the queue
        for (String fruit: queue) {
            System.out.println(fruit);
        }
    }
}
