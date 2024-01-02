/*
* the call stack is a fundamental concept in programming that's closely tied to how functions
* are executed and managed in most programming languages.
*/  

/*
*  ### Understanding the Call Stack:
*  
*  1. **What is it?**
*     - The call stack is a data structure in memory that keeps track of the sequence of function
*       calls during the execution of a program.
*     - It operates on the Last-In, First-Out (LIFO) principle, similar to a stack data structure.
*  
*  2. **How it Works:**
*     - Every time a function is called, a new frame (known as a stack frame or activation record)
*       representing that function call is pushed onto the stack.
*     - This frame contains information like the function's arguments, local variables, 
*       return address, and other bookkeeping details.
*     - When a function completes its execution or returns a value, its stack frame is popped off
*       the stack, returning control to the calling function.
*  
*  3. **Function Execution:**
*     - As functions call other functions (either recursively or otherwise), each new function
*       call adds a new frame onto the top of the call stack.
*     - When a function completes its task or reaches a return statement, its frame is removed
*       from the top of the stack, allowing the program to resume execution from the calling function.
*  
*  ### Why it's Important:
*  
*  1. **Tracking Function Calls**:
*     - The call stack enables the program to keep track of the sequence of function calls, 
*       maintaining the context and order of execution.
*  
*  2. **Managing Function Execution**:
*     - It's crucial for managing the flow of execution in a program, ensuring proper function
*       calls, and maintaining the order of operations.
*  
*  ### Visualization:
*  
*  1. **Debugging and Visualization Tools**:
*     - Debugging tools and IDEs often provide call stack visualization, showing the sequence
*       of function calls, their hierarchy, and their states during program execution.
*  
*  2. **Example**:
*     - Consider recursive functions, where each recursive call adds a new stack frame until a
*       base case is reached. The call stack keeps track of each recursive call and manages
*       their return.
*  
*  ### Importance in Error Handling:
*  
*  1. **Exception Handling**:
*     - When an error occurs, the call stack helps in tracing the sequence of function calls that
*       led to the error, aiding in error diagnosis and debugging.
*  
*  Understanding the call stack is crucial for developers, especially in debugging, understanding
*   code execution flow, and efficiently managing function calls in various programming scenarios.
*/

import java.util.Stack;

public class Main() {
    public static void main(String[] xargs) {
        Stack<Integer> stack = new Stack<>();
        
        // Pushing items onto the stack
        stack.push(10);
        stack.push(20);
        stack.push(30);

        // Popping an item from the stack
        int poppedItem = stack.pop(); // Removes 30 from the top
    }
}