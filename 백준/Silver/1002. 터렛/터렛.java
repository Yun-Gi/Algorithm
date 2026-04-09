import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();
        int[] lst = new int[6]; 
        for(int i=0; i < T; i++){
            lst = Arrays.stream(sc.nextLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int d = (lst[0] - lst[3])*(lst[0] - lst[3]) + (lst[1] - lst[4])*(lst[1] - lst[4]);
            int sum = (lst[2] + lst[5]) * (lst[2] + lst[5]);
            int diff = (lst[2] - lst[5]) * (lst[2] - lst[5]);
            if(d == 0){
                if(lst[2]==lst[5]){
                    System.out.println(-1);
                }
                else{
                    System.out.println(0);
                }
            }
            else{
                if(d == sum || d == diff ){
                    System.out.println(1);
                }
                else if(d < sum && d > diff){
                    System.out.println(2);
                }
                else{
                    System.out.println(0);
                }
            }
        }

        sc.close();
    }
}