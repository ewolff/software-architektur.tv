const peertubeContainer=document.getElementById("peertubeContainer");
const peertubeConsent = document.getElementById("peertubeConsent");
const peertubeVideoLink = peertubeContainer.getAttribute("peertube-video-link");
if (peertubeVideoLink) {
    peertubeConsent.addEventListener("change", event => {
	event.preventDefault();
	const iframe = document.createElement("iframe");
	iframe.setAttribute("src", peertubeVideoLink+"?autoplay=1");
	iframe.setAttribute("frameborder", "0");
	iframe.setAttribute("width", "560");
	iframe.setAttribute("height", "315");
	iframe.setAttribute("allow", "fullscreen; autoplay");
	iframe.setAttribute("sandbox", "allow-same-origin allow-scripts allow-popups allow-forms");
	peertubeContainer.innerHTML = "";
	peertubeContainer.appendChild(iframe);
    })
}
