---
cp9:
  canonical: https://developers.cloudflare.com/rules/normalization/how-it-works/
  description: How URL normalization modifies incoming request URIs before rule evaluation.
  full_title: How URL normalization works · Cloudflare Rules docs
  head_html: <title>How URL normalization works · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="How URL normalization modifies incoming request URIs before rule evaluation."><link rel="canonical" href="https://developers.cloudflare.com/rules/normalization/how-it-works/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/normalization/how-it-works/index.md"><meta property="og:title" content="How URL normalization works · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="How URL normalization modifies incoming request URIs before rule evaluation."><meta property="og:url" content="https://developers.cloudflare.com/rules/normalization/how-it-works/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Rules"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/normalization/how-it-works/#page","headline":"How URL normalization works \u00b7 Cloudflare Rules docs","description":"How URL normalization modifies incoming request URIs before rule evaluation.","url":"https://developers.cloudflare.com/rules/normalization/how-it-works/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /rules/normalization/how-it-works/
  schema: 1
---
<p>URL normalization modifies separators, encoded elements, and literal bytes in incoming URLs so that they conform to a consistent formatting standard.</p>
<p>For example, consider a WAF custom rule that blocks requests whose URLs match <code>www.example.com/hello</code>. The rule would not block a request containing an encoded element — <code>www.example.com/%68ello</code>. Normalizing incoming URLs on the Cloudflare global network helps simplify rules expressions containing URLs.</p>
<p>The two available types of URL normalization are:</p>
<ul>
<li><a href="#rfc-3986-normalization">RFC 3986 normalization</a></li>
<li><a href="#cloudflare-normalization">Cloudflare normalization</a></li>
</ul>
<p>The location where URL normalization will occur depends on the <a href="/rules/normalization/settings/">configured settings</a>.</p>
<p>For examples of the different settings and their impact on request URLs, refer to the <a href="/rules/normalization/examples/">URL normalization examples</a>.</p>
<h2 id="rfc-3986-normalization">RFC 3986 normalization</h2>
<p>The URL normalization performed according to <a href="https://www.ietf.org/rfc/rfc3986.txt">RFC 3986</a> is as follows:</p>
<ul>
<li>The following unreserved characters are <a href="https://tools.ietf.org/html/rfc3986#section-2.1">percent decoded</a> (converted from their <code>%XX</code> encoded form back to the original character):
<ul>
<li>Alphabetical characters: <code>a</code>-<code>z</code>, <code>A</code>-<code>Z</code> (decoded from <code>%41</code>-<code>%5A</code> and <code>%61</code>-<code>%7A</code>)</li>
<li>Digit characters: <code>0</code>-<code>9</code> (decoded from <code>%30</code>-<code>%39</code>)</li>
<li>hyphen <code>-</code> (<code>%2D</code>), period <code>.</code> (<code>%2E</code>), underscore <code>_</code> (<code>%5F</code>), and tilde <code>~</code> (<code>%7E</code>)</li>
</ul>
</li>
<li>These reserved characters are not encoded or decoded: <code>: / ? # [ ] @ ! $ &amp; ' ( ) * + , ; =</code></li>
<li>Other characters, for example literal byte values, are percent encoded.</li>
<li>Percent encoded representations are converted to upper case.</li>
<li>URL paths are normalized according to the <a href="https://tools.ietf.org/html/rfc3986#section-5.2.4">Remove Dot Segments</a> protocol.</li>
</ul>
<h2 id="cloudflare-normalization">Cloudflare normalization</h2>
<p>When using the Cloudflare URL normalization, some extra normalization techniques will be applied to URLs of incoming requests, in the following order:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/12974.md")
</div>
