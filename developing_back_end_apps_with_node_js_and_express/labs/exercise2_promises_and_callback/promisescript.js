//Create a promise method. The promise will get resolved when the timer times out in 6 seconds
let myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Promise 1 resolved')
    }, 6000)
})

//Create a promise method. The promise will get resolved when the timer times out in 3 seconds
let myPromise2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Promise 2 resolved')
    }, 3000)
})

//Call the promise and wait for it to be resolved
myPromise.then((successMessage) => {
    console.log('From callback ' + successMessage)
    myPromise2.then((successMessage) => {
        console.log('From Callback ' + successMessage)
    })
})
