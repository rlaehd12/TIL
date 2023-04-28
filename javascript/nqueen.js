function findQueens(n) {
    let lst1 = new Array((2*n)-1)
    let lst2 = new Array((2*n)-1)
    let visited = new Array(n)  // undefined
    let answer = 0
    for (let i = 0; i < lst1.length; i++) {  // array initialize
        lst1[i] = 0
        lst2[i] = 0
    }

	const dfs = function(i){  // dfs
        if (i === n) {  // base case
            answer += 1
            return
        }
        for (let cur = 0; cur < n; cur++) {
            if (visited[cur] === undefined) {
                if (lst1[i+cur] === 0 && lst2[i+n-1-cur] === 0) {  // can go
                    visited[cur] = 1
                    lst1[i+cur] = 1
                    lst2[i+n-1-cur] = 1
                    dfs(i+1)
                    visited[cur] = undefined
                    lst1[i+cur] = 0
                    lst2[i+n-1-cur] = 0
                }
            }
        }
    }
    dfs(0,0)

	return answer
}

console.log(findQueens(12)) // 2
