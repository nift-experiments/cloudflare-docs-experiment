---
cp9:
  canonical: https://developers.cloudflare.com/data-localization/regional-services/spectrum-applications/
  description: Regionalize Spectrum HTTP/S applications, with support for Static IPs and BYOIP.
  full_title: Regionalized Spectrum Applications · Cloudflare Data Localization Suite docs
  head_html: <title>Regionalized Spectrum Applications · Cloudflare Data Localization Suite docs</title><meta name="generator" content="Nift"><meta name="description" content="Regionalize Spectrum HTTP/S applications, with support for Static IPs and BYOIP."><link rel="canonical" href="https://developers.cloudflare.com/data-localization/regional-services/spectrum-applications/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/data-localization/regional-services/spectrum-applications/index.md"><meta property="og:title" content="Regionalized Spectrum Applications · Cloudflare Data Localization Suite docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Regionalize Spectrum HTTP/S applications, with support for Static IPs and BYOIP."><meta property="og:url" content="https://developers.cloudflare.com/data-localization/regional-services/spectrum-applications/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Data Localization Suite"><meta name="algolia_product_filter" content="Data Localization Suite"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Data Localization Suite"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/data-localization/regional-services/spectrum-applications/#page","headline":"Regionalized Spectrum Applications \u00b7 Cloudflare Data Localization Suite docs","description":"Regionalize Spectrum HTTP/S applications, with support for Static IPs and BYOIP.","url":"https://developers.cloudflare.com/data-localization/regional-services/spectrum-applications/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /data-localization/regional-services/spectrum-applications/
  schema: 1
---
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7410.md")
</aside>
<p>Regionalized Spectrum Applications regionalize HTTP/S traffic using <a href="/spectrum/">Spectrum</a>, Cloudflare's Layer 4 proxy. Unlike <a href="/data-localization/regional-services/regional-hostnames/">Regional Hostnames</a> — which steer proxied hostnames using Cloudflare's shared anycast IP addresses — a Regionalized Spectrum Application assigns a dedicated IP to your hostname, and that IP signals that all traffic to it must be processed in a specific region.</p>
<p>Choose this option when you need to regionalize traffic that is addressed by IP, or when you need to combine Regional Services with <a href="/spectrum/about/static-ip/">Spectrum Static IPs</a> or <a href="/byoip/">Bring Your Own IP (BYOIP)</a>.</p>
<h2 id="how-it-works">How it works</h2>
<p>You create a Spectrum HTTP/S application for each hostname you want to regionalize. Cloudflare assigns a single processing region to the zone, and that region applies to <strong>all</strong> Spectrum HTTP/S applications in that zone — you configure one region per zone, not one per application. From then on, traffic to each application's IP terminates TLS and is processed only within the configured region, following the same in-region processing model described in <a href="/data-localization/regional-services/">Regional Services</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li><a href="/spectrum/">Spectrum</a> is included in your Enterprise contract. Spectrum is an add-on, so it must be part of your contract before it can be enabled.</li>
<li>Your account has the <strong>Regional Services</strong> and <strong>Spectrum</strong> entitlements enabled. Contact your account team to enable them.</li>
<li>You have a hostname proxied through Cloudflare that you want to regionalize.</li>
<li>If you want to use your own addresses, you have onboarded <a href="/spectrum/about/static-ip/">Spectrum Static IPs</a> or a <a href="/byoip/">BYOIP</a> prefix.</li>
</ul>
<h2 id="set-up-a-regionalized-spectrum-application">Set up a Regionalized Spectrum Application</h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7412.md")
</div>
<h2 id="verify-the-configuration">Verify the configuration</h2>
<p>You can confirm regionalization using the same method as any other Regional Services configuration — refer to <a href="/data-localization/how-to/#verify-regional-services-behavior">Verify Regional Services behavior</a> for the general guidance.</p>
<p>Every Cloudflare HTTP response includes a <code>CF-RAY</code> header that ends with a three-letter <a href="https://en.wikipedia.org/wiki/IATA_airport_code">IATA airport code</a> identifying the data center where TLS termination occurred. Send a request to your regionalized hostname and check that the code corresponds to a data center inside your configured region:</p>
<pre tabindex="0"><code class="language-bash">curl --head https://www.example.com 2&gt;&amp;1 | grep -i cf-ray&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">cf-ray: 80cc9e64fd8a1519-MUC&#10;</code></pre>
<p>In this example, <code>MUC</code> (Munich) confirms that the request was processed in the European Union. A request sent from outside the region returns a code for an in-region data center, because out-of-region traffic is forwarded to the configured region for processing.</p>
<h2 id="custom-regions">Custom regions</h2>
<p>If the <a href="/data-localization/region-support/#region-types">managed regions</a> do not match your compliance requirements, you can request a custom region that restricts processing to a specific set of data centers. Custom regions are set up through your account team. To learn more about how custom regions work, refer to the <a href="https://blog.cloudflare.com/custom-regions/">Custom regions blog post</a>.</p>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/data-localization/regional-services/">Regional Services</a> — overview and in-region processing model.</li>
<li><a href="/data-localization/region-support/">Available regions and product support</a> — the full list of regions and their definitions.</li>
<li><a href="/spectrum/">Spectrum</a> — Cloudflare's Layer 4 proxy.</li>
</ul>
