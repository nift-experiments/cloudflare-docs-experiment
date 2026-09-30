<div class="video-frame"><img class="video-poster" src="https://imagedelivery.net/xDOJvHcv1KwTQn6S-BGFIw/5183edaa-5d65-4344-adda-37f2cbe69c00/public" alt="ERR_SSL_VERSION_OR_CIPHER_MISMATCH"><iframe src="https://customer-1mwganm1ma0xgnmj.cloudflarestream.com/03e51d8a6f9a15e16969b8cc117d9225/iframe?preload=true&amp;letterboxColor=transparent" title="ERR_SSL_VERSION_OR_CIPHER_MISMATCH" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<p>After you <a href="/fundamentals/manage-domains/add-site/">add a new domain</a> to Cloudflare, your visitors' browsers might display one of the following errors:</p>
<ul>
<li><code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code> (Chrome)</li>
<li><code>Unsupported protocol The client and server don’t support a common SSL protocol version or cipher suite</code> (Chrome)</li>
<li><code>SSL_ERROR_NO_CYPHER_OVERLAP</code> (Firefox)</li>
</ul>
<p>This error occurs when your domain or subdomain is not covered by an SSL/TLS certificate, which is usually caused by:</p>
<ul>
<li>A <a href="#certificate-activation">delay in certificate activation</a>.</li>
<li>An <a href="#proxied-dns-records">unproxied domain or subdomain DNS record</a>.</li>
<li>An <a href="#certificate-expiration">expired Custom certificate</a>.</li>
<li>A <a href="#multi-level-subdomains">multi-level subdomain</a> (<code>test.dev.example.com</code>).</li>
</ul>
<h2 id="decision-tree">Decision tree</h2>
<pre><code class="language-mermaid">flowchart TD&#10;accTitle: Troubleshooting ERR_SSL_VERSION_OR_CIPHER_MISMATCH decision tree&#10;A&gt;Is your certificate active?] -- Yes --&gt; B&gt;Is the DNS record proxied?]&#10;A -- No --&gt; C[Wait for certificate to activate or pause Cloudflare]&#10;B -- No --&gt; D[Proxy the DNS record]&#10;B -- Yes --&gt; E&gt;Are you using a custom certificate?]&#10;E -- Yes --&gt; F[Custom certificate may be expired]&#10;E -- No --&gt; G&gt;Are you accessing a multi-level subdomain?]&#10;G -- Yes --&gt; H[Get an advanced or custom certificate]&#10;</code></pre>
<hr />
<h2 id="certificate-activation">Certificate activation</h2>
<p>For domains on a <a href="/dns/zone-setups/full-setup/">primary setup (full)</a><sup><a href="#footnote-ssl-universal-ssl-enable-full-mdx-1">1</a></sup>, your domain should <strong>automatically</strong> receive its Universal SSL certificate within <strong>15 minutes to 24 hours</strong> of domain activation<sup><a href="#footnote-ssl-universal-ssl-enable-full-mdx-2">2</a></sup>.</p>
<p>This certificate will cover your zone apex (<code>example.com</code>) and all first-level subdomains (<code>subdomain.example.com</code>), and is provisioned even if your records are DNS only. However, the certificate will only be presented if your domain or subdomains are <a href="/dns/proxy-status/">proxied</a>.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-ssl-universal-ssl-enable-full-mdx-1">The most common Cloudflare setup that involves changing your authoritative nameservers.</li>
<li id="footnote-ssl-universal-ssl-enable-full-mdx-2">Provisioning time depends on certain security checks and other requirements mandated by Certificate Authorities (CA).</li></ol></section>
<h3 id="potential-issues">Potential issues</h3>
<p>If your visitors experience <code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code> (Chrome) or <code>SSL_ERROR_NO_CYPHER_OVERLAP</code> (Firefox), check the status of your Universal certificate:</p>
<ol>
<li>Log into the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>.</li>
<li>Choose your account and domain.</li>
<li>Go to the <a href="https://dash.cloudflare.com/?to=/:account/:zone/ssl-tls/edge-certificates"><strong>Edge Certificates</strong></a> page.</li>
<li>Find the certificate with the <strong>Type</strong> of <strong>Universal</strong>.</li>
<li>Make sure the <strong>Status</strong> is <strong>Active</strong>.</li>
</ol>
<p>If the <strong>Status</strong> is anything other than <strong>Active</strong>, you can either wait a bit longer for certificate activation or take immediate action.</p>
<h3 id="solutions">Solutions</h3>
<p>If you need to immediately resolve this error, <a href="/fundamentals/manage-domains/pause-cloudflare/">temporarily pause Cloudflare</a>.</p>
<p>Since Universal certificates can take up to 24 hours to be issued, wait and <a href="/ssl/reference/certificate-statuses/#ssltls">monitor the certificate's status</a>. Once your certificate becomes <strong>Active</strong>, unpause Cloudflare using whichever method you used previously.</p>
<p>If your certificate is still not <strong>Active</strong> after 24 hours, try the various troubleshooting steps used to <a href="/ssl/edge-certificates/universal-ssl/troubleshooting/#resolve-a-timed-out-state">resolve timeout issues</a>. If these methods are successful (and your certificate becomes <strong>Active</strong>), unpause Cloudflare using whichever method you used previously.</p>
<hr />
<h2 id="proxied-dns-records">Proxied DNS records</h2>
<p>Cloudflare Universal and Advanced certificates only cover the domains and subdomains you have <a href="/dns/proxy-status/">proxied through Cloudflare</a>.</p>
<p>If the <strong>Proxy status</strong> of <code>A</code>, <code>AAAA</code>, or <code>CNAME</code> records for a hostname are <strong>DNS-only</strong>, you will need to change it to <strong>Proxied</strong>.</p>
<p><img src="/assets/upstream/images/dns/proxy-status-screenshot.png" alt="Proxy status affects how Cloudflare treats traffic intended for specific DNS records" /></p>
<hr />
<h2 id="certificate-expiration">Certificate expiration</h2>
<p>If you have a <a href="/ssl/edge-certificates/custom-certificates/">Custom certificate</a> and visitors experience <code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code> (Chrome) or <code>SSL_ERROR_NO_CYPHER_OVERLAP</code> (Firefox), <a href="/ssl/reference/certificate-statuses/#ssltls">check its status</a> to make sure it is not expired.</p>
<p>If it is expired, <a href="/ssl/edge-certificates/custom-certificates/renewing/">upload a replacement certificate</a>.</p>
<hr />
<h2 id="multi-level-subdomains">Multi-level subdomains</h2>
<p>By default, Cloudflare <a href="/ssl/edge-certificates/universal-ssl/">Universal SSL certificates</a> only cover your apex domain and one level of subdomain.</p>
<table>
<thead>
<tr>
<th>Hostname</th>
<th>Covered by Universal certificate?</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>www.example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>docs.example.com</code></td>
<td>Yes</td>
</tr>
<tr>
<td><code>dev.docs.example.com</code></td>
<td>No</td>
</tr>
<tr>
<td><code>test.dev.api.example.com</code></td>
<td>No</td>
</tr>
</tbody>
</table>
<p>This means that you might experience <code>ERR_SSL_VERSION_OR_CIPHER_MISMATCH</code> (Chrome) or <code>SSL_ERROR_NO_CYPHER_OVERLAP</code> (Firefox) on multi-level subdomains.</p>
<p>To prevent insecure connections on a multi-level subdomain, do one of the following:</p>
<ul>
<li>Enable <a href="/ssl/edge-certificates/additional-options/total-tls/">Total TLS</a>, which automatically issues individual certificates to your proxied hostnames not covered by a Universal certificate.</li>
<li>Order an <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">Advanced Certificate</a> covering the subdomain.</li>
<li>Upload a <a href="/ssl/edge-certificates/custom-certificates/">Custom Certificate</a> covering the subdomain.</li>
</ul>
<p>If none of these solutions work, you could also remove the multi-level subdomain.</p>
