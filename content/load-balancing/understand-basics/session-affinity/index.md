---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/
  description: Route repeat visitors to the same origin server.
  full_title: Session affinity · Cloudflare Load Balancing docs
  head_html: <title>Session affinity · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Route repeat visitors to the same origin server."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/index.md"><meta property="og:title" content="Session affinity · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Route repeat visitors to the same origin server."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><meta name="pcx_tags" content="Cookies"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/#page","headline":"Session affinity \u00b7 Cloudflare Load Balancing docs","description":"Route repeat visitors to the same origin server.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/session-affinity/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Cookies"]}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/session-affinity/
  schema: 1
---
<p>When you enable session affinity, your load balancer directs all requests from a particular end user to a specific endpoint. This continuity preserves information about the user session — such as items in their shopping cart — that might otherwise be lost if requests were spread out among multiple servers.</p>
<p>Session affinity can also help reduce network requests, leading to savings for customers with usage-based billing.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10316.md")
</aside>
<h2 id="types">Types</h2>
<p>Session affinity specifies the type of session affinity the load balancer should use unless specified as <code>&quot;none&quot;</code> or <code>&quot;&quot;</code> (default).</p>
<h3 id="by-cloudflare-cookie-only">By Cloudflare cookie only</h3>
<p>On the first request to a proxied load balancer, a cookie is generated, encoding information of which endpoint the request will be forwarded to. Subsequent requests, by the same client to the same load balancer, will be sent to the endpoint the cookie encodes for the duration of the cookie and as long as the endpoint remains healthy. If the cookie has expired or the endpoint is unhealthy, a new endpoint is calculated and used.</p>
<h4 id="how-does-it-work">How does it work?</h4>
<p>Session affinity automatically directs requests from the same client to the same endpoint:</p>
<ol>
<li>When a client makes its first request, Cloudflare sets a <code>__cflb</code> cookie on the client (to track the associated endpoint).</li>
<li>Subsequent requests by the same client are forwarded to that endpoint for the duration of the cookie and as long as the endpoint remains healthy.</li>
<li>If the cookie expires or the endpoint becomes unhealthy, Cloudflare sets a new cookie tracking the new failover endpoint.</li>
</ol>
<pre tabindex="0"><code class="language-mermaid">    flowchart LR&#10;      accTitle: Session affinity process&#10;      accDescr: Session affinity directs requests from the same client to the same server.&#10;     A[Client] --Request--&gt; B{&lt;code&gt;__cflb&lt;/code&gt; cookie set?}&#10;     B --&gt;|Yes| C[Route to previous endpoint]&#10;     C --&gt; O2&#10;     B ----&gt;|No| E[Follow normal routing]&#10;     E --&gt; O2&#10;     E --Set &lt;code&gt;__cflb&lt;/code&gt; cookie--&gt; A&#10;     subgraph P1 [Pool 1]&#10;        O1[Endpoint 1]&#10;        O2[Endpoint 2]&#10;     end&#10;</code></pre>
<br/>
<p>All cookie-based sessions default to 23 hours unless you set a custom session <em>Time to live</em> (TTL).</p>
<p>The session cookie is secure when <a href="/ssl/edge-certificates/additional-options/always-use-https/">Always Use HTTPS</a> is enabled. Additionally, HttpOnly is always enabled for the cookie to prevent cross-site scripting attacks.</p>
<h3 id="by-cloudflare-cookie-and-client-ip-fallback">By Cloudflare cookie and Client IP fallback</h3>
<p>This behaves similar to <code>cookie</code> except the initial endpoint selection is stable and based on the client's IP address.</p>
<h3 id="by-http-header">By HTTP header</h3>
<p>On the first request to a proxied load balancer, a session key based on the configured HTTP headers is generated. The session key encodes the request headers used for storing which endpoint the request will be forwarded to during the load balancer session state. Subsequent requests to the load balancer with the same headers will be sent to the same endpoint, for the duration of the session and as long as the endpoint remains healthy. If the session has been idle for the duration of session affinity TTL seconds or the endpoint is unhealthy, then a new endpoint is calculated and used.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10315.md")
</aside>
<h4 id="control-how-headers-are-used">Control how headers are used</h4>
<p>By default, at least one of the HTTP headers that you configure for session affinity by HTTP header must be present on requests sent to your load balancer in order for header-based sessions to be created. If a client adds or removes HTTP headers on their requests and they have already established a session, a new session will be created based on the new HTTP headers found in subsequent requests as long as they are specified in your configuration.</p>
<p>If you would like to require all of your configured HTTP headers to be present on requests in order for sessions to be created, then set <code>session_affinity_attributes.require_all_headers</code> to <code>true</code> via the Cloudflare API or toggle <code>Require all headers</code> to <code>enabled</code> in the Cloudflare dashboard when editing your load balancer.</p>
<hr />
<h2 id="enabling-session-affinity-from-the-cloudflare-dashboard">Enabling Session Affinity from the Cloudflare dashboard</h2>
<p>Enable Session Affinity when you <a href="/load-balancing/load-balancers/create-load-balancer/">create or edit a load balancer</a>, during the <strong>Hostname</strong> step.</p>
<p>If you enable Session Affinity, choose one of the following options:</p>
<ul>
<li><strong>By Cloudflare cookie only</strong>: Sets a <code>__cflb</code> cookie to track the associated endpoint.</li>
<li><strong>By Cloudflare cookie and Client IP fallback</strong>: Sets a <code>__cflb</code> cookie, but also uses the client IP address when no session affinity cookie is provided.</li>
<li><strong>By HTTP header</strong>.</li>
</ul>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/10314.md")
</aside>
<hr />
<h2 id="enabling-session-affinity-via-the-cloudflare-api">Enabling Session Affinity via the Cloudflare API</h2>
<p>Session affinity is a property of load balancers, which you can set with the following endpoints:</p>
<ul>
<li><a href="/api/resources/load_balancers/methods/create/">Create a load balancer</a></li>
<li><a href="/api/resources/load_balancers/methods/update/">Edit a load balancer</a></li>
</ul>
<p>Customize the behavior of session affinity by using the <code>session_affinity</code>, <code>session_affinity_ttl</code>, and <code>session_affinity_attributes</code> parameters.</p>
<p>To enable session affinity by HTTP header, set the <code>session_affinity</code> value to <code>header</code> and add your
HTTP header names to <code>session_affinity_attributes.headers</code>.</p>
<p>For more details on API commands in context, refer to <a href="/load-balancing/load-balancers/create-load-balancer/">Create a load balancer with the API</a>.</p>
<hr />
<h2 id="endpoint-drain">Endpoint Drain</h2>
<p>Drain or remove all traffic from an endpoint without affecting any active customers using endpoint drain. For more details on endpoint drain, refer to <a href="/load-balancing/additional-options/planned-maintenance/#gradual-rotation">Performing planned maintenance</a>.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important-1">Important</h3>
@markup("md", "content/.markup/bodies/10313.md")
</aside>
<h2 id="zero-downtime-failover">Zero-Downtime Failover</h2>
<p>Zero-Downtime Failover automatically sends traffic to endpoints within a pool during transient network issues. This helps reduce errors shown to your users when issues occur in between active health monitors.</p>
<p>You can enable one of three options:</p>
<ul>
<li><strong>None</strong>: No failover will take place and errors may show to your users.</li>
<li><strong>Temporary</strong>: Traffic will be sent to other endpoint(s) until the originally pinned endpoint is available.</li>
<li><strong>Sticky</strong>: The session affinity cookie is updated and subsequent requests are sent to the new endpoint moving forward as needed.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10312.md")
</aside>
