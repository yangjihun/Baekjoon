import java.io.*;
import java.util.*;

class Staff {
    String name;
    long votes;
    int token = 0;
    Staff(String name, long votes) {
        this.name = name;
        this.votes = votes;
    }
}

class Score {
    int staffIdx;
    long votes;
    int div;
    Score(int staffIdx, long votes, int div) {
        this.staffIdx = staffIdx;
        this.votes = votes;
        this.div = div;
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static String next() throws Exception {
        while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }
    static int nextInt() throws Exception { return Integer.parseInt(next()); }
    static long nextLong() throws Exception { return Long.parseLong(next()); }

    public static void main(String[] args) throws Exception {
        long X = nextLong();
        int N = nextInt();

        List<Staff> staffs = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String name = next();
            long a = nextLong();

            // 5%만
            if (a * 20L >= X) staffs.add(new Staff(name, a));
        }

        // 점수 풀 생성
        List<Score> pool = new ArrayList<>();
        for (int i = 0; i < staffs.size(); i++) {
            long v = staffs.get(i).votes;
            for (int d = 1; d <= 14; d++) pool.add(new Score(i, v, d));
        }

        // 정렬
        pool.sort((s1, s2) -> {
            long left = s1.votes * s2.div;
            long right = s2.votes * s1.div;
            return Long.compare(right, left); // 내림차순
        });

        // 상위 14개 토큰
        for (int i = 0; i < 14; i++) {
            staffs.get(pool.get(i).staffIdx).token++;
        }

        // 정렬
        staffs.sort(Comparator.comparing(s -> s.name));
        StringBuilder sb = new StringBuilder();
        for (Staff s : staffs) {
            sb.append(s.name).append(' ').append(s.token).append('\n');
        }
        System.out.print(sb);
    }
}