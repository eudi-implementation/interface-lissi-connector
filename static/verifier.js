let lastPresentationSessionId = null;

async function createPresentationSession(cred_type) {
    const output = document.getElementById("output");
    output.textContent = "Creating verification session...";
    const oldQr = document.getElementById("qrcode");
    if (oldQr) oldQr.remove();
    let cred_url = "/api/verifier/"
    try {
        if (cred_type === "PID") {
            cred_url = cred_url + "pid-presentation-session";
        } else if (cred_type === "EHIC") {
            cred_url = cred_url + "ehic-presentation-session";
        } else if (cred_type === "PDA1") {
            cred_url = cred_url + "pda1-presentation-session";
        } else {
            cred_url = cred_url + "";
        }
        const response = await fetch(cred_url, { method: "POST" });
        const data = await response.json();
        if (data.presentationSessionId) {
            lastPresentationSessionId = data.presentationSessionId;
        }
        if (data.presentationRequestUri) {
            // Create a wrapper div for centering
            const wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.flexDirection = "column";
            wrapper.style.alignItems = "center";
            wrapper.style.justifyContent = "center";
            wrapper.style.marginTop = "1em";

            // Shorter, wrapped label
            const label = document.createElement("div");
            label.textContent = `Scan to present ${cred_type}:`;
            label.style.textAlign = "center";
            label.style.marginBottom = "0.5em";
            wrapper.appendChild(label);

            // QR code
            const qrDiv = document.createElement("div");
            qrDiv.id = "qrcode";
            wrapper.appendChild(qrDiv);
            new QRCode(qrDiv, {
                text: data.presentationRequestUri,
                width: 256,
                height: 256
            });
            output.textContent = "";
            output.appendChild(wrapper);
        } else {
            output.textContent = "Error: Could not get presentationRequestUri.\n" + JSON.stringify(data, null, 2);
        }
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
}

async function createPIDPresentationSession() {
    return createPresentationSession("PID")
}

async function createEHICPresentationSession() {
    return createPresentationSession("EHIC")
}

async function createPDA1PresentationSession() {
    return createPresentationSession("PDA1")
}

document.getElementById("verifyPID").addEventListener("click", createPIDPresentationSession);
document.getElementById("verifyEHIC").addEventListener("click", createEHICPresentationSession);
document.getElementById("verifyPDA1").addEventListener("click", createPDA1PresentationSession);

document.getElementById("checkPresentationResult").addEventListener("click", async () => {
   const output = document.getElementById("output");
   if (!lastPresentationSessionId) {
       output.textContent = "No verification started.";
       return;
   }
   output.textContent = "Checking verification result...";
   try {
       const response = await fetch(`/api/verifier/presentation-session-status/${encodeURIComponent(lastPresentationSessionId)}`);
       const data = await response.json();
       if (data.state === "COMPLETE") {
           let claims = "";
           if (data.presentedCredentials && data.presentedCredentials.length > 0) {
               claims = data.presentedCredentials.map(cred => {
                   if (cred.presentedClaims) {
                       return cred.presentedClaims.map(claim => `${claim.claimName}: ${claim.claimValue}`).join("\n");
                   }
                   return "";
               }).join("\n---\n");
           }
           output.textContent = `Verification successful!\n\nClaims:\n${claims}`;
       } else if (data.state === "FAILED") {
           output.textContent = `Verification failed: ${data.failureReason && data.failureReason.message ? data.failureReason.message : "Unknwon reason"}`;
       } else {
           output.textContent = `Session state: ${data.state || "Unknown"}`;
       }
   } catch (err) {
       output.textContent = "Error: " + err.message;
   }
});