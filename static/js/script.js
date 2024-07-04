
var loginModal = document.getElementById("login-modal");
var signupModal = document.getElementById("signup-modal");

var loginBtn = document.getElementById("login-button");
var signupBtn = document.getElementById("signup-button");

var closeLogin = document.getElementById("close-login");
var closeSignup = document.getElementById("close-signup");

var openSignup = document.getElementById("open-signup");
var openLogin = document.getElementById("open-login");

var accountProfile = document.getElementById("account-profile");
var logoutBtn = document.getElementById("logout-button");
var accountProfileSection = document.getElementById("account-profile-section");
var logoutBtnProfile = document.getElementById("logout-button-profile");

loginBtn.onclick = function() {
    loginModal.style.display = "flex";
}


signupBtn.onclick = function() {
    signupModal.style.display = "flex";
}


closeLogin.onclick = function() {
    loginModal.style.display = "none";
}


closeSignup.onclick = function() {
    signupModal.style.display = "none";
}

openSignup.onclick = function() {
    loginModal.style.display = "none";
    signupModal.style.display = "flex";
}

openLogin.onclick = function() {
    signupModal.style.display = "none";
    loginModal.style.display = "flex";
}

window.onclick = function(event) {
    if (event.target == loginModal) {
        loginModal.style.display = "none";
    }
    if (event.target == signupModal) {
        signupModal.style.display = "none";
    }
}

function showAccountProfile() {
    loginBtn.style.display = "none";
    signupBtn.style.display = "none";
    accountProfile.style.display = "block";
    logoutBtn.style.display = "block";
    accountProfileSection.style.display = "grid";
}

document.querySelector('#login-modal form').addEventListener('submit', function(event) {
    event.preventDefault();
    loginModal.style.display = "none";
    showAccountProfile();
});

document.querySelector('#signup-modal form').addEventListener('submit', function(event) {
    event.preventDefault();
    signupModal.style.display = "none";
    showAccountProfile();
});

function hideAccountProfile() {
    accountProfile.style.display = "none";
    logoutBtn.style.display = "none";
    loginBtn.style.display = "inline-block";
    signupBtn.style.display = "inline-block";
    accountProfileSection.style.display = "none";
}

logoutBtn.onclick = hideAccountProfile;
logoutBtnProfile.onclick = hideAccountProfile;
