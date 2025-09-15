const googleFormContainer = document.getElementById("googleFormContainer");
const formUrl = googleFormContainer.getAttribute("form-url");
const googleformConsent = document.getElementById("googleformConsent");
const googleFormOriginalContent = googleFormContainer.innerHTML;

function showGoogleForm() {
    const iframe = document.createElement("iframe");
    iframe.setAttribute("src", formUrl);
    iframe.setAttribute("frameborder", "0");
    iframe.setAttribute("marginheight", "0");
    iframe.setAttribute("marginwidth", "0");
    iframe.setAttribute("width", "640");
    iframe.setAttribute("height", "450");
    
    googleFormContainer.innerHTML = "";
    googleFormContainer.appendChild(iframe);
    localStorage.setItem("googleConsent","true");
}

function showGoogleThumbnail() {
    googleFormContainer.innerHTML = googleFormOriginalContent;
    localStorage.removeItem("googleConsent");
}

if (formUrl) {
    const savedGoogleConsent = localStorage.getItem("googleConsent");
    if (savedGoogleConsent === "true") {
	showGoogleForm();
	googleformConsent.checked = true;
    }

    googleformConsent.addEventListener("change", event => {
	if (event.target.checked) {
	    showGoogleForm();
	} else {
	    showGoogleThumbnail();
	}
    })
}
