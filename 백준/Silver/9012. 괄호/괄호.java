import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for (int t = 0; t < n; t++) {
            String s = br.readLine();
            int count = 0;
            boolean possible = true;

            for (int i = 0; i < s.length(); i++) {
                char p = s.charAt(i);
                count += (p == '(') ? 1 : -1;
                if (count < 0) {
                    possible = false;
                    break;
                }
            }

            if (count != 0) {
                possible = false;
            }

            bw.write(possible ? "YES\n" : "NO\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}