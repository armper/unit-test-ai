package com.example.demo;

import org.springframework.stereotype.Service;

@Service
public class MortgageService {

    /*
     * Calculate the monthly payment for a given principal, rate and years.
     */
    public double calculateMonthlyPayment(double principal, double rate, double years) {
        double monthlyRate = rate / 100 / 12;
        double numberOfPayments = years * 12;

        double monthlyPayment = principal
                * (monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments))
                / (Math.pow(1 + monthlyRate, numberOfPayments) - 1);

        return monthlyPayment;
    }

    /*
     * Calculate the rate for a given principal, monthly payment and years.
     */
    public double calculateRate(double principal, double monthlyPayment, double years) {
        double numberOfPayments = years * 12;

        double rate = 12 * (Math.pow(monthlyPayment, 1 / numberOfPayments) - 1);

        return rate;
    }
}
