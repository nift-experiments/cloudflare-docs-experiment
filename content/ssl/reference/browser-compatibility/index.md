<p>Cloudflare attempts to provide compatibility for as wide a range of user agents (browsers, API clients, etc.) as possible. However, the specific set of supported clients can vary depending on the different SSL/TLS certificate types, your visitor's <a href="#non-sni-support">browser version</a>, and the <a href="/ssl/reference/certificate-authorities/">certificate authority (CA)</a> that issues the certificate.</p>
<h2 id="universal-ssl">Universal SSL</h2>
<p>Cloudflare Universal SSL only supports browsers and API clients that use the <a href="https://www.cloudflare.com/learning/ssl/what-is-sni/">Server Name Indication (SNI)</a> extension to the TLS protocol.</p>
<p>Also, for zones on Free plan, Universal SSL is only compatible with browsers that support Elliptic Curve Digital Signature Algorithm (ECDSA).</p>
<p>Paid plans have additional compatibility, also supporting RSA algorithm.</p>
<h2 id="other-certificate-types">Other certificate types</h2>
<p>Refer to <a href="/ssl/reference/certificate-authorities/">Certificate authorities</a> for a detailed list of Cloudflare SSL/TLS offerings, the different algorithms available, and browser compatibility for each CA.</p>
<h2 id="non-sni-support">Non-SNI support</h2>
<p>Although <a href="https://www.cloudflare.com/learning/ssl/what-is-sni/">SNI extensions</a> to the TLS protocol were standardized in 2003, some browsers and operating systems only implemented this extension when TLS 1.1 was released in 2006 (or 2011 for mobile browsers). If your visitors use devices that have not been updated since 2011, they may not have SNI support.</p>
<p>To support non-SNI requests, you can:</p>
<ul>
<li>
<p><a href="/ssl/edge-certificates/custom-certificates/uploading/#upload-a-custom-certificate">Upload a custom certificate</a> and specify a value of <code>Legacy</code> for its client support.</p>
<p>Note that <code>Legacy</code> custom certificates are not compatible with <a href="/byoip/">BYOIP</a> and that, unlike <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a> or <a href="/ssl/edge-certificates/advanced-certificate-manager/">advanced certificates</a>, Cloudflare does not manage issuance and renewal for <a href="/ssl/edge-certificates/custom-certificates/">custom certificates</a>.</p>
</li>
<li>
<p>(BYOIP customers only) Enterprise customers can choose to bring their own IP prefix to the Cloudflare network and <a href="/byoip/address-maps/setup/#non-sni-support">specify the default SNI used for any non-SNI handshake in the address map</a>.</p>
</li>
<li>
<p>(Paid plans only) <a href="/support/contacting-cloudflare-support/">Contact Cloudflare Support</a> and request a set of non-SNI IPs for your zone.</p>
</li>
</ul>
<h2 id="https-records">HTTPS records</h2>
<p><a href="/dns/manage-dns-records/reference/dns-record-types/#svcb-and-https">HTTPS Service (HTTPS) records</a> allow you to provide a client with information about how it should connect to a server upfront, without the need of an initial plaintext HTTP connection.</p>
<p>If your domain has <a href="/speed/optimization/protocol/">HTTP/2 or HTTP/3 enabled</a>, <a href="/dns/proxy-status/">proxied DNS records</a>, and is also using <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL</a>, Cloudflare automatically generates HTTPS records on the fly, to advertise to clients how they should connect to your server.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="universal-ssl-required-for-automatic-https-records">Universal SSL required for automatic HTTPS records</h3>
@markup("md", "content/.markup/bodies/13987.md")
</aside>
<h2 id="ocsp-and-http-versions">OCSP and HTTP versions</h2>
<p>Cloudflare's OCSP implementation uses HTTP/1.1 by default for plain HTTP connections.</p>
<p>For HTTPS connections, the client automatically attempts to use HTTP/2 if the server supports it through the TLS ALPN (Application-Layer Protocol Negotiation) extension. If HTTP/2 is not available or supported by the server, it will fall back to HTTP/1.1.</p>
