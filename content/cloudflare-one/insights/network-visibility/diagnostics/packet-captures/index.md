---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/
  description: Request, monitor, and download packet captures to diagnose network issues.
  full_title: Packet captures · Cloudflare One docs
  head_html: <title>Packet captures · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Request, monitor, and download packet captures to diagnose network issues."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/index.md"><meta property="og:title" content="Packet captures · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Request, monitor, and download packet captures to diagnose network issues."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Debugging"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/#page","headline":"Packet captures \u00b7 Cloudflare One docs","description":"Request, monitor, and download packet captures to diagnose network issues.","url":"https://developers.cloudflare.com/cloudflare-one/insights/network-visibility/diagnostics/packet-captures/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Debugging"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/insights/network-visibility/diagnostics/packet-captures/
  schema: 1
---
<p>Packet captures record network traffic flowing through Cloudflare's network so you can analyze individual <span class="nb-glossary-tooltip" title="data packet">packets</span> for troubleshooting or security investigations. The output is contained within one or more files in PCAP format, which you can open in tools like <a href="https://www.wireshark.org/">Wireshark</a>.</p>
<p>There are two capture types:</p>
<ul>
<li><strong>Sample</strong> captures query historical traffic data that has already passed through Cloudflare's network. They complete immediately and can be downloaded directly from the API, or from the Cloudflare dashboard.</li>
<li><strong>Full</strong> captures actively monitor for new traffic matching your filters and write the complete packet data to a cloud storage bucket you own. Before starting a full capture, you must first <a href="/cloudflare-one/insights/network-visibility/diagnostics/buckets/">configure a bucket</a>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4996.md")
</aside>
<h2 id="send-a-packet-capture-request">Send a packet capture request</h2>
<p>Currently, when a packet capture is requested, packets flowing through Cloudflare's global network via the Magic Transit system are captured. The default API field for this is <code>&quot;system&quot;: &quot;magic-transit&quot;</code>, both for the request and response.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/4995.md")
</aside>
<h3 id="packet-capture-limits">Packet capture limits</h3>
<p><strong>Sample and full</strong></p>
<ul>
<li><code>time_limit</code>: The minimum value is <code>1</code> second and maximum value is <code>300</code> seconds.</li>
<li><code>packet_limit</code>: The minimum value is <code>1</code> packet and maximum value is <code>10000</code> packets.</li>
</ul>
<p><strong>Full</strong></p>
<ul>
<li><code>byte_limit</code>: The minimum value is <code>1</code> byte and maximum value is <code>1000000000</code> bytes (1 GB).</li>
</ul>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5002.md")
</div></div>
<h2 id="check-packet-capture-status">Check packet capture status</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5005.md")
</div></div>
<p>The capture status displays one of the following options:</p>
<ul>
<li><strong>Complete</strong> (API: <code>success</code>): The capture is done and ready for download.</li>
<li><strong>In progress</strong> (API: <code>pending</code>): Packets have been captured but the PCAP file is still being assembled.</li>
<li><strong>Failure</strong>: The capture failed. For full captures, verify that your bucket is correctly configured and that Cloudflare has write access to it. For sample captures, verify your filter configuration.</li>
</ul>
<h2 id="download-packet-captures">Download packet captures</h2>
<p>After your request finishes processing, you can download your packet captures.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5008.md")
</div></div>
<h2 id="list-packet-captures">List packet captures</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/5011.md")
</div></div>
