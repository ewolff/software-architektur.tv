const peertubeContainer = document.getElementById("peertubeContainer");
const peertubeConsent = document.getElementById("peertubeConsent");
const peertubeVideoLink = peertubeContainer.getAttribute("peertube-video-link");
const peertubeOriginalContent = peertubeContainer.innerHTML;

function showPeertubePlayer() {
    const iframe = document.createElement("iframe");
    iframe.setAttribute("src", peertubeVideoLink);
    iframe.setAttribute("frameborder", "0");
    iframe.setAttribute("width", "560");
    iframe.setAttribute("height", "315");
    iframe.setAttribute("allow", "fullscreen; autoplay");
    iframe.setAttribute("sandbox", "allow-same-origin allow-scripts allow-popups allow-forms");
    peertubeContainer.innerHTML = "";
    peertubeContainer.appendChild(iframe);
    localStorage.setItem("peertubeConsent","true");
}

function showPeertubeTHumbnail() {
    peertubeContainer.innerHTML = peertubeOriginalContent;
    localStorage.removeItem("peertubeConsent");
}

if (peertubeVideoLink) {
    const savedPeertubeConsent = localStorage.getItem("peertubeConsent");
    if (savedPeertubeConsent === "true") {
	showPeertubePlayer();
	peertubeConsent.checked = true;
    }
    peertubeConsent.addEventListener("change", event => {
	if (event.target.checked) {
	    showPeertubePlayer();
	} else {
	    showPeertubeTHumbnail()
	}
    })
}
