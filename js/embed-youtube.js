const youtubeContainer = document.getElementById("youtubeContainer");
const youtubeVideoId = youtubeContainer.getAttribute("youtube-video-id");
const youtubeConsent = document.getElementById("youtubeConsent");
const youtubeOriginalContent = youtubeContainer.innerHTML;
if (youtubeVideoId) {
    youtubeConsent.addEventListener("change", event => {
	if (event.target.checked) {
	    const iframe = document.createElement("iframe");
	    iframe.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + youtubeVideoId + "?autoplay=1");
	    iframe.setAttribute("frameborder", "0");
	    iframe.setAttribute("width", "560");
	    iframe.setAttribute("height", "315");
	    iframe.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen");
	    youtubeContainer.innerHTML = "";
	    youtubeContainer.appendChild(iframe);
	} else {
	    youtubeContainer.innerHTML = youtubeOriginalContent;
	}
    })
}
