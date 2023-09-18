package com.example.demo;

public class Fibonacci {

    /**
     * Calculates the Fibonacci number at the given position.
     * 
     * @param n The position in the Fibonacci sequence.
     * @return The Fibonacci number at the given position.
     */
    public int calculate(int n) {
        if (n <= 1) {
            return n;
        }
        return calculate(n - 1) + calculate(n - 2);
    }

    public static void main(String[] args) {
        Fibonacci fib = new Fibonacci();
        System.out.println("Fibonacci number at position 5: " + fib.calculate(5));
    }
}
