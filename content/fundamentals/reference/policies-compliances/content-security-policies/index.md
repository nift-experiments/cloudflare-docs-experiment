---
cp9:
  canonical: https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/
  description: Understand how Cloudflare interacts with Content Security Policies (CSPs) and which headers to update for specific Cloudflare features.
  full_title: Content Security Policies (CSPs) and Cloudflare · Cloudflare Fundamentals docs
  head_html: <title>Content Security Policies (CSPs) and Cloudflare · Cloudflare Fundamentals docs</title><meta name="generator" content="Nift"><meta name="description" content="Understand how Cloudflare interacts with Content Security Policies (CSPs) and which headers to update for specific Cloudflare features."><link rel="canonical" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/index.md"><meta property="og:title" content="Content Security Policies (CSPs) and Cloudflare · Cloudflare Fundamentals docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Understand how Cloudflare interacts with Content Security Policies (CSPs) and which headers to update for specific Cloudflare features."><meta property="og:url" content="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Fundamentals"><meta name="algolia_product_filter" content="Cloudflare Fundamentals"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Cloudflare Fundamentals"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/#page","headline":"Content Security Policies (CSPs) and Cloudflare \u00b7 Cloudflare Fundamentals docs","description":"Understand how Cloudflare interacts with Content Security Policies (CSPs) and which headers to update for specific Cloudflare features.","url":"https://developers.cloudflare.com/fundamentals/reference/policies-compliances/content-security-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /fundamentals/reference/policies-compliances/content-security-policies/
  schema: 1
---
<p>A <strong>Content Security Policy (CSP)</strong> is an added layer of security that helps detect and mitigate certain types of attacks, including:</p>
<ul>
<li>Content/code injection</li>
<li>Cross-site scripting (XSS)</li>
<li>Embedding malicious resources</li>
<li>Malicious iframes (clickjacking)</li>
</ul>
<p>To learn more about configuring a CSP in general, refer to the <a href="https://developer.mozilla.org/docs/web/http/csp">Mozilla documentation</a>.</p>
<h2 id="using-a-csp-with-cloudflare">Using a CSP with Cloudflare</h2>
<p>Cloudflare's <a href="/cache/">CDN</a> is compatible with CSP.</p>
<p>Cloudflare does not:</p>
<ul>
<li>Modify CSP headers from the origin web server (except when using Zaraz, to ensure the <a href="https://blog.cloudflare.com/cloudflare-zaraz-supports-csp/">Zaraz script is always running</a>).</li>
<li>Require changes to acceptable sources for first or third-party content.</li>
<li>Modify URLs (besides adding the <a href="/fundamentals/reference/cdn-cgi-endpoint/"><code>/cdn-cgi/</code> endpoint</a> and <a href="/speed/optimization/content/fonts/">Cloudflare Fonts</a> that rewrites Google Fonts urls).</li>
<li>Interfere with locations specified in your CSP.</li>
</ul>
<p>If you require the CSP headers to be changed or added, you can change them using some Cloudflare products:</p>
<ul>
<li>If your website is <a href="/dns/proxy-status/">proxied</a> through Cloudflare, you can use a <a href="/rules/transform/response-header-modification/">response header transform rule</a> to replace or add CSP headers.</li>
<li>If your website is hosted using <a href="/pages/">Cloudflare Pages</a>, you can set a <a href="/pages/configuration/headers/"><code>_headers file</code></a> to modify or add CSP headers.</li>
</ul>
<h3 id="product-requirements">Product requirements</h3>
<p>To use certain Cloudflare features, however, you may need to update the headers in your CSP:</p>
<table>
<thead>
<tr>
<th>Feature(s)</th>
<th>Updated headers</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="/speed/optimization/content/rocket-loader/">Rocket Loader</a></td>
<td><code>script-src 'self' ajax.cloudflare.com;</code></td>
</tr>
<tr>
<td><a href="/waf/tools/scrape-shield/">Scrape Shield</a></td>
<td><code>script-src 'self' 'unsafe-inline'</code></td>
</tr>
<tr>
<td><a href="/web-analytics/">Web Analytics</a></td>
<td><code>script-src static.cloudflareinsights.com; connect-src cloudflareinsights.com</code></td>
</tr>
<tr>
<td><a href="/bots/">Bot products</a></td>
<td>Refer to <a href="/cloudflare-challenges/challenge-types/javascript-detections/#if-you-have-a-content-security-policy-csp">JavaScript detections and CSPs</a>.</td>
</tr>
<tr>
<td><a href="/client-side-security/">Client-side security</a> (formerly Page Shield)</td>
<td>Refer to <a href="/client-side-security/reference/csp-header/">CSP header format</a>.</td>
</tr>
<tr>
<td><a href="/zaraz/">Zaraz</a></td>
<td>No updates required (<a href="https://blog.cloudflare.com/cloudflare-zaraz-supports-csp/">details</a>).</td>
</tr>
<tr>
<td><a href="/turnstile/">Turnstile</a></td>
<td>Refer to <a href="/turnstile/reference/content-security-policy/">Turnstile CSP</a>.</td>
</tr>
</tbody>
</table>
