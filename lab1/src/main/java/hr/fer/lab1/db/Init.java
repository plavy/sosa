package hr.fer.lab1.db;

import hr.fer.lab1.domain.Student;
import hr.fer.lab1.service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;
import org.springframework.stereotype.Component;

@Component
public class Init {

    @Autowired
    StudentService studentService;
    @EventListener(ApplicationReadyEvent.class)
    public void doSomethingAfterStartup() {
        Student student1 = new Student();
        student1.setUserName("Ivo");
        student1.setPassWord("Ivanović");
        Student student2 = new Student();
        student2.setUserName("Ivana");
        student2.setPassWord("Ivaković");
        if(studentService.listAll().size() == 0){
            studentService.createStudent(student1);
            studentService.createStudent(student2);
        }
    }
}
