(function () {

    if (window.__youtubeEmbedInitialized__) return;
    window.__youtubeEmbedInitialized__ = true;

    const youtubeContainers = document.querySelectorAll(".youtube-container");
    const youtubeConsents = document.querySelectorAll(".youtube-consent");
    const youtubeOriginalContent = new Map();

    function showYoutubePlayer() {
	youtubeContainers.forEach(youtubeContainer => {
	    const iframe = document.createElement("iframe");
	    const youtubeVideoId = youtubeContainer.getAttribute("youtube-video-id");
	    iframe.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + youtubeVideoId );
	    iframe.setAttribute("frameborder", "0");
	    iframe.setAttribute("width", "560");
	    iframe.setAttribute("height", "315");
	    iframe.setAttribute("allow", "accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen");
	    if (!youtubeOriginalContent.has(youtubeContainer)) {
		youtubeOriginalContent.set(youtubeContainer, youtubeContainer.innerHTML);
	    }
	    youtubeContainer.innerHTML = ""; 
	    youtubeContainer.appendChild(iframe);
	})
	youtubeConsents.forEach(youtubeConsent => {
	    youtubeConsent.checked = true;
	})
	localStorage.setItem("youtubeConsent","true");
    }
    
    function showYoutubeThumbnail() {
	youtubeContainers.forEach(youtubeContainer => {
	    youtubeContainer.innerHTML = youtubeOriginalContent.get(youtubeContainer);
	})
	youtubeConsents.forEach(youtubeConsent => {
	    youtubeConsent.checked = false;
	})
	localStorage.removeItem("youtubeConsent");
    }

    const savedYoutubeConsent = localStorage.getItem("youtubeConsent");
    if (savedYoutubeConsent === "true") {
	showYoutubePlayer();
    }
    youtubeConsents.forEach(youtubeConsent => {
	youtubeConsent.addEventListener("change", event => {
	    if (event.target.checked) {
		showYoutubePlayer();
	    } else {
		showYoutubeThumbnail();
	    }
	})
    })

})();
