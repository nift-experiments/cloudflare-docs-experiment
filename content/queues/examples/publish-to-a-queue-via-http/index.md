---
cp9:
  canonical: https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/
  description: Publish to a Queue directly via HTTP and Workers.
  full_title: Queues - Publish Directly via HTTP · Cloudflare Queues docs
  head_html: <title>Queues - Publish Directly via HTTP · Cloudflare Queues docs</title><meta name="generator" content="Nift"><meta name="description" content="Publish to a Queue directly via HTTP and Workers."><link rel="canonical" href="https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/index.md"><meta property="og:title" content="Queues - Publish Directly via HTTP · Cloudflare Queues docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Publish to a Queue directly via HTTP and Workers."><meta property="og:url" content="https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Queues"><meta name="algolia_product_filter" content="Queues"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Queues"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/#page","headline":"Queues - Publish Directly via HTTP \u00b7 Cloudflare Queues docs","description":"Publish to a Queue directly via HTTP and Workers.","url":"https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /queues/examples/publish-to-a-queue-via-http/
  schema: 1
---
<p class="article-summary">Publish to a Queue directly via HTTP.</p>
<p>The following example shows you how to publish messages to a Queue from any HTTP client, using a Cloudflare API token to authenticate.</p>
<p>This allows you to write to a Queue from any service or programming language that supports HTTP, including Go, Rust, Python or even a Bash script.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>A <a href="/queues/get-started/#3-create-a-queue">queue created</a> via the <a href="https://dash.cloudflare.com">Cloudflare dashboard</a> or the <a href="/workers/wrangler/install-and-update/">wrangler CLI</a>.</li>
<li>A Cloudflare API token with the <code>Queues Edit</code> permission.</li>
</ul>
<h3 id="1-send-a-test-message"><ol>
<li>Send a test message</li>
</ol></h3>
<p>To make sure you successfully authenticate and write a message to your queue, use <code>curl</code> on the command line:</p>
<pre tabindex="0"><code class="language-sh">&#35; Make sure to replace the placeholder with your shared secret&#10;curl -XPOST -H &quot;Authorization: Bearer &lt;paste-your-api-token-here&gt;&quot; &quot;https://api.cloudflare.com/client/v4/accounts/&lt;paste-your-account-id-here&gt;/queues/&lt;paste-your-queue-id-here&gt;/messages&quot; --data &#x27;{ &quot;body&quot;: { &quot;greeting&quot;: &quot;hello&quot; } }&#x27;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">{&quot;success&quot;:true}&#10;</code></pre>
<p>This will issue a HTTP POST request, and if successful, return a HTTP 200 with a <code>success: true</code> response body.</p>
<ul>
<li>If you receive a HTTP 403, this is because your API token is invalid or does not have the <code>Queues Edit</code> permission.</li>
</ul>
<p>For full documentation about the HTTP Push API, refer to the <a href="https://developers.cloudflare.com/api/resources/queues/subresources/messages/">Cloudflare API documentation</a>.</p>
