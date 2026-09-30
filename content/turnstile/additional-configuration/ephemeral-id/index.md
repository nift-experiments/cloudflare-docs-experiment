---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/
  description: Generate single-use Ephemeral IDs for fraud detection and analytics.
  full_title: Ephemeral IDs · Cloudflare Turnstile docs
  head_html: <title>Ephemeral IDs · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Generate single-use Ephemeral IDs for fraud detection and analytics."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/index.md"><meta property="og:title" content="Ephemeral IDs · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Generate single-use Ephemeral IDs for fraud detection and analytics."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Turnstile"><meta name="pcx_tags" content="Account takeover"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/#page","headline":"Ephemeral IDs \u00b7 Cloudflare Turnstile docs","description":"Generate single-use Ephemeral IDs for fraud detection and analytics.","url":"https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Account takeover"]}</script>
  markdown: true
  noindex: false
  route: /turnstile/additional-configuration/ephemeral-id/
  schema: 1
---
<p>Ephemeral IDs are short-lived device identifiers that Turnstile generates for each visitor interaction. Unlike IP-based detection, Ephemeral IDs link visitor behavior to a specific client device without relying on cookies or client-side storage. This makes them effective against attackers who change IP addresses between requests.</p>
<h2 id="how-ephemeral-ids-work">How Ephemeral IDs work</h2>
<p>Ephemeral IDs are dynamically generated for each Turnstile solve attempt. No cookies or local storage is required.</p>
<p>Ephemeral IDs are scoped to your Cloudflare account and cannot be shared across accounts. IDs expire within a few days and cannot be used to identify individual users.</p>
<p>This approach is particularly effective against credential stuffing and fake account creation attacks, where attackers rotate IP addresses to evade detection.</p>
<p>Refer to the <a href="https://blog.cloudflare.com/turnstile-ephemeral-ids-for-fraud-detection/">blog post</a> for more information.</p>
<hr />
<h2 id="implementation">Implementation</h2>
<h3 id="enable-ephemeral-ids">Enable Ephemeral IDs</h3>
<ol>
<li>Contact your Cloudflare account team to enable Ephemeral ID entitlement for your account. This feature requires Enterprise-level access and cannot be self-activated.</li>
<li>After entitlement is enabled, activate Ephemeral IDs for specific widgets using the Cloudflare API.</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;ephemeral_id&quot;: true&#10;  }&#x27;&#10;</code></pre>
<ol start="3">
<li>Confirm Ephemeral IDs are active by checking your widget configuration.</li>
</ol>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;  &#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<h3 id="access-ephemeral-ids">Access Ephemeral IDs</h3>
<p>Once enabled, Ephemeral IDs are included in Siteverify API responses.</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;success&quot;: true,&#10;	&quot;challenge_ts&quot;: &quot;2022-02-28T15:14:30.096Z&quot;,&#10;	&quot;hostname&quot;: &quot;example.com&quot;,&#10;	&quot;error-codes&quot;: [],&#10;	&quot;action&quot;: &quot;login&quot;,&#10;	&quot;cdata&quot;: &quot;sessionid-123456789&quot;,&#10;	&quot;metadata&quot;: {&#10;		&quot;ephemeral_id&quot;: &quot;x:9f78e0ed210960d7693b167e&quot;&#10;	}&#10;}&#10;</code></pre>
<hr />
<h2 id="availability">Availability</h2>
<p>Ephemeral IDs are available to Enterprise Bot Management customers with the Enterprise Turnstile add-on or standalone Enterprise Turnstile customers. Contact your account team for access to Ephemeral IDs.</p>
