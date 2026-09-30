---
cp9:
  canonical: https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/
  description: Learn how to use Terraform with Cloudflare Load Balancing product to fail traffic over as needed.
  full_title: Improve performance and reliability · Cloudflare Terraform docs
  head_html: <title>Improve performance and reliability · Cloudflare Terraform docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn how to use Terraform with Cloudflare Load Balancing product to fail traffic over as needed."><link rel="canonical" href="https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/index.md"><meta property="og:title" content="Improve performance and reliability · Cloudflare Terraform docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn how to use Terraform with Cloudflare Load Balancing product to fail traffic over as needed."><meta property="og:url" content="https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Terraform"><meta name="algolia_product_filter" content="Terraform"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Terraform"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/#page","headline":"Improve performance and reliability \u00b7 Cloudflare Terraform docs","description":"Learn how to use Terraform with Cloudflare Load Balancing product to fail traffic over as needed.","url":"https://developers.cloudflare.com/terraform/tutorial/use-load-balancing/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /terraform/tutorial/use-load-balancing/
  schema: 1
---
<p>In this tutorial, you will add a second origin for some basic round robining, and then use the <a href="/load-balancing/">Cloudflare Load Balancing</a> product to fail traffic over as needed. You will also enhance your load balancing configuration through the use of &quot;geo steering&quot; to serve results from an origin server that is geographically closest to your end users.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Completed <a href="/terraform/tutorial/initialize-terraform/">Tutorial 1</a>, <a href="/terraform/tutorial/track-history/">Tutorial 2</a> and <a href="/terraform/tutorial/configure-https-settings/">Tutorial 3</a></li>
<li><a href="/load-balancing/get-started/enable-load-balancing/">Load Balancing</a> enabled on your Cloudflare account</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14754.md")
</aside>
<h2 id="1-add-another-dns-record-for-www"><ol>
<li>Add another DNS record for www</li>
</ol></h2>
<p>Create a new branch and add a DNS record
for your Asia server:</p>
<pre tabindex="0"><code class="language-bash">git checkout -b step4-configure-load-balancing&#10;</code></pre>
<p>Add a DNS record for a second web server, located in Asia. For example purposes,
the IP address for this server is <code>198.51.100.15</code>. Add the second DNS record to
your <code>main.tf</code>:</p>
<pre tabindex="0"><code class="language-hcl">&#35; Asia origin server&#10;resource &quot;cloudflare_dns_record&quot; &quot;www_asia&quot; {&#10;  zone_id = var.zone_id&#10;  name    = &quot;www&quot;&#10;  content = &quot;198.51.100.15&quot;&#10;  type    = &quot;A&quot;&#10;  ttl     = 300&#10;  proxied = true&#10;  comment = &quot;Asia origin server&quot;&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14753.md")
</aside>
<p>Apply this change to see basic round-robin behavior:</p>
<pre tabindex="0"><code class="language-bash">terraform plan&#10;terraform apply&#10;</code></pre>
<p>Test the basic load distribution:</p>
<pre tabindex="0"><code class="language-bash">&#35; Make several requests to see both origins&#10;for i in {1..4}; do&#10;  curl https://www.example.com&#10;  sleep 1&#10;done&#10;</code></pre>
<p>Expected output:</p>
<pre tabindex="0"><code class="language-bash">Hello, this is 203.0.113.10!&#10;Hello, this is 203.0.113.10!&#10;Hello, this is 198.51.100.15!&#10;Hello, this is 203.0.113.10!&#10;</code></pre>
<p>You'll see random distribution between your two origin servers. This basic DNS-based load balancing has limitations - no health checks, no geographic steering, and unpredictable distribution patterns. For more advanced scenarios like origins in different geographies or automatic failover, you'll want to use <a href="/load-balancing/">Cloudflare's Load Balancing</a>.</p>
<h2 id="2-switch-to-using-cloudflare-s-load-balancing-product"><ol start="2">
<li>Switch to using Cloudflare's Load Balancing product</li>
</ol></h2>
<p>As described in the <a href="/learning-paths/load-balancing/concepts/">Load Balancing tutorial</a>, you will need to complete three tasks:</p>
<ol>
<li>Create a monitor to run health checks against your origin servers.</li>
<li>Create a pool of one or more origin servers that will receive load balanced traffic.</li>
<li>Create a load balancer with an external hostname — for example, <code>www.example.com</code> — and one or more pools.</li>
</ol>
<p>We can monitor the origins by creating a basic health check that makes a GET request to each origin on the URL. If the origin returns the 200 status code (OK) within five seconds, it is considered healthy. If it fails to do so three times in a row, it is considered unhealthy. This health check will be run once per minute from several regions and you can configure an email notification in the event any failures are detected.</p>
<p>In this example, the pool will be called <code>www-origins</code> with two origins added to it:</p>
<ul>
<li><code>www-us</code> (<code>203.0.113.10</code>)</li>
<li><code>www-asia</code> (<code>198.51.100.15</code>)</li>
</ul>
<p>For now, skip any sort of <a href="/load-balancing/understand-basics/traffic-steering/steering-policies/geo-steering/">geo routing</a>.</p>
<p>When you create a load balancer (LB), it will <a href="/load-balancing/load-balancers/dns-records/">replace any existing DNS records with the same name</a>. For example, if you create the <code>www.example.com</code> load balancer below, it will supersede the two <code>www</code> DNS records that you previously defined. One benefit of leaving the DNS records in place is that if you temporarily disable load balancing, connections to this hostname are still possible.</p>
<p>To achieve the above, add the load balancing configuration to <code>main.tf</code>:</p>
<pre tabindex="0"><code class="language-hcl">&#35; Health check monitor&#10;resource &quot;cloudflare_load_balancer_monitor&quot; &quot;health_check&quot; {&#10;  account_id     = var.account_id&#10;  expected_body = &quot;alive&quot;&#10;  expected_codes = &quot;2xx&quot;&#10;  method         = &quot;GET&quot;&#10;  timeout        = 5&#10;  path           = &quot;/health&quot;&#10;  interval       = 60&#10;  retries        = 2&#10;  description    = &quot;Health check for www origins&quot;&#10;  type           = &quot;https&quot;&#10;&#10;  header = {&#10;    Host = [&quot;${var.domain}&quot;]&#10;  }&#10;}&#10;&#10;&#35; Origin pool&#10;resource &quot;cloudflare_load_balancer_pool&quot; &quot;www_pool&quot; {&#10;  account_id = var.account_id&#10;  name       = &quot;www-origins&quot;&#10;  monitor    = cloudflare_load_balancer_monitor.health_check.id&#10;&#10;  origins = [{&#10;    name    = &quot;www-us&quot;&#10;    address = &quot;203.0.113.10&quot;&#10;    enabled = true&#10;  }, {&#10;    name    = &quot;www-asia&quot;&#10;    address = &quot;198.51.100.15&quot;&#10;    enabled = true&#10;  }]&#10;&#10;  description     = &quot;Primary www server pool&quot;&#10;  enabled         = true&#10;  minimum_origins = 1&#10;  notification_email = &quot;&lt;YOUR_EMAIL&gt;&quot;&#10;  check_regions   = [&quot;WEU&quot;, &quot;EEU&quot;, &quot;WNAM&quot;, &quot;ENAM&quot;, &quot;SEAS&quot;, &quot;NEAS&quot;]&#10;}&#10;&#10;&#35; Load balancer&#10;resource &quot;cloudflare_load_balancer&quot; &quot;www_lb&quot; {&#10;  zone_id       = var.zone_id&#10;  name          = &quot;www.${var.domain}&quot;&#10;  default_pools = [cloudflare_load_balancer_pool.www_pool.id]&#10;  fallback_pool = cloudflare_load_balancer_pool.www_pool.id&#10;  description   = &quot;Load balancer for www.${var.domain}&quot;&#10;  proxied       = true&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14752.md")
</aside>
<p>Preview and apply the changes:</p>
<pre tabindex="0"><code class="language-bash">terraform plan&#10;terraform apply&#10;</code></pre>
<p>Test the improved load balancing:</p>
<pre tabindex="0"><code class="language-bash">&#35; Test load distribution with health monitoring&#10;for i in {1..6}; do&#10;  echo &quot;Request $i:&quot;&#10;  curl -s https://www.example.com&#10;  sleep 2&#10;done&#10;</code></pre>
<p>Expected output:</p>
<pre tabindex="0"><code class="language-bash">Request 1:&#10;Hello, this is 198.51.100.15!&#10;Request 2:&#10;Hello, this is 203.0.113.10!&#10;Request 3:&#10;Hello, this is 198.51.100.15!&#10;Request 4:&#10;Hello, this is 203.0.113.10!&#10;Request 5:&#10;Hello, this is 203.0.113.10!&#10;Request 6:&#10;Hello, this is 198.51.100.15!&#10;</code></pre>
<p>You should now see more predictable load distribution with the added benefits of health monitoring and automatic failover.</p>
<p>Merge and verify:</p>
<pre tabindex="0"><code class="language-bash">git add main.tf&#10;git commit -m &quot;Step 4 - Create load balancer (LB) monitor, LB pool, and LB&quot;&#10;git push&#10;</code></pre>
<p>Verify the configuration is working by checking the Cloudflare dashboard under <strong>Traffic</strong> &gt; <strong>Load Balancing</strong>. You should see your monitor, pool, and load balancer with health status indicators.
Your load balancer will now:</p>
<ul>
<li>Distribute traffic intelligently between origins</li>
<li>Automatically route around unhealthy servers</li>
<li>Provide real-time health monitoring</li>
</ul>
