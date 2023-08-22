package com.example.demo;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class FibonacciTest {

    @Test
    public void testCalculate() {
        Fibonacci fib = new Fibonacci();

        // Test case 1: Fibonacci number at position 0
        int result1 = fib.calculate(0);
        Assertions.assertEquals(0, result1);

        // Test case 2: Fibonacci number at position 1
        int result2 = fib.calculate(1);
        Assertions.assertEquals(1, result2);

        // Test case 3: Fibonacci number at position 2
        int result3 = fib.calculate(2);
        Assertions.assertEquals(1, result3);

        // Test case 4: Fibonacci number at position 5
        int result4 = fib.calculate(5);
        Assertions.assertEquals(5, result4);

        // Test case 5: Fibonacci number at position 10
        int result5 = fib.calculate(10);
        Assertions.assertEquals(55, result5);
    }
}