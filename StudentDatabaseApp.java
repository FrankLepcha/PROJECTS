

public class StudentDatabaseApp {
  public static void main(String[] args){
    StudentApps stu1 = new StudentApps();
    stu1.enroll();
    stu1.viewBal();
    stu1.payBalance();
    System.out.print(stu1.showInfo());
  }
}

  