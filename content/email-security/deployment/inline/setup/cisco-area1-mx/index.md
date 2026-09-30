---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-area1-mx/
  description: Deploy Email Security as the MX record with Cisco IronPort for inline email scanning.
  full_title: Deploy and configure Cisco IronPort with Email security (formerly Area 1) as MX Record · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Deploy and configure Cisco IronPort with Email security (formerly Area 1) as MX Record · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Email Security as the MX record with Cisco IronPort for inline email scanning."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-area1-mx/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-area1-mx/index.md"><meta property="og:title" content="Deploy and configure Cisco IronPort with Email security (formerly Area 1) as MX Record · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Email Security as the MX record with Cisco IronPort for inline email scanning."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-area1-mx/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/inline/setup/cisco-area1-mx/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8529.md")
</aside>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/cisco-area1-mx/cisco-area1-mx.png" alt="A schematic showing where Email security security is in the life cycle of an email received" /></p>
<p>In this tutorial, you will learn how to configure Cisco IronPort with Email security as MX record. This tutorial is broken down into several steps.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To ensure changes made in this tutorial take effect quickly, update the Time to Live (TTL) value of the existing MX records on your domains to five minutes. Do this on all the domains you will be deploying.</p>
<p>Changing the TTL value instructs DNS servers on how long to cache this value before requesting an update from the responsible nameserver. You need to change the TTL value before changing your MX records to Cloudflare Email Security (formerly Area 1). This will ensure that changes take effect quickly and can also be reverted quickly if needed. If your DNS manager does not allow for a TTL of five minutes, set it to the lowest possible setting.</p>
<p>To check your existing TTL, open a terminal window and run the following command against your domain:</p>
<pre tabindex="0"><code class="language-sh">dig mx &lt;YOUR_DOMAIN&gt;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">&#10;; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; mx &lt;YOUR_DOMAIN&gt;&#10;;; global options: +cmd&#10;;; Got answer:&#10;;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 39938&#10;;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1&#10;&#10;;; OPT PSEUDOSECTION:&#10;; EDNS: version: 0, flags:; udp: 4096&#10;;; QUESTION SECTION:&#10;;domain.		IN	MX&#10;&#10;;; ANSWER SECTION:&#10;&lt;YOUR_DOMAIN&gt;.	300	IN	MX	5 mailstream-central.mxrecord.mx.&#10;&lt;YOUR_DOMAIN&gt;.	300	IN	MX	10 mailstream-east.mxrecord.io.&#10;&lt;YOUR_DOMAIN&gt;.	300	IN	MX	10 mailstream-west.mxrecord.io.&#10;</code></pre>
<p>In the above example, TTL is shown in seconds as <code>300</code> (or five minutes).</p>
<p>If you are using Cloudflare for DNS, you can leave the <a href="/dns/manage-dns-records/reference/ttl/">TTL setting as <strong>Auto</strong></a>.</p>
<p>Below is a list with instructions on how to edit MX records for some popular services:</p>
<ul>
<li><strong>Cloudflare</strong>: <a href="/dns/manage-dns-records/how-to/email-records/">Set up email records</a></li>
<li><strong>GoDaddy</strong>: <a href="https://www.godaddy.com/help/edit-an-mx-record-19235">Edit an MX Record</a></li>
<li><strong>AWS</strong>: <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html">Creating records by using the Amazon Route 53 console</a></li>
<li><strong>Azure</strong>: <a href="https://learn.microsoft.com/en-us/azure/dns/dns-web-sites-custom-domain">Create DNS records in a custom domain for a web app</a></li>
</ul>
<h2 id="1-add-a-sender-group-for-email-security-email-protection-ips"><ol>
<li>Add a Sender Group for Email security Email Protection IPs</li>
</ol></h2>
<p>To add a new Sender Group:</p>
<ol>
<li>
<p>Go to <strong>Mail Policies</strong> &gt; <strong>HAT Overview</strong>.</p>
</li>
<li>
<p>Select <strong>Add Sender Group</strong>.</p>
</li>
<li>
<p>Configure the new Sender Group as follows:</p>
<ul>
<li><strong>Name</strong>: <code>Area1</code>.</li>
<li><strong>Order</strong>: Order above the existing <strong>WHITELIST</strong> sender group.</li>
<li><strong>Comment</strong>: <code>Area 1 Email Protection egress IP Addresses</code>.</li>
<li><strong>Policy</strong>: <code>TRUSTED</code> (by default, spam detection is disabled for this mail flow policy).</li>
<li><strong>SBRS</strong>: Leave blank.</li>
<li><strong>DNS Lists</strong>: Leave blank.</li>
<li><strong>Connecting Host DNS Verification</strong>: Leave all options unchecked.</li>
</ul>
</li>
<li>
<p>Select <strong>Submit and Add Senders</strong> and add the IP addresses mentioned in <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs</a>.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/cisco-area1-mx/step1.png" alt="Sender group" /></p>
<h2 id="2-configure-incoming-relays"><ol start="2">
<li>Configure Incoming Relays</li>
</ol></h2>
<p>You need to configure the Incoming Relays section to tell IronPort to ignore upstream hops, since all the connections are now coming from Email security. This step is needed so the IronPort can retrieve the original IPs to calculate IP reputation. IronPort also uses this information in the Anti-Spam (IPAS) scoring of messages.</p>
<ol>
<li>To enable the Incoming Relays Feature, select <strong>Network</strong> &gt; <strong>Incoming Relays</strong>.</li>
<li>Select <strong>Enable</strong> and commit your changes.</li>
<li>Now, you will have to add an Incoming Relay. Select <strong>Network</strong> &gt; <strong>Incoming Relays</strong>.</li>
<li>Select <strong>Add Relay</strong> and give your relay a name.</li>
<li>Enter the IP address of the MTA, MX, or other machine that connects to the email gateway to relay incoming messages. You can use IPv4 or IPv6 addresses.</li>
<li>Specify the <code>Received:</code> header that will identify the IP address of the original external sender.</li>
<li>Commit your changes.</li>
</ol>
<h2 id="3-disable-spf-checks"><ol start="3">
<li>Disable SPF checks</li>
</ol></h2>
<p>Make sure you disable Sender Policy Framework (SPF) checks in IronPort. Because Email security is acting as the MX record, if you do not disable SPF checks, IronPort will block emails due to an SPF failure.</p>
<p>Refer to <a href="https://www.cisco.com/c/en/us/support/docs/security/email-security-appliance/117973-faq-esa-00.html">Cisco's documentation</a> for more information on how to disable SPF checks.</p>
<h2 id="4-update-your-domain-mx-records"><ol start="4">
<li>Update your domain MX records</li>
</ol></h2>
<p>Instructions to update your MX records will depend on the DNS provider you are using. In your domain DNS zone, you need to replace your current MX records with the Email security hosts. This will have to be done for every domain where Email security will be the primary MX. For example:</p>
<table>
<thead>
<tr>
<th>MX Priority</th>
<th>Host</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>5</code></td>
<td><code>mailstream-eu1.mxrecord.io</code></td>
</tr>
<tr>
<td><code>10</code></td>
<td><code>mailstream-central.mxrecord.mx</code></td>
</tr>
<tr>
<td><code>20</code></td>
<td><code>mailstream-east.mxrecord.io</code></td>
</tr>
<tr>
<td><code>20</code></td>
<td><code>mailstream-west.mxrecord.io</code></td>
</tr>
</tbody>
</table>
<p>When configuring the Email Security (formerly Area 1) MX records, it is important to configure hosts with the correct MX priority. This will allow mail flows to the preferred hosts and fail over as needed.</p>
<p>Choose from the following Email Security MX hosts, and order them by priority. For example, if you are located outside the US and want to prioritize email processing in the EU, add <code>mailstream-eu1.mxrecord.io</code> as your first host, and then the US servers.</p>
<table>
<thead>
<tr>
<th>Host</th>
<th>Location</th>
<th>Note</th>
</tr>
</thead>
<tbody>
<tr>
<td><un><li><code>mailstream-central.mxrecord.mx</code></li> <li><code>mailstream-east.mxrecord.io</code></li> <li><code>mailstream-west.mxrecord.io</code></li></un></td>
<td>US</td>
<td>Best option to ensure all email traffic processing happens in the US.</td>
</tr>
<tr>
<td><code>mailstream-eu1.mxrecord.io</code></td>
<td>EU</td>
<td>Best option to ensure all email traffic processing happens in Germany, with backup to US data centers.</td>
</tr>
<tr>
<td><code>mailstream-bom.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens within India.</td>
</tr>
<tr>
<td><code>mailstream-india-primary.mxrecord.mx</code></td>
<td>India</td>
<td>Same as <code>mailstream-bom.mxrecord.mx</code>, with backup to US data centers.</td>
</tr>
<tr>
<td><code>mailstream-asia.mxrecord.mx</code></td>
<td>India</td>
<td>Best option to ensure all email traffic processing happens in India, with Australia data centers as backup.</td>
</tr>
<tr>
<td><code>mailstream-syd.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens within Australia.</td>
</tr>
<tr>
<td><code>mailstream-australia-primary.area1.cloudflare.net</code></td>
<td>Australia / New Zealand</td>
<td>Best option to ensure all email traffic processing happens in Australia, with India and US data centers as backup.</td>
</tr>
</tbody>
</table>
<p>DNS changes will reach the major DNS servers in about an hour or follow the TTL value as described in the <a href="#prerequisites">Prerequisites section</a>.</p>
