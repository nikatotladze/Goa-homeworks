// 1

// Promise არის JavaScript-ის ობიექტი, რომელიც წარმოადგენს ასინქრონურ ოპერაციას.


// 2

const getUserData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("User data was successfully loaded.");
    }, 2000);
  });
};

getUserData().then(result => {
  console.log(result);
});


// 3

const getServerError = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      reject("An error occurred while retrieving data from the server.");
    }, 2000);
  });
};

getServerError()
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.error(error);
  });
