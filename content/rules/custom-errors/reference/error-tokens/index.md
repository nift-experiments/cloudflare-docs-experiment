---
cp9:
  canonical: https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/
  description: Dynamic tokens available for use in custom error page HTML.
  full_title: Custom error tokens · Cloudflare Rules docs
  head_html: <title>Custom error tokens · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Dynamic tokens available for use in custom error page HTML."><link rel="canonical" href="https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/index.md"><meta property="og:title" content="Custom error tokens · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Dynamic tokens available for use in custom error page HTML."><meta property="og:url" content="https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/#page","headline":"Custom error tokens \u00b7 Cloudflare Rules docs","description":"Dynamic tokens available for use in custom error page HTML.","url":"https://developers.cloudflare.com/rules/custom-errors/reference/error-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/custom-errors/reference/error-tokens/
  schema: 1
---
<h2 id="for-error-pages">For Error Pages</h2>
<p>Each custom error token provides diagnostic information or specific functionality that appears on the error page. Certain error pages require a page-specific custom error token.</p>
<p>To display a custom page for each error, create a separate page per error. For example, to create an error page for both <strong>IP/Country Block</strong> and <strong>Interactive Challenge</strong>, you must design and publish two separate pages.</p>
<p>The following custom error tokens are required by their respective error pages:</p>
<table>
<thead>
<tr>
<th>Token</th>
<th>Required for</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>::CAPTCHA_BOX::</code></td>
<td>Interactive Challenge <br/>Country Challenge (Managed Challenge)<br/>Managed Challenge / I'm Under Attack Mode (Interstitial Page)</td>
</tr>
<tr>
<td><code>::IM_UNDER_ATTACK_BOX::</code></td>
<td>Non-Interactive Challenge</td>
</tr>
<tr>
<td><code>::CLOUDFLARE_ERROR_500S_BOX::</code></td>
<td>5XX Errors</td>
</tr>
<tr>
<td><code>::CLOUDFLARE_ERROR_1000S_BOX::</code></td>
<td>1XXX Errors</td>
</tr>
</tbody>
</table>
<p>Each custom error token has a default look and feel. However, you can use CSS to stylize each custom error tag using each tag's class ID. All the external resources like images, CSS, and scripts will be inlined during the process. As such, all external resources need to be available (that is, they must return <code>200 OK</code>) otherwise an error will be thrown.</p>
<h2 id="for-custom-error-assets-inline-responses-and-error-pages">For Custom Error Assets, inline responses, and Error Pages</h2>
<p>A custom error asset, inline response, or error page may also include the following error tokens, which will be replaced with their real values before sending the response to the visitor:</p>
<table>
<thead>
<tr>
<th>Token</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>::CLIENT_IP::</code></td>
<td>The visitor's IP address.</td>
</tr>
<tr>
<td><code>::RAY_ID::</code></td>
<td>A unique identifier given to every request that goes through Cloudflare.</td>
</tr>
<tr>
<td><code>::GEO::</code></td>
<td>The country or region associated with the visitor's IP address.</td>
</tr>
</tbody>
</table>
