<p>HTTP/2 uses the TCP transport protocol and TLS to secure communications and improves page load times.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13910.md")
</aside>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Availability</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Can customize</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="enable-http-2">Enable HTTP/2</h2>
<p>HTTP/2 is enabled by default for all plans (though it does require an <a href="/ssl/get-started/">SSL certificate at Cloudflare’s edge network</a>).</p>
<h2 id="disable-http-2">Disable HTTP/2</h2>
<p>Domains on Free plans cannot disable Cloudflare's HTTP/2 setting.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/13913.md")
</div></div>
<h2 id="err-http2-protocol-error">ERR_HTTP2_PROTOCOL_ERROR</h2>
<p>Requests proxied by Cloudflare may result in an error for visitors with the error code <code>ERR_HTTP2_PROTOCOL_ERROR</code> visible in the Developer Tools Console. These errors are usually due to an issue on the origin web server configuration, but might only materialize when requests are proxied by Cloudflare depending on the client browser's behavior. Some possible causes are:</p>
<h3 id="malformed-http-response-headers">Malformed HTTP response headers</h3>
<p>The origin web server may be sending improperly formatted HTTP response headers.</p>
<h4 id="resolution">Resolution</h4>
<p>Make a request directly to your origin web server and inspect its HTTP response headers for anomalies. Make sure that the field values respect the following requirements:</p>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9110.html#section-5.5">RFC 9110</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc9113.html#section-8.2.1">RFC 9113</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc5234#appendix-B.1">RFC 5234</a></li>
</ul>
<h3 id="compression-issues">Compression issues</h3>
<p>Examples of compression issues include the origin web server serving gzip encoded compressed content but failing to update the <code>Content-Length</code> header, or the origin web server serving broken gzip compressed content.</p>
<h4 id="resolution-1">Resolution</h4>
<p>You can try to disable compression at your origin web server and rely on Cloudflare to <a href="/speed/optimization/content/compression/">compress content</a>.</p>
<p>You can also review your origin server's compression settings to make sure the compression is working as expected.</p>
