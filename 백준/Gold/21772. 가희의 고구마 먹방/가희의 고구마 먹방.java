import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int R,C,answer = 0;
	static String[][] G;
	static int[] dx = {0,0,1,-1};
	static int[] dy = {1,-1,0,0};
	static int nextInt() throws Exception {
		while (st == null || !st.hasMoreTokens()) {
			String line = br.readLine();
			st = new StringTokenizer(line);
		}
		return Integer.parseInt(st.nextToken());
	}
	static String next() throws Exception {
		while (st == null || !st.hasMoreTokens()) {
			String line = br.readLine();
			st = new StringTokenizer(line);
		}
		return st.nextToken();
	}
	static void BT(int y, int x, int depth, int num) {
		if (depth==0) {
			answer = Math.max(answer, num);
			return;
		}
		for (int i=0; i<4; i++) {
	        int nx = x + dx[i];
	        int ny = y + dy[i];
			if (nx>=0 && nx<C && ny>=0 && ny<R && !"#".equals(G[ny][nx])) {
				
				boolean ate = false;
		        if ("S".equals(G[ny][nx])) {
		            ate = true;
		            G[ny][nx] = ".";
		        }
				BT(ny, nx, depth - 1, num + (ate ? 1 : 0));
				if (ate) G[ny][nx] = "S";
			}
		}
	}
	public static void main(String[] args) throws Exception {
		R = nextInt();
		C = nextInt();
		int T = nextInt();
		int[] gahi = new int[2];
		G = new String[R][C];
		// 할당
		for (int i=0;i<R;i++) {
			G[i] = next().split("");
		}
		for (int i=0; i<R;i++) {
			for (int j=0; j<C; j++) {
				if (G[i][j].equals("G")) {
					gahi[0] = i;
					gahi[1] = j;
				}
			}
		}
		// Solution
		BT(gahi[0], gahi[1], T, 0);
		System.out.println(answer);
	}
}