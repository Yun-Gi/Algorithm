import java.util.*;

public class Main {
    static Map<Integer, List<Integer>> dictionary = new HashMap<>();
    static boolean[] visited;
    static boolean selfReachable;

    static void dfs(int node, int start) {
        visited[node] = true;

        for (int neighbor : dictionary.getOrDefault(node, new ArrayList<>())) {
            if (neighbor == start) {
                selfReachable = true; 
            }
            if (!visited[neighbor]) {
                dfs(neighbor, start);
            }
        }
    }

    static List<List<Integer>> DFS(Map<Integer, List<Integer>> dic, int N) {
        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            visited = new boolean[N];
            selfReachable = false;

            dfs(i, i);

            List<Integer> reachable = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                if (visited[j]) {
                    if (i == j && !selfReachable) {
                        reachable.add(-1); 
                    } else {
                        reachable.add(j);
                    }
                }
            }
            result.add(reachable);
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();

        List<List<Integer>> matrix = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            List<Integer> row = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                row.add(sc.nextInt());
            }
            matrix.add(row);
        } // 이 동네는 입력 받는 것도 왤케 힘드냐 그립다 파이썬

        for (int i = 0; i < N; i++) {
            List<Integer> adj = new ArrayList<>();
            for (int j = 0; j < N; j++) {
                if (matrix.get(i).get(j) == 1) {
                    adj.add(j);
                }
            }
            dictionary.put(i, adj);
        }

        List<List<Integer>> result = DFS(dictionary, N);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(result.get(i).contains(j) ? "1 " : "0 ");
            }
            System.out.println();
        }
        
        sc.close();
    }

}
