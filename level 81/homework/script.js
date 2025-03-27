const regForm = document.getElementById("register");
const loginForm = document.getElementById("login");
const userList = document.getElementById("user-list");

const loadUsers = () => {
    const storedUsers = JSON.parse(localStorage.getItem("users")) || [];
    if (!storedUsers.some(user => user.email === "admin@example.com")) {
        storedUsers.push({ username: "Admin", email: "admin@example.com", password: "admin123", isAdmin: true });
        localStorage.setItem("users", JSON.stringify(storedUsers));
    }
    return storedUsers;
};

let users = loadUsers();

const saveUsers = () => {
    localStorage.setItem("users", JSON.stringify(users));
};

const handleRegister = () => {
    const username = regForm.username.value;
    const email = regForm.email.value;
    const password = regForm.password.value;
    
    if (users.some(user => user.email === email)) {
        alert("Email is already registered");
        return;
    }
    
    const newUser = { username, email, password, isAdmin: false };
    users.push(newUser);
    saveUsers();
    alert("Registered successfully");
    regForm.reset();
};

const handleLogIn = () => {
    const email = loginForm.email.value;
    const password = loginForm.password.value;
    
    const user = users.find(user => user.email === email && user.password === password);
    
    if (user) {
        localStorage.setItem("loggedInUser", JSON.stringify(user));
        displayUserInfo(user);
    } else {
        alert("User not found");
    }
    loginForm.reset();
};

const displayUserInfo = (user) => {
    document.body.innerHTML = "";
    const userInfo = document.createElement("div");
    userInfo.innerHTML = `<h2>Welcome, ${user.username}</h2><p>Email: ${user.email}</p>`;
    document.body.appendChild(userInfo);
    
    if (user.isAdmin) {
        displayUserManagement();
    }
};

const displayUserManagement = () => {
    userList.innerHTML = "<h3>User List</h3>";
    users.forEach((user, index) => {
        if (!user.isAdmin) {
            const userItem = document.createElement("div");
            userItem.innerHTML = `${user.username} (${user.email}) <button onclick="deleteUser(${index})">Delete</button>`;
            userList.appendChild(userItem);
        }
    });
    document.body.appendChild(userList);
};

const deleteUser = (index) => {
    users.splice(index, 1);
    saveUsers();
    displayUserManagement();
};

regForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleRegister();
});

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleLogIn();
});