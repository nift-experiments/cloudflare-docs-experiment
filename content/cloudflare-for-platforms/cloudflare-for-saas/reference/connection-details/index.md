<p>When forwarding connections to your origin server, Cloudflare will set request parameters according to the following:</p>
<h2 id="host-header">Host header</h2>
<p>Cloudflare will not alter the Host header by default, and will forward exactly as sent by the client. If you wish to change the value of the Host header you can utilise <a href="/workers/configuration/workers-with-page-rules/">Page-Rules</a> or <a href="/workers/">Workers</a> using the steps outlined in <a href="/cloudflare-for-platforms/cloudflare-for-saas/security/certificate-management/">certificate management</a>.</p>
<h2 id="sni">SNI</h2>
<p>When establishing a TLS connection to your origin server, if the request is being sent to your configured Fallback Host then the value of the SNI sent by Cloudflare will match the value of the Host header sent by the client (i.e. the custom hostname).</p>
<p>If however the request is being forwarded to a Custom Origin, then the value of the SNI will be that of the Custom Origin.</p>
