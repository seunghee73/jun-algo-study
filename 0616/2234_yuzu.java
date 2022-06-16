package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ2234 {
    public static int n, m;
    public static int room_max = 0;
    public static int[][] arr;
    public static boolean[][] visit;
    public static int[] dx = {0, -1, 0, 1};
    public static int[] dy = {-1, 0, 1, 0};

    static class Point{
        int a, b;
        Point(int a, int b){
            this.a = a;
            this.b = b;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[m][n];
        visit = new boolean[m][n];

        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int room_cnt = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (!visit[i][j]) {
                    bfs(i, j);
                    room_cnt += 1;
                }
            }
        }
        System.out.println(room_cnt);
        System.out.println(room_max);

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                break_wall(i, j);
            }
        }
        System.out.println(room_max);
    }

    public static void bfs(int x, int y) {
        Queue<Point> q = new LinkedList<Point>();
        q.offer(new Point(x, y));
        visit[x][y] = true;
        int room_size = 0;

        while(!q.isEmpty()) {
            Point point = q.poll();
            int a = point.a;
            int b = point.b;
            int wall = arr[a][b];
            room_size += 1;

            for (int i = 0; i < 4; i++) {
                if ((wall & (1 << i)) > 0) {
                    continue;
                }
                int na = a + dx[i];
                int nb = b + dy[i];

                if ((na >= 0 && na < m) && (nb >= 0 && nb < n)) {
                    if (!visit[na][nb]) {
                        visit[na][nb] = true;
                        q.offer(new Point(na, nb));
                    }
                }
            }
        }
        room_max = Math.max(room_max, room_size);
    }

    public static void break_wall(int x, int y) {
        for (int i = 0; i < 4; i++) {
            if ((arr[x][y] & (1 << i)) != 0) {
                for (int j = 0; j < visit.length; j++) {
                    Arrays.fill(visit[j], false);
                }
                arr[x][y] -= (1 << i);
                bfs(x, y);
                arr[x][y] += (1 << i);
            }
        }
    }
}