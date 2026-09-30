<p>Refer to the following sections to learn how to manage certificates used with <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level</a> and <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> Authenticated Origin Pulls. <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/global/">Global AOP</a> uses a Cloudflare-provided certificate and does not require certificate management.</p>
<hr />
<h2 id="expired-certificates">Expired certificates</h2>
<p>Cloudflare does not delete client certificates upon expiration unless you send a delete request to the Cloudflare API for the relevant certificate (<a href="/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/delete/">Delete a zone-level certificate</a> or <a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/">Delete a hostname-level certificate</a>). If your origin only accepts a valid client certificate, it will drop requests when the certificate expires.</p>
<p>Make sure you have <a href="/notifications/notification-available/#ssltls">notifications</a> set up to get alerts 30 days and 14 days before an AOP certificate expires.</p>
<hr />
<h2 id="use-specialized-certificates">Use specialized certificates</h2>
<p>To apply different client certificates simultaneously at the zone and hostname level, you can combine zone-level and per-hostname custom certificates.</p>
<p>First, set up <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/zone-level/">zone-level AOP</a> using your certificate. Then, upload specialized certificates for <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">individual hostnames</a>. Per-hostname certificates take precedence over zone-level certificates for the specified hostname.</p>
<hr />
<h2 id="replace-a-certificate-without-downtime-via-api">Replace a certificate without downtime via API</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="no-automatic-removal">No automatic removal</h3>
@markup("md", "content/.markup/bodies/14319.md")
</aside>
<h3 id="per-hostname">Per-hostname</h3>
<ol>
<li><a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/create/">Upload the new certificate</a>.</li>
<li><a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list/">List your certificates</a> and note the ID for the certificate you uploaded.</li>
<li><a href="/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/">Enable Authenticated Origin Pulls for the specific hostname</a>, using the ID obtained in step 2 to specify the certificate you want to use:</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;config&quot;: [&#10;    {&#10;      &quot;enabled&quot;: true,&#10;      &quot;hostname&quot;: &quot;&lt;HOSTNAME&gt;&quot;,&#10;      &quot;cert_id&quot;: &quot;&lt;CERT_ID&gt;&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14318.md")
</aside>
<h3 id="zone-level">Zone-level</h3>
<ol>
<li><a href="/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/create/">Upload the new certificate</a>.</li>
<li><a href="/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/get/">Check whether new certificate is Active</a>.</li>
<li>Once certificate is active, <a href="/api/resources/origin_tls_client_auth/subresources/zone_certificates/methods/delete/">delete the previous certificate</a>.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14317.md")
</aside>
