package com.happyaggies.aggiefront.Controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {

    @GetMapping("/")
    public String index() {
        // 返回index.html页面的逻辑视图名称
        return "search"; // 如果HTML文件在resources/static目录下，不带扩展名
        // 如果HTML文件在resources/templates目录下，需要带上扩展名，比如return "index.html";
    }

    @GetMapping("/about")
    public String about() {
        // 返回index.html页面的逻辑视图名称
        return "about"; // 如果HTML文件在resources/static目录下，不带扩展名
        // 如果HTML文件在resources/templates目录下，需要带上扩展名，比如return "index.html";
    }
}
