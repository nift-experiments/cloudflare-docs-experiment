<p>E-commerce applications require exceptional performance, security, and reliability. Cloudflare protects and accelerates online stores with application security against attacks, bot security against credential stuffing and fraud, cache and image optimization for fast global delivery of product pages, load balancing and Waiting Room for handling traffic spikes, and Zaraz for server-side analytics and marketing tags.</p>
<ul class="directory-listing"><li><a href="/use-cases/e-commerce/protect/">Protect your store</a></li><li><a href="/use-cases/e-commerce/performance/">Accelerate your store&#x27;s performance</a></li><li><a href="/use-cases/e-commerce/traffic-at-scale/">Handle traffic at scale</a></li><li><a href="/use-cases/e-commerce/analytics/">Observe traffic patterns and analytics</a></li></ul>
<h2 id="architecture-patterns">Architecture patterns</h2>
<h3 id="self-hosted-storefront">Self-hosted storefront</h3>
<p>Protect and accelerate a store running on your own infrastructure:</p>
<ul>
<li><strong>SSL/TLS</strong> encrypts all traffic between shoppers and your store</li>
<li><strong>Cache</strong> serves static assets from 300+ edge locations</li>
<li><strong>Application security</strong> blocks attacks before they reach your origin</li>
<li><strong>Images</strong> optimizes product images on-the-fly</li>
</ul>
<h3 id="saas-hosted-storefront">SaaS-hosted storefront</h3>
<p>Add Cloudflare on top of a platform like Shopify, BigCommerce, or Salesforce Commerce Cloud:</p>
<ul>
<li><strong>Cloudflare for SaaS</strong> (Orange-to-Orange setup) layers your Cloudflare zone over your provider's existing Cloudflare configuration</li>
<li><strong>Application security</strong> adds protection beyond what the platform provides</li>
<li><strong>Zaraz</strong> loads analytics and marketing tags server-side to improve page speed</li>
</ul>
<h3 id="high-traffic-store">High-traffic store</h3>
<p>Handle flash sales, seasonal peaks, and viral demand:</p>
<ul>
<li><strong>Load Balancing</strong> distributes traffic across multiple origin servers</li>
<li><strong>Waiting Room</strong> queues excess visitors to prevent origin overload</li>
<li><strong>Cache</strong> and <strong>Argo Smart Routing</strong> reduce origin load and improve response times</li>
<li><strong>Health Checks</strong> detect unhealthy origins and reroute traffic automatically</li>
</ul>
<hr />
<h2 id="prerequisites">Prerequisites</h2>
<h3 id="create-a-new-application">Create a new application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> with DNS records proxied through Cloudflare. All solutions in this use case require traffic to pass through Cloudflare's network.</li>
</ul>
<h3 id="use-an-existing-application">Use an existing application</h3>
<ul>
<li>A <a href="https://dash.cloudflare.com/sign-up">Cloudflare account</a>.</li>
<li>A domain <a href="/fundamentals/manage-domains/add-site/">added to Cloudflare</a> with DNS records proxied through Cloudflare's network.</li>
<li>If your store is hosted on a SaaS platform that already uses Cloudflare — such as <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/shopify/">Shopify</a>, <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/bigcommerce/">BigCommerce</a>, or <a href="/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/provider-guides/salesforce-commerce-cloud/">Salesforce Commerce Cloud</a> — follow the setup steps in the provider guide for your platform to add your own Cloudflare zone on top of your provider's existing configuration.</li>
</ul>
<hr />
<h2 id="related-resources">Related resources</h2>
<div class="nb-card-grid">
@input("content/.markup/bodies/15235.md")
</div>
