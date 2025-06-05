document.addEventListener("DOMContentLoaded", async () => {
   const output = document.getElementById("callbackOutput");
   const params = new URLSearchParams(window.location.search);
   const sessionId = params.get("session_id");
   if (!sessionId) {
       output.textContent = "Missing session_id in URL.";
       return;
   }
   output.textContent = "Checking verification result...";
   try {
       const response = await fetch(`/api/verifier/presentation-session-status/${encodeURIComponent(sessionId)}`);
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