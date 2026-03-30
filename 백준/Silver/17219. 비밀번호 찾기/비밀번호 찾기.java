import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] mn = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int m = mn[0];
        int n = mn[1];

        Map<String, String> passwords = new HashMap<>(m);
        while (m-- > 0) {
            String[] infos = br.readLine().split(" ");
            String site = infos[0];
            String pwd = infos[1];

            passwords.put(site, pwd);
        }

        StringBuilder answer = new StringBuilder();
        while (n-- > 0)
            answer.append(passwords.get(br.readLine())).append('\n');
        System.out.println(answer);
    }
}