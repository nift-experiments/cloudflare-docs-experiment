---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/
  description: Add custom policies to the Network Firewall.
  full_title: Add custom policies · Cloudflare Network Firewall docs
  head_html: <title>Add custom policies · Cloudflare Network Firewall docs</title><meta name="generator" content="Nift"><meta name="description" content="Add custom policies to the Network Firewall."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/index.md"><meta property="og:title" content="Add custom policies · Cloudflare Network Firewall docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Add custom policies to the Network Firewall."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare Network Firewall"><meta name="algolia_product_filter" content="Cloudflare Network Firewall"><meta name="pcx_content_group" content="Cloudflare One"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="Cloudflare Network Firewall"><meta name="pcx_tags" content="Geolocation"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/#page","headline":"Add custom policies \u00b7 Cloudflare Network Firewall docs","description":"Add custom policies to the Network Firewall.","url":"https://developers.cloudflare.com/cloudflare-network-firewall/how-to/add-policies/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Geolocation"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-network-firewall/how-to/add-policies/
  schema: 1
---
<p>By default, you can create a maximum of 200 policies. We recommend you create lists of IP addresses to reference within policies to streamline policy management.</p>
<h2 id="add-a-policy">Add a policy</h2>
<ol>
<li>In the <a href="https://one.dash.cloudflare.com">Cloudflare One</a> dashboard, go to <strong>Firewall policies</strong> &gt; <strong>Custom policies</strong>.</li>
<li>Select <strong>Add a policy</strong>.</li>
<li>Fill out the information for your new policy. All existing policies apply to IPv4. You can use a managed <a href="https://www.cloudflare.com/en-gb/ips/">IP list</a> when populating the <strong>Value</strong>.</li>
<li>When you are done, select <strong>Add new policy</strong>.</li>
</ol>
<h2 id="create-a-disabled-policy">Create a disabled policy</h2>
<p>When you add a new policy, the policy is <strong>Enabled</strong> by default.</p>
<p>To create a <strong>Disabled</strong> policy, follow the steps in <a href="#add-a-policy">Add a policy</a> above and toggle <strong>Enabled</strong> to off. When a policy is in the disabled state, the policy will not perform the action until is set to <strong>Enabled</strong>.</p>
<p>To disable an existing policy, from the <strong>Custom policies</strong> tab, set the <strong>Enabled</strong> toggle to off.</p>
<h2 id="update-a-policy">Update a policy</h2>
<ol>
<li>In the <a href="https://one.dash.cloudflare.com">Cloudflare One</a> dashboard, go to <strong>Firewall policies</strong> &gt; <strong>Custom policies</strong>.</li>
<li>Locate the policy you want to edit and select the three dots &gt; <strong>Edit</strong>.</li>
<li>Update the policy with your changes and select <strong>Save</strong>.</li>
</ol>
<h2 id="delete-an-existing-policy">Delete an existing policy</h2>
<ol>
<li>Locate the policy you want to delete in the list.</li>
<li>From the end of the row, select <strong>Delete</strong>.</li>
<li>Select <strong>Delete</strong> again to confirm the deletion.</li>
</ol>
<h2 id="api">API</h2>
<p>Below, you can find examples of how to use the API to perform certain actions.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="warning">Warning</h3>
@markup("md", "content/.markup/bodies/4273.md")
</aside>
<h3 id="skip-action">Skip action</h3>
<p>The example below blocks all TCP ports, but allows one port (<code>8080</code>) by using the skip action.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Example ruleset&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;phase&quot;: &quot;magic_transit&quot;,&#10;  &quot;description&quot;: &quot;Example ruleset description&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;skip&quot;,&#10;      &quot;action_parameters&quot;: { &quot;ruleset&quot;: &quot;current&quot; },&#10;      &quot;expression&quot;: &quot;tcp.dstport in { 8080 } &quot;,&#10;      &quot;description&quot;: &quot;Allow port 8080&quot;&#10;    },&#10;    {&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;expression&quot;: &quot;tcp.dstport in { 1..65535 }&quot;,&#10;      &quot;description&quot;: &quot;Block all TCP ports&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="block-a-country">Block a country</h3>
<p>The example below blocks all packets with a source or destination IP address coming from Brazil by using its 2-letter country code in <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2</a> format.</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Example ruleset&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;phase&quot;: &quot;magic_transit&quot;,&#10;  &quot;description&quot;: &quot;Example ruleset description&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;expression&quot;: &quot;ip.src.country == \&quot;BR\&quot;&quot;,&#10;      &quot;description&quot;: &quot;Block traffic from Brazil&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="use-an-ip-list">Use an IP list</h3>
<p>Cloudflare Network Firewall supports <a href="/waf/tools/lists/use-in-expressions/">using lists in expressions</a> for the <code>ip.src</code> and <code>ip.dst</code> fields. The supported lists are:</p>
<ul>
<li><code>$cf.anonymizer</code> - Anonymizer proxies</li>
<li><code>$cf.botnetcc</code> - Botnet command and control channel</li>
<li><code>$cf.malware</code> - Sources of malware</li>
<li><code>$&lt;IP_LIST_NAME&gt;</code> - The name of an account-level IP list</li>
</ul>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{account_id}/rulesets \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;Example ruleset&quot;,&#10;  &quot;kind&quot;: &quot;root&quot;,&#10;  &quot;phase&quot;: &quot;magic_transit&quot;,&#10;  &quot;description&quot;: &quot;Example ruleset description&quot;,&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;expression&quot;: &quot;ip.src in $cf.anonymizer&quot;,&#10;      &quot;description&quot;: &quot;Block traffic from anonymizer proxies&quot;&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
