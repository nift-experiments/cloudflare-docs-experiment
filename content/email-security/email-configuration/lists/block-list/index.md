---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/lists/block-list/
  description: Block senders in Email security to automatically mark their messages with a MALICIOUS disposition.
  full_title: Block lists · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Block lists · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Block senders in Email security to automatically mark their messages with a MALICIOUS disposition."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/lists/block-list/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/lists/block-list/index.md"><meta property="og:title" content="Block lists · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Block senders in Email security to automatically mark their messages with a MALICIOUS disposition."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/lists/block-list/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/lists/block-list/
  schema: 1
---
<p>When you add <strong>blocked senders</strong>, Email security automatically marks all messages from these senders with a <code>MALICIOUS</code> <span class="nb-glossary-tooltip" title="disposition">disposition</span>.</p>
<h2 id="add-a-blocked-sender">Add a blocked sender</h2>
<p>To create a new blocked pattern:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Block List</strong> &gt; <strong>Blocked Senders</strong>.</p>
</li>
<li>
<p>Select <strong>+ New Sender</strong>.</p>
</li>
<li>
<p>Enter the pattern information:</p>
<ul>
<li>
<p><strong>Sender</strong>: Enter one of the following types of pattern:</p>
<ul>
<li><strong>Email addresses</strong>: Must be a valid email.</li>
<li><strong>IP addresses</strong>: Can only be IPv4. IPv6 and CIDR are invalid entries.</li>
<li><strong>Regular expressions</strong>: Must be <a href="https://www.freeformatter.com/java-regex-tester.html">valid Java expressions</a>. Regular expressions are matched with fields related to the sender email address (<code>envelope from</code>, <code>header from</code>, <code>reply-to</code>), the originating IP address, and the server name for the email.</li>
</ul>
</li>
<li>
<p><strong>Notes</strong>: Provide additional notes about the blocked sender pattern.</p>
</li>
</ul>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can also upload a CSV file of multiple allowed patterns. The CSV file must be smaller than 150 KB, start with a header row of all required values, and contain no additional fields.</p>
<p>An example file would look like this:</p>
<pre tabindex="0"><code class="language-txt">Blocked_Sender, Notes&#10;john.smith@email.com, John Smith&#10;melanie.turner@email.com, Melanie Turner&#10;</code></pre>
