import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        boolean[] exists = new boolean[2000002];

        while (n-- > 0)
            exists[Integer.parseInt(br.readLine())+1000000] = true;

        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < 2000002; i++) {
            if (exists[i])
                answer.append(i-1000000).append('\n');
        }

        System.out.println(answer);
    }
}