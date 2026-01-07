//Create a promise method. The promise will get resolved when the timer times out in 6 seconds
let myPromise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Promise resolved')
    }, 6000)
})

//Console log before calling the promise
console.log('Before calling promise')

//Call the promise and wait for it to be resolved
myPromise.then((successMessage) => {
    console.log('From callback ' + successMessage)
})

//Console log after calling the promise
    console.log('After calling promise')