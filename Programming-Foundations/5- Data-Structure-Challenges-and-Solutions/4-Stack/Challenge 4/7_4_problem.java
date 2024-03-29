import java.util.*;

/*
 * Check for Balanced Brackets in an expression (well-formedness) using Stack
 * 
 * Given an expression string exp, write a program to examine whether the pairs
 * and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given
 * expression.
 * 
 * Examples:
 * Input: exp = “[()]{}{[()()]()}” 
 * Output: Balanced
 * Explanation: all the brackets are well-formed
 * 
 * Examples:
 * Input: exp = “[(])” 
 * Output: Not Balanced 
 * Explanation: 1 and 4 brackets are not balanced because 
 * there is a closing ‘]’ before closing ‘(‘
 * 
 * Calculate the Time complexity of your solution.
 * 
 * This problem is derived from
 * https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
 */

class Main {
    public static void main(String[] args) {
        // DO NOT CHANGE THIS CODE
        // TEST CASES
        char[][] inputs = {
            {},
            {'('},
            {'['},
            {'{'},
            {')'},
            {']'},
            {'}'},
            {'(','}'},
            {'(',')'},
            {')','('},
            {'(',')','{'},
            {'(',')','}'},
            {'(',')','{','}'},
            {'(',')',')','}'},
            {')','(','{','}'},
            {'(','{',')','}'},
            {'(','{','}',')'},
            {'(','{','{','}',')'},
            {'(','{','[','}',')'},
            {'(','[','{','}',']',')'},
            {'(',')','{','}','[',']'},
            {'(',')','{','[',']','}'},
            {'(','{','[',']','}',')'},
            {'(','{','[',']','}',')','(',')'},
            {'(','{','[',']','}',')','(','{',')'},
            {'(','{','[',']','}',')','(','{',')','}'},
            {'(','{','[',']','}',')','(','{','}',')'},
            {']','(','{','[',']','}',')','(','{','}',')'},
            {'[','(','{','[',']','}',')','(','{','}',')',']'},
            {'[','(',')',']','{','}','{','[','(',')','(',')',']','(',')','}'},
        };
        boolean[] expected = {
            true,
            false,
            false,
            false,
            false,
            false,
            false,
            false,
            true,
            false,
            false,
            false,
            true,
            false,
            false,
            false,
            true,
            false,
            false,
            true,
            true,
            true,
            true,
            true,
            false,
            false,
            true,
            false,
            true,
            true,
        };
        int passCount = 0;
        for(int i = 0; i < inputs.length; i++) {
            if (assertResult(i + 1, expected[i], areBalanced(inputs[i]))) {
                passCount++;
            }
        }
        System.out.printf("Passed %d / %d Test Cases.\n", passCount, inputs.length);
    }

    public static boolean areBalanced(char[] exp) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> pairs = new HashMap<>();
        pairs.put(')', '(');
        pairs.put('}', '{');
        pairs.put(']', '[');
        
        for (char c : exp) {
            if (pairs.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != pairs.get(c)) {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        
        return stack.isEmpty();
    }

    private static boolean assertResult(int testNumber, boolean expected, boolean actual) {
        if (actual == expected) {
            System.out.printf("Test case %d: PASS!\n", testNumber);
        } else {
            System.out.printf("Test case %d: FAIL!\n", testNumber);
        }
        return actual == expected;
    }
}
