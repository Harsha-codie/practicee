// Violates: Functions should not exceed 50 lines
// Violates: Functions should have at most 4 parameters
function processUserData(userId, name, email, age, role, status) {
    let user = {};
    user.id = userId;
    user.name = name;
    user.email = email;
    user.age = age;
    user.role = role;
    user.status = status;

    console.log("Processing user...");

    // Violates: Prefer immutable array methods
    let numbers = [1, 2, 3, 4, 5];
    numbers.push(6);
    numbers.splice(0, 1);

    // Violates: Boolean variable naming convention
    let active = true;
    let valid = false;

    if (active) {
        valid = true;
    }

    // Violates: Functions should either always return a value or never return
    if (valid) {
        return user;
    }

    console.log("Invalid user");

    // Violates: Consistent file naming convention (rule-level test)
    // Example filename: UserDataProcessor.js

    // More unnecessary code to increase function length
    for (let i = 0; i < numbers.length; i++) {
        console.log(numbers[i]);
    }

    console.log("Finished processing");

    return;
}
