import java.util.HashMap;
import java.util.Scanner;

public class OopExample {
  public static void main(String[] args) {
    System.out.println("Student registration system\n Enter student details");

    UserInputs userInputs = new UserInputs();

  }
}

class UserDetails {

  private String firstName;
  private String lastName;
  private String email;
  private String mobile;
  private int age;

  public void setFirstName(String userFirstName) {
    firstName = userFirstName;
  }

  public String getFirstName() {
    return firstName;
  }

  public void setLastName(String userLastName) {
    lastName = userLastName;
  }

  public String getLastName() {
    return lastName;
  }

  public void setEmail(String userEmail) {
    email = userEmail;
  }

  public String getEmail() {
    return email;
  }

  public void setMobile(String userMobile) {
    mobile = userMobile;
  }

  public String getMobile() {
    return mobile;
  }

  public void setAge(int userAge) {
    age = userAge;
  }

  public int getAge() {
    return age;
  }
}

class UserDetailsManipulate {

  UserDetailsManipulate(String firstName, String lastName, String email, String number, int age) {
    UserDetails userDetails = new UserDetails();
    userDetails.setAge(age);
    userDetails.setEmail(email);
    userDetails.setFirstName(firstName);
    userDetails.setLastName(lastName);
    userDetails.setMobile(number);

    HashMap<String, String> hmap = new HashMap<String, String>();

    hmap.put("FirstName", userDetails.getFirstName());
    hmap.put("LastName", userDetails.getLastName());
    hmap.put("Email", userDetails.getEmail());
    hmap.put("Mobile", userDetails.getEmail());

    // show user details

    System.out.println("User details:\n " + hmap);

  }

}

class UserInputs {
  Scanner scanner = new Scanner(System.in);

  UserInputs() {
    System.out.println("Student First Name: ");
    String fName = scanner.next();

    System.out.println("Student Last Name: ");
    String lName = scanner.next();

    System.out.println("Student Email: ");
    String email = scanner.next();

    System.out.println("Student Number: ");
    String number = scanner.next();

    System.out.println("Student Age: ");
    int age = scanner.nextInt();

    UserDetailsManipulate userDetailsManipulate = new UserDetailsManipulate(fName, lName, email, number, age);

  }

}