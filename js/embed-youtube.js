const container=document.getElementById("youtubeContainer");
const youtubeVideoId = container.getAttribute("youtube-video-id");
const link = container.querySelector("a");
if (youtubeVideoId) {
    link.addEventListener("click", event => {
	event.preventDefault();
	const iframe = document.createElement("iframe");
	iframe.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + youtubeVideoId + "?autoplay=1");
	iframe.setAttribute("frameborder", "0");
	iframe.setAttribute("width", "560");
	iframe.setAttribute("height", "315");
	iframe.setAttribute("allow", "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen");
	container.innerHTML = "";
	container.appendChild(iframe);
    })
}

