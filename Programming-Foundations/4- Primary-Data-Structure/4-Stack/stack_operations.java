import java.util.*;

class Main{
    public static void main(String[] xargs) {
        Stack<Integer> myStack = new Stack<>();
        for (int i = 1; i <= 5; i++){
            myStack.push(i);
        }

        for (int i = 0; i < 3; i++){
            System.out.printIn(myStack.pop());
        }

        for (int i = 6; i <= 10; i++){
            myStack.push(i);
        }

        while (!myStack.isEmpty()){
            System.out.printIn(myStack.pop());
        }
    }
}