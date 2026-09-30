---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/
  description: Integrate Google Workspace as MX Record with Email Security.
  full_title: Google Workspace as MX Record · Cloudflare One docs
  head_html: <title>Google Workspace as MX Record · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Integrate Google Workspace as MX Record with Email Security."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/index.md"><meta property="og:title" content="Google Workspace as MX Record · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Integrate Google Workspace as MX Record with Email Security."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Cloudflare One"><meta name="pcx_tags" content="Google"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/#page","headline":"Google Workspace as MX Record \u00b7 Cloudflare One docs","description":"Integrate Google Workspace as MX Record with Email Security.","url":"https://developers.cloudflare.com/cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Google"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/email-security/setup/pre-delivery-deployment/prerequisites/gsuite-email-security-mx/
  schema: 1
---
<p><img src="/assets/upstream/email-security/Email_Security_Gmail_MX_Inline.png" alt="A schematic showing where Email security is in the life cycle of an email received" /></p>
<p>In this tutorial, you will learn how to configure Google Workspace with Email security as MX record.</p>
<h2 id="prerequisites">Prerequisites</h2>
<p>To ensure changes made in this tutorial take effect quickly, update the Time to Live (TTL) value of the existing MX records on your domains to five minutes. Do this on all the domains you will be deploying.</p>
<p>Changing the TTL value instructs DNS servers on how long to cache this value before requesting an update from the responsible nameserver. You need to change the TTL value before changing your MX records to Email security. This will ensure that changes take effect quickly and can also be reverted quickly if needed. If your DNS manager does not allow for a TTL of five minutes, set it to the lowest possible setting.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4957.md")
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
<h2 id="requirements">Requirements</h2>
<ul>
<li>Provisioned Email security account.</li>
<li>Access to the Google administrator console (<a href="https://admin.google.com/">Google administrator console</a> &gt; <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong>).</li>
<li>Access to the domain nameserver hosting the MX records for the domains that will be processed by Email security.</li>
</ul>
<h2 id="1-set-up-inbound-email-configuration"><ol>
<li>Set up Inbound Email Configuration</li>
</ol></h2>
<p>Set up <a href="https://support.google.com/a/answer/60730?hl=en">Inbound Email Configuration</a> with the following details:</p>
<ul>
<li>In <strong>Gateway IPs</strong>, select the <strong>Add</strong> link, and add the IPs mentioned in <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/egress-ips/">Egress IPs</a>.</li>
<li>Select <strong>Automatically detect external IP (recommended)</strong>.</li>
<li>Select <strong>Require TLS for connections from the email gateways listed above</strong>.</li>
<li>Do not select <strong>Reject all mail not from gateway IPs</strong>. You will enable this option at a later time to ensure your mail flows.</li>
<li>Select <strong>SAVE</strong>.</li>
</ul>
<h2 id="2-optional-set-up-an-email-quarantine"><ol start="2">
<li>(Optional) Set up an email quarantine</li>
</ol></h2>
<p><a href="https://support.google.com/a/answer/6104172?hl=en#add-new-quarantine">Set up an email quarantine</a> with the following details:</p>
<ul>
<li><strong>Name</strong>: Email security Malicious.</li>
<li><strong>Description</strong>: Email security Malicious.</li>
<li>For the <strong>Inbound denial consequence</strong>, select <strong>Drop message</strong>.</li>
<li>For the <strong>Outbound denial consequence</strong>, select <strong>Drop message</strong>.</li>
<li>Select <strong>SAVE</strong>.</li>
</ul>
<p>To access the newly created quarantine, select <strong>GO TO ADMIN QUARANTINE</strong> or access the quarantine directly by pointing your browser to <a href="https://email-quarantine.google.com/adminreview">https://email-quarantine.google.com/adminreview</a>.</p>
<h2 id="3-optional-create-a-content-compliance-filter"><ol start="3">
<li>(Optional) Create a content compliance filter</li>
</ol></h2>
<p>Go to <strong>Compliance</strong>, and create a <a href="https://support.google.com/a/answer/1346934?hl=en#zippy=%2Cstep-go-to-gmail-compliance-settings-in-the-google-admin-console%2Cstep-enter-email-messages-to-affect">content compliance filter</a> to send malicious messages to quarantine. Enter the following details:</p>
<ul>
<li><strong>Content compliance</strong>: Add <code>Quarantine Email security Malicious</code>.</li>
<li><strong>Email messages to affect</strong>: Select <strong>Inbound</strong>.</li>
<li><strong>Add expressions that describe the content you want to search for in each message</strong>:
<ul>
<li>Select <strong>Add</strong> to add the condition.</li>
<li>In <strong>Simple content match</strong>, select <strong>Advanced content match</strong>.</li>
<li>In <strong>Location</strong>, select <strong>Full headers</strong>.</li>
<li>In <strong>Match type</strong>, select <strong>Contains text</strong>.</li>
<li>In <strong>Content</strong>, enter <code>X-CFEmailSecurity-Disposition: MALICIOUS</code>.</li>
<li>Select <strong>SAVE</strong> to save the condition.</li>
</ul>
</li>
<li>If the above expression match, do the following, select <strong>Quarantine message</strong> and the <strong>Email security Malicious</strong> quarantine that was created in the previous step.</li>
<li>Select <strong>SAVE</strong>.</li>
</ul>
<p>If you would like to quarantine the other dispositions, repeat the above steps and use the following strings for the other dispositions:</p>
<ul>
<li><code>X-CFEmailSecurity-Disposition: BULK</code></li>
<li><code>X-CFEmailSecurity-Disposition: SPOOF</code></li>
<li><code>X-CFEmailSecurity-Disposition: UCE</code> (<code>UCE</code> is the equivalent of <code>SPAM</code>)</li>
</ul>
<p>If desired, you can create a separate quarantine for each of the dispositions.</p>
<h2 id="4-set-up-mx-inline"><ol start="4">
<li>Set up MX/Inline</li>
</ol></h2>
<p>Now that you have completed the prerequisite steps, set up MX/Inline on the Cloudflare dashboard. Refer to <a href="/cloudflare-one/email-security/setup/pre-delivery-deployment/mx-inline-deployment-setup/">Set up MX/Inline deployment</a> for the next steps.</p>
<h2 id="5-recommended-secure-google-workspace-from-mx-records-bypass"><ol start="5">
<li>(Recommended) Secure Google Workspace from MX records bypass</li>
</ol></h2>
<p>One method of a DNS attack is to search for old MX records and send <span class="nb-glossary-tooltip" title="phishing">phishing</span> emails directly to the mail server. To secure the email flow, you should enforce an email flow where inbound messages are accepted by Google Workspace only when they originate from Email security. This can be done by adding a connector to only allow email from Email security with TLS encryption. This step is optional but recommended.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="important">Important</h3>
@markup("md", "content/.markup/bodies/4956.md")
</aside>
<p>After 72 hours, the MX record DNS update will have sufficiently propagated across the Internet. It is now safe to secure your email flow. This will ensure that Google Workspace only accepts messages that are first received by Email security. This step is highly recommended to prevent threat actors from using cached MX entries to bypass Email security by injecting messages directly into Google Workspace.</p>
<ol>
<li>
<p>Access the <a href="https://admin.google.com/">Google Administrative Console</a>, then select <strong>Apps</strong> &gt; <strong>Google Workspace</strong> &gt; <strong>Gmail</strong>.</p>
</li>
<li>
<p>Select <strong>Spam, Phishing and Malware</strong>.</p>
</li>
<li>
<p>Go to <strong>Inbound gateway</strong> and select <strong>Edit Inbound gateway</strong>.</p>
</li>
<li>
<p>Enable <strong>Reject all mail not from gateway IPs</strong> and select <strong>Save</strong>.</p>
</li>
<li>
<p>Select <strong>Save</strong> once more to commit and activate the configuration change in the Gmail advanced configuration console.</p>
</li>
</ol>
