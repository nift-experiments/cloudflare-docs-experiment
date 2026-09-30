---
cp9:
  canonical: https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/
  description: Receive threat intelligence about DDoS botnets targeting your network infrastructure.
  full_title: DDoS Botnet Threat Feed for service providers · Cloudflare DDoS Protection docs
  head_html: <title>DDoS Botnet Threat Feed for service providers · Cloudflare DDoS Protection docs</title><meta name="generator" content="Nift"><meta name="description" content="Receive threat intelligence about DDoS botnets targeting your network infrastructure."><link rel="canonical" href="https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/index.md"><meta property="og:title" content="DDoS Botnet Threat Feed for service providers · Cloudflare DDoS Protection docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Receive threat intelligence about DDoS botnets targeting your network infrastructure."><meta property="og:url" content="https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="DDoS Protection"><meta name="algolia_product_filter" content="DDoS Protection"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="DDoS Protection"><meta name="pcx_tags" content="REST API"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/#page","headline":"DDoS Botnet Threat Feed for service providers \u00b7 Cloudflare DDoS Protection docs","description":"Receive threat intelligence about DDoS botnets targeting your network infrastructure.","url":"https://developers.cloudflare.com/ddos-protection/botnet-threat-feed/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["REST API"]}</script>
  markdown: true
  noindex: false
  route: /ddos-protection/botnet-threat-feed/
  schema: 1
---
<p>The Cloudflare DDoS Botnet Threat Feed is a threat intelligence feed for service providers (SPs) such as hosting providers and Internet service providers (ISPs) that provides information about their own IP addresses that have participated in HTTP DDoS attacks as observed from Cloudflare's global network. The feed aims to help service providers stop the abuse and reduce DDoS attacks originating from within their networks.</p>
<p>Each offense is a mitigated HTTP request from the specific IP address. For example, if an IP has 3,000 offenses, it means that Cloudflare has mitigated 3,000 HTTP requests from that IP.</p>
<p>A service provider can only get information about IP addresses associated with their autonomous system numbers (ASNs). The affiliation of a service provider with their ASNs will be checked against <a href="https://www.peeringdb.com/">PeeringDB</a>, a reliable and globally recognized interconnection database.</p>
<p>To ensure the feed's accuracy, Cloudflare will only include IP addresses that have participated in multiple HTTP DDoS attacks and have triggered high-confidence rules.</p>
<h2 id="context">Context</h2>
<p>A single DDoS attack consisting of thousands of bots can involve as little as one single IP per service provider. Service providers usually only see a small fraction of the attack traffic leaving their network, and it can be hard to correlate it to malicious activity, while trying to identify abusers.</p>
<p>In the case of HTTPS DDoS attacks, service providers only see encrypted payloads leaving their network without any possibility to decrypt or understand if it is malicious or legitimate traffic. However, Cloudflare can see an entire attack and all of its sources if the attack targets an Internet property that uses Cloudflare's services. This global view can help service providers stop the abusers.</p>
<p>For more details, refer to <a href="/ddos-protection/about/how-ddos-protection-works/">How DDoS protection works</a>.</p>
<h2 id="availability">Availability</h2>
<p>The Cloudflare DDoS Botnet Threat Feed is available for free to service providers. For more information, refer to the <a href="https://www.cloudflare.com/en-gb/service-specific-terms-application-services/#ddos-botnet-threat-feed">Terms of Use</a>.</p>
<hr />
<h2 id="before-you-begin">Before you begin</h2>
<p>Make sure that:</p>
<ul>
<li>You have <a href="/fundamentals/account/">created a Cloudflare account</a>.</li>
</ul>
<h2 id="get-started">Get started</h2>
<h3 id="1-authenticate-your-asn-via-peeringdb"><ol>
<li>Authenticate your ASN via PeeringDB</li>
</ol></h3>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/1159.md")
</div>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/1158.md")
</aside>
<h3 id="2-obtain-cloudflare-api-token"><ol start="2">
<li>Obtain Cloudflare API token</li>
</ol></h3>
<p>You must <a href="/fundamentals/api/get-started/create-token/">obtain a Cloudflare API token</a> with at least the following account-level permission:</p>
<ul>
<li><em>DDoS Botnet Feed</em> &gt; <em>Read</em></li>
</ul>
<h3 id="3-call-botnet-threat-feed-api"><ol start="3">
<li>Call Botnet Threat Feed API</li>
</ol></h3>
<p>Invoke one of the Botnet Threat Feed API endpoints:</p>
<ul>
<li><a href="#get-full-report">Get full report</a></li>
<li><a href="#get-day-report">Get day report</a></li>
</ul>
<hr />
<h2 id="available-api-endpoints">Available API endpoints</h2>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-notes">Important notes</h3>
@markup("md", "content/.markup/bodies/1157.md")
</aside>
<p>To invoke an API endpoint, append the operation endpoint to the Cloudflare API base URL:</p>
<pre tabindex="0"><code class="language-txt">https://api.cloudflare.com/client/v4&#10;</code></pre>
<h3 id="get-full-report">Get full report</h3>
<p>Retrieves all the data in the botnet tracking database for a given ASN (currently two weeks worth of data).</p>
<ul>
<li>HTTP verb: <code>GET</code></li>
<li>Operation endpoint: <code>/accounts/{account_id}/botnet_feed/asn/{asn}/full_report</code></li>
</ul>
<p>The provided <code>{asn}</code> must be affiliated with your account.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/botnet_feed/asn/{asn_id}/full_report \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;cidr&quot;: &quot;127.0.0.1/32&quot;,&#10;      &quot;date&quot;: &quot;1970-01-01T00:00:00Z&quot;,&#10;      &quot;offense_count&quot;: 10000&#10;    },&#10;    // ... other entries ...&#10;  ],&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
<h3 id="get-day-report">Get day report</h3>
<p>Retrieves all the data the botnet tracking database has for a given ASN on a given date. This operation currently allows dates greater than two weeks prior, but in this case it will return an empty dataset (the database currently stores two-weeks worth of data).</p>
<ul>
<li>HTTP verb: <code>GET</code></li>
<li>Operation endpoint: <code>/accounts/{account_id}/botnet_feed/asn/{asn}/day_report?date={date}</code></li>
</ul>
<p>The provided <code>{asn}</code> must be affiliated with your account.</p>
<p><code>{date}</code> must be an ISO 8601-formatted date: <code>YYYY-MM-DD</code>. If no date is specified, the API responds with the data from the day before.</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/accounts/{account_id}/botnet_feed/asn/{asn_id}/day_report \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<pre tabindex="0"><code class="language-json">{&#10;  &quot;result&quot;: [&#10;    {&#10;      &quot;cidr&quot;: &quot;127.0.0.1/32&quot;,&#10;      &quot;date&quot;: &quot;2024-05-05T00:00:00Z&quot;,&#10;      &quot;offense_count&quot;: 10000&#10;    },&#10;    // ... other entries ...&#10;  ],&#10;  &quot;success&quot;: true,&#10;  &quot;errors&quot;: [],&#10;  &quot;messages&quot;: []&#10;}&#10;</code></pre>
