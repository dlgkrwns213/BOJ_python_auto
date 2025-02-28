import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        boolean[] d = new boolean[10001];

        // d 배열에 각 생성자를 기록
        for (int num = 1; num < 10000; num++) {
            int make = num + String.valueOf(num)
                    .chars()
                    .map(c -> c - '0')
                    .sum();

            if (make < 10001)
                d[make] = true;
        }

        StringBuilder sb = new StringBuilder();
        IntStream.range(1, 10000)
                .filter(num -> !d[num])
                .forEach(num -> sb.append(num).append("\n"));

        System.out.print(sb.toString());
    }
}