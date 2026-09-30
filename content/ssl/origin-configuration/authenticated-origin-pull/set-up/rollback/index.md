<p>If you need to disable or remove your <a href="/ssl/origin-configuration/authenticated-origin-pull/set-up/per-hostname/">per-hostname</a> Authenticated Origin Pulls configuration, follow these steps.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14301.md")
</aside>
<ol>
<li>Use a <a href="/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update/"><code>PUT</code> request</a> to disable Authenticated Origin Pulls on the hostname.</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request PUT \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;config&quot;: [&#10;    {&#10;      &quot;enabled&quot;: false,&#10;      &quot;cert_id&quot;: &quot;&lt;CERT_ID&gt;&quot;,&#10;      &quot;hostname&quot;: &quot;&lt;YOUR_HOSTNAME&gt;&quot;&#10;    }&#10;  ]&#10;}&#x27;</code></pre>
<ol start="2">
<li>(Optional) Use a <a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/list/"><code>GET</code> request</a> to obtain a list of the client certificate IDs. You will need the ID of the certificate you want to remove for the following step.</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<ol start="3">
<li>Use the <a href="/api/resources/origin_tls_client_auth/subresources/hostname_certificates/methods/delete/">Delete hostname client certificate</a> endpoint to remove the certificate you had uploaded.</li>
</ol>
<pre class="nb-api-request"><code class="language-bash">curl --request DELETE \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
