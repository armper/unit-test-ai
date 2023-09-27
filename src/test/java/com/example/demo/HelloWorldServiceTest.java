package com.example.demo;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class HelloWorldServiceTest {

    @Test
    public void testSayHelloWorldTo() {
        HelloWorldService helloWorldService = new HelloWorldService();
        String result = helloWorldService.sayHelloWorldTo("John");
        assertEquals("Hello John!", result);
    }
}