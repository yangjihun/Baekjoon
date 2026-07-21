class Solution {
    public int[] dfs(int depth, int[] level, int[][] users, int[] emoticons) {
        // 최대에 도달한다면 계산
        if (depth==emoticons.length) {
            int join = 0;
            int count = 0;
            for (int user=0; user<users.length; user++) {
                int bill = 0;
                for (int i=0; i<emoticons.length; i++) {
                    // 할인율이 만족되지 못하면 스킵
                    if (level[i] < users[user][0]) {
                        continue;
                    }
                    // 할인율을 만족하면 bill에 더하기
                    bill += emoticons[i] - (emoticons[i] * level[i] / 100);
                }
                // 만약 더한 값이 초과한다면 가입자+1
                if (bill >= users[user][1]) {
                    join++;
                }
                // 초과하지 않는다면 수익에 포함
                else {
                    count += bill;
                }
            }
            return new int[] {join, count};
        }
        int[] answer = new int[2];
        for (int i=1; i<=4; i++) {
            level[depth] = i * 10;
            int[] current = dfs(depth+1, level, users, emoticons);
            if (answer[0] < current[0]) {
                answer = current;
            }
            else if (answer[0]==current[0] && answer[1]<current[1]) {
                answer = current;
            }
        }
        return answer;
    }
    public int[] solution(int[][] users, int[] emoticons) {
        int[] answer = new int[2];
        int[] level = new int[emoticons.length];
        answer = dfs(0, level, users, emoticons);
        return answer;
    }
}