console.log('hello hello2 hello3')
words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    
    let len = word.length
    len = parseInt(len/2)
    // console.log(len)
    let flag = 0
    for (let i = 0; i < len; i++) {
        if (word[i] !== word[word.length-i-1]) {
            flag = 1
        }
    }
    console.log(flag === 0 ? true:false)
}
palindrome('asdf')

// ===============================================
const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']
const rcp = {
    'rock':0,
    'scissors':1,
    'paper':2,
}

const playGame = (p1_choice, p2_choice) => {
    if (rcp[p1_choice] === rcp[p2_choice]) {
        console.log(0)
    }
    else if ((rcp[p1_choice] - rcp[p2_choice]) === -1 || (rcp[p1_choice] - rcp[p2_choice]) === 2) {
        console.log(1)
    } 
    else {
        console.log(2)
    }
}
// for (let i = 0; i < p1.length; i++) {
//     playGame(p1[i], p2[i])
// }

// ==================================================================
const participantNums =  [[1, 1, 2, 2, 3], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]
for (const arr of participantNums) {
    for (let i = 0; i < arr.length; i++) {
        if (i === arr.lastIndexOf(arr[i]) && i === arr.indexOf(arr[i])) {
            console.log(arr[i])
            break
        }
    }
}