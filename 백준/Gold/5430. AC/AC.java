import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int tc = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
        for (int unused = 0; unused < tc; unused++) {
            String p = new StringTokenizer(br.readLine()).nextToken();
            int n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());

            String token = new StringTokenizer(br.readLine()).nextToken();
            int[] numbers;
            if (token.equals("[]")) {
                numbers = new int[0];
            } else {
                numbers = Arrays.stream(token.substring(1, token.length() - 1).split(","))
                        .mapToInt(Integer::parseInt)
                        .toArray();
            }

            bw.write(function(p, n, numbers) + '\n');
        }
        bw.flush();
    }

    public static String function(String command, int n, int[] numbers) {
        int left = 0, right = n;
        boolean reversed = false;
        for (char c: command.toCharArray()) {
            if (c == 'R') {
                reversed = !reversed;
                continue;
            }

            if (left == right)
                return "error";

            if (reversed)
                right -= 1;
            else
                left += 1;
        }

        int[] ans = new int[right-left];
        if (reversed) {
            for (int i = right-1; i >= left; i--)
                ans[right-1-i] = numbers[i];
        } else {
            for (int i = left; i < right; i++) {
                ans[i - left] = numbers[i];
            }
        }

        return "[" + Arrays.stream(ans)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining(",")) + "]";
    }
}