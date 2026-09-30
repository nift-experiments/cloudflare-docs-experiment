---
cp9:
  canonical: https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/
  description: Block R-U-Dead-Yet slow POST attacks with custom rules.
  full_title: Stop R-U-Dead-Yet? (R.U.D.Y.) attacks · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Stop R-U-Dead-Yet? (R.U.D.Y.) attacks · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Block R-U-Dead-Yet slow POST attacks with custom rules."><link rel="canonical" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/index.md"><meta property="og:title" content="Stop R-U-Dead-Yet? (R.U.D.Y.) attacks · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block R-U-Dead-Yet slow POST attacks with custom rules."><meta property="og:url" content="https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/#page","headline":"Stop R-U-Dead-Yet? (R.U.D.Y.) attacks \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Block R-U-Dead-Yet slow POST attacks with custom rules.","url":"https://developers.cloudflare.com/waf/custom-rules/use-cases/stop-rudy-attacks/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/custom-rules/use-cases/stop-rudy-attacks/
  schema: 1
---
<p>R-U-Dead-Yet (R.U.D.Y.) attacks accomplish denial of service (DoS) by submitting long form fields. Use custom rules to stop these attacks by blocking requests that do not have a legitimate session cookie.</p>
<p>This example combines three expressions to target HTTP <code>POST</code> requests that do not contain a legitimate authenticated session cookie:</p>
<ul>
<li>The first expression uses the <a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.path/"><code>http.request.uri.path</code></a> field to target the paths to secure from R.U.D.Y.:</li>
</ul>
<pre tabindex="0"><code class="language-txt">http.request.uri.path matches &quot;(comment|conversation|event|poll)/create&quot;&#10;</code></pre>
<ul>
<li>The second uses a regular expression to match the format of a legitimate <code>auth_session</code> cookie. The <code>not</code> operator targets requests where that cookie is not formatted correctly:</li>
</ul>
<pre tabindex="0"><code class="language-txt">not http.cookie matches &quot;auth_session=[0-9a-zA-Z]{32}-[0-9]{10}-[0-9a-z]{6}&quot;&#10;</code></pre>
<ul>
<li>The third expression targets HTTP <code>POST</code> requests:</li>
</ul>
<pre tabindex="0"><code class="language-txt">http.request.method eq &quot;POST&quot;&#10;</code></pre>
<p>To generate the final <a href="/waf/custom-rules/create-dashboard/">custom rule</a> expression for this example, the three expressions are combined into a compound expression using the <code>and</code> operator. When an HTTP <code>POST</code> request to any of the specified URIs does not contain a properly formatted <code>auth_session</code> cookie, Cloudflare blocks the request:</p>
<ul>
<li>
<p><strong>When incoming requests match</strong>:</p>
<p>Use the expression editor:<br/>
<code>(http.request.method eq &quot;POST&quot; and http.request.uri.path matches &quot;(comment|conversation|event|poll)/create&quot; and not http.cookie matches &quot;auth_session=[0-9a-zA-Z]{32}-[0-9]{10}-[0-9a-z]{6}&quot;)</code></p>
</li>
<li>
<p><strong>Then take action</strong>: <em>Block</em></p>
</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15455.md")
</aside>
