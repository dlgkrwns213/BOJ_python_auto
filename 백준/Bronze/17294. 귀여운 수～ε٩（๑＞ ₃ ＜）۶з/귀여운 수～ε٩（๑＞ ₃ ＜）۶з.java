import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String k = br.readLine();

        boolean isCute = true;

        if (k.length() > 2) {
            int diff = k.charAt(1) - k.charAt(0);

            for (int i=1; i<k.length()-1; i++) {
                if (k.charAt(i+1) - k.charAt(i) != diff) {
                    isCute = false;
                    break;
                }
            }
        }

        System.out.println(isCute
                ? "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!"
                : "흥칫뿡!! <(￣ ﹌ ￣)>");
    }
}