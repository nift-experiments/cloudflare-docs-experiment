---
cp9:
  canonical: https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/
  description: Configure Dedicated CDN Egress IPs using the Cloudflare API.
  full_title: Set up Dedicated CDN Egress IPs · Cloudflare Smart Shield docs
  head_html: <title>Set up Dedicated CDN Egress IPs · Cloudflare Smart Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure Dedicated CDN Egress IPs using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/index.md"><meta property="og:title" content="Set up Dedicated CDN Egress IPs · Cloudflare Smart Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure Dedicated CDN Egress IPs using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Smart Shield"><meta name="algolia_product_filter" content="Smart Shield"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Smart Shield"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/#page","headline":"Set up Dedicated CDN Egress IPs \u00b7 Cloudflare Smart Shield docs","description":"Configure Dedicated CDN Egress IPs using the Cloudflare API.","url":"https://developers.cloudflare.com/smart-shield/configuration/dedicated-egress-ips/setup/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /smart-shield/configuration/dedicated-egress-ips/setup/
  schema: 1
---
<p>You can use the <a href="/api/resources/zones/subresources/settings/methods/edit/">Edit Zone Settings API endpoint</a> to set up Dedicated CDN Egress IPs (formerly known as Aegis). If you are not familiar with how Cloudflare API works, refer to <a href="/fundamentals/api/">Fundamentals</a>.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="enterprise-only">Enterprise-only</h3>
@markup("md", "content/.markup/bodies/13855.md")
</aside>
<h2 id="requirements">Requirements</h2>
<ul>
<li>The Dedicated CDN Egress IPs (DCEI) zone setting is only available within Cloudflare accounts that own leased IPs, or accounts to which a <a href="/byoip/">BYOIP prefix</a> has been delegated. If you wish to use Dedicated CDN Egress IPs for zones that do not meet this criteria, contact your account team.</li>
<li></li>
</ul>
<p>Each dedicated egress pool can consist of either IPs from a <a href="/byoip/">BYOIP prefix</a> or Cloudflare-leased IPs. A single dedicated egress pool cannot contain both BYOIPs and leased IPs. Also, a single BYOIP prefix can be used for either CDN ingress or CDN egress, but not both.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13854.md")
</aside>
<h2 id="turn-on-dcei-for-a-zone">Turn on DCEI for a zone</h2>
<ol>
<li>Contact your account team to get the ID for your dedicated egress pool.</li>
<li>Make a <code>PATCH</code> request to the <a href="/api/resources/zones/subresources/settings/methods/edit/">Edit Zone Setting</a> endpoint:</li>
</ol>
<ul>
<li>Specify <code>aegis</code> as the setting ID in the URL.</li>
<li>In the request body, set <code>enabled</code> to <code>true</code> and use the ID from the previous step as the <code>pool_id</code> value.</li>
</ul>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/{setting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;id&quot;: &quot;aegis&quot;,&#10;  &quot;value&quot;: {&#10;    &quot;enabled&quot;: true,&#10;    &quot;pool_id&quot;: &quot;&lt;EGRESS_POOL_ID&gt;&quot;&#10;  }&#10;}&#x27;</code></pre>
<h2 id="check-dcei-status-for-a-zone">Check DCEI status for a zone</h2>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/{setting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h2 id="turn-off-dcei-for-a-zone">Turn off DCEI for a zone</h2>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/settings/{setting_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;id&quot;: &quot;aegis&quot;,&#10;  &quot;value&quot;: {&#10;    &quot;enabled&quot;: false&#10;  }&#10;}&#x27;</code></pre>
<h2 id="check-your-ips">Check your IPs</h2>
<p>You can find your leased dedicated IPs for CDN egress on the dashboard under <a href="https://dash.cloudflare.com/?to=/:account/ip-addresses/address-space"><strong>Address space</strong> &gt; <strong>Leased IPs</strong></a>.</p>
<p>If you are using BYOIP, refer to <strong>BYOIP prefixes</strong> instead.</p>
