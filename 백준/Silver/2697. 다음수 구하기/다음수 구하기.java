import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for (int unused = 0; unused < t; unused++) {
            String number = new StringTokenizer(br.readLine()).nextToken();

            ArrayList<Character> behind = new ArrayList<>();
            char small = '0' - 1;
            char change = small;
            behind.add(small);
            for (int idx = number.length() - 1; idx >= 0; idx--) {
                char num = number.charAt(idx);
                if (behind.get(behind.size() - 1) > num) {
                    behind.add(num);
                    change = behind.stream()
                            .filter(c -> c > num)
                            .min(Character::compare)
                            .orElse(small);
                    break;
                }

                behind.add(num);
            }

            if (change == small) {
                bw.write("BIGGEST\n");
                continue;
            }

            String ret = number.substring(0, number.length() - behind.size() + 1) + change;
            behind.remove(Character.valueOf(change));
            ret += behind.stream()
                    .sorted()
                    .skip(1)
                    .map(String::valueOf)
                    .collect(Collectors.joining());

            bw.write(ret + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}