package BOJ;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ5427 {
    public static int w, h, ans;
    public static int[][] arr;
    public static Queue<int[]> fire;
    public static Queue<int[]> man;
    public static String ans_fail = "IMPOSSIBLE";
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = null;

        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            w = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            arr = new int[h][w];
            fire = new LinkedList<>();
            man = new LinkedList<>();
            ans = 0;

            for (int i = 0; i < h; i++) {
                String s = br.readLine();
                for (int j = 0; j < w; j++) {
                    char c = s.charAt(j);
                    arr[i][j] = c;
                    if (c == '*') {
                        fire.offer(new int[]{i, j});
                    } else if (c == '@') {
                        man.offer(new int[]{i, j, 0});
                    }
                }
            }
            bfs();
            sb.append((ans > 0) ? ans + "\n" : ans_fail + "\n");

        }
        System.out.println(sb.toString());
    }

    public static void bfs() {
        while (!fire.isEmpty() || !man.isEmpty()) {
            int len1 = fire.size();
            if (len1 > 0) {
                while (len1-- > 0) {
                    int x = fire.peek()[0];
                    int y = fire.peek()[1];
                    fire.poll();

                    for (int i = 0; i < 4; i++) {
                        int nx = x + dx[i];
                        int ny = y + dy[i];

                        if (nx < 0 || nx >= h) {
                            continue;
                        }
                        if (ny < 0 || ny >= w) {
                            continue;
                        }
                        if (arr[nx][ny] == '#' || arr[nx][ny] == '*') {
                            continue;
                        }
                        arr[nx][ny] = '*';
                        fire.offer(new int[]{nx, ny});
                    }
                }
            }

            int len2 = man.size();
            boolean p = false;
            if (len2 > 0) {
                while (len2-- > 0) {
                    int x = man.peek()[0];
                    int y = man.peek()[1];
                    int cnt = man.peek()[2];
                    man.poll();

                    for (int i = 0; i < 4; i++) {
                        int nx = x + dx[i];
                        int ny = y + dy[i];
                        if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
                            ans = cnt + 1;
                            p = true;
                            break;
                        }
                        if (arr[nx][ny] == '.') {
                            arr[nx][ny] = cnt + 1;
                            man.offer(new int[]{nx, ny, cnt + 1});
                        }
                    }
                    if (p) {
                        break;
                    }
                }
                if (p) {
                    break;
                }
            } else {
                ans = -1;
                break;
            }
        }
    }
}