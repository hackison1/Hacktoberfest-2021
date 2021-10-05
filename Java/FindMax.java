import java.util.Scanner;

public class FindMax {
    public static void main(String[] args) {
        //this program is to determine the largest number out of three integers

        Scanner sc = new Scanner(System.in);
        int x,y,z;

        System.out.println("\nInput three numbers to check the largest");
        System.out.println("-----------------------------------------");
        System.out.print("First Number: ");
        x=sc.nextInt();
        System.out.print("Second Number: ");
        y= sc.nextInt();
        System.out.print("Third Number: ");
        z= sc.nextInt();

        int  max=x;

        if(x>y){
            if(x>z){
                max=x;
            }else{
                max=z;
            }
        }else {
            if(y>z){
                max=y;
            }else{
                max=z;
            }

        }

        if(x==y){
            if(x==z){
                if(y==z){
                    System.out.println("\nAll three numbers are same: "+ x);
                }
            }
        }
        else{
            System.out.print("Maximum of the numbers ");
            System.out.print(x+ ","+ y+ ","+z+" is : ");
            System.out.println(max);
        }

        sc.close();

    }
}
