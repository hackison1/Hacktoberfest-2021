//import required classes and packages  
import java.util.*;   
import java.io.*;   
import java.util.Scanner;  
  
//create ISBNNumberExample class to check whether the given number is a valid ISBN or not  
class ISBNNumberExample {   
    
     static boolean checkISBNNumber(long number)  
    {  
            int sum = 0;  
    int i, t, intNumber, dNumber;  
    String strNumber;  
          
    strNumber = ""+number;  
          
    if (strNumber.length() != 10) {  
                    return false;  
            }  
          
            for (i = 0; i < strNumber.length(); i++) {  
                    intNumber = Integer.parseInt(strNumber.substring(i, i+1));  
                    dNumber = i + 1;  
                    t = dNumber * intNumber;  
                    sum = sum + t;  
            }  
  
            // check whether the sum is divisible by 11 or not  
        
            if ((sum % 11) == 0) {  
                    return true;  
            }  
          
    return false;  
          
    }  
    
    // main() method start  
    public static void main(String args[])   
    {     
long n1, n2;  
          
    try {  
              
        //create BufferedReader class object to get input from user  
        InputStreamReader in = new InputStreamReader(System.in);  
        BufferedReader br = new BufferedReader(in);  
          
        //show custom message  
        System.out.println("Enter first 10 digit ISBN number");  
              
        //store user entered value into variable n1  
        n1 = Long.parseLong(br.readLine());  
              
        //show custom message  
        System.out.println("Enter second 10 digit ISBN number");  
              
        //store user entered value into variable n2  
        n2 = Long.parseLong(br.readLine());  
              
        if (checkISBNNumber(n1))   
            System.out.println(n1 + " is a valid ISBN number");   
        else  
            System.out.println(n1 + " is not a valid ISBN number");   
        if (checkISBNNumber(n2))   
            System.out.println(n2 + " is a a valid ISBN number");   
        else  
            System.out.println(n2 + " is not a valid ISBN number");  
              
        }catch(java.lang.Exception e) {  
            System.out.println("Error while reading the data.");  
        }   
        }   
}  
