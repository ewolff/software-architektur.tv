// Highlights share the consent key of the main PeerTube embed ("peertubeConsent").
const highlightsConsent = document.getElementById("highlightsConsent");
const highlightContainers = Array.from(document.querySelectorAll(".highlight-container"));
const highlightOriginalContent = highlightContainers.map(container => container.innerHTML);

function showHighlightPlayers() {
    highlightContainers.forEach(container => {
	const iframe = document.createElement("iframe");
	iframe.setAttribute("src", container.getAttribute("data-peertube-video-link"));
	iframe.setAttribute("title", container.getAttribute("data-title"));
	iframe.setAttribute("frameborder", "0");
	iframe.setAttribute("allow", "fullscreen; autoplay");
	iframe.setAttribute("sandbox", "allow-same-origin allow-scripts allow-popups allow-forms");
	container.innerHTML = "";
	container.appendChild(iframe);
    });
    localStorage.setItem("peertubeConsent", "true");
}

function showHighlightThumbnails() {
    highlightContainers.forEach((container, i) => {
	container.innerHTML = highlightOriginalContent[i];
    });
    localStorage.removeItem("peertubeConsent");
}

if (highlightsConsent && highlightContainers.length > 0) {
    if (localStorage.getItem("peertubeConsent") === "true") {
	showHighlightPlayers();
	highlightsConsent.checked = true;
    }
    highlightsConsent.addEventListener("change", event => {
	if (event.target.checked) {
	    showHighlightPlayers();
	} else {
	    showHighlightThumbnails();
	}
    });
}
