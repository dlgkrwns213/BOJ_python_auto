import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] startTime = sc.nextLine().split(":");
        String[] destTime = sc.nextLine().split(":");

        int sh = Integer.parseInt(startTime[0]);
        int sm = Integer.parseInt(startTime[1]);
        int dh = Integer.parseInt(destTime[0]);
        int dm = Integer.parseInt(destTime[1]);

        int cnt = dm - sm;
        if (sm > dm) {
            cnt += 60;
            sh += 1;
        }

        cnt += (dh - sh + 24) % 24;
        System.out.println(cnt);
    }
}
