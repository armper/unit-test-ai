package com.example.demo;

import com.example.demo.MortgageService;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class MortgageServiceTest {

    private final MortgageService mortgageService = new MortgageService();

    @Test
    public void testCalculateMortgage() {
        double principal = 200000.0;
        double rate = 5.0;
        double years = 30.0;

        double expectedMortgage = 1073.643246310767;
        double actualMortgage = mortgageService.calculateMortgage(principal, rate, years);

        assertEquals(expectedMortgage, actualMortgage, 0.01, "Mortgage calculation is incorrect");
    }

    @Test
    public void testCalculateMonthlyPayment() {
        double principal = 200000.0;
        double rate = 5.0;
        double years = 30.0;

        double expectedMonthlyPayment = 1073.643246310767;
        double actualMonthlyPayment = mortgageService.calculateMonthlyPayment(principal, rate, years);

        assertEquals(expectedMonthlyPayment, actualMonthlyPayment, 0.01, "Monthly payment calculation is incorrect");
    }
}