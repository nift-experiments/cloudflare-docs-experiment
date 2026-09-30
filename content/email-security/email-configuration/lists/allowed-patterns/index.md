---
cp9:
  canonical: https://developers.cloudflare.com/email-security/email-configuration/lists/allowed-patterns/
  description: Exempt messages matching specific patterns from Email security detection scanning.
  full_title: Allowed patterns · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Allowed patterns · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Exempt messages matching specific patterns from Email security detection scanning."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/email-configuration/lists/allowed-patterns/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/email-configuration/lists/allowed-patterns/index.md"><meta property="og:title" content="Allowed patterns · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Exempt messages matching specific patterns from Email security detection scanning."><meta property="og:url" content="https://developers.cloudflare.com/email-security/email-configuration/lists/allowed-patterns/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/email-configuration/lists/allowed-patterns/
  schema: 1
---
<p>When you set up <strong>allowed patterns</strong>, Email security email security exempts messages that match certain patterns from normal detection scanning.</p>
<h2 id="add-an-allowed-pattern">Add an allowed pattern</h2>
<p>To create a new allowed pattern:</p>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Go to <strong>Settings</strong> (the gear icon).</p>
</li>
<li>
<p>On <strong>Email Configuration</strong>, go to <strong>Allow List</strong> &gt; <strong>Allowed Patterns</strong>.</p>
</li>
<li>
<p>Select <strong>+ New Pattern</strong>.</p>
</li>
<li>
<p>Enter the pattern information:</p>
<ul>
<li>
<p><strong>Allowed Pattern</strong>: Enter one of the following types of pattern:</p>
<ul>
<li><strong>Email addresses</strong>: Must be a valid email.</li>
<li><strong>IP addresses</strong>: Can only be IPv4. IPv6 and CIDR are invalid entries.</li>
<li><strong>Regular expressions</strong>: Must be <a href="https://www.freeformatter.com/java-regex-tester.html">valid Java expressions</a>.</li>
</ul>
</li>
<li>
<p><strong>Allow Type</strong>: Choose one or more of the following types:</p>
<ul>
<li><strong>Trusted Sender</strong>: Messages will bypass all <a href="/email-security/reference/dispositions-and-attributes/">detections</a> and link following by Email security. Typically, only applies to <span class="nb-glossary-tooltip" title="phishing">phishing</span> simulations from vendors such as KnowBe4.</li>
<li><strong>Exempt Recipient</strong>: Will exempt messages from all Email security <a href="/email-security/reference/dispositions-and-attributes/">detections</a> intended for recipients matching this pattern (email address or regular expression only). Typically, this only applies to submission mailboxes for user reporting to security.</li>
<li><strong>Acceptable Sender</strong>: Will exempt messages from the <code>SPAM</code>, <code>SPOOF</code>, and <code>BULK</code> <a href="/email-security/reference/dispositions-and-attributes/#available-values">dispositions</a> (but not <code>MALICIOUS</code> or <code>SUSPICIOUS</code>). Commonly used for external domains and sources that send mail on behalf of your organization, such as marketing emails or internal tools.</li>
</ul>
</li>
<li>
<p><strong>Notes</strong>: Provide additional notes about the allowed pattern.</p>
</li>
</ul>
</li>
<li>
<p>If you chose <em>Trusted Sender</em> or <em>Acceptable Sender</em> in the previous step, you will be able to choose whether to verify the sender. When the <strong>Verify Sender</strong> option is selected, the allow list entry will only be honored if it aligns with a passing authentication by DMARC or SPF or DKIM.</p>
</li>
<li>
<p>Select <strong>Save</strong>.</p>
</li>
</ol>
<h3 id="csv-uploads">CSV uploads</h3>
<p>You can also upload a CSV file of multiple allowed patterns. The CSV file must be smaller than 150 KB, start with a header row of all required values, and contain no additional fields.</p>
<p>An example file would look like this:</p>
<pre tabindex="0"><code class="language-txt">Pattern, Notes, Verify Email, Trusted Sender,&#10;Exempt Recipient, Acceptable Sender&#10;whale@notaphish.com, not a phish, true, true, false, true&#10;</code></pre>
