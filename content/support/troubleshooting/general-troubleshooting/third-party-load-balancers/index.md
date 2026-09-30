---
cp9:
  canonical: https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/third-party-load-balancers/
  description: Troubleshoot Cloudflare with third-party load balancers.
  full_title: Third-party load balancers · Cloudflare Support docs
  head_html: <title>Third-party load balancers · Cloudflare Support docs</title><meta name="generator" content="Nift"><meta name="description" content="Troubleshoot Cloudflare with third-party load balancers."><link rel="canonical" href="https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/third-party-load-balancers/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/third-party-load-balancers/index.md"><meta property="og:title" content="Third-party load balancers · Cloudflare Support docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Troubleshoot Cloudflare with third-party load balancers."><meta property="og:url" content="https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/third-party-load-balancers/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Support"><meta name="algolia_product_filter" content="Support"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Troubleshooting"><meta name="algolia_content_type" content="Troubleshooting"><meta name="pcx_additional_products" content="Support"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/third-party-load-balancers/#page","headline":"Third-party load balancers \u00b7 Cloudflare Support docs","description":"Troubleshoot Cloudflare with third-party load balancers.","url":"https://developers.cloudflare.com/support/troubleshooting/general-troubleshooting/third-party-load-balancers/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /support/troubleshooting/general-troubleshooting/third-party-load-balancers/
  schema: 1
---
<p>This guide explains how to troubleshoot common issues when using Cloudflare in front of third-party load balancers.</p>
<hr />
<h2 id="f5-big-ip-cookie-persistence">F5 BIG-IP cookie persistence</h2>
<p>When using Cloudflare as a reverse proxy (<a href="/dns/proxy-status/#benefits">orange-clouded</a>) in front of F5 BIG-IP load balancers, you may encounter session affinity issues due to how Cloudflare maintains persistent connections.</p>
<h3 id="the-problem">The problem</h3>
<p>F5 BIG-IP load balancers typically set a session cookie at the beginning of a TCP connection (if none exists) and then ignore all cookies from subsequent HTTP requests on the same TCP connection. This breaks session affinity because Cloudflare sends multiple HTTP sessions on the same TCP connection due to HTTP keep-alive.</p>
<p>Symptoms include:</p>
<ul>
<li>Users being logged out or experiencing authentication flow issues.</li>
<li>Shopping carts showing empty at checkout.</li>
<li>Other session-dependent inconsistencies.</li>
</ul>
<h4 id="1-identify-f5-session-cookies"><ol>
<li>Identify F5 session cookies</li>
</ol></h4>
<p>F5 session cookies can have arbitrary names but typically follow a specific format:</p>
<ul>
<li>Without encryption (trivially decoded to show origin server IP and port):</li>
</ul>
<pre tabindex="0"><code class="language-txt">BIGipCookie=16908480.16415.0000;path=/; Httponly; Secure&#10;</code></pre>
<ul>
<li>With encryption:</li>
</ul>
<pre tabindex="0"><code class="language-txt">BIGipCookie=TS019a202c=01625f1893a7d6e4b2c1a0f98e7d6c5b4a3f2e1d; path=/; Httponly; Secure&#10;</code></pre>
<h4 id="2-test-for-the-issue"><ol start="2">
<li>Test for the issue</li>
</ol></h4>
<p>You can test for this issue using curl. Run multiple requests and check if the session cookie is set consistently:</p>
<pre tabindex="0"><code class="language-sh">for i in {1..100}; do curl -sI https://example.com; done 2&gt;&amp;1 | grep &quot;&lt;COOKIE_NAME&gt;&quot; | wc -l&#10;</code></pre>
<p>If the count is significantly less than 100 when proxied through Cloudflare but equals 100 when connecting directly to the origin, you are experiencing this issue.</p>
<h3 id="solution-configure-f5-oneconnect-profile">Solution: configure F5 OneConnect profile</h3>
<p>The recommended solution is to configure an F5 OneConnect profile with a single host (<code>/32</code>) mask on your F5 BIG-IP load balancer.</p>
<h4 id="how-oneconnect-helps">How OneConnect helps</h4>
<ul>
<li>The client is not fixed to a backend server by a TCP connection</li>
<li>HTTP requests are load balanced individually</li>
<li>Different cookies with different persistence information are honored within the same TCP session</li>
<li>Cookies are set with each HTTP response</li>
</ul>
<h4 id="important-considerations">Important considerations</h4>
<ol>
<li>Validate that OneConnect is compatible with your version of TMOS (Traffic Management OS).</li>
<li>Test this configuration in staging or test Virtual IP (VIP) first, as it changes how the F5 device behaves.</li>
<li>The <code>/32</code> mask is critical for proper operation with Cloudflare.</li>
</ol>
<hr />
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/load-balancing/understand-basics/session-affinity/">Session affinity</a></li>
<li><a href="/fundamentals/reference/tcp-connections/">TCP connections and keep-alives</a></li>
<li><a href="https://my.f5.com/manage/s/article/K7208">F5 K7208: Overview of the OneConnect profile</a></li>
<li><a href="https://my.f5.com/manage/s/article/K7964">F5 K7964: The BIG-IP system may appear to ignore persistence information for Keep-Alive connections</a></li>
</ul>
