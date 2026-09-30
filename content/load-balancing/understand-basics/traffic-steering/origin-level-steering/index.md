---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/
  description: Steer traffic between origins within a pool.
  full_title: Local traffic steering · Cloudflare Load Balancing docs
  head_html: <title>Local traffic steering · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Steer traffic between origins within a pool."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/index.md"><meta property="og:title" content="Local traffic steering · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Steer traffic between origins within a pool."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/#page","headline":"Local traffic steering \u00b7 Cloudflare Load Balancing docs","description":"Steer traffic between origins within a pool.","url":"https://developers.cloudflare.com/load-balancing/understand-basics/traffic-steering/origin-level-steering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/understand-basics/traffic-steering/origin-level-steering/
  schema: 1
---
<p>Endpoint steering customizes how each <a href="/load-balancing/pools/">pool</a> distributes requests to its associated endpoints.</p>
<p>These distributions are a combination of two properties:</p>
<ul>
<li>The endpoint steering <a href="#policies">policy</a> chosen for your pool.</li>
<li>The <a href="#weights">weights</a> assigned to each endpoint.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/10466.md")
</aside>
<h2 id="policies">Policies</h2>
<p>When you <a href="/load-balancing/pools/create-pool/">create a pool</a>, you have to choose an option for <strong>Endpoint Steering</strong>.
<br /></p>
<ul class="directory-listing"><li><a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/random-origin-steering/">Random</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/hash-origin-steering/">Hash</a></li><li><a href="/load-balancing/understand-basics/traffic-steering/origin-level-steering/least-outstanding-requests-pools/">Least Outstanding Requests</a></li></ul>
<h2 id="weights">Weights</h2>
<p>The weight assigned to an endpoint controls the percentage of pool traffic sent to that endpoint. By default, all endpoints within a pool have a weight of <strong>1</strong>.</p>
<p>If you leave each endpoint with the default setting and choose a <strong>Random</strong> endpoint steering policy, each endpoint will receive the same percentage of traffic. If you use a <strong>Hash</strong> policy, that percentage will vary based on the IP distribution of your requests.</p>
<h3 id="customize-weights">Customize weights</h3>
<p>To customize weights when you <a href="/load-balancing/pools/create-pool/">create or edit a pool</a>, set the <strong>Weight</strong> to a number between 0 and 1 (expressed in increments of .01). Cloudflare will then send traffic to that pool based on a combination of your endpoint steering policy and the following formula.</p>
<pre tabindex="0"><code class="language-txt">% of traffic to endpoint = endpoint weight ÷ sum of all weights in the pool&#10;</code></pre>
<details class="nb-details"><summary>Endpoint weight example</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/10467.md")
</div></details>
<p>An endpoint with a weight of <strong>0</strong> should not receive any traffic sent to that pool (though the endpoint will still receive health monitor requests).</p>
<p>You can also see this value in the <strong>Percent</strong> field when creating or editing a pool in the dashboard.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note:</h3>
@markup("md", "content/.markup/bodies/10465.md")
</aside>
<h3 id="limitations">Limitations</h3>
<p>If you choose <strong>Hash</strong> for your <strong>Endpoint Steering</strong> or enable <a href="/load-balancing/understand-basics/session-affinity/">session affinity</a>, these options can affect traffic distribution.</p>
<p>Additionally, session affinity takes precedence over any selected weight or endpoint steering policy.</p>
<p>When using <a href="/load-balancing/understand-basics/proxy-modes/#dns-only-load-balancing">DNS-only load balancing</a>, DNS resolvers may cache resolved IPs for clients and affect traffic distribution.</p>
