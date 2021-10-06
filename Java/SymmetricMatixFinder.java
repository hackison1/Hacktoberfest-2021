import java.util.Scanner;

class SymmetricMatrix {
    public static void main(String[] args) {
        int row, column;

        Scanner sc = new Scanner(System.in);

        System.out.println("Note: the matrix should be a square matrix");
        System.out.print("Enter number of rows or columns:");//get user input to determine order of the square matrix

        int n=sc.nextInt();
        row=column=n;

        int [][] m1 = new int[row][column];
        int [][] m2 = new int[row][column];

        System.out.println("Enter the matrix elements:");

        //get the matrix element from user input
        for(int i=0; i<row; i++){
            for(int j=0; j<column; j++){
                m1[i][j]= sc.nextInt();
            }
        }

        //assign the transpose of m1 matrix to m2 matrix
        for(int i=0; i<row; i++){
            for(int j=0; j<column; j++){
                m2[i][j]=m1[j][i];
            }
        }

        int x=1;

        for(int i=0; i<row; i++){
            for(int j=0; j<column; j++){
                if(m1[i][j]!=m2[i][j]){
                    x=0;
                }
            }
        }

        if(x==1){
            System.out.println("The matrix;");
            for(int i=0; i<row; i++){
                for(int j=0; j<column; j++){
                    System.out.print(m1[i][j]+ " ");
                }
                System.out.println();
            }
            System.out.println("is symmetric !!!");
        }else {
            System.out.println("Ohh...the matrix;");
            for(int i=0; i<row; i++){
                for(int j=0; j<column; j++){
                    System.out.print(m1[i][j]+ " ");
                }
                System.out.println();
            }
            System.out.println("is not symmetric !!!");
        }

        sc.close();

    }
}

