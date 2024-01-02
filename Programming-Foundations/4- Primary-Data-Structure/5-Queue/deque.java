/* 
 *    Practical Applications:
 *   
 *   - Implementing Stacks and Queues Offers flexibility for both FIFO and LIFO operations.
 *   - Dequeuing/Enqueuing in Algorithms Efficiently adding/removing elements at both ends.
 *   - Parsing and Tree Traversal Useful in algorithms like breadth-first search (BFS).
 *   
 *    Why Use ArrayDeque?
 *   
 *   - Provides efficient constant-time operations for adding/removing elements at both ends.
 *   - Suitable for scenarios requiring flexibility in managing elements at both ends without
 *      fixed capacity restrictions.
 *   
 *   `ArrayDeque` serves as a versatile data structure offering efficient double-ended queue 
 *    operations, making it valuable in various programming scenarios where fast insertions 
 *    and removals at both ends are required.
*/

import java.util.ArrayDeque;

public class deque{
    public static void main(String[] xargs) {
        ArrayDeque<Integer> deque = new ArrayDeque<>();

        // Enqueuing 
        deque.addFirst(10); // Add item at the front
        deque.addFirst(20); // Add item at the front
        deque.addFirst(30); // Add item at the front

        deque.addLast(40); // Add item at the end
        deque.addLast(50); // Add item at the end

        for (Integer num : deque) {
            System.out.println(num);
        }

        // Dequeuing 
        Integer dequeuedItemF = deque.removeFirst();
        System.out.println(dequeuedItemF);
        
        Integer dequeuedItemL = deque.removeLast();
        System.out.println(dequeuedItemL);
    }
}



