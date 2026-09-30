---
cp9:
  canonical: https://developers.cloudflare.com/rules/snippets/errors/
  description: Common Snippet errors and how to resolve them.
  full_title: Troubleshoot Snippets · Cloudflare Rules docs
  head_html: <title>Troubleshoot Snippets · Cloudflare Rules docs</title><meta name="generator" content="Nift"><meta name="description" content="Common Snippet errors and how to resolve them."><link rel="canonical" href="https://developers.cloudflare.com/rules/snippets/errors/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/rules/snippets/errors/index.md"><meta property="og:title" content="Troubleshoot Snippets · Cloudflare Rules docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Common Snippet errors and how to resolve them."><meta property="og:url" content="https://developers.cloudflare.com/rules/snippets/errors/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Rules"><meta name="algolia_product_filter" content="Rules"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Rules"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/rules/snippets/errors/#page","headline":"Troubleshoot Snippets \u00b7 Cloudflare Rules docs","description":"Common Snippet errors and how to resolve them.","url":"https://developers.cloudflare.com/rules/snippets/errors/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /rules/snippets/errors/
  schema: 1
---
<h2 id="error-1201-snippet-tried-to-continue-to-origin-multiple-times">Error 1201: Snippet tried to continue to origin multiple times</h2>
<p>This error occurs when a Snippet attempts to call <code>fetch(request)</code> more than once.</p>
<h3 id="resolution">Resolution</h3>
<p>Ensure that your Snippet code only calls <code>fetch(request)</code> once. This method is used to send the modified request to the origin server, and it should be called only once per Snippet to avoid conflicts.</p>
<h2 id="error-1202-snippets-exceeded-subrequests-limit">Error 1202: Snippets exceeded subrequests limit</h2>
<p>This error occurs when the number of <span class="nb-glossary-tooltip" title="Snippets subrequest">subrequests</span> exceeds <a href="/rules/snippets/#availability">the limit</a> for your Cloudflare plan.</p>
<h3 id="resolution-1">Resolution</h3>
<p>Review your Snippet to ensure your code is within the <span class="nb-glossary-tooltip" title="Snippets subrequest">subrequest</span> <a href="/rules/snippets/#availability">limits</a> for your plan. Each subrequest counts against your limit, including any redirects within a subrequest chain.</p>
<h2 id="error-1203-snippets-exceeded-cpu-time-limit">Error 1203: Snippets exceeded CPU time limit</h2>
<p>This error occurs when a Snippet exceeds the defined <a href="/rules/snippets/#limits">CPU time limit</a> for Snippets.</p>
<h3 id="resolution-2">Resolution</h3>
<p>Review your Snippet to ensure your code is within the CPU time limit. If you need a higher CPU time limit, consider using <a href="/workers/">Cloudflare Workers</a>. Refer to <a href="/rules/snippets/when-to-use/">When to use Snippets vs Workers</a> for details.</p>
<h2 id="error-1204-snippets-exceeded-memory-limit">Error 1204: Snippets exceeded memory limit</h2>
<p>This error occurs when a Snippet exceeds the defined <a href="/rules/snippets/#limits">memory limit</a> for Snippets.</p>
<h3 id="resolution-3">Resolution</h3>
<p>Review your Snippet to ensure your code is within the memory limit. If you need a higher memory limit, consider using <a href="/workers/">Cloudflare Workers</a>. Refer to <a href="/rules/snippets/when-to-use/">When to use Snippets vs Workers</a> for details.</p>
<h2 id="error-1205-deployment-in-progress">Error 1205: Deployment in progress</h2>
<p>A new Snippet was just deployed and is currently propagating across Cloudflare's global network. During this short window, requests may not be processed as expected.</p>
<h3 id="resolution-4">Resolution</h3>
<p>This is a temporary issue. Retry your request after a few seconds — the Snippet will be active once propagation completes.</p>
<h2 id="error-1206-snippet-threw-exception">Error 1206: Snippet threw exception</h2>
<p>The Snippet encountered an unhandled JavaScript exception during execution. This may be caused by one of the following:</p>
<ul>
<li>Runtime JavaScript errors in Snippet code</li>
<li>Unhandled promise rejections</li>
<li>Type errors or reference errors</li>
</ul>
<h3 id="resolution-5">Resolution</h3>
<ul>
<li>Review the Snippet code to identify where the exception might have occurred and fix any detected bugs.</li>
<li>Add proper error handling (<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch"><code>try...catch</code></a> blocks).</li>
</ul>
<h2 id="snippets-cannot-be-renamed">Snippets cannot be renamed</h2>
<p>The name you define when creating a Snippet will be used as the Snippet ID and cannot be edited afterwards.</p>
<h3 id="resolution-6">Resolution</h3>
<p>To change the name of your Snippet, create a new Snippet and delete the old one.</p>
