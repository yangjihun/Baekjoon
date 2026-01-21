import java.io.*;
import java.util.*;

public class Main {
	static Scanner sc = new Scanner(System.in);
	
	static int req(int n, int y, int x, int answer) {
		if (n == 0) {
			return answer;
		}
		int half = (int) Math.pow(2, n-1);
		int zone;
		if (y < half) {
			if (x < half) zone = 0;
			else {
				zone = 1;
				x -= half;
			}
		}
		else {
			y -= half;
			if (x<half) zone = 2;
			else {
				zone = 3;
				x -= half;
			}
		}
		return half * half * zone + req(n-1,y,x,answer);
	}
	public static void main(String[] args) throws Exception {
		int N = sc.nextInt();
		int r = sc.nextInt();
		int c = sc.nextInt();
		System.out.println(req(N,r,c,0));
	}
}
