import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.IntStream;


public class Main {
    private static int answer = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nh = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int n = nh[0];
        int hp = nh[1];

        int[][] skills = new int[n][2];
        for (int i = 0; i < n; i++)
            skills[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

        backtracking(skills, n, hp, 0, new int[n]);
        System.out.println(answer);
    }

    private static void backtracking(int[][] skills, int n, int hp, int time, int[] cooldowns) {
        if (hp <= 0) {
            answer = Math.min(answer, time);
            return;
        }

        int[] usable = IntStream.range(0, n)
                .filter(i -> cooldowns[i] <= time)
                .toArray();

        if (usable.length == 0) {
            backtracking(skills, n, hp, Arrays.stream(cooldowns).min().orElse(0), cooldowns);
        } else {
            for (int i: usable) {
                int bef = cooldowns[i];
                cooldowns[i] = time + skills[i][0];
                backtracking(skills, n, hp-skills[i][1], time+1, cooldowns);
                cooldowns[i] = bef;
            }
        }
    }
}
