// 매개변수보다 인자 개수 적을 경우(허용)
const threeArgs = function (arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

console.log(threeArgs())
console.log(threeArgs(1))
console.log(threeArgs(1, 2))

// Spread syntax (rest parameters)
const restArgs = function (arg1, arg2, ...restArgs) {
    return [arg1, arg2, restArgs]
}

console.log(restArgs(1,2,3,4,5,6))

// arrow function================================================================
const arrow1 = function (name) {
    return `hello ${name}`
}


// [1] function 키워드 삭제
const arrow2 = (name) => {
    return `hello ${name}`
}


// [2] 인자 하나인 경우에만 () 생략 가능
const arrow3 = name => {
    return `hello ${name}`
}


// [3] 함수 바디가 return 을 포함한 표현식 1개일 경우 {}, return 삭제 가능
const arrow4 = name => `hello ${name}`

console.log(arrow1('1'))
console.log(arrow2('2'))
console.log(arrow3('3'))
console.log(arrow4('4'))