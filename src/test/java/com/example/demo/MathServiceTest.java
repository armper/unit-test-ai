package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import com.example.demo.MathService;

public class MathServiceTest {

    private MathService mathService = new MathService();

    @Test
    public void testAdd() {
        int result = mathService.add(10, 5);
        assertEquals(15, result, "10 + 5 should equal 15");
    }

    @Test
    public void testSubtract() {
        int result = mathService.subtract(10, 5);
        assertEquals(5, result, "10 - 5 should equal 5");
    }

    @Test
    public void testMultiply() {
        int result = mathService.multiply(10, 5);
        assertEquals(50, result, "10 * 5 should equal 50");
    }

    @Test
    public void testDivide() {
        double result = mathService.divide(10.0, 5.0);
        assertEquals(2.0, result, 0.001, "10.0 / 5.0 should equal 2.0");
    }
}