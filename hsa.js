
const API_KEY = "sk_live_1234567890abcdef";
const SECRET_TOKEN = "my_private_auth_token_123";

// 1. Hardcoded URL
const API_URL = "https://api.example.com/v1/users";
const LOGIN_URL = "https://example.com/api/login";

// 2. Incorrect PascalCase naming
class userManager {
    constructor() {
        this.user_name = "Harsha";
    }
}

class payment_service {
    processPayment(amount) {
        return amount;
    }
}

// 3. Mutating array methods instead of immutable methods
function processUsers(users) {
    users.push({ name: "Test User", role: "admin" });

    users.sort((a, b) => a.name.localeCompare(b.name));

    users.reverse();

    users.splice(0, 1);

    users[0].active = true;

    return users;
}

// 4. More hardcoded secrets
function authenticateUser(username, password) {
    const dbPassword = "Admin@12345";
    const jwtSecret = "jwt_secret_987654321";

    if (password === dbPassword) {
        return jwtSecret;
    }

    return null;
}

// Additional violations
function addProduct(products, product) {
    products.push(product);
    return products;
}

function removeProduct(products, index) {
    products.splice(index, 1);
    return products;
}

function updateUsers(users) {
    users.sort((a, b) => a.id - b.id);
    return users;
}
