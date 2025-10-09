import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] connects = {{1, 3}, {0, 2}, {1, 5}, {0, 6}, {}, {2, 8}, {3, 7}, {6, 8}, {5, 7}};

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            char[] board = new char[9];
            for (int i = 0; i < 3; i++) {
                String line = br.readLine();
                for (int j = 0; j < 3; j++)
                    board[3*i + j] = line.charAt(j);
            }

            boolean[] visited = new boolean[9];
            List<Integer> group = new ArrayList<>();
            for (int start = 0; start < 9; start++) {
                if (board[start] == 'O' && !visited[start]) {
                    int count = 1;
                    visited[start] = true;
                    Queue<Integer> q = new ArrayDeque<>();
                    q.add(start);
                    while (!q.isEmpty()) {
                        int now = q.poll();

                        for (int connect: connects[now]) {
                            if (board[connect] == 'O' && !visited[connect]) {
                                visited[connect] = true;
                                count++;
                                q.add(connect);
                            }
                        }
                    }

                    group.add(count);
                }
            }

            int[] inputs = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            Collections.sort(group);

            boolean match = inputs.length == group.size()+1 &&
                    IntStream.range(0, group.size())
                            .allMatch(i -> inputs[i+1] == group.get(i));

            System.out.println(match ? 1 : 0);
        }
    }
}