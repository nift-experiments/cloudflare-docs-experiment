---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/
  description: Integrate Cisco - Email security as MX Record with Email Security.
  full_title: Cisco - Email security as MX Record · Cloudflare One docs
  head_html: <title>Cisco - Email security as MX Record · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Cisco - Email security as MX Record with Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/index.md"><meta property="og:title" content="Cisco - Email security as MX Record · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Cisco - Email security as MX Record with Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/#page","headline":"Cisco - Email security as MX Record \u00b7 Cloudflare One docs","description":"Integrate Cisco - Email security as MX Record with Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/cisco-email-security-mx/
  schema: 1
---
<p><img src="/assets/upstream/email-security/Cisco_to_Email_Security_MX_Inline.png" alt="A schematic showing where Email security sits in the life cycle of an email received" /></p>
<p>In this tutorial, you will learn how to configure Cisco IronPort with Email security as MX record.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To ensure changes made in this tutorial take effect quickly, update the Time to Live (TTL) value of the existing MX records on your domains to five minutes. Do this on all the domains you will be deploying.</p>
<p>Changing the TTL value instructs DNS servers on how long to cache this value before requesting an update from the responsible nameserver. You need to change the TTL value before changing your MX records to Email security. This will ensure that changes take effect quickly and can also be reverted quickly if needed. If your DNS manager does not allow for a TTL of five minutes, set it to the lowest possible setting.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4960.md")
</aside>
<p>To check your existing TTL, open a terminal window and run the following command against your domain:</p>
<pre tabindex="0"><code class="language-sh">dig mx &lt;YOUR_DOMAIN&gt;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; mx &lt;YOUR_DOMAIN&gt;&#10;;; global options: +cmd&#10;;; Got answer:&#10;;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 39938&#10;;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1&#10;&#10;;; OPT PSEUDOSECTION:&#10;; EDNS: version: 0, flags:; udp: 4096&#10;;; QUESTION SECTION:&#10;;&lt;YOUR_DOMAIN&gt;.		IN	MX&#10;&#10;;; ANSWER SECTION:&#10;&lt;YOUR_DOMAIN&gt;.    300    IN    MX    10 mxa.global.inbound.cf-emailsecurity.net.&#10;&lt;YOUR_DOMAIN&gt;.    300    IN    MX    10 mxb.global.inbound.cf-emailsecurity.net.&#10;</code></pre>
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
<li><strong>Name</strong>: <code>Email security</code>.</li>
<li><strong>Order</strong>: Order above the existing <strong>WHITELIST</strong> sender group.</li>
<li><strong>Comment</strong>: <code>Email security Email Protection egress IP Addresses</code>.</li>
<li><strong>Policy</strong>: <code>TRUSTED</code> (by default, spam detection is disabled for this mail flow policy).</li>
<li><strong>SBRS</strong>: Leave blank.</li>
<li><strong>DNS Lists</strong>: Leave blank.</li>
<li><strong>Connecting Host DNS Verification</strong>: Leave all options unchecked.</li>
</ul>
</li>
<li>
<p>Select <strong>Submit and Add Senders</strong> and add the IP addresses mentioned in <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/" target="_blank">Egress IPs</a></p>
</li>
</ol>
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
<h2 id="4-set-up-mx-inline"><ol start="4">
<li>Set up MX/Inline</li>
</ol></h2>
<p>Now that you have completed the prerequisite steps, set up MX/Inline on the Cloudflare dashboard. Refer to <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/">Set up MX/Inline deployment</a> for the next steps.</p>
