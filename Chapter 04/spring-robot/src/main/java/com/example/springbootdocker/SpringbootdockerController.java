package com.example.springbootdocker;
import com.diozero.util.SleepUtil;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import com.diozero.devices.motor.CamJamKitDualMotor;

@Controller
public class SpringbootdockerController {

    @RequestMapping("/index")
    public String getIndex() {
        return "index";
    }

    @RequestMapping("/forward")
    public String forward() {
        try(CamJamKitDualMotor robot = new CamJamKitDualMotor()) {
            robot.rotateRight(1);
            SleepUtil.sleepSeconds(1);
            robot.stop();
            SleepUtil.sleepSeconds(1);
        }
        return "index";
    }

    @RequestMapping("/backward")
    public String backward() {
        try(CamJamKitDualMotor torvalds = new CamJamKitDualMotor()) {
            torvalds.rotateLeft(1);
            SleepUtil.sleepSeconds(1);
            torvalds.stop();
            SleepUtil.sleepSeconds(1);
        }
        return "index";
    }

    @RequestMapping("/left")
    public String left() {
        try(CamJamKitDualMotor torvalds = new CamJamKitDualMotor()) {
            torvalds.forward(1);
            SleepUtil.sleepSeconds(0.3);
            torvalds.stop();
            SleepUtil.sleepSeconds(1);
        }
        return "index";
    }

    @RequestMapping("/right")
    public String right() {
        try(CamJamKitDualMotor torvalds = new CamJamKitDualMotor()) {
            torvalds.backward(1);
            SleepUtil.sleepSeconds(0.3);
            torvalds.stop();
            SleepUtil.sleepSeconds(1);
        }
        return "index";
    }
}
