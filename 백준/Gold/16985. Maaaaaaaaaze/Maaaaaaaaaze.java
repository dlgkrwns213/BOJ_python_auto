import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {
    static int INF = Integer.MAX_VALUE;
    static int ans = INF;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][][] cube = new int[5][5][5];
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int k = 0; k < 5; k++)
                    cube[i][j][k] = Integer.parseInt(st.nextToken());
            }
        }

        makeCube(cube, 0, new int[]{0, 0, 0, 0, 0}, 0);
        System.out.println(ans != INF ? ans : -1);
    }

    public static int bfs(int[][][] cube) {
        if (cube[0][0][0] == 0 || cube[4][4][4] == 0)
            return INF;

        int[] goX = {-1, 1, 0, 0, 0, 0};
        int[] goY = {0, 0, -1, 1, 0, 0};
        int[] goZ = {0, 0, 0, 0, -1, 1};

        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0, 0, 0, 0});
        boolean[][][] visited = new boolean[5][5][5];
        visited[0][0][0] = true;

        while (!q.isEmpty()) {
            int[] first = q.poll();
            int x = first[0];
            int y = first[1];
            int z = first[2];
            int count = first[3];

            if (x == 4 && y == 4 && z == 4)
                return count;

            for (int idx = 0; idx < 6; idx++) {
                int nx = x + goX[idx];
                int ny = y + goY[idx];
                int nz = z + goZ[idx];

                if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5 || nz < 0 || nz >= 5)
                    continue;
                if (cube[nx][ny][nz] == 0 || visited[nx][ny][nz])
                    continue;

                visited[nx][ny][nz] = true;
                q.add(new int[]{nx, ny, nz, count+1});
            }
        }

        return INF;
    }

    public static void rotateYZ(int[][][] cube, int x) {
        // 1. y-z 평면을 전치 (transpose)
        for (int y = 0; y < 5; y++) {
            for (int z = y; z < 5; z++) {
                int temp = cube[x][y][z];
                cube[x][y][z] = cube[x][z][y];
                cube[x][z][y] = temp;
            }
        }

        // 2. 각 행을 좌우 반전 (x축 기준으로)
        for (int y = 0; y < 5; y++) {
            for (int z = 0; z < 2; z++) {
                int temp = cube[x][y][z];
                cube[x][y][z] = cube[x][y][4 - z];
                cube[x][y][4 - z] = temp;
            }
        }
    }

    public static void makeCube(int[][][] cube, int count, int[] arr, int use) {
        if (use == 31) {
            int[][][] newCube = new int[5][5][5];
            for (int layer = 0; layer < 5; layer++)
                newCube[layer] = cube[arr[layer]];
            rotateCube(newCube, 0);
        }

        for (int i = 0; i < 5; i++) {
            int iBit = 1 << i;
            if ((use & iBit) == 0) {
                arr[count] = i;
                makeCube(cube, count + 1, arr, use | iBit);
            }
        }
    }

    public static void rotateCube(int[][][] cube, int idx) {
        if (idx == 5) {
            ans = Math.min(ans, bfs(cube));
            return;
        }

        for (int rotate = 0; rotate < 4; rotate++) {
            rotateYZ(cube, idx);
            rotateCube(cube, idx+1);
        }
    }
}