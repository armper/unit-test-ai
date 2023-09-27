package com.example.demo;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MortgageServiceTest {

    @Test
    public void testCalculateMonthlyPayment() {
        MortgageService mortgageService = new MortgageService();
        double principal = 200000.0;
        double rate = 5.0;
        double years = 30.0;
        double expected = 1073.64;
        double delta = 0.01;

        double result = mortgageService.calculateMonthlyPayment(principal, rate, years);

        assertEquals(expected, result, delta, "Monthly payment should be 1073.64");
    }
}