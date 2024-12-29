    document.addEventListener("DOMContentLoaded", function() {
        let video = document.createElement("video");
        video.setAttribute("id", "background-video");
        video.setAttribute("autoplay", "");
        video.setAttribute("muted", "");
        video.setAttribute("loop", "");
        video.innerHTML = `
            <source src="/static/videos/Business Man Walking(1080p).mp4" type="video/mp4">
            Your browser does not support the video tag.
        `;
        document.body.prepend(video);
    });
