import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder ans = new StringBuilder();
        ans.append("YES").append('\n');

        String p = br.readLine().split("\\.")[1];
        ans.append(Integer.parseInt(p)).append(' ').append("1").append("0".repeat(p.length()));

        System.out.println(ans);
    }
}