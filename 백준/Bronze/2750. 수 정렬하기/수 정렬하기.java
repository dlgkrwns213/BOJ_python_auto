import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++)
            numbers[i] = Integer.parseInt(br.readLine());

        // bubbleSort(numbers);
        selectionSort(numbers);
        // insertionSort(numbers);

        StringBuilder answer = new StringBuilder();
        for (int number: numbers)
            answer.append(number).append('\n');
        System.out.println(answer);
    }

    private static void bubbleSort(int[] numbers) {
        int n = numbers.length;

        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-1-i; j++) {
                if (numbers[j] > numbers[j+1]) {
                    int tmp = numbers[j];
                    numbers[j] = numbers[j+1];
                    numbers[j+1] = tmp;
                }
            }
        }
    }

    private static void selectionSort(int[] numbers) {
        int n = numbers.length;

        for (int i = 0; i < n-1; i++) {
            int minIdx = i;

            for (int j = i+1; j < n; j++) {
                if (numbers[j] < numbers[minIdx])
                    minIdx = j;
            }

            int tmp = numbers[i];
            numbers[i] = numbers[minIdx];
            numbers[minIdx] = tmp;
        }
    }

    private static void insertionSort(int[] numbers) {
        int n = numbers.length;

        for (int i = 1; i < n; i++) {
            int key = numbers[i];
            int j = i-1;

            while (j >= 0 && numbers[j] > key) {
                numbers[j+1] = numbers[j];
                j--;
            }
        }
    }
}