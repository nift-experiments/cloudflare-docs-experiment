---
cp9:
  canonical: https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-tor/
  description: If you do not want to disclose your IP address to the resolver, you can use our Tor onion service. Resolving DNS queries through the Tor network guarantees a significantly higher level of anonymity than making the requests directly.
  full_title: DNS over Tor · Cloudflare 1.1.1.1 docs
  head_html: <title>DNS over Tor · Cloudflare 1.1.1.1 docs</title><meta name="generator" content="Nift"><meta name="description" content="If you do not want to disclose your IP address to the resolver, you can use our Tor onion service. Resolving DNS queries through the Tor network guarantees a significantly higher level of anonymity than making the requests directly."><link rel="canonical" href="https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-tor/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-tor/index.md"><meta property="og:title" content="DNS over Tor · Cloudflare 1.1.1.1 docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="If you do not want to disclose your IP address to the resolver, you can use our Tor onion service. Resolving DNS queries through the Tor network guarantees a significantly higher level of anonymity than making the requests directly."><meta property="og:url" content="https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-tor/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="1.1.1.1 (DNS Resolver)"><meta name="algolia_product_filter" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_content_group" content="Consumer services"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="1.1.1.1 (DNS Resolver)"><meta name="pcx_tags" content="Privacy,Proxying"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-tor/#page","headline":"DNS over Tor \u00b7 Cloudflare 1.1.1.1 docs","description":"If you do not want to disclose your IP address to the resolver, you can use our Tor onion service. Resolving DNS queries through the Tor network guarantees a significantly higher level of anonymity than making the requests directly.","url":"https://developers.cloudflare.com/1.1.1.1/additional-options/dns-over-tor/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Privacy","Proxying"]}</script>
  markdown: true
  noindex: false
  route: /1.1.1.1/additional-options/dns-over-tor/
  schema: 1
---
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/1817.md")
</aside>
<p>When you send a standard DNS query, both your ISP and the DNS resolver can see your IP address and the domains you look up. Cloudflare's Tor onion service routes your DNS queries through the Tor network, which guarantees a significantly higher level of anonymity than making requests directly. The resolver never sees your IP address, and your ISP cannot determine that you attempted to resolve a domain name.</p>
<p>Read more about this service in <a href="https://blog.cloudflare.com/welcome-hidden-resolver/">this blog post</a>.</p>
<h2 id="setting-up-a-tor-client">Setting up a Tor client</h2>
<p>Unlike standard DNS modes where traffic is sent directly to an IP address, the Tor network routes traffic without exposing IP addresses. This means all connections to the hidden resolver must go through a Tor client.</p>
<p>Before you start, head to the <a href="https://www.torproject.org/download/download.html.en">Tor Project website</a> to download and install a Tor client. If you use the Tor Browser, it will automatically start a <a href="https://en.wikipedia.org/wiki/SOCKS">SOCKS proxy</a> at <code>127.0.0.1:9150</code>.</p>
<p>If you use Tor from the command line, create the following configuration file:</p>
<pre tabindex="0"><code class="language-txt">SOCKSPort 9150&#10;</code></pre>
<p>Then you can run tor with:</p>
<pre tabindex="0"><code class="language-sh">tor -f tor.conf&#10;</code></pre>
<p>Also, if you use the Tor Browser, you can head to the resolver's address to see the usual 1.1.1.1 page:</p>
<pre tabindex="0"><code class="language-txt">https://dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion/&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="note">Note</h3>
@markup("md", "content/.markup/bodies/1816.md")
</aside>
<p>If you ever forget 1.1.1.1's address, use cURL to retrieve it:</p>
<pre tabindex="0"><code class="language-sh">curl -sI https://tor.cloudflare-dns.com | grep -i alt-svc&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">alt-svc: h2=&quot;dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion:443&quot;; ma=315360000; persist=1&#10;</code></pre>
<h2 id="setting-up-a-local-dns-proxy-using-socat">Setting up a local DNS proxy using socat</h2>
<p>Not all DNS clients support connecting to the Tor network directly. The <a href="http://www.dest-unreach.org/socat/"><code>socat</code></a> utility bridges this gap by forwarding local ports through the Tor proxy, so any DNS-speaking software can reach the hidden resolver.</p>
<h3 id="dns-over-tcp-tls-and-https">DNS over TCP, TLS, and HTTPS</h3>
<p>The hidden resolver listens on TCP port 53 (DNS over TCP) and port 853 (DNS over TLS). After setting up a Tor proxy, run the following <code>socat</code> command as a privileged user, setting <code>PORT</code> to 53 or 853 depending on your protocol:</p>
<pre tabindex="0"><code class="language-sh">PORT=853; socat TCP4-LISTEN:${PORT},reuseaddr,fork SOCKS4A:127.0.0.1:dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion:${PORT},socksport=9150&#10;</code></pre>
<p>From here, you can follow the regular guide for <a href="/1.1.1.1/setup/">setting up 1.1.1.1</a>, except you should always use <code>127.0.0.1</code> instead of <code>1.1.1.1</code>. If you need to access the proxy from another device, replace <code>127.0.0.1</code> in the <code>socat</code> command with your local IP address.</p>
<h3 id="dns-over-https">DNS over HTTPS</h3>
<p><a href="https://blog.cloudflare.com/welcome-hidden-resolver/">As explained in the blog post</a>, the preferred method is DNS over HTTPS (DoH), which encrypts the entire DNS query within an HTTPS connection. To set it up:</p>
<ol>
<li>
<p>Download <code>cloudflared</code> by following the guide for <a href="/1.1.1.1/encryption/dns-over-https/dns-over-https-client/">connecting to 1.1.1.1 using DNS over HTTPS clients</a>.</p>
</li>
<li>
<p>Start a Tor SOCKS proxy and use <code>socat</code> to forward port TCP:443 to localhost:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">socat TCP4-LISTEN:443,reuseaddr,fork SOCKS4A:127.0.0.1:dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion:443,socksport=9150&#10;</code></pre>
<ol start="3">
<li>Instruct your machine to treat the <code>.onion</code> address as localhost:</li>
</ol>
<pre tabindex="0"><code class="language-bash">cat &lt;&lt; EOF &gt;&gt; /etc/hosts&#10;127.0.0.1 dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion&#10;EOF&#10;</code></pre>
<p>If you run this command more than once, remove duplicate entries from <code>/etc/hosts</code> to avoid conflicts.</p>
<ol start="4">
<li>Finally, start a local DNS over UDP daemon:</li>
</ol>
<pre tabindex="0"><code class="language-sh">cloudflared proxy-dns --upstream &quot;https://dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion/dns-query&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">INFO[0000] Adding DNS upstream                           url=&quot;https://dns4torpnlfs2ifuz2s2yf3fc7rdmsbhm6rw75euj35pac6ap25zgqad.onion/dns-query&quot;&#10;INFO[0000] Starting DNS over HTTPS proxy server          addr=&quot;dns://localhost:53&quot;&#10;INFO[0000] Starting metrics server                       addr=&quot;127.0.0.1:35659&quot;&#10;</code></pre>
