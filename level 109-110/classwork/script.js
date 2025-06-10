const obj = {
  arr: [
    {
      level: [10, 50, 100],
    },

    {
      level: [20, 40, 60],
      students: [
        {
          name: "jemala",
          surname: "barkalaia",
          score: [8, 8, 10],
        },
        {
          name: "jumbera",
          surname: "lamazi",
          score: [10, 7, 9],
        },
      ],
    },
  ],
};



const {
  arr: [
    { level: [level1_1, level1_2, level1_3] },  
    {
      level: [level2_1, level2_2, level2_3],  
      students: [
        {
          name: student1_name,
          surname: student1_surname,
          score: [student1_score1, student1_score2, student1_score3],
        },
        {
          name: student2_name,
          surname: student2_surname,
          score: [student2_score1, student2_score2, student2_score3],
        },
      ],
    },
  ],
} = obj;


console.log("First item's levels:", level1_1, level1_2, level1_3);

console.log("Second item's levels:", level2_1, level2_2, level2_3);

console.log("Student 1: Name:", student1_name, ", Surname:", student1_surname);

console.log("Student 1: Scores:", student1_score1, student1_score2, student1_score3);

console.log("Student 2: Name:", student2_name, ", Surname:", student2_surname);

console.log("Student 2: Scores:", student2_score1, student2_score2, student2_score3);

