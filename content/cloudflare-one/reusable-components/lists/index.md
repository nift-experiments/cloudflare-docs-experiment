---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/
  description: Lists in Zero Trust.
  full_title: Lists · Cloudflare One docs
  head_html: <title>Lists · Cloudflare One docs</title><meta name="generator" content="Nift"><meta name="description" content="Lists in Zero Trust."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/index.md"><meta property="og:title" content="Lists · Cloudflare One docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Lists in Zero Trust."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare One"><meta name="algolia_product_filter" content="Cloudflare One"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare One"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/#page","headline":"Lists \u00b7 Cloudflare One docs","description":"Lists in Zero Trust.","url":"https://developers.cloudflare.com/cloudflare-one/reusable-components/lists/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /cloudflare-one/reusable-components/lists/
  schema: 1
---
<p>With Cloudflare One, you can create lists of URLs, hostnames, or other entries to reference when creating <a href="/cloudflare-one/traffic-policies/">Gateway policies</a> or <a href="/cloudflare-one/access-controls/policies/">Access policies</a>. This allows you to quickly create rules that match and take actions against several items at once.</p>
<p>Before creating a list, make note of the <a href="#limitations">limitations</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4435.md")
</aside>
<h2 id="list-types">List types</h2>
<p>Lists can contain a single type of data each. Supported data types include:</p>
<ul>
<li>URLs</li>
<li>Hostnames or domains</li>
<li>Serial numbers</li>
<li>User email addresses</li>
<li>IP addresses</li>
<li>Device ID numbers</li>
<li>AAGUIDs (used by <a href="/cloudflare-one/access-controls/access-settings/independent-mfa/#restrict-authenticators-by-aaguid">Access independent MFA</a> to restrict the WebAuthn authenticators users can enroll)</li>
</ul>
<h2 id="create-a-list-from-a-csv-file">Create a list from a CSV file</h2>
<p>To test uploading CSV lists, you can download a <a href="/cloudflare-one/static/list-test.csv">sample CSV file</a> of IP address ranges or copy the following into a file:</p>
<pre tabindex="0"><code class="language-csv">value,description&#10;192.0.2.0/24,This is an IP address range in CIDR format&#10;198.51.100.0/24,This is also an IP address range&#10;203.0.113.0/24,This is the third IP address range&#10;</code></pre>
<p>When you format a CSV file for upload:</p>
<ul>
<li>Each line should be a single entry that includes a value and an optional description.</li>
<li>A header row must be present for Zero Trust to recognize descriptions.</li>
<li>Trailing whitespace characters are not allowed.</li>
<li>CRLF (Windows) and LF (Unix) line endings are valid.</li>
</ul>
<p>To upload the list to the Cloudflare dashboard:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4438.md")
</div></div>
<p>You can now use this list in the policy builder by choosing the <em>in list</em> operator.</p>
<h2 id="create-a-list-manually">Create a list manually</h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/4442.md")
</div></div>
<p>You can now use this list in the policy builder by choosing the <em>in list</em> operator.</p>
<h2 id="edit-a-list">Edit a list</h2>
<ol>
<li>
<p>In the <strong>Lists</strong> page, locate the list you want to edit.</p>
</li>
<li>
<p>Select <strong>Edit</strong>. This will allow you to:</p>
<ul>
<li>Edit list name and description by selecting on the three-dots menu to the right of your list's name.</li>
<li>Delete the list by selecting the three-dots menu to the right of your list's name.</li>
<li>Delete individual entries.</li>
<li>Manually add entries to your list.</li>
</ul>
</li>
<li>
<p>Once you have edited your list, select <strong>Save</strong>.</p>
</li>
</ol>
<h2 id="limitations">Limitations</h2>
<h3 id="list-size">List size</h3>
<p>Your lists can include up to 1,000 entries for Standard plans and 5,000 for Enterprise plans. An uploaded CSV file must be smaller than 2 MB.</p>
<h3 id="wildcard-entries">Wildcard entries</h3>
<p>Hostname lists do not support wildcard entries (<code>*.example.com</code>). You will need to add domains as exact matches. Adding a wildcard to lists comprised of hostnames will return an error when you save.</p>
<h3 id="non-latin-characters">Non-Latin characters</h3>
<p>Gateway supports non-Latin characters by converting all domains and hostnames to <a href="https://www.rfc-editor.org/rfc/rfc3492.txt">Punycode</a>. Once you save a list with non-Latin characters, Gateway will display the entry as Punycode.</p>
<h3 id="duplicate-entries">Duplicate entries</h3>
<p>Lists cannot have duplicate entries. Because domains and hostnames are converted to <a href="#non-latin-characters">Punycode</a>, multiple list entries that convert to the same string will count as duplicates. For example, <code>éxàmple.com</code> converts to <code>xn—xmple-rqa5d.com</code>, so including both <code>éxàmple.com</code> and <code>xn—xmple-rqa5d.com</code> in a list will result in a duplicate error.</p>
<h3 id="url-slashes">URL slashes</h3>
<p>Gateway ignores trailing forward slashes (<code>/</code>) in URLs. For example, <code>https://example.com</code> and <code>https://example.com/</code> will count as the same URL and may return a duplicate error.</p>
<h3 id="extended-email-addresses">Extended email addresses</h3>
<p>Extended email addresses (also known as plus addresses) are variants of an existing email address with <code>+</code> or <code>.</code> modifiers. Many email providers, such as Gmail and Outlook, deliver emails intended for an extended address to its original address. For example, providers will deliver emails sent to <code>contact+123@example.com</code> or <code>con.tact@example.com</code> to <code>contact@example.com</code>.</p>
<p>By default, Gateway will either filter only exact matches or all extended variants depending on the type of policy and action used:</p>
<details class="nb-details"><summary>DNS policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4443.md")
</div></details>
<details class="nb-details"><summary>Network policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4444.md")
</div></details>
<details class="nb-details"><summary>HTTP policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4445.md")
</div></details>
<details class="nb-details"><summary>Other policies</summary><div class="nb-details-body">
@input("content/.markup/bodies/4446.md")
</div></details>
<p>To force Gateway to match all email address variants, go to <strong>Traffic policies</strong> &gt; <strong>Traffic settings</strong> &gt; <strong>Policy settings</strong> and turn on <strong>Match extended email addresses</strong>. This setting applies to all firewall, egress, and resolver policies.</p>
<h3 id="api-rate-limit">API rate limit</h3>
<p>You can send 600 requests to the <a href="/api/resources/zero_trust/subresources/gateway/subresources/lists/">Gateway Lists</a> endpoint per minute. If you exceed the rate limit, Cloudflare will block subsequent requests for 120 seconds.</p>
