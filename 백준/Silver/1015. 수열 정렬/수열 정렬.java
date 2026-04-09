import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] A = new int[N];
        int[] P = new int[N];

        // A 입력받기
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }

        // (값, 원래 인덱스) 쌍을 저장하는 리스트 생성
        List<Pair> sortedList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            sortedList.add(new Pair(A[i], i));
        }

        // 값 기준으로 정렬 (값이 같으면 원래 인덱스 기준 정렬)
        Collections.sort(sortedList, Comparator.comparingInt(p -> p.value));

        // P 배열 만들기
        for (int newIdx = 0; newIdx < N; newIdx++) {
            P[sortedList.get(newIdx).index] = newIdx;
        }

        // P 배열 출력
        for (int i = 0; i < N; i++) {
            System.out.print(P[i] + " ");
        }
    }

    // (값, 원래 인덱스) 저장을 위한 Pair 클래스
    static class Pair {
        int value, index;
        Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}
