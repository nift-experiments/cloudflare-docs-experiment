---
cp9:
  canonical: https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/
  description: Troubleshoot issues with client certificates
  full_title: Troubleshooting client certificates · Cloudflare SSL/TLS docs
  head_html: <title>Troubleshooting client certificates · Cloudflare SSL/TLS docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot issues with client certificates"><link rel="canonical" href="https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/index.md"><meta property="og:title" content="Troubleshooting client certificates · Cloudflare SSL/TLS docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot issues with client certificates"><meta property="og:url" content="https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="SSL/TLS"><meta name="algolia_product_filter" content="SSL/TLS"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="SSL/TLS"><meta name="pcx_tags" content="mTLS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/#page","headline":"Troubleshooting client certificates \u00b7 Cloudflare SSL/TLS docs","description":"Troubleshoot issues with client certificates","url":"https://developers.cloudflare.com/ssl/client-certificates/troubleshooting/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["mTLS"]}</script>
  markdown: true
  noindex: false
  route: /ssl/client-certificates/troubleshooting/
  schema: 1
---
<p>If your query returns an error even after configuring and embedding a client SSL certificate, check the following settings.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14012.md")
</aside>
<hr />
<h2 id="check-ssl-tls-handshake">Check SSL/TLS handshake</h2>
<p>On your terminal, use the following command to check whether an SSL/TLS connection can be established successfully between the client and the API endpoint.</p>
<pre tabindex="0"><code class="language-sh">curl --verbose --cert /path/to/certificate.pem --key /path/to/key.pem https://your-api-endpoint.com&#10;</code></pre>
<p>If the SSL/TLS handshake cannot be completed, check whether the certificate and the private key are correct.
If the handshake completes but requests are still blocked, confirm that Cloudflare is verifying the client certificate.</p>
<hr />
<h2 id="check-mtls-hosts">Check mTLS hosts</h2>
<p>Check whether <a href="/ssl/client-certificates/enable-mtls/">mTLS has been enabled</a> for the correct host. The host should match the API endpoint that you want to protect.</p>
<hr />
<h2 id="review-mtls-rules">Review mTLS rules</h2>
<p>To review mTLS rules, consider the steps below. For further guidance refer to <a href="/waf/custom-rules/create-dashboard/">Custom rules</a>.</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Security rules</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>
<p>On a specific rule, select <strong>Edit</strong>.</p>
</li>
<li>
<p>On that rule, check whether:</p>
<ul>
<li>The Expression Preview is correct.</li>
<li>The hostname, if defined, matches your API endpoint. For example, for the API endpoint <code>api.trackers.ninja/time</code>, the rule should look like:</li>
</ul>
</li>
</ol>
<pre tabindex="0"><code class="language-txt">(http.host in {&quot;api.trackers.ninja&quot;} and not cf.tls_client_auth.cert_verified)&#10;</code></pre>
<ol start="4">
<li>To edit the rule, either use the user interface or select <strong>Edit expression</strong>.</li>
</ol>
<hr />
<h2 id="advanced-debugging">Advanced debugging</h2>
<p>You can use <a href="/workers/">Cloudflare Workers</a> to debug client certificate validation failures.</p>
<ol>
<li>Create a Worker to debug print <a href="/workers/runtime-apis/request/#incomingrequestcfproperties">cf.properties</a>:</li>
</ol>
<pre tabindex="0"><code class="language-js">export default {&#10;  async fetch(request, env, ctx) {&#10;    console.info({ message: JSON.stringify(request.cf, null, 2) });&#10;    return new Response(JSON.stringify(request.cf, null, 2))&#10;  }&#10;};&#10;</code></pre>
<ol start="2">
<li>
<p>Associate the Worker with the hostname where mTLS is enabled using a <a href="/workers/configuration/routing/routes/">Worker route</a> or a <a href="/workers/configuration/routing/custom-domains/">Custom Domain</a>.</p>
</li>
<li>
<p>Make requests to the hostname and/or path configured, with and without sending the mTLS client certificate.</p>
</li>
<li>
<p>View your logs on the <a href="/workers/observability/">Observability</a> dashboard and compare the responses against the expected values listed below.</p>
</li>
</ol>
<div class="nb-dash-button"></div>
<ul>
<li>Valid certificate</li>
</ul>
<pre tabindex="0"><code class="language-json">&quot;tlsClientAuth&quot;: {&#10;  &quot;certPresented&quot;: &quot;1&quot;,&#10;  &quot;certVerified&quot;: &quot;SUCCESS&quot;,&#10;},&#10;</code></pre>
<ul>
<li>Invalid certificate (for example, self-signed certificates)</li>
</ul>
<pre tabindex="0"><code class="language-json">&quot;tlsClientAuth&quot;: {&#10;  &quot;certPresented&quot;: &quot;1&quot;,&#10;  &quot;certVerified&quot;: &quot;FAILED:self signed certificate&quot;,&#10;},&#10;</code></pre>
<ul>
<li>No certificate</li>
</ul>
<pre tabindex="0"><code class="language-json">&quot;tlsClientAuth&quot;: {&#10;  &quot;certPresented&quot;: &quot;0&quot;,&#10;  &quot;certVerified&quot;: &quot;NONE&quot;,&#10;},&#10;</code></pre>
