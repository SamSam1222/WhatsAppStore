document.addEventListener("DOMContentLoaded", function() {
    let video = document.createElement("video");
    video.setAttribute("id", "background-video");
    video.setAttribute("autoplay", "true");
    video.setAttribute("muted", "true");
    video.setAttribute("loop", "true");
    video.innerHTML = `
        <source src="/static/videos/VerifyPro/static/videos/Business Man Walking(1080p).mp4" type="video/mp4">
        Your browser does not support the video tag.
    `;
    document.body.prepend(video);
});
