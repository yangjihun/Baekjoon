import java.util.*;
/*
P : 응시자
O : 빈 테이블
X : 파티션

접근방법
1. 각 응시자 간의 위치를 저장한다.
2. 응시자끼리의 맨해튼 거리를 구한다.
    2-1. 응시자 간 거리가 2 이하라면, 접근 가능한지 파악한다.
    2-2. 응시자 간 거리가 2 초과라면, continue
*/
class Solution {
    // 맨해튼 거리 계산 함수
    public int manhattan(int[] start, int[] end) {
        int y = Math.abs(start[0] - end[0]);
        int x = Math.abs(start[1] - end[1]);
        return y + x;
    }
    // 접근 가능한지 확인하는 함수
    public boolean canGo(char[][] map, int[] start, int[] end) {
        // 거리가 1이면 true 반환
        if (manhattan(start, end) == 1)
            return true;
        // 거리가 2일 경우 파티션 계산
        int y1 = start[0];
        int y2 = end[0];
        int x1 = start[1];
        int x2 = end[1];
        if (y1 == y2) {
            int mid = (x1 + x2) / 2;
            return map[y1][mid] != 'X';
        }
        if (x1 == x2) {
            int mid = (y1 + y2) / 2;
            return map[mid][x1] != 'X';
        }
        // 대각선인 경우
        return map[y1][x2] != 'X' || map[y2][x1] != 'X';
    }
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        Arrays.fill(answer, 1);
        for (int T = 0; T < 5; T++) {
            String[] place = places[T];
            char[][] map = new char[5][5];
            List<int[]> part = new ArrayList<>();
            // map 할당 및 응시자 위치 할당
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < 5; j++) {
                    map[i][j] = place[i].charAt(j);
                    if (map[i][j] == 'P') {
                        part.add(new int[] {i, j});
                    }
                }
            }
            // 응시자 간 맨해튼 거리 계산
            for (int i = 0; i < part.size(); i++) {
                for (int j = i + 1; j < part.size(); j++) {
                    // 맨해튼 거리 <= 2라면 파티션 여부 파악
                    int[] start = part.get(i);
                    int[] end = part.get(j);
                    if (manhattan(start, end) <= 2) {
                        if (canGo(map, start, end)) {
                            answer[T] = 0;
                        }
                    }
                }
            }
            
        }
        return answer;
    }
}