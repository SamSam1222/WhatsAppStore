// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    // Check if we are on the login page
    const loginContainer = document.querySelector(".login-box");

    if (loginContainer) {
        // Inject the video into the body
        const video = document.createElement("video");
        video.autoplay = true;
        video.muted = true;
        video.loop = true;
        video.id = "background-video";

        // Add the video source
        const source = document.createElement("source");
        source.src = "/static/videos/People Working in Office - Busy Day - Royalty Free Stock Video.mp4"; // Adjust path if needed
        source.type = "video/mp4";

        // Append the source to the video
        video.appendChild(source);

        // Style the video
        video.style.position = "fixed";
        video.style.top = "0";
        video.style.left = "0";
        video.style.width = "100vw";
        video.style.height = "100vh";
        video.style.objectFit = "cover";
        video.style.zIndex = "-1";

        // Inject the video into the body
        document.body.prepend(video);
    }
});



// This script is for the login Form of the Django Jazzmin
// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function() {
    // Target the login form card body
    const loginCard = document.querySelector(".card-body, .auth-card, .login-box .card");

    if (loginCard) {
        // Apply styles dynamically
        loginCard.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
        loginCard.style.color = "#ffffff";
        loginCard.style.borderRadius = "10px";
        loginCard.style.padding = "20px";
        loginCard.style.border = "none";
    }

    // Target input fields
    const inputs = document.querySelectorAll(".card-body input.form-control, .auth-card input");
    inputs.forEach(input => {
        input.style.backgroundColor = "rgba(255, 255, 255, 0.9)";
        input.style.color = "#000";
        input.style.border = "1px solid #ccc";
        input.style.padding = "10px";
    });

    // Target the submit button
    const submitButton = document.querySelector(".card-body button, .auth-card button");
    if (submitButton) {
        submitButton.style.backgroundColor = "#007bff";
        submitButton.style.color = "#fff";
        submitButton.style.fontWeight = "bold";
        submitButton.style.borderRadius = "5px";
        submitButton.style.padding = "10px";
        submitButton.style.border = "none";
        submitButton.addEventListener("mouseover", () => {
            submitButton.style.backgroundColor = "#0056b3";
        });
        submitButton.addEventListener("mouseout", () => {
            submitButton.style.backgroundColor = "#007bff";
        });
    }
});
