// 스택/큐
function solution(progresses, speeds) {
    let answer = [];
    let beforeCommitDay = 0;

    progresses.map((a, i) => {
        let day = Math.ceil((100 - a) / speeds[i]);   

        if(day > beforeCommitDay) {
            answer.push(1)
            beforeCommitDay = day 
        }
        else {
            answer[answer.length - 1]++
        }
    })

    return answer;
}