// Test file with intentional violations
const API_KEY = "sk-secret-12345";  // Hardcoded secret!
var bad_name = "snake_case";         // Not camelCase!
console.log("Debug message");        // Console.log!

function x() {                       // Function name too short!
  return "test";
}
