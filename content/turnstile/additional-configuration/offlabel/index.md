---
cp9:
  canonical: https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/
  description: Remove Cloudflare branding from Turnstile widgets with Offlabel mode.
  full_title: Remove Cloudflare branding with Offlabel · Cloudflare Turnstile docs
  head_html: <title>Remove Cloudflare branding with Offlabel · Cloudflare Turnstile docs</title><meta name="generator" content="Nift"><meta name="description" content="Remove Cloudflare branding from Turnstile widgets with Offlabel mode."><link rel="canonical" href="https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/index.md"><meta property="og:title" content="Remove Cloudflare branding with Offlabel · Cloudflare Turnstile docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Remove Cloudflare branding from Turnstile widgets with Offlabel mode."><meta property="og:url" content="https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Turnstile"><meta name="algolia_product_filter" content="Turnstile"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Turnstile"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/#page","headline":"Remove Cloudflare branding with Offlabel \u00b7 Cloudflare Turnstile docs","description":"Remove Cloudflare branding from Turnstile widgets with Offlabel mode.","url":"https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /turnstile/additional-configuration/offlabel/
  schema: 1
---
<p>Offlabel is an Enterprise-only feature that removes Cloudflare branding and logo from Turnstile widgets. When enabled, widgets display without any visual references to Cloudflare.</p>
<p>When Offlabel is enabled:</p>
<ul>
<li>The Cloudflare logo and color schemes are removed from all widget states.</li>
<li>The widget maintains the same functionality, behavior, and WCAG 2.2 AA accessibility compliance.</li>
<li>All security features remain unchanged.</li>
</ul>
<p>The widget will display with a clean, unbranded appearance that integrates seamlessly with your website's design.</p>
<hr />
<h2 id="implementation">Implementation</h2>
<h3 id="enable-offlabel">Enable Offlabel</h3>
<p>After your account team enables the Offlabel entitlement, you can activate it for specific widgets using the Cloudflare API.</p>
<pre tabindex="0"><code class="language-bash">curl -X PUT &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;&#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;&#45;H &quot;Content-Type: application/json&quot; \&#10;&#45;d &#x27;{&#10;    &quot;offlabel&quot;: true&#10;}&#x27;&#10;</code></pre>
<h3 id="create-new-widgets-with-offlabel">Create new widgets with Offlabel</h3>
<p>You can enable Offlabel when creating new widgets.</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets&quot; \&#10;&#45;H &quot;Authorization: Bearer $API_TOKEN&quot; \&#10;&#45;H &quot;Content-Type: application/json&quot; \&#10;&#45;d &#x27;{&#10;    &quot;name&quot;: &quot;Branded Widget&quot;,&#10;    &quot;domains&quot;: [&quot;example.com&quot;],&#10;    &quot;mode&quot;: &quot;managed&quot;,&#10;    &quot;offlabel&quot;: true&#10;}&#x27;&#10;</code></pre>
<h3 id="verification">Verification</h3>
<p>Confirm Offlabel is enabled by checking your widget configuration.</p>
<pre tabindex="0"><code class="language-bash">curl -X GET &quot;https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/challenges/widgets/$WIDGET_ID&quot; \&#10;&#45;H &quot;Authorization: Bearer $API_TOKEN&quot;&#10;</code></pre>
<p>The response will include <code>&quot;offlabel&quot;: true</code> when the feature is active.</p>
<h3 id="link-to-cloudflare-s-turnstile-privacy-policy">Link to Cloudflare's Turnstile Privacy Policy</h3>
<p>As a condition of enabling offlabel, you must reference Cloudflare's <a href="https://www.cloudflare.com/turnstile-privacy-policy/">Turnstile Privacy Addendum</a> in one of two ways:</p>
<ol>
<li>Link to it in your own privacy policy.</li>
<li>Configure the widget to display a link to Cloudflare's privacy policy using the <a href="/turnstile/get-started/client-side-rendering/widget-configurations/#complete-configuration-reference">JavaScript Render Parameters</a>.</li>
</ol>
<hr />
<h2 id="availability">Availability</h2>
<p>Offlabel is available exclusively to Enterprise customers with the Enterprise Turnstile add-on or Standalone Enterprise Turnstile customers.</p>
<p>Contact your account team for access to the Offlabel feature.</p>
