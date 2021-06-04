import java.util.*;
public class treeOrGraph {
    static double numberofEdges(double a) {
        return Math.pow(2,a)-2;

    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int arr[] = new int[n];


        for(int i=0;i<n;i++) {
            arr[i]=scanner.nextInt();
        }
       // System.out.println(n);
        for(int i=0;i<n;i++) {
         //   System.out.println(arr[i]);
        }
        int edges = (int)numberofEdges(n);

        int sum = degreeVertices(arr);

        if(sum==2*(n-1))
        System.out.println("Yes");
        else
        System.out.println("No");

    }

    private static int degreeVertices(int[] arr) {
        int sum=0;
        for(int i=0;i<arr.length;i++)
        {
            sum=sum+arr[i];
        }
        return sum;
    }
}
