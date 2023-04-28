// forEach ========================================================
const colors = ['red', 'blue', 'green']
const printFunc = function (color) {
    console.log(color)
}

// [1] 미리 정의
colors.forEach(printFunc)
// [2] 직접 함수 정의
colors.forEach(function(color, index, array){
    console.log(color)
    console.log(index)
    console.log(array)
})

// map ============================================================
let a
a = colors.map(function(color){
    return color + ' color'
})
console.log(a)

// filter ==========================================================
const product = [
    { name:'cucumber', type:'vegetable'},
    { name:'banana', type:'fruit'},
    { name:'carrot', type:'vegetable'},
    { name:'apple', type:'fruit'},
]
const fruitfilter = function (product) {
    return product.type === 'fruit'
}
const fruits = product.filter(fruitfilter)
console.log(fruits)

// reduce ==========================================================
const tests = [90, 90, 85, 77]
const sum = tests.reduce(function (total, x){ // total = acc, x = element
    return total + x
})
console.log(sum)