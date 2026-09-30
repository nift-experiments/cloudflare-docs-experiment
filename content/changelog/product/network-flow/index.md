---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product/network-flow/
  description: '2026-02-17'
  full_title: network-flow changelog | Cloudflare Docs
  head_html: <title>network-flow changelog | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2026-02-17"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product/network-flow/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="network-flow changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2026-02-17"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product/network-flow/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product/network-flow/#page","headline":"network-flow changelog | Cloudflare Docs","description":"2026-02-17","url":"https://developers.cloudflare.com/changelog/product/network-flow/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product/network-flow/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-one-product-name-updates"><a href="/changelog/post/2026-02-17-product-name-updates/">Cloudflare One Product Name Updates</a></h2>
<p><em>2026-02-17</em></p>
<p>We are updating naming related to some of our Networking products to better clarify their place in the Zero Trust and Secure Access Service Edge (SASE) journey.</p>
<p>We are retiring some older brand names in favor of names that describe exactly what the products do within your network. We are doing this to help customers build better, clearer mental models for comprehensive SASE architecture delivered on Cloudflare.</p>
<h4 id="2026-02-17-product-name-updates-what-s-changing">What's changing</h4>
<ul>
<li><strong>Magic WAN</strong> → <strong>Cloudflare WAN</strong></li>
<li><strong>Magic WAN IPsec</strong> → <strong>Cloudflare IPsec</strong></li>
<li><strong>Magic WAN GRE</strong> → <strong>Cloudflare GRE</strong></li>
<li><strong>Magic WAN Connector</strong> → <strong>Cloudflare One Appliance</strong></li>
<li><strong>Magic Firewall</strong> → <strong>Cloudflare Network Firewall</strong></li>
<li><strong>Magic Network Monitoring</strong> → <strong>Network Flow</strong></li>
<li><strong>Magic Cloud Networking</strong> → <strong>Cloudflare One Multi-cloud Networking</strong></li>
</ul>
<p><strong>No action is required by you</strong> — all functionality, existing configurations, and billing will remain exactly the same.</p>
<p>For more information, visit the <a href="/cloudflare-one/">Cloudflare One documentation</a>.</p>


<h2 id="network-services-navigation-update"><a href="/changelog/post/2026-01-15-networking-navigation-update/">Network Services navigation update</a></h2>
<p><em>2026-01-15</em></p>
<p>The Network Services menu structure in Cloudflare's dashboard has been updated to reflect solutions and capabilities instead of product names. This will make it easier for you to find what you need and better reflects how our services work together.</p>
<p>Your existing configurations will remain the same, and you will have access to all of the same features and functionality.</p>
<p>The changes visible in your dashboard may vary based on the products you use. Overall, changes relate to <a href="https://developers.cloudflare.com/magic-transit/">Magic Transit</a>, <a href="https://developers.cloudflare.com/magic-wan/">Magic WAN</a>, and <a href="https://developers.cloudflare.com/cloudflare-network-firewall/">Magic Firewall</a>.</p>
<p><strong>Summary of changes:</strong></p>
<ul>
<li>A new <strong>Overview</strong> page provides access to the most common tasks across Magic Transit and Magic WAN.</li>
<li>Product names have been removed from top-level navigation.</li>
<li>Magic Transit and Magic WAN configuration is now organized under <strong>Routes</strong> and <strong>Connectors</strong>. For example, you will find IP Prefixes under <strong>Routes</strong>, and your GRE/IPsec Tunnels under <strong>Connectors.</strong></li>
<li>Magic Firewall policies are now called <strong>Firewall Policies.</strong></li>
<li>Magic WAN Connectors and Connector On-Ramps are now referenced in the dashboard as <strong>Appliances</strong> and <strong>Appliance profiles.</strong> They can be found under <strong>Connectors &gt; Appliances.</strong></li>
<li>Network analytics, network health, and real-time analytics are now available under <strong>Insights.</strong></li>
<li>Packet Captures are found under <strong>Insights &gt; Diagnostics.</strong></li>
<li>You can manage your Sites from <strong>Insights &gt; Network health.</strong></li>
<li>You can find Magic Network Monitoring under <strong>Insights &gt; Network flow</strong>.</li>
</ul>
<p>If you would like to provide feedback, complete <a href="https://forms.gle/htWyjRsTjw1usdis5">this form</a>. You can also find these details in the January 7, 2026 email titled <strong>[FYI] Upcoming Network Services Dashboard Navigation Update</strong>.</p>
<p>Preview:
<img src="/assets/upstream/images/changelog/cloudflare-network-firewall/networking-overview-and-navigation.png" alt="Networking Navigation" /></p>


<h2 id="try-out-magic-network-monitoring"><a href="/changelog/post/2024-09-24-magic-network-monitoring/">Try out Magic Network Monitoring</a></h2>
<p><em>2024-09-24</em></p>
<p>The free version of Magic Network Monitoring (MNM) is now available to everyone with a Cloudflare account by default.</p>
<ol>
<li>Log in to your <a href="https://dash.cloudflare.com">Cloudflare dashboard</a>, and select your account.</li>
<li>Go to <strong>Analytics &amp; Logs</strong> &gt; <strong>Magic Monitoring</strong>.</li>
</ol>
<p><img src="/assets/upstream/images/changelog/network-flow/get-started.png" alt="Try out the free version of Magic Network Monitoring" /></p>
<p>For more details, refer to the <a href="/network-flow/get-started/">Get started guide</a>.</p>


<h2 id="explore-product-updates-for-cloudflare-one"><a href="/changelog/post/2024-06-16-cloudflare-one/">Explore product updates for Cloudflare One</a></h2>
<p><em>2024-06-16</em></p>
<p>Welcome to your new home for product updates on <a href="/cloudflare-one/">Cloudflare One</a>.</p>
<p>Our <a href="/changelog/">new changelog</a> lets you read about changes in much more depth, offering in-depth examples, images, code samples, and even gifs.</p>
<p>If you are looking for older product updates, refer to the following locations.</p>
<details class="nb-details" open><summary>Older product updates</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/17707.md")</div></details>



