// 1

const promise = new Promise((resolve, reject) => {
  resolve("Hello, Promise!");
});

promise.then(message => {
  console.log(message); 
});


// 2

const errorPromise = new Promise((resolve, reject) => {
  reject("Something went wrong!");
});

errorPromise
  .catch(error => {
    console.error(error);
  });


// 3

const delayedPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("2 seconds have passed");
  }, 2000);
});

delayedPromise.then(message => {
  console.log(message); 
});


// 4

const randomPromise = new Promise((resolve, reject) => {
  const success = Math.random() > 0.5;
  if (success) {
    resolve("Success!");
  } else {
    reject("Failed!");
  }
});

randomPromise
  .then(result => {
    console.log(result); 
  })
  .catch(error => {
    console.error(error); 
  });



// 5

const chainPromise = new Promise((resolve, reject) => {
  resolve(5);
});

chainPromise
  .then(num => num * 2)  
  .then(num => num * 2)  
  .then(num => num * 2)  
  .then(result => {
    console.log(result); 
  });


// 6

const fetchData = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Data fetched!");
  }, 1000);
});

fetchData.then(data => {
  console.log(data); 
});
