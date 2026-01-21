import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int N = Integer.parseInt(sc.nextLine());
		int[][] arr = new int[N][N];
		int[][] rgb = new int[N][N];
		boolean[][] visited = new boolean[N][N];
		Queue<int[]> q = new ArrayDeque<>();
		for (int y=0; y<N; y++) {
			String line = sc.nextLine();
			for (int x=0;x<N;x++) {
				if (line.charAt(x)=='R') {
					arr[y][x] = 0;
					rgb[y][x] = 1;
				}
				else if (line.charAt(x)=='G') {
					arr[y][x] = 1;
					rgb[y][x] = 1;
				}
				else if (line.charAt(x)=='B'){
					arr[y][x] = 2;
					rgb[y][x] = 2;
				}
			}
		}
		
		int[] nc = {1,0,-1,0};
		int[] nr = {0,1,0,-1};
		int[] dot;
		int count = 0;
		int nx,ny;
		for (int y=0; y<N; y++) {
			for (int x=0; x<N; x++) {
				if (!visited[y][x]) {
					count++;
					q.offer(new int[] {y,x});
					while(!q.isEmpty()) {
						dot = q.poll();
						for (int i=0; i<4; i++) {
							nx = dot[1] + nc[i];
							ny = dot[0] + nr[i];
							
							if (nx>=0 && nx<N && ny>=0 && ny<N && !visited[ny][nx] && arr[ny][nx]==arr[y][x]) {
								q.offer(new int[] {ny,nx});
								visited[ny][nx] = true;
							}
						}
					}
				}
			}
		}
		System.out.print(count + " ");
		visited = new boolean[N][N];
		count = 0;
		for (int y=0; y<N; y++) {
			for (int x=0; x<N; x++) {
				if (!visited[y][x]) {
					count++;
					q.offer(new int[] {y,x});
					while(!q.isEmpty()) {
						dot = q.poll();
						for (int i=0; i<4; i++) {
							nx = dot[1] + nc[i];
							ny = dot[0] + nr[i];
							
							if (nx>=0 && nx<N && ny>=0 && ny<N && !visited[ny][nx] && rgb[ny][nx]==rgb[y][x]) {
								q.offer(new int[] {ny,nx});
								visited[ny][nx] = true;
							}
						}
					}
				}
			}
		}
		System.out.println(count);
	}
}
