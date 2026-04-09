import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int L = sc.nextInt();
        int M=0 , K=0, B = 0;

        for (int i=L; i<=100; i++) {
            int a = (N-(i*(i-1))/2)/i;
            int sum = 0;
            for (int j=0; j<i; j++) {
                sum += a + j;
            }
            if (N == sum) {
                K = a;
                M = i;
                B = 1;
                break;
            }
        }

        if(B == 1){
            if(K >= 0){
            for(int i=0; i<M; i++){
                System.out.print(K+i+" ");
            }
        }
            else{
                System.out.print(-1);
            }
    }
        else{
            System.out.print(-1);
        }
        sc.close();
    }
}
