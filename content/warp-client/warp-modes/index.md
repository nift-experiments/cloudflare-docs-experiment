---
cp9:
  canonical: https://developers.cloudflare.com/warp-client/warp-modes/
  description: Available WARP connection modes and their behavior.
  full_title: WARP modes · Cloudflare WARP client docs
  head_html: <title>WARP modes · Cloudflare WARP client docs</title><meta name="generator" content="Nift"><meta name="description" content="Available WARP connection modes and their behavior."><link rel="canonical" href="https://developers.cloudflare.com/warp-client/warp-modes/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/warp-client/warp-modes/index.md"><meta property="og:title" content="WARP modes · Cloudflare WARP client docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Available WARP connection modes and their behavior."><meta property="og:url" content="https://developers.cloudflare.com/warp-client/warp-modes/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="WARP Client"><meta name="algolia_product_filter" content="WARP Client"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="WARP Client"><meta name="pcx_tags" content="Post-quantum"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/warp-client/warp-modes/#page","headline":"WARP modes \u00b7 Cloudflare WARP client docs","description":"Available WARP connection modes and their behavior.","url":"https://developers.cloudflare.com/warp-client/warp-modes/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Post-quantum"]}</script>
  markdown: true
  noindex: false
  route: /warp-client/warp-modes/
  schema: 1
---
<p>The WARP client has several modes to better suit different connection needs.</p>
<h2 id="dns-only">DNS only</h2>
<p>Formerly known as <strong>1.1.1.1</strong>.</p>
<p>In <strong>DNS only</strong> mode, WARP routes only DNS queries through Cloudflare's 1.1.1.1 resolver and does not tunnel device traffic. DNS queries are always encrypted: <strong>DNS only (HTTPS)</strong> uses DNS-over-HTTPS (DoH), and <strong>DNS only (TLS)</strong> uses DNS-over-TLS (DoT).</p>
<p>Refer to <a href="/1.1.1.1/encryption/">1.1.1.1 resolver</a> to learn more about DNS encryption.</p>
<h2 id="traffic-and-dns">Traffic and DNS</h2>
<p>Formerly known as <strong>1.1.1.1 with WARP</strong>.</p>
<p>The WARP application uses <a href="https://blog.cloudflare.com/zero-trust-warp-with-a-masque/">MASQUE</a> to encrypt and send traffic from your device directly to Cloudflare's global network. This ensures Internet traffic between your device and the Internet is secure and private, while also preventing third parties from accessing your traffic. All traffic<sup><a href="#footnote-1">1</a></sup> tunneled over the MASQUE connection is encrypted using <a href="https://blog.cloudflare.com/post-quantum-warp/">post-quantum cryptography</a> to protect against <a href="https://www.nist.gov/cybersecurity/what-post-quantum-cryptography">harvest-now-decrypt-later attacks</a>.</p>
<p>This mode is available in three flavors:</p>
<ul>
<li><strong>Traffic and DNS (UDP)</strong> — All device traffic is routed through WARP, and DNS queries use UDP inside the tunnel.</li>
<li><strong>Traffic and DNS (TLS)</strong> — All device traffic is routed through WARP, and DNS queries are encrypted via DNS-over-TLS (DoT).</li>
<li><strong>Traffic and DNS (HTTPS)</strong> — All device traffic is routed through WARP, and DNS queries are encrypted via DNS-over-HTTPS (DoH).</li>
</ul>
<p>If the site you are visiting is already a Cloudflare customer, the content is immediately sent to your device. If not, Cloudflare uses its global network of data centers to devise the shortest path to the site. For more information, refer to our blog post <a href="https://blog.cloudflare.com/1111-warp-better-vpn/">Introducing WARP: Fixing Mobile Internet Performance and Security</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/105.md")
</aside>
<h2 id="traffic-only">Traffic only</h2>
<p>In <strong>Traffic only</strong> mode, all device traffic is routed through WARP, but DNS resolution remains managed by the device operating system.</p>
<h2 id="local-proxy">Local proxy</h2>
<p>Currently, this mode is available on desktop clients only. When WARP is configured as a local proxy, only the applications that you configure to use the proxy (HTTPS or SOCKS5) will have their traffic sent through WARP. This allows you to pick and choose which traffic is encrypted — for example, your web browser or a specific application. Everything else will not be encrypted and will be sent over a regular Internet connection.</p>
<p>Because this feature restricts WARP to just applications configured to use the local proxy, leaving all other traffic over the Internet unencrypted by default, we have hidden it in the <strong>Advanced</strong> menu. To turn it on:</p>
<ol>
<li>Navigate to <strong>Preferences</strong> &gt; <strong>Advanced</strong> and select <strong>Configure Proxy</strong>.</li>
<li>On the window that opens, check the box and configure the port you want to listen on.</li>
</ol>
<p>This will enable the <strong>Local proxy</strong> option in the <strong>WARP Settings</strong> menu.</p>
<p>If you enable <a href="/cloudflare-one/traffic-policies/http-policies/tls-decryption/#fips-compliance">FIPS compliance</a> for TLS decryption, you must <a href="/cloudflare-one/traffic-policies/http-policies/http3/#force-http2-traffic">disable QUIC</a> in your users' browsers. Otherwise, HTTP/3 traffic will bypass inspection by the WARP client.</p>
<h2 id="warp-unlimited">WARP+ Unlimited</h2>
<p>While WARP can take advantage of the many Cloudflare data centers around the world to give you a more private and robust connection, WARP+ Unlimited subscribers get access to a larger network. More cities to connect to means you are likely to be closer to a Cloudflare data center, which can reduce latency and improve your browsing speed.</p>
<p>WARP+ Unlimited is a paid, monthly subscription that can be purchased via the Apple App Store or Google Play Store.</p>
<p>To subscribe to WARP+ Unlimited:</p>
<ol>
<li>On an iOS or Android device, launch the <strong>1.1.1.1: Faster Internet</strong> app.</li>
<li>Select <strong>Settings</strong> &gt; <strong>Upgrade to WARP+</strong>. A dialog will appear with the subscription price.</li>
<li>To confirm your subscription, select <strong>Subscribe to WARP+ Unlimited</strong>. All payments are handled by the Apple/Google app store, and the payment information associated with your Apple/Google account will be charged for these subscriptions.</li>
</ol>
<p>WARP+ Unlimited is now active on this device. You can use your license key on up to five devices.</p>
<section class="footnotes"><h2 id="footnotes">Footnotes</h2><ol><li id="footnote-1">Post-quantum cryptography requires the following minimum WARP versions: <br/> **Android**: 2.4.3<br/> **iOS**: 1.11.1 <br/> **Windows, macOS, and Linux**: 2025.6.1335.0</li></ol></section>
