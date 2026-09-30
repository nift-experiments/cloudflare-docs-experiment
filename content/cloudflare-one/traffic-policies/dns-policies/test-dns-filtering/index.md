---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/
  description: Test DNS filtering in Gateway.
  full_title: Test DNS filtering · Cloudflare One docs
  head_html: <title>Test DNS filtering · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Test DNS filtering in Gateway."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/index.md"><meta property="og:title" content="Test DNS filtering · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Test DNS filtering in Gateway."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="DNS"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/#page","headline":"Test DNS filtering \u00b7 Cloudflare One docs","description":"Test DNS filtering in Gateway.","url":"https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["DNS"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/traffic-policies/dns-policies/test-dns-filtering/
  schema: 1
---
<p>This section covers how to validate your Gateway DNS configuration. Testing your policies after setup helps confirm that queries are being filtered as expected before you rely on them in production.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>Before you start, make sure your device is sending DNS queries to Gateway. You can do this in one of two ways:</p>
<ul>
<li><strong>Cloudflare One Client</strong> — If your device runs the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/">Cloudflare One Client</a>, DNS queries route through Gateway automatically.</li>
<li><strong>DNS location</strong> — If you are using a DNS-only deployment (without the Cloudflare One Client), verify that your network's DNS resolver points to your <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">Gateway DNS location's</a> IP address.</li>
</ul>
<h2 id="test-a-dns-policy">Test a DNS policy</h2>
<p>Once you have created a DNS policy to block a domain, you can use either <code>dig</code> (a command-line DNS lookup tool, available on macOS and Linux) or <code>nslookup</code> (available on Windows) to see if the policy is working as intended.</p>
<p>For example, if you created a policy to block <code>example.com</code>, you can do the following to see if Gateway is successfully blocking <code>example.com</code>:</p>
<ol>
<li>
<p>Open your terminal.</p>
</li>
<li>
<p>Type <code>dig example.com</code> (<code>nslookup example.com</code> if you are using Windows) and press <strong>Enter</strong>.</p>
</li>
<li>
<p>In the <code>dig</code> output, check the <code>status:</code> field in the header line (the line starting with <code>;; -&gt;&gt;HEADER&lt;&lt;-</code>). If the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">block page</a> is turned off for the policy, you should see <code>REFUSED</code> — a DNS response code meaning the server declined to answer the query:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">dig example.com&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#10;; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; example.com&#10;;; global options: +cmd&#10;;; Got answer:&#10;;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: REFUSED, id: 6503&#10;;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0&#10;&#10;;; QUESTION SECTION:&#10;;example.com.                   IN      A&#10;&#10;;; Query time: 46 msec&#10;;; SERVER: 172.64.36.1#53(172.64.36.1)&#10;;; WHEN: Tue Mar 10 20:22:18 CDT 2020&#10;;; MSG SIZE  rcvd: 29&#10;</code></pre>
<p>If the <a href="/cloudflare-one/reusable-components/custom-pages/gateway-block-page/">block page</a> is enabled for the policy, you should see <code>NOERROR</code> (meaning the query was resolved) in the header with <code>162.159.36.12</code> and <code>162.159.46.12</code> as the answers. These are Cloudflare's block page IP addresses:</p>
<pre tabindex="0"><code class="language-sh">dig example.com&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#10;; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; example.com&#10;;; global options: +cmd&#10;;; Got answer:&#10;;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR id: 14531&#10;;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1&#10;&#10;;; OPT PSEUDOSECTION:&#10;; EDNS: version: 0, flags:; udp: 1452&#10;;; QUESTION SECTION:&#10;;example.com.                   IN      A&#10;&#10;;;ANSWER SECTION:&#10;example.com.            60      IN      A                  162.159.36.12&#10;example.com.            60      IN      A                  162.159.46.12&#10;&#10;;; Query time: 53 msec&#10;;; SERVER: 172.64.36.1#53(172.64.36.1)&#10;;; WHEN: Tue Mar 10 20:19:52 CDT 2020&#10;;; MSG SIZE  rcvd: 83&#10;</code></pre>
<h3 id="test-a-security-or-content-category">Test a security or content category</h3>
<p>If you are blocking a <a href="/cloudflare-one/traffic-policies/dns-policies/#security-categories">security category</a> or a <a href="/cloudflare-one/traffic-policies/dns-policies/#content-categories">content category</a>, you can test that the policy is working by using the <a href="#common-test-domains">test domain</a> associated with each category.</p>
<p>Once you have configured your Gateway policy to block the category, the test domain will show a block page when you attempt to visit the domain in your browser, or will return <code>REFUSED</code> when you perform <code>dig</code> using the command-line interface.</p>
<h4 id="test-domain-format">Test domain format</h4>
<ul>
<li><strong>One-word category</strong> — For categories with one-word names (for example, <em>Malware</em>), the test domain uses the following format:</li>
</ul>
<pre tabindex="0"><code class="language-txt">&lt;NAME_OF_CATEGORY&gt;.testcategory.com&#10;</code></pre>
<ul>
<li><strong>Multi-word category</strong> — For categories with multiple words in the name (for example, <em>Parked &amp; For Sale Domains</em>), the test domain uses the following format:
<ul>
<li>Remove any spaces between the words</li>
<li>Replace <code>&amp;</code> with <code>and</code></li>
<li>Lowercase all letters</li>
</ul>
</li>
</ul>
<h4 id="common-test-domains">Common test domains</h4>
<table>
<thead>
<tr>
<th>Category</th>
<th>Test domain</th>
</tr>
</thead>
<tbody>
<tr>
<td><em>Anonymizer</em></td>
<td><code>anonymizer.testcategory.com</code></td>
</tr>
<tr>
<td><em>Command and Control &amp; Botnet</em></td>
<td><code>commandandcontrolandbotnet.testcategory.com</code></td>
</tr>
<tr>
<td><em>compromised Domain</em></td>
<td><code>compromiseddomain.testcategory.com</code></td>
</tr>
<tr>
<td><em>Cryptomining</em></td>
<td><code>cryptomining.testcategory.com</code></td>
</tr>
<tr>
<td><em>Malware</em></td>
<td><code>malware.testcategory.com</code></td>
</tr>
<tr>
<td><em>New Domains</em></td>
<td><code>newdomains.testcategory.com</code></td>
</tr>
<tr>
<td><em>Parked &amp; For Sale Domains</em></td>
<td><code>parkedandforsaledomains.testcategory.com</code></td>
</tr>
<tr>
<td><em>Phishing</em></td>
<td><code>phishing.testcategory.com</code></td>
</tr>
<tr>
<td><em>Potentially Unwanted Software</em></td>
<td><code>potentiallyunwantedsoftware.testcategory.com</code></td>
</tr>
<tr>
<td><em>Private IP Address</em></td>
<td><code>privateipaddress.testcategory.com</code></td>
</tr>
<tr>
<td><em>Spam</em></td>
<td><code>spam.testcategory.com</code></td>
</tr>
<tr>
<td><em>Spyware</em></td>
<td><code>spyware.testcategory.com</code></td>
</tr>
<tr>
<td><em>Unreachable</em></td>
<td><code>unreachable.testcategory.com</code></td>
</tr>
</tbody>
</table>
<h2 id="test-edns-configuration">Test EDNS configuration</h2>
<p>EDNS client subnet (ECS) is a DNS extension that sends a portion of the user's IP address to authoritative DNS nameservers, allowing them to return geographically optimal answers. Cloudflare sends the first <code>/24</code> of the user's IP address to preserve privacy while still providing location information. If you <a href="/cloudflare-one/networks/resolvers-and-proxies/dns/locations/">enabled EDNS client subnet</a> for your DNS location, you can validate it as follows:</p>
<ol>
<li>
<p>Obtain your DNS location's DoH (DNS over HTTPS) subdomain:</p>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Networks</strong> &gt; <strong>Resolvers &amp; Proxies</strong> &gt; <strong>DNS locations</strong>.</li>
<li>Select the DNS location you are testing.</li>
<li>Note the value of <strong>DNS over HTTPS</strong>.</li>
</ol>
</li>
<li>
<p>Open a terminal and run the following command:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">curl &#x27;https://&lt;DOH_SUBDOMAIN&gt;.cloudflare-gateway.com/dns-query?type=TXT&amp;name=o-o.myaddr.google.com&#x27; -H &#x27;Accept: application/dns-json&#x27; | json_pp&#10;</code></pre>
<p>The output should contain your EDNS client subnet:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;AD&quot;: false,&#10;	&quot;Answer&quot;: [&#10;		{&#10;			&quot;TTL&quot;: 60,&#10;			&quot;data&quot;: &quot;\&quot;108.162.218.211\&quot;&quot;,&#10;			&quot;name&quot;: &quot;o-o.myaddr.google.com&quot;,&#10;			&quot;type&quot;: 16&#10;		},&#10;		{&#10;			&quot;TTL&quot;: 60,&#10;			&quot;data&quot;: &quot;\&quot;edns0-client-subnet 136.62.0.0/24\&quot;&quot;,&#10;			&quot;name&quot;: &quot;o-o.myaddr.google.com&quot;,&#10;			&quot;type&quot;: 16&#10;		}&#10;	],&#10;	&quot;CD&quot;: false,&#10;	&quot;Question&quot;: [&#10;		{&#10;			&quot;name&quot;: &quot;o-o.myaddr.google.com&quot;,&#10;			&quot;type&quot;: 16&#10;		}&#10;	],&#10;	&quot;RA&quot;: true,&#10;	&quot;RD&quot;: true,&#10;	&quot;Status&quot;: 0,&#10;	&quot;TC&quot;: false&#10;}&#10;</code></pre>
<ol start="3">
<li>To verify your EDNS client subnet, obtain your source IP address:</li>
</ol>
<pre tabindex="0"><code class="language-sh">curl ifconfig.me&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">136.62.12.156%&#10;</code></pre>
<p>The source IP address should fall within the /24 range specified by your EDNS client subnet.</p>
<h2 id="clear-dns-cache">Clear DNS cache</h2>
<p>Modern web browsers and operating systems are designed to cache DNS records for a set amount of time. When a request is made for a DNS record, the browser cache is the first location checked for the requested record. A DNS policy may not appear to work if the response is already cached.</p>
<p>To clear your DNS cache:</p>
<details class="nb-details"><summary>ChromeOS</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6642.md")
</div></details>
<details class="nb-details"><summary>Windows</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6643.md")
</div></details>
<details class="nb-details"><summary>macOS</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/6644.md")
</div></details>
