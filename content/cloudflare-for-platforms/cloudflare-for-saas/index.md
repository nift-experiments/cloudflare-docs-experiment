---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/
  description: Extend Cloudflare security and performance to your customers' custom hostnames.
  full_title: Cloudflare for SaaS · Cloudflare for Platforms docs
  head_html: <title>Cloudflare for SaaS · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Extend Cloudflare security and performance to your customers&#x27; custom hostnames."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/index.md"><meta property="og:title" content="Cloudflare for SaaS · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Extend Cloudflare security and performance to your customers&#x27; custom hostnames."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Overview"><meta name="algolia_content_type" content="Overview"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/#page","headline":"Cloudflare for SaaS \u00b7 Cloudflare for Platforms docs","description":"Extend Cloudflare security and performance to your customers' custom hostnames.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/
  schema: 1
---
<p>Cloudflare for SaaS allows you to extend the security and performance benefits of Cloudflare's network to your customers via their own custom or vanity domains.</p>
<br />
<p>As a SaaS provider, you may want to support subdomains under your own zone in addition to letting your customers use their own domain names with your services. For example, a customer may want to use their vanity domain <code>app.customer.com</code> to point to an application hosted on your Cloudflare zone <code>service.saas.com</code>. Cloudflare for SaaS allows you to increase security, performance, and reliability of your customers' domains.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4065.md")
</aside>
<h2 id="benefits">Benefits</h2>
<p>When you use Cloudflare for SaaS, it helps you to:</p>
<ul>
<li>Provide custom domain support.</li>
<li>Keep your customers' traffic encrypted.</li>
<li>Keep your customers online.</li>
<li>Facilitate fast load times of your customers' domains.</li>
<li>Gain insight through traffic analytics.</li>
</ul>
<h2 id="limitations">Limitations</h2>
<p>If your customers already have their applications on Cloudflare, they cannot control some Cloudflare features for hostnames managed by your Custom Hostnames configuration, including:</p>
<ul>
<li>Argo</li>
<li>Early Hints</li>
<li>Client-side security (formerly known as Page Shield)</li>
<li>Spectrum</li>
<li>Wildcard DNS</li>
</ul>
<h2 id="how-it-works">How it works</h2>
<p>As the SaaS provider, you can extend Cloudflare's products to customer-owned custom domains by adding them to your zone <a href="/cloudflare-for-platforms/cloudflare-for-saas/domain-support/">as custom hostnames</a>. Through a suite of easy-to-use products, Cloudflare for SaaS routes traffic from custom hostnames to an origin, set up on your domain. Cloudflare for SaaS is highly customizable. Three possible configurations are shown below.</p>
<h3 id="standard-cloudflare-for-saas-configuration">Standard Cloudflare for SaaS configuration:</h3>
<p>Custom hostnames are routed to a default origin server called fallback origin. This configuration is available on all plans.</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/use-cases/Standard.png" alt="Standard case" /></p>
<h3 id="cloudflare-for-saas-with-apex-proxying">Cloudflare for SaaS with Apex Proxying:</h3>
<p>This allows you to support apex domains even if your customers are using a DNS provider that does not allow a CNAME at the apex. This is available as an add-on for Enterprise plans. For more details, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/apex-proxying/">Apex Proxying</a>.</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/use-cases/Advanced.png" alt="Advanced case" /></p>
<h3 id="cloudflare-for-saas-with-byoip">Cloudflare for SaaS with BYOIP:</h3>
<p>This allows you to support apex domains even if your customers are using a DNS provider that does not allow a CNAME at the apex. Also, you can point to your own IPs if you want to bring an IP range to Cloudflare (instead of Cloudflare provided IPs). This is available as an add-on for Enterprise plans.</p>
<p><img src="/assets/upstream/images/cloudflare-for-platforms/use-cases/Pro.png" alt="Pro Case" /></p>
<h2 id="availability">Availability</h2>
<p>Cloudflare for SaaS is bundled with non-Enterprise plans and available as an add-on for Enterprise plans. For more details, refer to <a href="/cloudflare-for-platforms/cloudflare-for-saas/plans/">Plans</a>.</p>
<h2 id="next-steps">Next steps</h2>
<p><a class="nb-link-button" href="/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/">Get started</a>
<a class="nb-link-button" href="https://blog.cloudflare.com/introducing-ssl-for-saas/">Learn more</a></p>
