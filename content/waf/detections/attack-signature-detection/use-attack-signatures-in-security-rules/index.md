---
cp9:
  canonical: https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/
  description: Create scoped Security Rules from reviewed attack signature confidence, category, and Ref metadata.
  full_title: Use attack signatures in Security Rules · Cloudflare Web Application Firewall (WAF) docs
  head_html: <title>Use attack signatures in Security Rules · Cloudflare Web Application Firewall (WAF) docs</title><meta name="generator" content="Nift"><meta name="description" content="Create scoped Security Rules from reviewed attack signature confidence, category, and Ref metadata."><link rel="canonical" href="https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/index.md"><meta property="og:title" content="Use attack signatures in Security Rules · Cloudflare Web Application Firewall (WAF) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Create scoped Security Rules from reviewed attack signature confidence, category, and Ref metadata."><meta property="og:url" content="https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WAF"><meta name="algolia_product_filter" content="WAF"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="WAF"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/#page","headline":"Use attack signatures in Security Rules \u00b7 Cloudflare Web Application Firewall (WAF) docs","description":"Create scoped Security Rules from reviewed attack signature confidence, category, and Ref metadata.","url":"https://developers.cloudflare.com/waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /waf/detections/attack-signature-detection/use-attack-signatures-in-security-rules/
  schema: 1
---
<p>Attack Signature Detection fields let Security Rules act on matching traffic. The detection fields do not apply actions by themselves.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15537.md")
</aside>
<h2 id="create-a-mitigation-policy">Create a mitigation policy</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15538.md")
</div>
<p>Start with the narrowest application scope that meets your security objective. Treat low-confidence signatures as candidates for application-specific review instead of broad blocking.</p>
<p>You can use these fields in Security Rules created in the dashboard or through the API. For rule creation steps, refer to <a href="/waf/custom-rules/create-dashboard/">Create a custom rule in the dashboard</a> or <a href="/waf/custom-rules/create-api/">Create a custom rule via API</a>.</p>
<h2 id="match-a-category">Match a category</h2>
<p>This expression matches the SQL injection category:</p>
<pre tabindex="0"><code class="language-txt">any(cf.waf.signature.request.categories[*] eq &quot;sqli&quot;)&#10;</code></pre>
<p>Use the same array expression for another category, including a specific CVE category. Review historical matches before selecting an action.</p>
<h2 id="match-confidence">Match confidence</h2>
<p>This expression matches high-confidence signatures:</p>
<pre tabindex="0"><code class="language-txt">any(cf.waf.signature.request.confidence[*] eq &quot;high&quot;)&#10;</code></pre>
<p>Replace <code>high</code> with <code>low</code> to match low-confidence signatures. You can create separate rules to apply different actions to each confidence level.</p>
<h2 id="match-a-signature-ref">Match a signature Ref</h2>
<p>This expression matches a specific signature Ref:</p>
<pre tabindex="0"><code class="language-txt">any(cf.waf.signature.request.refs[*] eq &quot;d68f8101f6e14e25aefcaea69c530a29&quot;)&#10;</code></pre>
<p>The Ref is the same value as the corresponding Managed Rule public Rule ID. Use this mapping to reconcile the rule with your Managed Rules configuration.</p>
<h2 id="scope-rules-and-exceptions">Scope rules and exceptions</h2>
<p>Combine a signature condition with request properties in the rule builder. Use properties such as hostname, path, and method to limit mitigation to the affected application surface.</p>
<p>For a known false positive, exclude the legitimate endpoint from mitigation. Keep protection for the rest of the application. Validate combined expressions in the rule builder before deployment.</p>
<h2 id="understand-rule-ordering">Understand rule ordering</h2>
<p>Attack Signature Detection and Managed Rules have no special interaction. A Custom Rule using a detection field follows normal Custom Rules ordering.</p>
<p>A terminating action stops request processing at that rule. Managed Rules do not evaluate the same request. A non-terminating <em>Log</em> action lets processing continue to Managed Rules.</p>
<h2 id="compare-with-managed-rules">Compare with Managed Rules</h2>
<p>To compare the two products without changing traffic:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/15539.md")
</div>
<p>Verify whether Managed Rules already mitigate the traffic before adding duplicate handling. Recheck your Security Rules after application releases or major traffic changes.</p>
<p>For field types and Logpush mappings, refer to <a href="/waf/detections/attack-signature-detection/fields/">Attack Signature Detection fields</a>.</p>
