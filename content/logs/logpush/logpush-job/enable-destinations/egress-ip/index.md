---
cp9:
  canonical: https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/
  description: Send Logpush logs via a dedicated egress IP.
  full_title: Dedicated Egress IP for Logpush · Cloudflare Logs docs
  head_html: <title>Dedicated Egress IP for Logpush · Cloudflare Logs docs</title><meta name="generator" content="Nift"><meta name="description" content="Send Logpush logs via a dedicated egress IP."><link rel="canonical" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/index.md"><meta property="og:title" content="Dedicated Egress IP for Logpush · Cloudflare Logs docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Send Logpush logs via a dedicated egress IP."><meta property="og:url" content="https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Logs"><meta name="algolia_product_filter" content="Logs"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Logpush"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/#page","headline":"Dedicated Egress IP for Logpush \u00b7 Cloudflare Logs docs","description":"Send Logpush logs via a dedicated egress IP.","url":"https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/egress-ip/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /logs/logpush/logpush-job/enable-destinations/egress-ip/
  schema: 1
---
<p>This guide covers <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> and Logpush configuration and testing instructions to enable log delivery with a fixed, dedicated egress IP.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To use Logpush with a dedicated egress IP, you will need to have <a href="/smart-shield/get-started/#smart-shield-advanced">Smart Shield Advanced</a> with Dedicated CDN Egress IPs (formerly known as Aegis). Note that the Dedicated CDN Egress IPs pool is associated with a zone, not with an account. To use Logpush with dedicated IPs, traffic must be routed to a single zone.</p>
<p>The general approach is to have your Logpush job proxying Logpush data through a Cloudflare zone with Dedicated CDN Egress IPs enabled to send data to your desired destination. This way your destination will only need to allowlist the provisioned dedicated egress IPs of your proxy zone.</p>
<p>As a prerequisite, you need to create a dedicated zone or use an existing zone. If using an existing zone, be aware that the zone's egress will be restricted to Dedicated CDN Egress IPs. Make sure all services using that zone will not be impacted.</p>
<p>It is recommended to use a separate, dedicated zone as a proxy to avoid impacting production systems. If you choose to create a new zone, follow the <a href="/registrar/get-started/register-domain/">steps</a> to register a new domain with Cloudflare.</p>
<p>The following example shows how to set up logpush and Dedicated CDN Egress IPs to proxy an HTTPS destination, but the proxying should work for any supported Logpush destination as all destinations use the HTTP protocol underneath.</p>
<h2 id="1-provision-dedicated-egress-ip-pool"><ol>
<li>Provision dedicated egress IP Pool</li>
</ol></h2>
<ol>
<li>
<p>Work with your Cloudflare account team to purchase <a href="/smart-shield/configuration/dedicated-egress-ips/">Dedicated CDN Egress IPs</a> for your zone.</p>
</li>
<li>
<p>(Optional but recommended) Request two IPs — one in PDX-B and one in SJC-A — to ensure coverage across regions.</p>
</li>
<li>
<p>Confirm Pool ID once provisioned.</p>
</li>
</ol>
<h2 id="2-configure-a-zone"><ol start="2">
<li>Configure a zone</li>
</ol></h2>
<ol>
<li>Register or use an existing zone for the dedicated egress IPs pool.</li>
<li>Contact your account team to get the ID for your dedicated egress IPs pool.</li>
<li>Make a <code>PATCH</code> request to the <a href="/api/resources/zones/subresources/settings/methods/edit/">Edit Zone Setting</a> endpoint:</li>
</ol>
<ul>
<li>Specify <code>aegis</code> as the setting ID in the URL.</li>
<li>In the request body, set <code>enabled</code> to <code>true</code> and use the ID from the previous step as <code>pool_id</code>.</li>
</ul>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/{setting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;id&quot;: &quot;aegis&quot;,&#10;  &quot;value&quot;: {&#10;    &quot;enabled&quot;: true,&#10;    &quot;pool_id&quot;: &quot;&lt;YOUR_EGRESS_POOL_ID&gt;&quot;&#10;  }&#10;}&#x27;</code></pre>
<h2 id="3-proxy-zone-setup"><ol start="3">
<li>Proxy zone setup</li>
</ol></h2>
<ol>
<li>In your zone, add a DNS record (CNAME or A/AAAA) with <strong>Target</strong> as HTTP destination endpoint.</li>
</ol>
<p><img src="/assets/upstream/images/logs/endpoint.png" alt="Create a DNS record in the Cloudflare dashboard to define the HTTP destination endpoint" /></p>
<ol start="2">
<li>If needed, configure <a href="/rules/origin-rules/">origin rules</a> to specify a custom port. This is useful if your destination only accepts traffic on a non standard port, for example <code>12345</code>. You can configure <code>logpush.yourdestinationendpoint.com</code> (without specifying a port, as Cloudflare by default only proxies traffic on HTTP/HTTPS ports) to proxy to <code>yourdestinationendpoint.com:12345</code>.</li>
</ol>
<h2 id="4-configure-logpush"><ol start="4">
<li>Configure Logpush</li>
</ol></h2>
<ol>
<li>Create a Logpush job with the following details:</li>
</ol>
<ul>
<li>Destination: HTTP</li>
<li>Endpoint: Use the domain/path set up (the Cloudflare dashboard will auto-validate the destination). Use the server name specified in the <strong>Name</strong> section in the DNS record. In this case, <code>logpush.yourdestionationendpoint.com</code>.</li>
</ul>
<p><img src="/assets/upstream/images/logs/destination-details.png" alt="Enter destination details when creating a Logpush job in the Cloudflare dashboard" /></p>
<ul>
<li>Configuration: Select dataset, job name, filters, and fields. Refer to the <a href="/logs/logpush/">Logpush documentation</a> for more details.</li>
</ul>
<ol start="2">
<li>Check destination to confirm if the logs are received.</li>
</ol>
<h2 id="5-secure-your-proxy-zone-endpoint"><ol start="5">
<li>Secure your proxy zone endpoint</li>
</ol></h2>
<p>The proxy zone hostname is publicly resolvable, but traffic passes through Cloudflare's edge where you can apply security controls. Use the following best practices to protect your endpoint.</p>
<h3 id="add-a-secret-header-with-waf-validation">Add a secret header with WAF validation</h3>
<p>Add a secret token as an HTTP header in your Logpush job, then create a WAF rule to block requests without it. This is the recommended approach for most deployments.</p>
<p><strong>Configure Logpush with a secret header</strong></p>
<p>Any URL parameter starting with <code>header_</code> becomes an HTTP header in the request. When creating or updating your Logpush job, add the secret header to your destination URL:</p>
<pre tabindex="0"><code class="language-txt">https://logpush.yourdestinationendpoint.com?header_X-Logpush-Secret=YOUR_RANDOM_SECRET_TOKEN&#10;</code></pre>
<p>Generate a strong random token using <code>openssl rand -hex 32</code>.</p>
<p><strong>Create a WAF custom rule</strong></p>
<p>In the proxy zone, go to <strong>Security</strong> &gt; <strong>WAF</strong> &gt; <strong>Custom rules</strong> and create a rule to block requests without the correct secret header.</p>
<ul>
<li><strong>Expression:</strong></li>
</ul>
<pre tabindex="0"><code class="language-txt">(http.host eq &quot;logpush.yourdestinationendpoint.com&quot; and all(http.request.headers[&quot;x-logpush-secret&quot;][*] ne &quot;YOUR_RANDOM_SECRET_TOKEN&quot;))&#10;</code></pre>
<ul>
<li><strong>Action:</strong> Block</li>
</ul>
<h3 id="add-asn-based-filtering">Add ASN-based filtering</h3>
<p>For defense in depth, add a rule to only allow traffic from Cloudflare's ASNs. Logpush traffic originates from Cloudflare's network (ASN 13335, 132892, or 202623).</p>
<ul>
<li><strong>Expression:</strong></li>
</ul>
<pre tabindex="0"><code class="language-txt">(http.host eq &quot;logpush.yourdestinationendpoint.com&quot; and not ip.geoip.asnum in {13335 132892 202623})&#10;</code></pre>
<ul>
<li><strong>Action:</strong> Block</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10561.md")
</aside>
<h3 id="use-access-service-tokens-for-high-security-environments">Use Access Service Tokens for high-security environments</h3>
<p>For stronger authentication, use <a href="/cloudflare-one/access-controls/service-credentials/service-tokens/">Cloudflare Access Service Tokens</a> for machine-to-machine authentication. Create a Service Token in the Zero Trust dashboard, then configure Logpush with the Access headers:</p>
<pre tabindex="0"><code class="language-txt">https://logpush.yourdestinationendpoint.com?header_CF-Access-Client-Id=YOUR_CLIENT_ID&amp;header_CF-Access-Client-Secret=YOUR_CLIENT_SECRET&#10;</code></pre>
<h3 id="verify-your-security-configuration">Verify your security configuration</h3>
<p>Test that your WAF rules are blocking unauthorized requests:</p>
<pre tabindex="0"><code class="language-bash">$ curl https://logpush.yourdestinationendpoint.com&#10;&#35; Expected: error code: 1020&#10;&#10;$ curl -H &quot;X-Logpush-Secret: wrong-token&quot; https://logpush.yourdestinationendpoint.com&#10;&#35; Expected: error code: 1020&#10;</code></pre>
<p>Check Cloudflare Analytics for the proxy zone to confirm Logpush traffic is flowing, and monitor WAF events to ensure unauthorized requests are blocked.</p>
