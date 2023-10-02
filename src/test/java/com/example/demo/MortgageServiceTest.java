
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

    @Test
    public void testCalculateMonthlyPaymentWithZeroYears() {
        MortgageService mortgageService = new MortgageService();
        double principal = 200000.0;
        double rate = 5.0;
        double years = 0.0;
        double expected = Double.POSITIVE_INFINITY;

        double result = mortgageService.calculateMonthlyPayment(principal, rate, years);

        assertEquals(expected, result, "Monthly payment should be infinity when years is zero");
    }

    @Test
    public void testCalculateMonthlyPaymentWithZeroRate() {
        MortgageService mortgageService = new MortgageService();
        double principal = 200000.0;
        double rate = 0.0;
        double years = 30.0;
        double expected = principal / (years * 12);

        double result = mortgageService.calculateMonthlyPayment(principal, rate, years);

        assertEquals(expected, result,
                "Monthly payment should be principal divided by number of payments when rate is zero");
    }
}