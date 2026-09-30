<h2 id="error-501-not-implemented">Error 501: not implemented</h2>
<p>Cloudflare Workers returns a <code>501</code> error when a request uses an HTTP method that is not supported by the Workers Runtime.</p>
<h3 id="common-causes">Common causes</h3>
<ul>
<li>A client sent a request to a Workers script using a custom or non-standard HTTP method (methods outside of <code>GET</code>, <code>POST</code>, <code>PUT</code>, etc.).</li>
<li>A typo in the HTTP method (for example, <code>POT</code> instead of <code>POST</code>).</li>
</ul>
<h3 id="resolution">Resolution</h3>
<ul>
<li>Update the client to use a valid, standard <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods">HTTP request method</a>.</li>
</ul>
