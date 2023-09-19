package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class MortgageServiceTest {

    private final MortgageService mortgageService = new MortgageService();

    @Test
    public void testCalculateMonthlyPayment() {
        double principal = 100000.0;
        double rate = 5.0;
        double years = 30.0;

        double expectedMonthlyPayment = 536.82;
        double actualMonthlyPayment = mortgageService.calculateMonthlyPayment(principal, rate, years);

        assertEquals(expectedMonthlyPayment, actualMonthlyPayment, 0.01, "Monthly payment calculation failed");
    }

 
}