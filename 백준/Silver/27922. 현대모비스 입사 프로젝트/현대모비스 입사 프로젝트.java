import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] lectures = new int[n][3];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j ++)
                lectures[i][j] = Integer.parseInt(st.nextToken());
        }

        int mx = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = i+1; j < 3; j++)
                mx = Math.max(mx, getSumK(lectures, i, j, m));
        }

        System.out.println(mx);
    }

    public static int getSumK(int[][] lectures, int idx1, int idx2, int m) {
        return Arrays.stream(lectures)
                .mapToInt(lecture -> lecture[idx1] + lecture[idx2])
                .sorted()
                .skip(lectures.length - m)
                .sum();
    }
}