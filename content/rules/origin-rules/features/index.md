<p>The following sections describe the available settings in Origin Rules.</p>
<h2 id="host-header">Host header</h2>
<p>Allows you to rewrite the HTTP <code>Host</code> header of incoming requests. The <code>Host</code> header tells the destination server which website or application the request is intended for.</p>
<p>A common use case for this functionality is when your content is hosted on a third-party server that only accepts <code>Host</code> headers with their own server names. In this situation, you must update the <code>Host</code> HTTP header in incoming requests from <code>Host: example.com</code> to <code>Host: thirdpartyserver.example.net</code>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes">Notes</h3>
@markup("md", "content/.markup/bodies/12960.md")
</aside>
<h2 id="server-name-indication-sni">Server Name Indication (SNI)</h2>
<p>Allows you to override the Server Name Indication (SNI) <sup><a href="#footnote-1">1</a></sup> value of a request. For more information, refer to <a href="https://www.cloudflare.com/learning/ssl/what-is-sni/">What is SNI (Server Name Indication)?</a> in the Learning Center.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="notes-1">Notes</h3>
@markup("md", "content/.markup/bodies/12959.md")
</aside>
<h2 id="dns-record">DNS record</h2>
<p>Allows you to override the resolved hostname of incoming requests, which controls which origin server Cloudflare sends the request to. This functionality is also known as resolve override.</p>
<p>A common use case is when you are serving an application from a specific path (for example, <code>mydomain.com/app</code>). In this case, the <code>app</code> may be hosted on a different server or by a third party. A DNS record override allows you to redirect requests to this endpoint to the server for that third-party application.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/12958.md")
</aside>
<p>The following example DNS records configure a <code>resolve.example.com</code> hostname pointing to an external hostname and IP address using a <code>CNAME</code> record and an <code>A</code> record, respectively:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/12961.md")
</div>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/12962.md")
</div>
<h2 id="destination-port">Destination port</h2>
<p>Allows you to override the destination port of a request.</p>
<p>When you configure a destination port override, you can redirect incoming requests to a different port. For example, you could override the destination port for requests received for <code>mydomain.com</code> so that they are served by the application running on port 9000 (<code>mydomain.com:9000</code>).</p>
<p>The destination port must be between 1 and 65,535.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">SNI allows a server to host multiple TLS Certificates for multiple websites using a single IP address. SNI adds the website hostname in the TLS handshake to inform the server which website to present when using shared IPs.</li></ol></section>
