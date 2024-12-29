







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
        source.src = "/static/videos/"; // Adjust path if needed
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
