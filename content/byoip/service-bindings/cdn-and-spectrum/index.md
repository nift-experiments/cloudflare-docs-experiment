<p>With <a href="/byoip/service-bindings/">service bindings</a>, CDN<sup><a href="#footnote-1">1</a></sup> customers using BYOIP can take the same prefix they have onboarded to Cloudflare and use it to selectively route traffic on a per-IP address basis to <a href="/spectrum/">Spectrum</a><sup><a href="#footnote-2">2</a></sup>, or vice versa. This means:</p>
<ul>
<li>
<p>You can upgrade individual IPs within a CDN prefix to a Spectrum IP. For example, if you have a CDN prefix 203.0.113.0/24, you can upgrade 203.0.113.1 to Spectrum.</p>
</li>
<li>
<p>You can upgrade individual IPs within a Spectrum prefix to a CDN IP. For example, if you have a Spectrum prefix 203.0.113.0/24, you can upgrade 203.0.113.1 to CDN.</p>
</li>
</ul>
<p>This guide will use the first example and consider a prefix that was onboarded to the CDN, with a few IPs upgraded to Spectrum.</p>
<h2 id="before-you-begin">Before you begin</h2>
<p>Cloudflare <strong>strongly</strong> recommends implementing service bindings through an <strong>aggregated</strong> CIDR block, as it is more efficient than adding discrete bindings for non-contiguous CIDR blocks.</p>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3756.md")
</div></details>
<p>Once a service binding is created (or deleted), it will take <strong>four to six hours</strong> to propagate across Cloudflare's global network. Services for the IP addresses in scope will likely be disrupted during this window.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3755.md")
</aside>
<hr />
<h2 id="prepare-your-ips">Prepare your IPs</h2>
<h3 id="1-get-account-information"><ol>
<li>Get account information</li>
</ol></h3>
<ol>
<li>Log in to your Cloudflare account and get your <a href="/fundamentals/account/find-account-and-zone-ids/">account ID</a> and <a href="/fundamentals/api/get-started/">authentication key or token</a>. If using an <a href="/fundamentals/api/get-started/create-token/">API token</a>, the permissions should include <code>Account</code> - <code>IP Prefixes</code> - <code>Edit</code>.</li>
<li>Make a <code>GET</code> request to the <a href="/api/resources/addressing/subresources/services/methods/list/">List Services</a> endpoint and take note of the <code>id</code> associated with the Spectrum service.</li>
<li>Use the <a href="/api/resources/addressing/subresources/prefixes/methods/list/">List Prefixes</a> endpoint and take note of the <code>id</code> associated with the prefix (<code>cidr</code>) you will configure.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/3757.md")
</div>
<ol start="4">
<li>To confirm you currently have a CDN service binding and that it spans across your entire prefix, make a <code>GET</code> request to the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/list/">List Service Bindings</a> endpoint. Replace the <code>{prefix_id}</code> in the URI path by the actual prefix ID you got from the previous step.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example-1">Example</h3>
@markup("md", "content/.markup/bodies/3758.md")
</div>
<h3 id="2-create-service-bindings"><ol start="2">
<li>Create service bindings</li>
</ol></h3>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="caution">Caution</h3>
@markup("md", "content/.markup/bodies/3754.md")
</aside>
<ol>
<li>Make a <code>POST</code> request to the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/create/">Create service binding</a> endpoint, indicating the IP address you want to bind to Spectrum. Specify the <strong>corresponding network mask</strong> as needed.</li>
</ol>
<div class="nb-example"><h3 class="nb-component-title" id="example-2">Example</h3>
@markup("md", "content/.markup/bodies/3759.md")
</div>
<p>You can periodically check the service binding status using the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/list/">List Service Bindings</a> endpoint.</p>
<h3 id="3-verify-all-service-bindings"><ol start="3">
<li>Verify all service bindings</li>
</ol></h3>
<p>After the propagation time (four to six hours), the <a href="/api/resources/addressing/subresources/prefixes/subresources/service_bindings/methods/get/">List Service Bindings</a> endpoint should return all service bindings that are part of the prefix - in this case, CDN and Spectrum.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<hr />
<h2 id="set-up-your-cloudflare-services">Set up your Cloudflare services</h2>
<h3 id="cdn">CDN</h3>
<p>If you already use BYOIP with CDN, you might be able to skip this step. However, if you are using this guide to upgrade a few IPs from a Spectrum prefix to the CDN, consider the following sections on <a href="#address-maps">address maps</a> and <a href="#dns-records">DNS records</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3753.md")
</aside>
<h4 id="address-maps">Address maps</h4>
<p>Use <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/3760.md")
</div> to specify which IPs should be used by Cloudflare in DNS responses when a record is <div class="nb-interactive-component" data-cf-component="GlossaryTooltip">
@markup("md", "content/.markup/bodies/3761.md")
</div>.
<p>You can choose between two different scopes:</p>
<ul>
<li>Account-level: uses the address map for all proxied DNS records across all of the zones within an account.</li>
<li>Zone-level: uses the address map for all proxied DNS records within a zone.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3752.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3764.md")
</div></div>
<h4 id="dns-records">DNS records</h4>
<p>While the DNS record proxy status and address map will determine how Cloudflare's authoritative DNS responds to requests for your hostnames, the IP addresses specified in <code>A</code>/<code>AAAA</code> records will determine <a href="/fundamentals/concepts/how-cloudflare-works/#cloudflare-as-a-reverse-proxy">how Cloudflare reaches the configured origin</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3751.md")
</aside>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/3767.md")
</div></div>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3768.md")
</div></details>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3750.md")
</aside>
<details class="nb-details"><summary>Example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3769.md")
</div></details>
<h3 id="spectrum">Spectrum</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="udp-applications">UDP applications</h3>
@markup("md", "content/.markup/bodies/3749.md")
</aside>
<p>Configuring Spectrum to use your own IP address is only possible via the <a href="/api/resources/spectrum/">Cloudflare API</a>.</p>
<p>The <code>origin_direct</code> field takes the origin IP address, while <code>edge_ips</code> allows you to define which IP address from your BYOIP prefix Cloudflare should use to process requests for your Spectrum application.</p>
<pre class="nb-api-request"><code class="language-bash">curl --request POST \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/spectrum/apps \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;[&#10;  {&#10;    &quot;protocol&quot;: &quot;tcp/22&quot;,&#10;    &quot;dns&quot;: {&#10;      &quot;type&quot;: &quot;CNAME&quot;,&#10;      &quot;name&quot;: &quot;ssh.example.com&quot;&#10;    },&#10;    &quot;origin_direct&quot;: [&#10;      &quot;tcp://192.0.2.1:22&quot;&#10;    ],&#10;    &quot;proxy_protocol&quot;: &quot;off&quot;,&#10;    &quot;ip_firewall&quot;: true,&#10;    &quot;tls&quot;: &quot;full&quot;,&#10;    &quot;edge_ips&quot;: {&#10;      &quot;type&quot;: &quot;static&quot;,&#10;      &quot;ips&quot;: [&#10;        &quot;203.0.113.18&quot;&#10;      ]&#10;    },&#10;    &quot;traffic_type&quot;: &quot;direct&quot;&#10;  }&#10;]&#x27;</code></pre>
<hr />
<h2 id="optional-add-layer-7-functionality">(Optional) Add layer 7 functionality</h2>
<p>Leverage other features according to your needs. For example:</p>
<ul>
<li><a href="/cache/">Cache</a></li>
<li><a href="/waf/custom-rules/">WAF custom rules</a></li>
<li><a href="/waf/analytics/security-analytics/">Security analytics</a></li>
</ul>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Layer 7 HTTP-based</li>
<li id="footnote-2">Layer 4 or Layer 7 HTTP with custom ports</li></ol></section>
