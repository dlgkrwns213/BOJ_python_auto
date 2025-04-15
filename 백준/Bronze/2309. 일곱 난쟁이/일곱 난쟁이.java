import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] heights = new int[9];
        for (int i = 0; i < 9; i++)
            heights[i] = Integer.parseInt(br.readLine());
        Arrays.sort(heights);

        int total = Arrays.stream(heights).sum();
        for (int i = 0; i < 9; i++) {
            for (int j = i+1; j < 9; j++) {
                if (heights[i] + heights[j] == total - 100) {
                    for (int k = 0; k < 9; k++) {
                        if (k != i && k != j)
                            System.out.println(heights[k]);
                    }
                    return;
                }
            }
        }
    }
}
