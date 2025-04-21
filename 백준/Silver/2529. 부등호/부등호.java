import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    static int[] mn;
    static int[] mx;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = Integer.parseInt(sc.nextLine());
        String[] ieqs = sc.nextLine().split(" ");

        mn = IntStream.rangeClosed(0, n).map(i -> 9 - i).toArray();
        mx = IntStream.rangeClosed(0, n).toArray();

        getNumbers(n, ieqs, 0, 0, new int[n+1]);

        System.out.println(Arrays.stream(mx)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining()));
        System.out.println(Arrays.stream(mn)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining()));
    }

    public static void getNumbers(int n, String[] ieqs, int use, int count, int[] arr) {
        if (count == n+1) {
            if (isBigger(mn, arr))
                mn = Arrays.copyOf(arr, arr.length);
            if (isBigger(arr, mx))
                mx = Arrays.copyOf(arr, arr.length);
            return;
        }

        if (count == 0) {
            for (int i = 0; i <= 9; i++) {
                arr[count] = i;
                getNumbers(n, ieqs, use | (1 << i), count + 1, arr);
            }
        } else if (ieqs[count-1].equals(">")) {
            for (int i = 0; i < arr[count-1]; i++) {
                int iBit = 1 << i;
                if ((use & iBit)==0) {
                    arr[count] = i;
                    getNumbers(n, ieqs, use | iBit, count + 1, arr);
                }
            }
        } else {
            for (int i = arr[count-1] + 1; i <= 9; i++) {
                int iBit = 1 << i;
                if ((use & iBit) == 0) {
                    arr[count] = i;
                    getNumbers(n, ieqs, use | iBit, count + 1, arr);
                }
            }
        }
    }

    public static boolean isBigger(int[] arr1, int[] arr2) {
        int length = arr1.length;
        for (int i = 0; i < length; i++) {
            if (arr1[i] == arr2[i])
                continue;
            return arr1[i] > arr2[i];
        }
        return false;
    }
}
