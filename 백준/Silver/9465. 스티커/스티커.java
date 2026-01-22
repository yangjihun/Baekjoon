import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test=0; test<T; test++) {
			int N = sc.nextInt();
			int[][] arr = new int[2][N+2];
			for (int i=0; i<2;i++) {
				for (int j=2; j<=N+1; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			// solution
			for (int i=2; i<=N+1;i++) {
				arr[0][i] += Math.max(Math.max(arr[1][i-1], arr[0][i-2]), arr[1][i-2]);
				arr[1][i] += Math.max(Math.max(arr[0][i-1], arr[1][i-2]), arr[0][i-2]);
			}
			System.out.println(Math.max(arr[0][N+1], arr[1][N+1]));
		}
	}
}
