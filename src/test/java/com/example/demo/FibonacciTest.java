package com.example.demo;

import com.example.demo.Fibonacci;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class FibonacciTest {

    @Test
    public void testCalculate() {
        Fibonacci fib = new Fibonacci();
        assertEquals(0, fib.calculate(0));
        assertEquals(1, fib.calculate(1));
        assertEquals(1, fib.calculate(2));
        assertEquals(2, fib.calculate(3));
        assertEquals(3, fib.calculate(4));
        assertEquals(5, fib.calculate(5));
        assertEquals(8, fib.calculate(6));
        assertEquals(13, fib.calculate(7));
        assertEquals(21, fib.calculate(8));
        assertEquals(34, fib.calculate(9));
        assertEquals(55, fib.calculate(10));
    }
}