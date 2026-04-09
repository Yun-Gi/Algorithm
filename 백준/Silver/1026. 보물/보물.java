import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        sc.nextLine();  // 개행 문자 제거

        int[] A = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        int[] B = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Arrays.sort(A);
        Arrays.sort(B);

        int S = 0;
        
        for(int i = 0; i < N; i++) {
            S += A[i]*B[(N-1)-i]; 
        }

        System.out.println(S);

        sc.close();
    }
}