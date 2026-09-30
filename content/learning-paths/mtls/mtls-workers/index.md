<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9828.md")
</aside>
<p><a href="/workers/runtime-apis/bindings/mtls/">mTLS for Workers</a> can be used for requests made to services that are <a href="/dns/proxy-status/#dns-only-records">not proxied</a> on Cloudflare, or alternatively used to gain visibility into certificate details and optionally add your own programmatic logic for further checks or actions.</p>
<h2 id="expose-mtls-headers">Expose mTLS headers</h2>
<p>All Client Certificate details can be found in the <a href="/workers/runtime-apis/request#incomingrequestcfproperties">tlsClientAuth</a> object in Cloudflare Workers. Refer to <a href="/ssl/client-certificates/client-certificate-variables/">Client certificate variables</a> for a full list of available properties.</p>
<p>Example Cloudflare Workers code to return all headers and gain visibility, including <a href="/ssl/client-certificates/forward-a-client-certificate/#cloudflare-workers">Client Certificate headers</a>:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/9831.md")
</div></div>
<p>The response when using the browser with a P12 Certificate to visit the mTLS hostname would look similar to this example:</p>
<p><img src="/assets/upstream/images/learning-paths/mtls/expose-mtls-workers.png" alt="Example response after exposing an mTLS header with Cloudflare Workers" /></p>
<pre><code class="language-txt">{&#10;  &quot;X-CERT-ISSUER-DN&quot;: &quot;CN=Managed CA abcdefghijklmnopq123456789,OU=www.cloudflare.com,O=Cloudflare\\, Inc.,L=San Francisco,ST=California,C=US&quot;,&#10;  &quot;X-CERT-SUBJECT-DN&quot;: &quot;CN=Cloudflare,C=US&quot;,&#10;  &quot;X-CERT-ISSUER-DN-L&quot;: &quot;/C=US/ST=California/L=San Francisco/O=Cloudflare, Inc./OU=www.cloudflare.com/CN=Managed CA abcdefghijklmnopq123456789&quot;,&#10;  &quot;X-CERT-SUBJECT-DN-L&quot;: &quot;/C=US/CN=Cloudflare&quot;,&#10;  &quot;X-CERT-SERIAL&quot;: &quot;37C52778E2F1820CC6342172A0E0ED33A4555F8B&quot;,&#10;  &quot;X-CERT-FINGER&quot;: &quot;161e3a2089add0b2134ec43c9071f460e9f4b898&quot;,&#10;  &quot;X-CERT-NOTBE&quot;: &quot;May 25 23:11:00 2024 GMT&quot;,&#10;  &quot;X-CERT-NOTAF&quot;: &quot;May 23 23:11:00 2034 GMT&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9826.md")
</aside>
<p>This approach can also be useful to handle additional checks and logic on the mTLS via the Cloudflare Workers.</p>
