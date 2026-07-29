function solution(info, query) {
    const map = new Map();

    // 1. 조합 생성을 위한 DFS 함수
    function makeCombinations(tokens, currentKey, depth, score) {
        if (depth === 4) {
            if (!map.has(currentKey)) {
                map.set(currentKey, []);
            }
            map.get(currentKey).push(score);
            return;
        }

        // 선택 1: 해당 조건 포함
        makeCombinations(tokens, currentKey + tokens[depth], depth + 1, score);
        // 선택 2: '-' (상관없음) 포함
        makeCombinations(tokens, currentKey + '-', depth + 1, score);
    }

    // 2. info 파싱 및 조합 생성
    for (const item of info) {
        const tokens = item.split(' ');
        const score = Number(tokens.pop()); // 마지막 요소는 점수
        makeCombinations(tokens, '', 0, score);
    }

    // 3. 각 조건 키에 해당하는 점수 배열 오름차순 정렬
    for (const [key, scores] of map) {
        scores.sort((a, b) => a - b);
    }

    // 4. Lower Bound 이분 탐색 함수
    function binarySearch(arr, target) {
        let left = 0;
        let right = arr.length;

        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (arr[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    console.log(map);
    // 5. query 처리
    const answer = [];
    for (const q of query) {
        // ' and '를 공백으로 바꾸고, 공백 기준으로 잘라냄
        const tokens = q.replace(/ and /g, ' ').split(' ');
        const targetScore = Number(tokens.pop());
        const key = tokens.join('');

        if (map.has(key)) {
            const scores = map.get(key);
            const idx = binarySearch(scores, targetScore);
            answer.push(scores.length - idx);
        } else {
            answer.push(0);
        }
    }

    return answer;
}