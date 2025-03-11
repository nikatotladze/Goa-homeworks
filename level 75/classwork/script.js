// 1

const child = document.getElementById('child');

let x = 225;
let y = 225;

const moveUp = setInterval(() => {
   y -= 1; 
   child.style.top = `${y}px`;
   if (y == 0){
      clearInterval(moveUp);
      const moveRight = setInterval(() => {
         x += 1; 
         child.style.left = `${x}px`;
         if (x == 450){
            clearInterval(moveRight);
            const moveDown = setInterval(() => {
               y += 1; 
               child.style.top = `${y}px`;
               if (y == 450){
                  clearInterval(moveDown);
                  const moveLeft = setInterval(() => {
                     x -= 1; 
                     child.style.left = `${x}px`;
                     if (x == 225 && y == 225){
                        clearInterval(moveLeft);
                     }
                  }, 5);
               }
            }, 5);
         }
      }, 5);
   }
}, 5);



// 2

const Child = document.getElementById("child");

let left = 0;
let Y = 0;
let direction = "top";

const move = setInterval(function(){
    if(direction == "top"){
        y--;
        if(y == 0){
            direction = "left";
        }
    } else if(direction == "left"){
        left--;
        if(left == 0){
            direction = "bottom";
        }
    } else if(direction == "bottom"){
        y++;
        if(y == 450){
            direction = "right";
        }
    } else{
        left++;
        if(left == 450){
            direction = "top";
        }
    }

    child.style.left = left + 'px';
    child.style.top = y + 'px';
}, 5);
