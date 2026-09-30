<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>April 17, 2026</time><h2 id="post-title">Smart Tiered Cache optimizes public cloud origins</h2>
<div class="changelog-badges"><span>cache</span></div><div class="changelog-body"><p>You can now achieve higher cache HIT rates and reduce origin load for origins hosted on public cloud providers with <a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Smart Tiered Cache</a>. By setting a cloud region hint for your origin, Cloudflare selects the optimal upper-tier data center for that cloud region, funneling all cache MISSes through a single location close to your origin.</p>
<p>Previously, Smart Tiered Cache could not reliably select an optimal upper tier for origins behind anycast or regional unicast networks commonly used by cloud providers. Origins on AWS, GCP, Azure, and Oracle Cloud would fall back to a multi-upper-tier topology, resulting in lower cache HIT rates and more requests reaching your origin.</p>
<h4 id="how-it-works">How it works</h4>
<p>Set a cloud region hint (for example, <code>aws/us-east-1</code> or <code>gcp/europe-west1</code>) for your origin IP or hostname. Smart Tiered Cache uses this hint along with real-time latency data to select a primary upper tier close to your cloud region, plus a fallback in a different location for resilience.</p>
<ul>
<li><strong>Supported providers</strong>: AWS, GCP, Azure, and Oracle Cloud.</li>
<li><strong>All plans</strong>: Available on Free, Pro, Business, and Enterprise plans at no additional cost.</li>
<li><strong>Dashboard and API</strong>: Configure from <strong>Caching</strong> &gt; <strong>Tiered Cache</strong> &gt; <strong>Origin Configuration</strong>, or use the API and Terraform.</li>
</ul>
<h4 id="get-started">Get started</h4>
<p>To get started, enable <a href="/cache/how-to/tiered-cache/">Smart Tiered Cache</a> and set a cloud region hint for your origin in the <a href="/cache/how-to/tiered-cache/#public-cloud-origins">Tiered Cache settings</a>.</p>
</div></article></div>
