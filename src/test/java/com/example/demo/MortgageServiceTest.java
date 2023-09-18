package com.example.demo;

import com.example.demo.MortgageService;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

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

    @Test
    public void testCalculateRate() {
        double principal = 100000.0;
        double monthlyPayment = 536.82;
        double years = 30.0;

        double expectedRate = 5.0;
        double actualRate = mortgageService.calculateRate(principal, monthlyPayment, years);

        assertEquals(expectedRate, actualRate, 0.01, "Rate calculation failed");
    }
}