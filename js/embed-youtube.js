const youtubeContainer = document.getElementById("youtubeContainer");
const youtubeVideoId = youtubeContainer.getAttribute("youtube-video-id");
const youtubeLink = youtubeContainer.querySelector("a");
if (youtubeVideoId) {
    youtubeLink.addEventListener("click", event => {
	event.preventDefault();
	const iframe = document.createElement("iframe");
	iframe.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + youtubeVideoId + "?autoplay=1");
	iframe.setAttribute("frameborder", "0");
	iframe.setAttribute("width", "560");
	iframe.setAttribute("height", "315");
	iframe.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen");
	youtubeContainer.innerHTML = "";
	youtubeContainer.appendChild(iframe);
    })
}

