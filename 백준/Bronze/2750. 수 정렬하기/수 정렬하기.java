import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++)
            numbers[i] = Integer.parseInt(br.readLine());

        mergeSort(numbers, 0, n-1);

        StringBuilder answer = new StringBuilder();
        for (int number: numbers)
            answer.append(number).append('\n');
        System.out.println(answer);
    }

    private static void mergeSort(int[] numbers, int left, int right) {
        if (left >= right)
            return;

        int mid = left + right >> 1;
        mergeSort(numbers, left, mid);
        mergeSort(numbers, mid+1, right);
        merge(numbers, left, mid, right);
    }

    private static void merge(int[] numbers, int left, int mid, int right) {
        int[] tmp = new int[right-left+1];

        int i = left;
        int j = mid+1;
        int k = 0;

        while (i <= mid && j <= right) {
            tmp[k++] = numbers[i] <= numbers[j] ? numbers[i++] : numbers[j++];
        }

        while (i <= mid)
            tmp[k++] = numbers[i++];
        while (j <= right)
            tmp[k++] = numbers[j++];

        for (int idx = 0; idx < right-left+1; idx++)
            numbers[idx+left] = tmp[idx];
    }
}