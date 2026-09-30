<h2 id="error-1013-http-hostname-and-tls-sni-hostname-mismatch">Error 1013: HTTP hostname and TLS SNI hostname mismatch</h2>
<p>This error indicates a mismatch between the HTTP hostname and the TLS SNI hostname.</p>
<h3 id="common-cause">Common cause</h3>
<p>The hostname sent by the client or browser via <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14737.md")
</div> does not match the request host header.
<h3 id="resolution">Resolution</h3>
<p>Error <code>1013</code> is commonly caused by the following:</p>
<ul>
<li>Your local browser setting the incorrect SNI host header, or</li>
<li>A network proxying SSL traffic caused a mismatch between SNI and the Host header of the request.</li>
</ul>
<p>Test for an SNI mismatch via an online tool, such as <a href="https://www.sslshopper.com/ssl-checker.html">SSL Shopper</a>.</p>
<p>Provide Cloudflare Support the following information:</p>
<ul>
<li>A <a href="/support/troubleshooting/general-troubleshooting/gathering-information-for-troubleshooting-sites/">HAR file</a> captured while duplicating the error.</li>
</ul>
