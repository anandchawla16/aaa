
import java.util.*;
public class OrderZero {
    public static void main(String arg[]) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int arr[]=new int[n];
        
        for(int i=0;i<n;i++) {
            arr[i] = s.nextInt();
        }

        orderzero(arr);
        for(int i=0;i<n;i++) {
            System.out.print(arr[i]+" ");
        }
    }

    private static int[] orderzero(int[] arr) {
        int b[] = new int[arr.length];
        int count = 0;
        int j=0;
        for(int i=0;i<arr.length;i++) {
            if(arr[i]!=0) {
                b[j++] = arr[i];

            } else {
                count++;
            }
        }
        System.out.println(count);
        for(int i=0;i<count;i++) {
            b[j++] = 0;
        }

        return b;
    }
}
