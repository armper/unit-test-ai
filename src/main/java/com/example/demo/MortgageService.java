package com.example.demo;

import org.springframework.stereotype.Service;

@Service
public class MortgageService {

    /*
     * Calculate the mortgage payment for a given principal, rate and years.
     */
    public double calculateMortgage(double principal, double rate, double years) {
        double monthlyRate = rate / 100 / 12;
        double numberOfPayments = years * 12;

        double mortgage = principal
                * (monthlyRate * Math.pow(1 + monthlyRate, numberOfPayments))
                / (Math.pow(1 + monthlyRate, numberOfPayments) - 1);

        return mortgage;
    }

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
}
