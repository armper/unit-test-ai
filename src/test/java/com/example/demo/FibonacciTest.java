```java
package com.example.demo;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class FibonacciTest {

    @Test
    public void testCalculate() {
        Fibonacci fibonacci = new Fibonacci();
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
        Fibonacci fibonacci = new Fibonacci();
        assertEquals(3, fibonacci.calculatePi());
    }
}
```