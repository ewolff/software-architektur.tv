const youtubeContainer = document.getElementById("youtubeContainer");
const youtubeVideoId = youtubeContainer.getAttribute("youtube-video-id");
const youtubeConsent = document.getElementById("youtubeConsent");
const youtubeOriginalContent = youtubeContainer.innerHTML;

function showYoutubePlayer() {
    const iframe = document.createElement("iframe");
    iframe.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + youtubeVideoId );
    iframe.setAttribute("frameborder", "0");
    iframe.setAttribute("width", "560");
    iframe.setAttribute("height", "315");
    iframe.setAttribute("allow", "accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen");
    youtubeContainer.innerHTML = "";
    youtubeContainer.appendChild(iframe);
    localStorage.setItem("youtubeConsent","true");
}

function showYoutubeThumbnail() {
    youtubeContainer.innerHTML = youtubeOriginalContent;
    localStorage.removeItem("youtubeConsent");
}

if (youtubeVideoId) {
    const savedYoutubeConsent = localStorage.getItem("youtubeConsent");
    if (savedYoutubeConsent === "true") {
	showYoutubePlayer();
	youtubeConsent.checked = true;
    }
    youtubeConsent.addEventListener("change", event => {
	if (event.target.checked) {
	    showYoutubePlayer();
	} else {
	    showYoutubeThumbnail();
	}
    })
}
