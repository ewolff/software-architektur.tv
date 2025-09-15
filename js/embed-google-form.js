const googleFormContainer = document.getElementById("googleFormContainer");
const formUrl = googleFormContainer.getAttribute("form-url");
const googleformConsent = document.getElementById("googleformConsent");
const googleFormOriginalContent = googleFormContainer.innerHTML;
if (formUrl) {
    googleformConsent.addEventListener("change", event => {
	if (event.target.checked) {
	    event.preventDefault();
	    const iframe = document.createElement("iframe");
	    iframe.setAttribute("src", formUrl);
	    iframe.setAttribute("frameborder", "0");
	    iframe.setAttribute("marginheight", "0");
	    iframe.setAttribute("marginwidth", "0");
	    iframe.setAttribute("width", "640");
	    iframe.setAttribute("height", "450");

	    googleFormContainer.innerHTML = "";
	    googleFormContainer.appendChild(iframe);
	} else {
	    googleFormContainer.innerHTML = googleFormOriginalContent;
	}
    })
}
