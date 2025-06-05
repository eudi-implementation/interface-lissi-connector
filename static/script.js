document.getElementById("checkStatus").addEventListener("click", async () => {
    const output = document.getElementById("output");
    output.textContent = "Loading credential templates...";
    try {
        const response = await fetch("/api/credential-templates");
        const data = await response.json();
        output.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
});

document.getElementById("issueCredentialHoeger").addEventListener("click", async () => {
    const output = document.getElementById("output");
    output.textContent = "Creating credential offer for Hoeger, Hollis...";
    // Remove any previous QR code
    const oldQr = document.getElementById("qrcode");
    if (oldQr) oldQr.remove();
    try {
        const response = await fetch("/api/issue-credential-hoeger", { method: "POST" });
        const data = await response.json();
        if (data.credentialOfferDetails && data.credentialOfferDetails.credentialOfferUri) {
            // Create a wrapper div for centering
            const wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.flexDirection = "column";
            wrapper.style.alignItems = "center";
            wrapper.style.justifyContent = "center";
            wrapper.style.marginTop = "1em";

            // Shorter, wrapped label
            const label = document.createElement("div");
            label.textContent = "Scan to accept credential offer:";
            label.style.textAlign = "center";
            label.style.marginBottom = "0.5em";
            wrapper.appendChild(label);

            // QR code
            const qrDiv = document.createElement("div");
            qrDiv.id = "qrcode";
            wrapper.appendChild(qrDiv);
            new QRCode(qrDiv, {
                text: data.credentialOfferDetails.credentialOfferUri,
                width: 256,
                height: 256
            });
            output.textContent = "";
            output.appendChild(wrapper);
        } else {
            output.textContent = "Error: Could not get credentialOfferUri.\n" + JSON.stringify(data, null, 2);
        }
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
});

document.getElementById("issueCredentialCastaneda").addEventListener("click", async () => {
    const output = document.getElementById("output");
    output.textContent = "Creating credential offer for Castaneda, Carlos...";
    // Remove any previous QR code
    const oldQr = document.getElementById("qrcode");
    if (oldQr) oldQr.remove();
    try {
        const response = await fetch("/api/issue-credential-castaneda", { method: "POST" });
        const data = await response.json();
        if (data.credentialOfferDetails && data.credentialOfferDetails.credentialOfferUri) {
            // Create a wrapper div for centering
            const wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.flexDirection = "column";
            wrapper.style.alignItems = "center";
            wrapper.style.justifyContent = "center";
            wrapper.style.marginTop = "1em";

            // Shorter, wrapped label
            const label = document.createElement("div");
            label.textContent = "Scan to accept credential offer:";
            label.style.textAlign = "center";
            label.style.marginBottom = "0.5em";
            wrapper.appendChild(label);

            // QR code
            const qrDiv = document.createElement("div");
            qrDiv.id = "qrcode";
            wrapper.appendChild(qrDiv);
            new QRCode(qrDiv, {
                text: data.credentialOfferDetails.credentialOfferUri,
                width: 256,
                height: 256
            });
            output.textContent = "";
            output.appendChild(wrapper);
        } else {
            output.textContent = "Error: Could not get credentialOfferUri.\n" + JSON.stringify(data, null, 2);
        }
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
});

document.getElementById("issueCredentialGM").addEventListener("click", async () => {
    const output = document.getElementById("output");
    output.textContent = "Creating credential offer for Goepper Mayer, Maria...";
    // Remove any previous QR code
    const oldQr = document.getElementById("qrcode");
    if (oldQr) oldQr.remove();
    try {
        const response = await fetch("/api/issue-credential-gm", { method: "POST" });
        const data = await response.json();
        if (data.credentialOfferDetails && data.credentialOfferDetails.credentialOfferUri) {
            // Create a wrapper div for centering
            const wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.flexDirection = "column";
            wrapper.style.alignItems = "center";
            wrapper.style.justifyContent = "center";
            wrapper.style.marginTop = "1em";

            // Shorter, wrapped label
            const label = document.createElement("div");
            label.textContent = "Scan to accept credential offer:";
            label.style.textAlign = "center";
            label.style.marginBottom = "0.5em";
            wrapper.appendChild(label);

            // QR code
            const qrDiv = document.createElement("div");
            qrDiv.id = "qrcode";
            wrapper.appendChild(qrDiv);
            new QRCode(qrDiv, {
                text: data.credentialOfferDetails.credentialOfferUri,
                width: 256,
                height: 256
            });
            output.textContent = "";
            output.appendChild(wrapper);
        } else {
            output.textContent = "Error: Could not get credentialOfferUri.\n" + JSON.stringify(data, null, 2);
        }
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
});

document.getElementById("issueCredentialLM").addEventListener("click", async () => {
    const output = document.getElementById("output");
    output.textContent = "Creating credential offer for Goepper Meitner, Lise...";
    // Remove any previous QR code
    const oldQr = document.getElementById("qrcode");
    if (oldQr) oldQr.remove();
    try {
        const response = await fetch("/api/issue-credential-lm", { method: "POST" });
        const data = await response.json();
        if (data.credentialOfferDetails && data.credentialOfferDetails.credentialOfferUri) {
            // Create a wrapper div for centering
            const wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.flexDirection = "column";
            wrapper.style.alignItems = "center";
            wrapper.style.justifyContent = "center";
            wrapper.style.marginTop = "1em";

            // Shorter, wrapped label
            const label = document.createElement("div");
            label.textContent = "Scan to accept credential offer:";
            label.style.textAlign = "center";
            label.style.marginBottom = "0.5em";
            wrapper.appendChild(label);

            // QR code
            const qrDiv = document.createElement("div");
            qrDiv.id = "qrcode";
            wrapper.appendChild(qrDiv);
            new QRCode(qrDiv, {
                text: data.credentialOfferDetails.credentialOfferUri,
                width: 256,
                height: 256
            });
            output.textContent = "";
            output.appendChild(wrapper);
        } else {
            output.textContent = "Error: Could not get credentialOfferUri.\n" + JSON.stringify(data, null, 2);
        }
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
});

const addHardcodedDocumentBtn = document.getElementById("addHardcodedDocument");
if (addHardcodedDocumentBtn) {
    addHardcodedDocumentBtn.addEventListener("click", async () => {
        const output = document.getElementById("output");
        output.textContent = "Adding Hardcoded Document to Datastore...";
        try {
            const response = await fetch("api/add-hardcoded-document", {method: "POST"});
            const data = await response.json();
            output.textContent = data.success ? "Added Hardcoded Document." : (data.error || "unknwon error");
        } catch (err) {
            output.textContent = "Error: " + err.message;
        }
    });
}

const collectIdInputEHIC = document.getElementById("collectIdInputEHIC");
const issueEHICBtn = document.getElementById("issueEHIC");
if (collectIdInputEHIC && issueEHICBtn) {
    collectIdInputEHIC.addEventListener("input", () => {
        issueEHICBtn.disabled = !collectIdInputEHIC.value.trim();
    });
}

issueEHICBtn.addEventListener("click", async () => {
    const output = document.getElementById("output");
    const collectId = collectIdInputEHIC.value.trim();
    if (!collectId) {
        output.textContent = "Collect ID is required.";
        return;
    }
    output.textContent = "Creating EHIC credential offer...";
    // Remove any previous QR code
    const oldQr = document.getElementById("qrcode");
    if (oldQr) oldQr.remove();
    try {
        const response = await fetch("api/issue-ehic", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ collectId: collectId })
        });
        const data = await response.json();
        if (data.credentialOfferDetails && data.credentialOfferDetails.credentialOfferUri) {
            // Create a wrapper div for centering
            const wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.flexDirection = "column";
            wrapper.style.alignItems = "center";
            wrapper.style.justifyContent = "center";
            wrapper.style.marginTop = "1em";

            // Shorter, wrapped label
            const label = document.createElement("div");
            label.textContent = "Scan to accept EHIC offer:";
            label.style.textAlign = "center";
            label.style.marginBottom = "0.5em";
            wrapper.appendChild(label);

            // QR code
            const qrDiv = document.createElement("div");
            qrDiv.id = "qrcode";
            wrapper.appendChild(qrDiv);
            new QRCode(qrDiv, {
                text: data.credentialOfferDetails.credentialOfferUri,
                width: 256,
                height: 256
            });
            output.textContent = "";
            output.appendChild(wrapper);
        } else {
            output.textContent = "Error: Could not get credentialOfferUri.\n" + JSON.stringify(data, null, 2);
        }
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
});


const collectIdInputPDA1 = document.getElementById("collectIdInputPDA1");
const issuePDA1Btn = document.getElementById("issuePDA1");
if (collectIdInputPDA1 && issuePDA1Btn) {
    collectIdInputPDA1.addEventListener("input", () => {
        issuePDA1Btn.disabled = !collectIdInputPDA1.value.trim();
    });
}

issuePDA1Btn.addEventListener("click", async () => {
    const output = document.getElementById("output");
    const collectId = collectIdInputPDA1.value.trim();
    if (!collectId) {
        output.textContent = "Collect ID is required.";
        return;
    }
    output.textContent = "Creating PDA1 credential offer...";
    // Remove any previous QR code
    const oldQr = document.getElementById("qrcode");
    if (oldQr) oldQr.remove();
    try {
        const response = await fetch("api/issue-pda1", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ collectId: collectId })
        });
        const data = await response.json();
        if (data.credentialOfferDetails && data.credentialOfferDetails.credentialOfferUri) {
            // Create a wrapper div for centering
            const wrapper = document.createElement("div");
            wrapper.style.display = "flex";
            wrapper.style.flexDirection = "column";
            wrapper.style.alignItems = "center";
            wrapper.style.justifyContent = "center";
            wrapper.style.marginTop = "1em";

            // Shorter, wrapped label
            const label = document.createElement("div");
            label.textContent = "Scan to accept PDA1 offer:";
            label.style.textAlign = "center";
            label.style.marginBottom = "0.5em";
            wrapper.appendChild(label);

            // QR code
            const qrDiv = document.createElement("div");
            qrDiv.id = "qrcode";
            wrapper.appendChild(qrDiv);
            new QRCode(qrDiv, {
                text: data.credentialOfferDetails.credentialOfferUri,
                width: 256,
                height: 256
            });
            output.textContent = "";
            output.appendChild(wrapper);
        } else {
            output.textContent = "Error: Could not get credentialOfferUri.\n" + JSON.stringify(data, null, 2);
        }
    } catch (err) {
        output.textContent = "Error: " + err.message;
    }
});

const clearSessionMapBtn = document.getElementById("clearSessionMap");
if (clearSessionMapBtn) {
    clearSessionMapBtn.addEventListener("click", async () => {
        const output = document.getElementById("output");
        output.textContent = "Clearing Session -> Collect ID Map...";
        try {
            const response = await fetch("api/clear-session-map", {method: "POST"});
            const data = await response.json();
            output.textContent = data.success ? "Session -> Collect ID Map cleared!" : (data.error || "unknwon error");
        } catch (err) {
            output.textContent = "Error: " + err.message;
        }
    });
}

const viewSessionMapBtn = document.getElementById("viewSessionMap");
if (viewSessionMapBtn) {
    viewSessionMapBtn.addEventListener("click", async () => {
        const output = document.getElementById("output");
        output.textContent = "Loading Session -> Collect ID Map...";
        try {
            const response = await fetch("api/view-session-map");
            const data = await response.json();
            if (data && typeof data === 'object') {
                output.textContent = JSON.stringify(data, null, 2);
            } else {
                output.textContent = "No map found or error.";
            }
        } catch (err) {
            output.textContent = "Error: " + err.message;
        }
    });
}