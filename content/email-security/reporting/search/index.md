---
cp9:
  canonical: https://developers.cloudflare.com/email-security/reporting/search/
  description: Search for messages with a detection disposition or that have been processeded by Email security (formerly Area 1).
  full_title: Search · Cloudflare Email security (formerly Area 1) docs
  head_html: <title>Search · Cloudflare Email security (formerly Area 1) docs</title><meta name="generator" content="Nift"><meta name="description" content="Search for messages with a detection disposition or that have been processeded by Email security (formerly Area 1)."><meta name="robots" content="noindex"><link rel="canonical" href="https://developers.cloudflare.com/email-security/reporting/search/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/email-security/reporting/search/index.md"><meta property="og:title" content="Search · Cloudflare Email security (formerly Area 1) docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Search for messages with a detection disposition or that have been processeded by Email security (formerly Area 1)."><meta property="og:url" content="https://developers.cloudflare.com/email-security/reporting/search/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Email security (formerly Area 1)"><meta name="algolia_product_filter" content="Email security (formerly Area 1)"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Email security (formerly Area 1)">
  markdown: true
  noindex: true
  route: /email-security/reporting/search/
  schema: 1
---
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="area-1-has-been-renamed">Area 1 has been renamed</h3>
@markup("md", "content/.markup/bodies/8578.md")
</aside>
<p>You can search for emails that have been processed by Email security (formerly Area 1), whether they are marked with a <span class="nb-glossary-tooltip" title="disposition">detection disposition</span> or not.</p>
<p>There are two ways for searching emails:</p>
<ul>
<li><strong>Fielded Search</strong>: Presents you with fields where you can enter search terms.</li>
<li><strong>Freeform Search</strong>: Has one search field where you can construct your own search query, like <code>My great products</code>.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8577.md")
</aside>
<h2 id="search-terms">Search terms</h2>
<p>In Freeform Search, you can search for any value or combination of values separated by a space. Using spaces with multiple search terms is the equivalent of using the operator <code>AND</code>.</p>
<p>Terms less than three characters long and common English words that do not offer significance for search value like <code>and</code>, <code>the</code>, <code>then</code>, <code>their</code> are ignored.</p>
<p>For more exact matches, use the named fields in <strong>Fielded Search</strong> to denote which field should contain the value. For example, to find only messages sent by <code>demo@example.com</code>, enter <code>demo@example.com</code> in <strong>FROM (EXACT)</strong>. <code>EXACT</code> in a field descriptor means the term will match how the value appears in the message.</p>
<h2 id="fielded-search">Fielded Search</h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Select the <strong>Search</strong> bar.</p>
</li>
<li>
<p>Fill out one or more of the following fields. Filling multiple fields is the equivalent of adding the <code>AND</code> operator between the following terms:</p>
<ul>
<li><strong>Terms</strong>: Searches for terms in any of the available fields. If you want to search for a message that matches multiple recipients, use this field. Only one value can be specified in the <strong>From</strong> and <strong>To</strong> fields.</li>
<li><strong>From (Exact)</strong>: Searches for the sender’s exact email address.</li>
<li><strong>To (Exact)</strong>: Searches for the recipient’s exact email address.</li>
<li><strong>Subject</strong>: Searches for the terms in the subject field.</li>
<li><strong>Domain</strong>: Searches for messages from a specific domain.</li>
<li><strong>Message ID</strong>: Searches for messages with the stated message ID.</li>
<li><strong>Alert ID</strong>: Searches for messages with the stated alert ID.</li>
</ul>
</li>
<li>
<p><strong>Detections only</strong> is enabled by default. This means that the system will only search through and display emails that Email Security (formerly Area 1) has marked with a detection <span class="nb-glossary-tooltip" title="disposition">disposition</span>. If you prefer to search through and view all emails that have been processed by Email Security, whether they are marked with a detection disposition or not, disable this option.</p>
</li>
<li>
<p>The <strong>All detections</strong> drop-down menu allows you to refine your search by detection disposition. This menu will be disabled if <strong>Detections only</strong> is not selected.</p>
</li>
<li>
<p>By default, the search results are limited to the previous 30 days. Select <strong>Last 30 days</strong> to change this setting.</p>
</li>
<li>
<p>(Optional) You can download the results from your search in CSV format. The CSV file is capped at 1,000 rows.</p>
</li>
<li>
<p>The system returns a list of emails that fit your search criteria, and will inform you if there are emails similar to the ones found. If Email Security finds emails similar to the ones returned by your query, select <strong>Show</strong> to display them. Otherwise, select <strong>View</strong> on the email you are interested in. This will show you more information about that particular email, such as:</p>
<ul>
<li>Disposition (if any)</li>
<li>Email status (for example <code>Quarantined</code>)</li>
<li>Sender details (for example, IP address)</li>
</ul>
</li>
</ol>
<h2 id="freeform-search">Freeform Search</h2>
<ol>
<li>
<p>Log in to the <a href="https://horizon.area1security.com/">Email security dashboard</a>.</p>
</li>
<li>
<p>Select the <strong>Search bar</strong> &gt; <strong>Freeform Search</strong>.</p>
</li>
<li>
<p>Build your search query — for example, <code>My great products</code>. The system will return all the emails that fit the query.</p>
</li>
<li>
<p><strong>Detections only</strong> is enabled by default. This means that the system will only search through and display emails that Email Security (formerly Area 1) has marked with a detection <span class="nb-glossary-tooltip" title="disposition">disposition</span>. If you prefer to search through and view all emails that have been processed by Email Security, whether they are marked with a detection disposition or not, disable this option.</p>
</li>
<li>
<p>The <strong>All detections</strong> drop-down menu allows you to refine your search by detection disposition. This menu will be disabled if <strong>Detections only</strong> is not selected.</p>
</li>
<li>
<p>By default, the search results are limited to the previous 30 days. Select <strong>Last 30 days</strong> to change this setting.</p>
</li>
<li>
<p>(Optional) You can download the results from your search in CSV format. The CSV file is capped at 1,000 rows.</p>
</li>
<li>
<p>The system returns a list of emails that fit your search criteria, and will inform you if there are emails similar to the ones found. If Email Security finds emails similar to the ones returned by your query, select <strong>Show</strong> to display them. Otherwise, select <strong>View</strong> on the email you are interested in. This will show you more information about that particular email, such as:</p>
<ul>
<li>Disposition (if any)</li>
<li>Email status (for example <code>Quarantined</code>)</li>
<li>Sender details (for example, IP address)</li>
</ul>
</li>
</ol>
<h2 id="search-tips">Search tips</h2>
<h3 id="parameter-filtering">Parameter filtering</h3>
<p>To search for specific values in one of the <a href="/email-security/reporting/search/available-parameters/">available parameters</a>, format your search to be:</p>
<pre tabindex="0"><code class="language-txt">&lt;&lt;FIELD_NAME&gt;&gt;:&lt;&lt;VALUE&gt;&gt;&#10;</code></pre>
<p>For example, you might search for <code>final_disposition:MALICIOUS</code>. Refer to our reference material for a full list of <a href="/email-security/reference/dispositions-and-attributes/">dispositions</a>.</p>
<h3 id="message-id"><code>message_id</code></h3>
<p>For normal queries, spaces split search terms into different values. For example, <code>billing statement</code> would look for all messages that contain both <code>billing</code> and <code>statement</code>.</p>
<p>However, spaces, quotations, and other characters are sometimes part of the <code>message_id</code> parameter. To ensure these values are included as part of filtering on the message ID, you should prefix the <code>message_id</code> value with <code>message_id</code>.</p>
<p>For example, the following query would find all messages that contain the terms <code>billing</code> and <code>statement</code> and have a <code>message_id</code> equal to <code>&lt;Amazon aws Support@email.amazonses.com&gt;</code>.</p>
<pre tabindex="0"><code class="language-txt">billing statement message_id:&lt;Amazon aws Support@email.amazonses.com&gt;&#10;</code></pre>
