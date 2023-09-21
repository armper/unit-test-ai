package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import com.example.demo.Fibonacci;

public class FibonacciTest {

    private final Fibonacci fibonacci = new Fibonacci();

    @Test
    public void testCalculate() {
        assertEquals(0, fibonacci.calculate(0));
        assertEquals(1, fibonacci.calculate(1));
        assertEquals(1, fibonacci.calculate(2));
        assertEquals(2, fibonacci.calculate(3));
        assertEquals(3, fibonacci.calculate(4));
        assertEquals(5, fibonacci.calculate(5));
        assertEquals(8, fibonacci.calculate(6));
    }

    @Test
    public void testCalculatePi() {
        assertEquals(3, fibonacci.calculatePi());
    }
}