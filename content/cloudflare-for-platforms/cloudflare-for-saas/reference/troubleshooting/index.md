<h2 id="rate-limits">Rate limits</h2>
<p>By default, you may issue up to 15 certificates per minute. Only successful submissions (POSTs that return 200) are counted towards your limit. If you exceed your limit, you will be prevented from issuing new certificates for 30 seconds.</p>
<p>If you require a higher rate limit, contact your account team.</p>
<hr />
<h2 id="purge-cache">Purge cache</h2>
<p>To remove specific files from Cloudflare’s cache, <a href="/cache/how-to/purge-cache/purge-by-hostname/">purge the cache</a> while specifying one or more hostnames.</p>
<hr />
<h2 id="resolution-error-1016-origin-dns-error-when-accessing-the-custom-hostname">Resolution error 1016 (Origin DNS error) when accessing the custom hostname</h2>
<p>Cloudflare returns a 1016 error when the custom hostname cannot be routed or proxied.</p>
<p>There are three main causes of error 1016:</p>
<ol>
<li>Custom Hostname ownership validation is not complete. To check validation status, run an API call to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/common-api-calls/">search for a certificate by hostname</a> and check the verification error field: <code>&quot;verification_errors&quot;: [&quot;custom hostname does not CNAME to this zone.&quot;]</code>.</li>
<li>Fallback Origin is not <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin">correctly set</a>. Confirm that you have created a DNS record for the fallback origin and also set the fallback origin.</li>
<li>A Wildcard Custom Hostname has been created, but the requested hostname is associated with a domain that exists in Cloudflare as a standalone zone. In this case, the <a href="/ssl/reference/certificate-and-hostname-priority/#hostname-priority">hostname priority</a> for the standalone zone will take precedence over the wildcard custom hostname. This behavior applies even if there is no DNS record for this standalone zone hostname.</li>
</ol>
<p>In this scenario each hostname that needs to be served by the <a href="/cloudflare-for-platforms/cloudflare-for-saas/">Cloudflare for SaaS</a> parent zone needs to be added as an individual Custom Hostname.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4093.md")
</aside>
<hr />
<h2 id="old-saas-provider-content-after-updating-a-cname">Old SaaS provider content after updating a CNAME</h2>
<p>When switching SaaS providers, an older configuration can take precedence if the old provider provisioned a specific custom hostname and the new provider provisioned a wildcard custom hostname. This is expected as per the <a href="/ssl/reference/certificate-and-hostname-priority/#hostname-priority">certificate and hostname priority</a>.</p>
<p>In this case there are two ways forward:</p>
<ul>
<li>(Recommended) Ask the new SaaS provider to provision a specific custom hostname for you instead of the wildcard - <code>mystore.example.com</code> instead of <code>*.example.com</code>.</li>
<li>Ask the Super Administrator of your account to contact <a href="/support/contacting-cloudflare-support/">Cloudflare Support</a> to request an update of the SaaS configuration.</li>
</ul>
<hr />
<h2 id="custom-hostname-in-moved-status">Custom hostname in Moved status</h2>
<p>To move a custom hostname back to an Active status, send a <a href="/api/resources/custom_hostnames/methods/edit/">PATCH request</a> to restart the hostname validation. A Custom Hostname in a Moved status is deleted after 7 days.</p>
<p>In some circumstances, custom hostnames can also enter a <strong>Moved</strong> state if your customer changes their DNS records pointing to your SaaS service. For more details, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/remove-custom-hostnames/">Remove custom hostnames</a>.</p>
<hr />
<h2 id="caa-errors">CAA Errors</h2>
<p>The <code>caa_error</code> in the status of a custom hostname means that the CAA records configured on the domain prevented the Certificate Authority to issue the certificate.</p>
<p>You can check which CAA records are configured on a domain using the <code>dig</code> command:
<code>dig CAA example.com</code></p>
<p>You will need to ensure that the required CAA records for the selected Certificate Authority are configured.
For example, here are the records required to issue <a href="https://letsencrypt.org/docs/caa/">Let's Encrypt</a> and <a href="https://pki.goog/faq/#caa">Google Trust Services</a> certificates:</p>
<pre><code class="language-txt">example.com CAA 0 issue &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;example.com CAA 0 issuewild &quot;pki.goog; cansignhttpexchanges=yes&quot;&#10;&#10;example.com CAA 0 issue &quot;letsencrypt.org&quot;&#10;example.com CAA 0 issuewild &quot;letsencrypt.org&quot;&#10;&#10;example.com CAA 0 issue &quot;ssl.com&quot;&#10;example.com CAA 0 issuewild &quot;ssl.com&quot;&#10;</code></pre>
<p>For more details, refer to <a href="/ssl/faq/#caa-records">CAA records FAQ</a>.</p>
<hr />
<h2 id="custom-hostname-matches-zone-name-403-forbidden">Custom hostname matches zone name (403 Forbidden)</h2>
<p>Do not configure a custom hostname which matches the zone name. For example, if your SaaS zone is <code>example.com</code>, do not create a custom hostname named <code>example.com</code>.</p>
<p>This configuration will cause a 403 Forbidden error due to DNS override restrictions applied for security reasons. This limitation also affects Worker Routes making subrequests.</p>
<hr />
<h2 id="older-devices-have-issues-connecting">Older devices have issues connecting</h2>
<p>As Let's Encrypt - one of the <a href="/ssl/reference/certificate-authorities/">certificate authorities (CAs)</a> used by Cloudflare - has announced changes in its <a href="/ssl/concepts/#chain-of-trust">chain of trust</a>, starting September 9, 2024, there may be issues with older devices trying to connect to your custom hostname certificate.</p>
<p>Consider the following solutions:</p>
<ul>
<li>
<p>Use the <a href="/api/resources/custom_hostnames/methods/edit/">Edit Custom Hostname</a> endpoint to set the <code>certificate_authority</code> parameter to an empty string (<code>&quot;&quot;</code>): this sets the custom hostname certificate to &quot;default CA&quot;, leaving the choice up to Cloudflare. Cloudflare will always attempt to issue the certificate from a more compatible CA, such as <a href="/ssl/reference/certificate-authorities/#google-trust-services">Google Trust Services</a>, and will only fall back to using Let’s Encrypt if there is a <a href="/ssl/edge-certificates/caa-records/">CAA record</a> in place that blocks Google from issuing a certificate.</p>
<details class="nb-details"><summary>Example API call</summary><div class="nb-details-body">
</li>
</ul>
@markup("md", "content/.markup/bodies/4094.md")
</div></details>
<ul>
<li>Use the <a href="/api/resources/custom_hostnames/methods/edit/">Edit Custom Hostname</a> endpoint to set the <code>certificate_authority</code> parameter to <code>google</code>: this sets Google Trust Services as the CA for your custom hostnames. In your API call, make sure to also include <code>method</code> and <code>type</code> in the <code>ssl</code> object.</li>
<li>If you are using a custom certificate for your custom hostname, refer to the <a href="/ssl/edge-certificates/custom-certificates/troubleshooting/#lets-encrypt-chain-update">custom certificates troubleshooting</a>.</li>
</ul>
<h2 id="custom-hostname-fails-to-verify-because-the-zone-is-held">Custom hostname fails to verify because the zone is held</h2>
<p>The <a href="/fundamentals/account/account-security/zone-holds/">zone hold feature</a> is a toggle that will prevent their zone from being activated on other Cloudflare account. When enabled, Cloudflare is not able to issue an SSL/TLS certificate on behalf of that domain name for either a zone or custom hostname.
When the option <code>Also prevent subdomains</code> is enabled, this prevents the verification of custom hostnames for this domain. The custom hostname will remain in the <code>Blocked</code> status, with the following error message: <code>The hostname is associated with a held zone. Please contact the owner of this domain to have the hold removed.</code> In this case, the owner of the zone needs to <a href="/fundamentals/account/account-security/zone-holds/#release-zone-holds">release the hold</a> before the custom hostname can become activated.</p>
<p>The <code>Blocked</code> status is terminal — the custom hostname will not retry validation automatically. After the zone hold is released, select <strong>Refresh</strong> on the custom hostname in the Cloudflare dashboard, or send a <a href="/api/resources/custom_hostnames/methods/edit/">PATCH request</a> to the custom hostname, to restart the validation process. After the hostname has been validated, the zone hold can be enabled again.</p>
<h2 id="hostnames-over-64-characters">Hostnames over 64 characters</h2>
<p>The Common Name (CN) restriction establishes a limit of 64 characters (<a href="https://www.rfc-editor.org/rfc/rfc5280.html">RFC 5280</a>). If you have a hostname that exceeds this length, you may find the following error:</p>
<pre><code class="language-txt">Since no host is 64 characters or fewer, Cloudflare Branding is required. Please check your input and try again. (1469)&#10;</code></pre>
<p>To solve this, you can set <code>cloudflare_branding</code> to <code>true</code> when <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/create-custom-hostnames/#hostnames-over-64-characters">creating your custom hostnames</a> via API.</p>
<p>Cloudflare branding means that <code>sni.cloudflaressl.com</code> will be added as the certificate Common Name (CN) and the long hostname will be included as a part of the Subject Alternative Name (SAN).</p>
