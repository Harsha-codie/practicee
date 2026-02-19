// SECURITY: Hardcoded credentials
const DB_PASSWORD = "super_secret_123";
const API_KEY = "sk-live-1234567890abcdef";
const auth_token = "ghp_FakeToken123456";
const jwt_secret = "my-jwt-secret-key";

// SECURITY: eval() usage (js-sec-001)
function processInput(userInput) {
    return eval(userInput);
}

// SECURITY: new Function() constructor (js-sec-002)
function createHandler(code) {
    const handler = new Function("data", code);
    return handler;
}

// SECURITY: innerHTML XSS (js-sec-003)
function renderComment(comment) {
    document.getElementById("output").innerHTML = comment;
}

// SECURITY: document.write XSS (js-sec-004)
function writeHTML(content) {
    document.write(content);
}

// SECURITY: Weak crypto MD5 (js-sec-006)
const crypto = require("crypto");
function hashData(data) {
    return crypto.createHash("md5").update(data).digest("hex");
}

// SECURITY: Weak crypto SHA1 (js-sec-007)
function checksumSHA1(data) {
    return crypto.createHash("sha1").update(data).digest("hex");
}

// SECURITY: Math.random for security (js-sec-008)
function generateToken() {
    return Math.random().toString(36).substring(2);
}

// SECURITY: SSL verification disabled (js-sec-009)
const https = require("https");
const insecureAgent = new https.Agent({ rejectUnauthorized: false });

// SECURITY: setTimeout with string (js-sec-010)
function delayedAction(code) {
    setTimeout("alert('hacked')", 1000);
}

// SECURITY: setInterval with string (js-sec-011)
function repeatedAction() {
    setInterval("console.log('tick')", 5000);
}

// SECURITY: CORS wildcard (js-sec-012)
const corsConfig = { origin: "*", credentials: true };

// SECURITY: outerHTML (js-sec-013)
function replaceElement(el, html) {
    el.outerHTML = html;
}

// SECURITY: prototype pollution (js-sec-014)
function merge(target, source) {
    target.__proto__.admin = true;
}

// STYLE: console.log left in code (js-style-001)
function processOrder(order) {
    console.log("Processing order:", order);
    console.debug("Debug info:", order.id);
    console.info("Order total:", order.total);
    console.warn("Low stock warning");
}

// STYLE: debugger statement (js-style-002)
function buggyFunction() {
    debugger;
    return 42;
}

// STYLE: alert() usage (js-style-003)
function showMessage(msg) {
    alert(msg);
}

// STYLE: var instead of let/const (js-style-004)
function oldStyleCode() {
    var x = 10;
    var y = 20;
    var result = x + y;
    return result;
}

// STYLE: TODO/FIXME/HACK comments (js-style-005)
// TODO: refactor this entire module
// FIXME: this breaks on edge cases
// HACK: temporary workaround for API bug
// XXX: needs review

// STYLE: nested ternary (js-style-006)
function getLabel(status) {
    return status === "active" ? "Active" : status === "pending" ? "Pending" : status === "cancelled" ? "Cancelled" : "Unknown";
}

// BEST PRACTICE: empty catch block (js-bp-001)
function unsafeOperation() {
    try {
        JSON.parse("invalid");
    } catch (e) {
    }
}

// BEST PRACTICE: throw literal (js-bp-002)
function validate(input) {
    if (!input) {
        throw "Input is required";
    }
}

// BEST PRACTICE: with statement (js-bp-003)
function hackyCode(obj) {
    with (obj) {
        return name + age;
    }
}

// BEST PRACTICE: magic numbers (js-bp-008)
function calculateDiscount(price) {
    if (price > 100) {
        return price * 0.85;
    } else if (price > 50) {
        return price * 0.92;
    }
    return price * 0.97;
}

// BEST PRACTICE: too many parameters (js-bp-009)
function createUser(name, email, age, address, phone, role, department) {
    return { name, email, age, address, phone, role, department };
}

// BEST PRACTICE: string concatenation (js-bp-007)
function formatMessage(user, action, target) {
    return "User " + user + " performed " + action + " on " + target;
}

// PERFORMANCE: sync fs operations (js-perf-001)
const fs = require("fs");
function readConfig() {
    const data = fs.readFileSync("/etc/config.json", "utf8");
    const exists = fs.existsSync("/tmp/cache");
    fs.writeFileSync("/tmp/output.log", data);
    return JSON.parse(data);
}

// PERFORMANCE: await in loop (js-perf-002)
async function fetchAllUsers(userIds) {
    const users = [];
    for (const id of userIds) {
        const user = await fetch(`/api/users/${id}`);
        users.push(await user.json());
    }
    return users;
}

// NAMING: single-letter variables (js-name-001)
function calculate(a, b, c, d) {
    const x = a * b;
    const y = c + d;
    return x - y;
}

module.exports = {
    processInput, createHandler, renderComment,
    hashData, generateToken, processOrder, calculateDiscount
};