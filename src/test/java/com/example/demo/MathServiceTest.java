package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import com.example.demo.MathService;

public class MathServiceTest {

    @Test
    public void testAdd() {
        MathService mathService = new MathService();
        assertEquals(5, mathService.add(2, 3));
        assertEquals(-1, mathService.add(2, -3));
        assertEquals(0, mathService.add(0, 0));
    }
}