import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] numbers = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++)
                numbers[i][j] = Integer.parseInt(st.nextToken());
        }

        // O(N^2)
        int[] maxNumbers = new int[n];
        for (int i = 0; i < n; i++) {
            int[] maxNumberData = getMaxNumberData(numbers[i]);
            numbers[i][maxNumberData[0]] = Integer.MIN_VALUE;
            maxNumbers[i] = maxNumberData[1];
        }

        int ans = -1;
        for (int unused = 0; unused < n; unused++) {
            // O(N)
            int[] maxMaxNumberData = getMaxNumberData(maxNumbers);
            int idx = maxMaxNumberData[0];
            ans = maxMaxNumberData[1];
            // System.out.println(ans);

            // O(N)
            // 최대 값이 있던 줄에서 그 다음 큰 수를 가져옴
            int[] nxtMaxNumberData = getMaxNumberData(numbers[idx]);
            numbers[idx][nxtMaxNumberData[0]] = Integer.MIN_VALUE;
            maxNumbers[idx] = nxtMaxNumberData[1];
        }

        System.out.println(ans);
    }

    public static int[] getMaxNumberData(int[] numbers) {
        int idx = 0, maxNumber = Integer.MIN_VALUE;
        for (int i = 0; i < numbers.length; i++) {
            if (maxNumber < numbers[i]) {
                maxNumber = numbers[i];
                idx = i;
            }
        }
        return new int[]{idx, maxNumber};
    }
}