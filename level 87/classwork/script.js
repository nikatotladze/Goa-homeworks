const form = document.getElementById('userForm');

form.addEventListener('submit', function(e) {
  e.preventDefault();

  const name = form.name.value;
  const email = form.email.value;
  const age = form.age.value;

  const personData = {
    name,
    email,
    age
  };

  let index = 1;
  while (localStorage.getItem(`person${index}`)) {
    index++;
  }

  localStorage.setItem(`person${index}`, JSON.stringify(personData));
  alert(`მონაცემები შენახულია როგორც person${index}`);

  form.reset();
});