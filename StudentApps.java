

import java.util.Scanner;

public class StudentApps{
  private String firstName;
  private String lastName;
  private int gradeYear;
  private String studentID;
  private String courses;
  private static int tuitionBalance = 0;
  private static int costofCourse = 600;
  private static int id = 1000;

  public StudentApps() {
    // Constructor 
    // User input for Student's name and grade year
    Scanner in = new Scanner(System.in);
    System.out.print("Enter Student's First Name: ");
    this.firstName = in.nextLine();

    
    System.out.print("Enter Student's Last Name: ");
    this.lastName = in.nextLine();

    System.out.print("Student's Grade: 1 - Freshmen, 2 - Sophmore, 3 - Junior, 4 - Senior: ");
    this.gradeYear = in.nextInt();

    setStudentID();
    
    System.out.println(firstName + " " + lastName + " " + gradeYear + " " + studentID);


  }

  // Generating Student IDs
  private void setStudentID()
  {
    id++; //each student created will increment our id variable by 1
    this.studentID = gradeYear + "" + id;
  }

  //Enrolling courses
  public void enroll() {
    do {
      System.out.println("Enter course for regesteration: (Enter Q to Terminate) ");
      Scanner in = new Scanner(System.in);
      String course = in.nextLine();
     
        if (!course.equals("Q")){
        courses = courses + "\n" + course;
        tuitionBalance = tuitionBalance + costofCourse;
        }
      else { break; }
    } while (1 != 0);

    System.out.println("Enrolled in: " + courses);
    System.out.println("Tuition Balance: " + tuitionBalance);
  }

  //Viewing Balance
  public void viewBal(){
    System.out.println("Total Balance: $" + tuitionBalance);
  }

  //Paying Balance

  public void payBalance(){
    viewBal();
    System.out.print("Enter the amount to be paid: ");
    Scanner in = new Scanner(System.in);
    int payment = in.nextInt();
    tuitionBalance = tuitionBalance - payment;
    System.out.print("Thank you for your payment of $ " + payment);
    viewBal();
  }

  // Showing Staus

  public String showInfo(){
    return "Name: " + firstName + " " + lastName +
      "\nGrade Level: " + gradeYear + 
      "\nStudent ID: " + studentID + 
      "\n Courses Enrolled: " + courses +
      "\nBalance: $" + tuitionBalance;

  }






}