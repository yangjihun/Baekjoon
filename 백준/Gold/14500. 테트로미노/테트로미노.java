import java.io.*;
import java.util.*;

public class Main
{
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int nextInt() throws Exception {
		while (st==null || !st.hasMoreTokens()) {
			String line = br.readLine();
			if (line==null) return Integer.MIN_VALUE;
			st = new StringTokenizer(line);
		}
		return Integer.parseInt(st.nextToken());
	}
	static String next() throws Exception {
		while (st==null || !st.hasMoreTokens()) {
			String line = br.readLine();
			if (line==null) return "";
			st = new StringTokenizer(line);
		}
		return st.nextToken();
	}
	static int N,M;
	static int[][] arr;
	static boolean[][] visited;
	static int[] dy = {1,-1,0,0};
	static int[] dx = {0,0,1,-1};
	static int answer = 0;

	private static void dfs(int y, int x, int depth, int sum) {
		if (depth<4) {
			int nx,ny;
			for (int i=0; i<4; i++) {
				ny = y + dy[i];
				nx = x + dx[i];
				if (nx>=0 && nx<M && ny>=0 && ny<N && !visited[ny][nx]) {
					visited[ny][nx] = true;
					dfs(ny,nx,depth+1, sum + arr[ny][nx]);
					visited[ny][nx] = false;
				}
			}
		}
		else {
			answer = Math.max(answer, sum);
		}
	}
	public static void main(String args[]) throws Exception
	{
		N = nextInt();
		M = nextInt();
		arr = new int[N][M];
		visited = new boolean[N][M];
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				arr[i][j] = nextInt();
			}
		}
		// ----
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				visited[i][j] = true;
				dfs(i, j, 1, arr[i][j]);
				visited[i][j] = false;
			}
		}
		
		// ㅗ
		int ny, nx, sum, direct, count;
		for (int y=0; y<N; y++) {
			for (int x=0; x<M; x++) {
				for (direct=0;direct<4;direct++) {
					sum = arr[y][x];
					count = 0;
					for (int i=0; i<4; i++) {
						if (i!=direct) {
							ny = y + dy[i];
							nx = x + dx[i];
							if (nx>=0 && ny>=0 && nx<M && ny<N) {
								sum += arr[ny][nx];
								count++;
							}
						}
					}
					if (count==3) 
						answer = Math.max(answer, sum);
				}
			}
		}
		System.out.println(answer);
	}
	
}