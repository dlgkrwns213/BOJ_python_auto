import java.io.*;
import java.util.ArrayDeque;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());

        StringBuilder ans = new StringBuilder();
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int use = 1;
        boolean possible = true;

        for (int unused = 0; unused < n; unused++) {
            int num = Integer.parseInt(new StringTokenizer(br.readLine()).nextToken());
            while (use <= num) {
                stack.push(use++);
                ans.append('+');
            }

            if (stack.pop() == num) {
                ans.append('-');
            } else {
                possible = false;
                break;
            }
        }

        if (possible) {
            for (int i = 0; i < ans.length(); i++) {
                bw.write(ans.charAt(i));
                bw.newLine();
            }
        }
        else {
            bw.write("NO");
        }
        bw.flush();
    }
}