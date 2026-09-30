---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/dns/
  description: DNS filtering in Gateway.
  full_title: Set up DNS filtering · Cloudflare One docs
  head_html: <title>Set up DNS filtering · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="DNS filtering in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/dns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/dns/index.md"><meta property="og:title" content="Set up DNS filtering · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="DNS filtering in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/dns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/dns/#page","headline":"Set up DNS filtering \u00b7 Cloudflare One docs","description":"DNS filtering in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/get-started/dns/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/get-started/dns/
  schema: 1
---
<p>Secure Web Gateway allows you to inspect DNS traffic — the queries your devices make to translate domain names like <code>example.com</code> into IP addresses — and control which websites users can visit. Because every connection starts with a DNS lookup, DNS filtering blocks threats at the earliest stage of a connection, before the device ever reaches the destination. Use DNS policies to block malware domains, phishing sites, or entire content categories across your organization.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6609.md")
</aside>
<h2 id="1-connect-to-gateway"><ol>
<li>Connect to Gateway</li>
</ol></h2>
<p>You can filter DNS queries from individual devices (for example, employee laptops) or from entire network locations (for example, an office router). Choose the option that matches your deployment.</p>
<h3 id="connect-devices">Connect devices</h3>
<p>To filter DNS requests from an individual device such as a laptop or phone:</p>
<ol>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">Install the Cloudflare One Client</a> on your device. The Cloudflare One Client is a lightweight agent that routes the device's DNS queries through Cloudflare so Gateway can inspect and filter them.</li>
<li><a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/manual-deployment/">Enroll the Cloudflare One Client</a> in your organization's <span class="nb-glossary-tooltip" title="team name">Zero Trust instance</span> [^1]. This tells WARP which Gateway policies to enforce.</li>
<li>(Optional) If you want to display a <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">custom block page</a> instead of a generic browser error when a request is blocked, <a href="/cloudflare-one/team-and-resources/devices/user-side-certificates/">install a Cloudflare root certificate</a> on your device.</li>
</ol>
<h3 id="connect-dns-locations">Connect DNS locations</h3>
<p>To filter DNS requests from a network location such as an office or data center without installing software on each device:</p>
<ol>
<li><a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">Add the location</a> to your Cloudflare One settings. A DNS location represents a network (such as an office) whose DNS queries you want to filter.</li>
<li>On your router, browser, or OS, change the DNS server setting to point to the Cloudflare address shown in the location setup UI. This forwards all DNS queries from that network through Gateway.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/6608.md")
</aside>
<h2 id="2-verify-device-connectivity"><ol start="2">
<li>Verify device connectivity</li>
</ol></h2>
<p>To confirm that your device's DNS queries are flowing through Gateway:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong>.</li>
<li>Under <strong>Log traffic activity</strong>, enable activity logging for all DNS logs.</li>
<li>On your device, open a browser and go to any website.</li>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Insights</strong> &gt; <strong>Logs</strong> &gt; <strong>DNS</strong>.</li>
<li>Make sure DNS queries from your device appear.</li>
</ol>
<h2 id="3-create-your-first-dns-policy"><ol start="3">
<li>Create your first DNS policy</li>
</ol></h2>
<p>A DNS policy has two parts: a <strong>traffic condition</strong> that defines which queries to match (for example, all queries to gambling sites) and an <strong>action</strong> that defines what to do with matching queries (for example, block them). To create a new DNS policy:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/6613.md")
</div></div>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/">DNS policies</a>.</p>
<h2 id="4-add-optional-policies"><ol start="4">
<li>Add optional policies</li>
</ol></h2>
<p>Once your first policy is active, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/common-policies">common DNS policies</a> for other policies you may want to add. Common additions include blocking specific content categories (such as social media or streaming), enabling SafeSearch on search engines, and restricting DNS queries so devices can only use resolvers that you have approved.</p>
