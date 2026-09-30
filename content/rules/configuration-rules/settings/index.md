---
cp9:
  canonical: https://developers.cloudflare.com/rules/configuration-rules/settings/
  description: Available settings you can customize with Configuration Rules.
  full_title: Configuration Rules settings · Cloudflare Rules docs
  head_html: <title>Configuration Rules settings · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Available settings you can customize with Configuration Rules."><link rel="canonical" href="https://developers.cloudflare.com/rules/configuration-rules/settings/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/configuration-rules/settings/index.md"><meta property="og:title" content="Configuration Rules settings · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available settings you can customize with Configuration Rules."><meta property="og:url" content="https://developers.cloudflare.com/rules/configuration-rules/settings/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/configuration-rules/settings/#page","headline":"Configuration Rules settings \u00b7 Cloudflare Rules docs","description":"Available settings you can customize with Configuration Rules.","url":"https://developers.cloudflare.com/rules/configuration-rules/settings/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/configuration-rules/settings/
  schema: 1
---
<p>You can change the configuration settings described below in a configuration rule.</p>
<h2 id="automatic-https-rewrites">Automatic HTTPS Rewrites</h2>
<p><a href="/ssl/edge-certificates/additional-options/automatic-https-rewrites/">Automatic HTTPS Rewrites</a> prevents end users from seeing <code>Mixed content</code> errors by rewriting URLs from <code>http</code> to <code>https</code> for resources or links on your website that can be served with HTTPS.</p>
<p>Use this setting to turn on or off Automatic HTTPS Rewrites for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13005.md")
</div></details>
<h2 id="browser-integrity-check">Browser Integrity Check</h2>
<p><a href="/waf/tools/browser-integrity-check/">Browser Integrity Check</a> blocks access to pages based on specific HTTP headers commonly abused by spammers.</p>
<p>Use this setting to turn on or off Browser Integrity Check for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13006.md")
</div></details>
<h2 id="disable-real-user-monitoring-rum">Disable Real User Monitoring (RUM)</h2>
<p><a href="/web-analytics/">Cloudflare Web Analytics</a>, also known as Real User Monitoring (RUM), is Cloudflare's free, privacy-first analytics for your website.</p>
<p>Use this setting to turn off Web Analytics for matching requests.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/13004.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13007.md")
</div></details>
<h2 id="disable-zaraz">Disable Zaraz</h2>
<p><a href="/zaraz/">Cloudflare Zaraz</a> gives you complete control over third-party tools and services for your website, and allows you to offload them to the Cloudflare global network.</p>
<p>Use this setting to turn off Zaraz for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13008.md")
</div></details>
<h2 id="email-obfuscation">Email Obfuscation</h2>
<p><a href="/waf/tools/scrape-shield/email-address-obfuscation/">Email Obfuscation</a> prevents spam by hiding email addresses from bots and harvesters while keeping them visible to human visitors to your site.</p>
<p>Use this setting to turn on or off Email Obfuscation for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13009.md")
</div></details>
<h2 id="fonts">Fonts</h2>
<p><a href="/speed/optimization/content/fonts/">Cloudflare Fonts</a> rewrites Google Fonts to be delivered from a website's own origin, eliminating the need to rely on third-party font providers.</p>
<p>Use this setting to turn on or off Cloudflare Fonts for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13010.md")
</div></details>
<h2 id="hotlink-protection">Hotlink Protection</h2>
<p><a href="/waf/tools/scrape-shield/hotlink-protection/">Hotlink Protection</a> prevents your images from being used by other sites, potentially reducing the bandwidth consumed by your origin server.</p>
<p>Use this setting to turn on or off Hotlink Protection for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13011.md")
</div></details>
<h2 id="i-m-under-attack">I'm Under Attack</h2>
<p>When enabled, <a href="/fundamentals/reference/under-attack-mode/">Under Attack mode</a> performs additional security checks to help mitigate layer 7 DDoS attacks. Validated users access your website and suspicious traffic is blocked.</p>
<p>Use this setting to turn on or off Under Attack mode for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13012.md")
</div></details>
<h2 id="markdown-for-agents">Markdown for Agents</h2>
<p><a href="/fundamentals/reference/markdown-for-agents/">Markdown for Agents</a> automatically converts HTML to Markdown for requests that use content negotiation headers (<code>Accept: text/markdown</code>).</p>
<p>Use this setting to turn on or off Markdown for Agents for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13013.md")
</div></details>
<h2 id="opportunistic-encryption">Opportunistic Encryption</h2>
<p><a href="/ssl/edge-certificates/additional-options/opportunistic-encryption/">Opportunistic Encryption</a> allows browsers to access HTTP URIs over an encrypted TLS channel.</p>
<p>Use this setting to turn on or off Opportunistic Encryption for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13014.md")
</div></details>
<h2 id="polish">Polish</h2>
<p><a href="/images/polish/">Cloudflare Polish</a> is a one-click image optimization product that automatically optimizes images in your site.</p>
<p>Use this setting to configure Polish for matching requests:</p>
<ul>
<li>Off</li>
<li>Lossless</li>
<li>Lossy</li>
<li>WebP</li>
</ul>
<p>Refer to <a href="/images/polish/compression/#compression-options">Compression options</a> for more information on these values.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13015.md")
</div></details>
<h2 id="request-body-buffering">Request Body Buffering</h2>
<p>Use the Request Body Buffering setting to configure the request body buffering mode for matching requests:</p>
<ul>
<li><strong>Standard</strong> (default): Allows Cloudflare products to inspect a prefix of the request body when necessary for enabled functionality on your zone.</li>
<li><strong>Full</strong>: Buffers the entire request body before sending the request to your origin server.</li>
<li><strong>None</strong>: Strictly no buffering. The request body is streamed directly to the origin server without inspection.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13003.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13016.md")
</div></details>
<h2 id="response-body-buffering">Response Body Buffering</h2>
<p>Use the Response Body Buffering setting to configure the response body buffering mode for matching requests:</p>
<ul>
<li><strong>Standard</strong> (default): Allows Cloudflare products to inspect a prefix of the response body when necessary for enabled functionality on your zone.</li>
<li><strong>None</strong>: Strictly no buffering. The response body is streamed directly to the client without inspection.</li>
</ul>
<p>For features that inspect response content and troubleshooting guidance, refer to <a href="/rules/configuration-rules/response-body-inspection/">Response body inspection</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/13002.md")
</aside>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13017.md")
</div></details>
<h2 id="rocket-loader">Rocket Loader</h2>
<p><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a> prioritizes your website's content (such as text, images, and fonts) by deferring the loading of all your JavaScript code until after rendering.</p>
<p>Use this setting to turn on or off Rocket Loader for matching requests.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13018.md")
</div></details>
<h2 id="ssl">SSL</h2>
<p><a href="/ssl/origin-configuration/ssl-modes/">SSL/TLS encryption modes</a> control the scheme (<code>http://</code> or <code>https://</code>) that Cloudflare uses to connect to your origin web server and how SSL certificates presented by your origin will be validated.</p>
<p>Use this setting to configure the SSL/TLS encryption mode for matching requests:</p>
<ul>
<li>Off</li>
<li>Flexible</li>
<li>Full</li>
<li>Strict</li>
<li>Origin Pull</li>
</ul>
<p>Refer to <a href="/ssl/origin-configuration/ssl-modes/#available-encryption-modes">Available encryption modes</a> for more information on these values.</p>
<details class="nb-details"><summary>API information</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/13019.md")
</div></details>
