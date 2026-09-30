---
cp9:
  canonical: https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-cisco-mx/
  description: Deploy Email Security with Cisco as the MX record for inline email protection.
  full_title: Deploy and configure Email security (formerly Area 1) with Cisco as MX record · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Deploy and configure Email security (formerly Area 1) with Cisco as MX record · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Email Security with Cisco as the MX record for inline email protection."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-cisco-mx/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-cisco-mx/index.md"><meta property="og:title" content="Deploy and configure Email security (formerly Area 1) with Cisco as MX record · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Email Security with Cisco as the MX record for inline email protection."><meta property="og:url" content="https://developers.cloudflare.com/email-security/deployment/inline/setup/cisco-cisco-mx/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Integration guide"><meta name="algolia_content_type" content="Integration guide"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/deployment/inline/setup/cisco-cisco-mx/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8527.md")
</aside>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/cisco-cisco-mx/cisco-mx.png" alt="A schematic showing where Email security is in the life cycle of an email received" /></p>
<p>In this tutorial, you will learn how to configure Email security with Cisco as MX record. This tutorial is broken down into several steps.</p>
<h2 id="1-add-a-sender-group-for-email-security-email-protection-ips"><ol>
<li>Add a Sender Group for Email security Email Protection IPs</li>
</ol></h2>
<p>To add a new Sender Group:</p>
<ol>
<li>
<p>Go to <strong>Mail Policies</strong> &gt; <strong>HAT Overview</strong>.</p>
</li>
<li>
<p>Select the <strong>Add Sender Group</strong> button.</p>
</li>
<li>
<p>Configure the new Sender Group as follows:</p>
<ul>
<li><strong>Name</strong>: <code>Area1</code>.</li>
<li><strong>Order</strong>: Order above the existing <strong>WHITELIST</strong> sender group.</li>
<li><strong>Comment</strong>: <code>Email security Email Protection egress IP Addresses</code>.</li>
<li><strong>Policy</strong>: <code>TRUSTED</code> (by default, spam detection is disabled for this mail flow policy).</li>
<li><strong>SBRS</strong>: Leave blank.</li>
<li><strong>DNS Lists</strong>: Leave blank.</li>
<li><strong>Connecting Host DNS Verification</strong>: Leave all options unchecked.</li>
</ul>
</li>
<li>
<p>Select <strong>Submit and Add Senders</strong>, and add the IP addresses mentioned in <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs</a>. If you need to process emails in the EU or India regions for compliance purposes, add those IP addresses as well.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/cisco-cisco-mx/step1.png" alt="Sender group" /></p>
<h2 id="2-add-smtp-route-for-the-email-security-email-protection-hosts"><ol start="2">
<li>Add <span class="nb-glossary-tooltip" title="SMTP">SMTP</span> route for the Email security Email Protection Hosts</li>
</ol></h2>
<p>To add a new SMTP Route:</p>
<ol>
<li>
<p>Go to <strong>Network</strong> &gt; <strong>SMTP Routes</strong>.</p>
</li>
<li>
<p>Select <strong>Add Route</strong>.</p>
</li>
<li>
<p>Configure the new SMTP Route as follows:</p>
<ul>
<li><strong>Receiving Domain</strong>: <code>a1s.mailstream</code></li>
<li>In <strong>Destination Hosts</strong>, select <strong>Add Row</strong>, and add the Email security MX hosts. Refer to the <a href="#5-geographic-locations">Geographic locations</a> table for more information on what MX hosts to use.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/cisco-cisco-mx/step2.png" alt="Edit SMTP route" /></p>
<h2 id="3-create-incoming-content-filters"><ol start="3">
<li>Create Incoming Content Filters</li>
</ol></h2>
<p>To manage the mail flow between Email security and Cisco ESA, you need two filters:</p>
<ul>
<li>One to direct all incoming messages to Email security.</li>
<li>One to recognize messages coming back from Email security to route for normal delivery.</li>
</ul>
<h3 id="incoming-content-filter-to-email-security">Incoming Content Filter - To Email security</h3>
<p>To create a new Content Filter:</p>
<ol>
<li>
<p>Go to <strong>Mail Policies</strong> &gt; <strong>Incoming Content Filters</strong>.</p>
</li>
<li>
<p>Select <strong>Add Filter</strong> to create a new filter.</p>
</li>
<li>
<p>Configure the new Incoming Content Filter as follows:</p>
<ul>
<li><strong>Name</strong>: <code>ESA_to_A1S</code></li>
<li><strong>Description</strong>: <code>Redirect messages to Email security for anti-phishing inspection</code></li>
<li><strong>Order</strong>: This will depend on your other filters.</li>
<li><strong>Condition</strong>: No conditions.</li>
<li><strong>Actions</strong>:
<ul>
<li>For <strong>Action</strong> select <strong>Send to Alternate Destination Host</strong>.</li>
<li>For <strong>Mail Host</strong> input <code>a1s.mailstream</code> (the SMTP route configured in step 2).</li>
</ul>
</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/cisco-cisco-mx/step3-to-area1.png" alt="Content filter" /></p>
<h3 id="incoming-content-filter-from-email-security">Incoming Content Filter - From Email security</h3>
<p>To create a new Content Filter:</p>
<ol>
<li>
<p>Go to <strong>Mail Policies</strong> &gt; <strong>Incoming Content Filters</strong>.</p>
</li>
<li>
<p>Select the <strong>Add Filter</strong> button to create a new filter.</p>
</li>
<li>
<p>Configure the new Incoming Content Filter as follows:</p>
<ul>
<li><strong>Name</strong>: <code>A1S_to_ESA</code></li>
<li><strong>Description</strong>: <code>Email security inspected messages for final delivery</code></li>
<li><strong>Order</strong>: This filter must come before the previously created filter.</li>
<li><strong>Conditions</strong>: Add conditions of type <strong>Remote IP/Hostname</strong> with all the IP addresses mentioned in <a href="/email-security/deployment/inline/reference/egress-ips/">Egress IPs</a>. For example:</li>
</ul>
</li>
</ol>
<table>
<thead>
<tr>
<th>Order</th>
<th>Condition</th>
<th>Rule</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>1</code></td>
<td><code>Remote IP/Hostname</code></td>
<td><code>Remote IP/Hostname</code></td>
</tr>
<tr>
<td><code>2</code></td>
<td><code>Remote IP/Hostname</code></td>
<td><code>52.89.255.11</code></td>
</tr>
<tr>
<td><code>3</code></td>
<td><code>Remote IP/Hostname</code></td>
<td><code>52.0.67.109</code></td>
</tr>
<tr>
<td><code>4</code></td>
<td><code>Remote IP/Hostname</code></td>
<td><code>54.173.50.115</code></td>
</tr>
<tr>
<td><code>5</code></td>
<td><code>Remote IP/Hostname</code></td>
<td><code>104.30.32.0/19</code></td>
</tr>
<tr>
<td><code>6</code></td>
<td><code>Remote IP/Hostname</code></td>
<td><code>158.51.64.0/26</code></td>
</tr>
<tr>
<td><code>7</code></td>
<td><code>Remote IP/Hostname</code></td>
<td><code>158.51.65.0/26</code></td>
</tr>
</tbody>
</table>
   - Ensure that the _Apply rule:_ dropdown is set to **If one or more conditions match**.
   - **Actions**: Select **Add Action**, and add the following:
<table>
<thead>
<tr>
<th>Order</th>
<th>Action</th>
<th>Rule</th>
</tr>
</thead>
<tbody>
<tr>
<td>--1</td>
<td><code>Skip Remaining Content Filters (Final Action)</code></td>
<td><code>skip-filters()</code></td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/email-security/deployment/inline-setup/cisco-cisco-mx/step3-from-area1.png" alt="Content filter" /></p>
<h2 id="4-add-the-incoming-content-filter-to-the-inbound-policy-table"><ol start="4">
<li>Add the Incoming Content Filter to the Inbound Policy table</li>
</ol></h2>
<p>Assign the Incoming Content Filters created in <a href="#3-create-incoming-content-filters">step 3</a> to your primary mail policy in the Incoming Mail Policy table. Then, commit your changes to activate the email redirection.</p>
<h2 id="5-geographic-locations"><ol start="5">
<li>Geographic locations</li>
</ol></h2>
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
