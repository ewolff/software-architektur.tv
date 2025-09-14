document.querySelectorAll(".embed-container").forEach(container => {
  const link = container.querySelector("a");
  const peertubeVideoLink = container.getAttribute("peertube-video-link");
  if (peertubeVideoLink) {
    link.addEventListener("click", event => {
      event.preventDefault();
      const iframe = document.createElement("iframe");
      iframe.setAttribute("src", peertubeVideoLink+"?autoplay=1");
      iframe.setAttribute("frameborder", "0");
      iframe.setAttribute("width", "560");
      iframe.setAttribute("height", "315");
	iframe.setAttribute("allow", "fullscreen; autoplay");
      iframe.setAttribute("sandbox", "allow-same-origin allow-scripts allow-popups allow-forms");
      container.innerHTML = "";
      container.appendChild(iframe);
    })
  }
});
