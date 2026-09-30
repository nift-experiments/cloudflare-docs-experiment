---
cp9:
  canonical: https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/
  description: Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.
  full_title: Remove locale from URL path · Cloudflare Rules docs
  head_html: <title>Remove locale from URL path · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format."><link rel="canonical" href="https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/index.md"><meta property="og:title" content="Remove locale from URL path · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format."><meta property="og:url" content="https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Redirect Rules"><meta name="pcx_tags" content="Redirects,Localization"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/#page","headline":"Remove locale from URL path \u00b7 Cloudflare Rules docs","description":"Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.","url":"https://developers.cloudflare.com/rules/url-forwarding/examples/remove-locale-url/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Redirects","Localization"]}</script>
  markdown: true
  noindex: false
  route: /rules/url-forwarding/examples/remove-locale-url/
  schema: 1
---
<p class="article-summary">Create a redirect rule to redirect visitors from an old URL format with locale information to a new URL format.</p>
<p>This example single redirect for zone <code>example.com</code> will redirect visitors from an old URL format that included the locale (for example, <code>/en-us/&lt;page_name&gt;</code>) to the new format <code>/&lt;page_name&gt;</code>.</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13196.md")
</div>
<p>The function <a href="/ruleset-engine/rules-language/functions/#regex_replace"><code>regex_replace()</code></a> allows you to extract parts of the URL using regular expressions' capture groups. Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using <code>${&lt;num&gt;}</code> in the replacement string, where <code>&lt;num&gt;</code> is the number of the capture group.</p>
<p>For example, the redirect rule would perform the following redirects:</p>
<table>
<thead>
<tr>
<th>Request URL</th>
<th>Target URL</th>
<th>Status code</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>example.com/en-us/meet-our-team</code></td>
<td><code>example.com/meet-our-team</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/pt-BR/meet-our-team</code></td>
<td><code>example.com/meet-our-team</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/en-us/calendar?view=month</code></td>
<td><code>example.com/calendar?view=month</code></td>
<td><code>301</code></td>
</tr>
<tr>
<td><code>example.com/meet-our-team</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
<tr>
<td><code>example.com/robots.txt</code></td>
<td>(unchanged)</td>
<td>n/a</td>
</tr>
</tbody>
</table>
