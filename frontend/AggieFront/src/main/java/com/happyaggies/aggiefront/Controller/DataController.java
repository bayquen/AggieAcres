package com.happyaggies.aggiefront.Controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import java.util.Map;


@RestController
public class DataController {

    @PostMapping("/processData")
    public String processData(@RequestParam("inputData") String inputData, Model model) {
        String flaskResponse = sendToFlask(inputData);
        System.out.println(flaskResponse);
        return flaskResponse;

    }
    public String sendToFlask(String data) {
        String flaskUrl = "http://localhost:25565/api/process-data";
        RestTemplate restTemplate = new RestTemplate();

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.TEXT_PLAIN);

        HttpEntity<String> entity = new HttpEntity<>(data, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(flaskUrl, entity, String.class);
        return response.getBody();
    }


    @PostMapping("/receive-from-flask")
    public ResponseEntity<String> receiveProcessedData(@RequestBody String processedData) {
        System.out.println(processedData);
        // 处理或存储接收到的数据
        return ResponseEntity.ok("Processed data received successfully");
    }
}
