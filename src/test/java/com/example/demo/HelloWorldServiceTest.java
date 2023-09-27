package com.example.demo;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import com.example.demo.HelloWorldService;

public class HelloWorldServiceTest {

    @Test
    public void testSayHelloWorldTo() {
        HelloWorldService helloWorldService = new HelloWorldService();
        String result = helloWorldService.sayHelloWorldTo("John");
        assertEquals("Hello John!", result);
    }
}