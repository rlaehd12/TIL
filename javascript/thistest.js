const tom = {
    name: 'Tom',
    introduce() {
      console.log(this)  // {name: 'Tom', introduce: ƒ}
      console.log('Hi, my name is' + this.name)  // Hi, my name isTom
    }
}
const tomy = {
    // tomy == this 
    name: 'Tom',
    introduce:()=> {
      console.log(this)  // tomy의 상위 객체 == window
      console.log('Hi, my name is' + this.name)  // Hi, my name is
    }
}
const tomyy = {
    // this == tomyy 결정
    name: 'Tom',
    introduce() {
        console.log(this, 'a')  // {name: 'Tom', introduce: ƒ}
        const tomin = {
            name: 'tasdf',
            intro: function(){
                console.log(this)  // {name: 'tasdf', intro: ƒ}
                console.log('Hi, my name is' + this.name)  // Hi, my name isundefined
            },
            intro2:() => {
                console.log(this)  // {name: 'Tom', introduce: ƒ}  
                console.log('Hi, my name is' + this.name)  // Hi, my name isTom 
            },
            innerObj : {
                name : "innerObj",
                innerMethod:()=>{
                    console.log('innerObj :',this)  // {name: 'Tom', introduce: ƒ}
                }
            }

        }
        tomin.intro()
        tomin.intro2() 
        tomin.innerObj.innerMethod()
    }
}