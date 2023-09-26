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
}