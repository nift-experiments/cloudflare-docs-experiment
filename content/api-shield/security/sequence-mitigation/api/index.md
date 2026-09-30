---
cp9:
  canonical: https://developers.cloudflare.com/api-shield/security/sequence-mitigation/api/
  description: Build and configure sequence mitigation rules using the Cloudflare API.
  full_title: Configure sequence mitigation via the API · Cloudflare API Shield docs
  head_html: <title>Configure sequence mitigation via the API · Cloudflare API Shield docs</title><meta name="generator" content="Nift"><meta name="description" content="Build and configure sequence mitigation rules using the Cloudflare API."><link rel="canonical" href="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/api/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/api/index.md"><meta property="og:title" content="Configure sequence mitigation via the API · Cloudflare API Shield docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Build and configure sequence mitigation rules using the Cloudflare API."><meta property="og:url" content="https://developers.cloudflare.com/api-shield/security/sequence-mitigation/api/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="API Shield"><meta name="algolia_product_filter" content="API Shield"><meta name="pcx_content_group" content="Application security"><meta name="pcx_content_type" content="How to"><meta name="algolia_content_type" content="How to"><meta name="pcx_additional_products" content="API Shield"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/api-shield/security/sequence-mitigation/api/#page","headline":"Configure sequence mitigation via the API \u00b7 Cloudflare API Shield docs","description":"Build and configure sequence mitigation rules using the Cloudflare API.","url":"https://developers.cloudflare.com/api-shield/security/sequence-mitigation/api/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /api-shield/security/sequence-mitigation/api/
  schema: 1
---
<p>Configuring sequence mitigation via the API consists of building a rule object by choosing the sequence and setting the type of rule and its action.</p>
<pre tabindex="0"><code class="language-json">{&#10;    &quot;id&quot;: &quot;d4909253-390f-4956-89fd-92a5b0cd86d8&quot;,&#10;    &quot;title&quot;: &quot;&lt;RULE_TITLE&gt;&quot;,&#10;    &quot;kind&quot;: &quot;allow&quot;,&#10;    &quot;action&quot;: &quot;block&quot;,&#10;    &quot;sequence&quot;: [&#10;     &quot;0d9bf70c-92e1-4bb3-9411-34a3bcc59003&quot;,&#10;     &quot;b704ab4d-5be0-46e0-9875-b2b3d1ab42f9&quot;&#10;    ],&#10;    &quot;priority&quot;: 0,&#10;    &quot;last_updated&quot;: &quot;2023-07-24T12:06:51.796286Z&quot;,&#10;    &quot;created_at&quot;: &quot;2023-07-24T12:06:51.796286Z&quot;&#10;}&#10;</code></pre>
<p>This rule enforces that a request to endpoint <code>0d9bf70c-92e1-4bb3-9411-34a3bcc59003</code> must come before a request to endpoint <code>b704ab4d-5be0-46e0-9875-b2b3d1ab42f9</code>.</p>
<p>Otherwise, the request to endpoint <code>b704ab4d-5be0-46e0-9875-b2b3d1ab42f9</code> is blocked.</p>
<h3 id="fields">Fields</h3>
<table>
<thead>
<tr>
<th><span style="width:115px">Field name</span></th>
<th>Description</th>
<th>Possible Values</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>id</code></td>
<td>An opaque identifier that identifies a rule.</td>
<td>A UUID</td>
<td><code>&quot;d4909253-390f-4956-89fd-92a5b0cd86d8&quot;</code></td>
</tr>
<tr>
<td><code>title</code></td>
<td>A string that helps to identify the rule.</td>
<td>A value between 1 and 50 characters</td>
<td><code>&quot;Allow checkout sequence&quot;</code></td>
</tr>
<tr>
<td><code>kind</code></td>
<td>Defines the semantics of this rule. Block rules have a negative security model and allow to explicitly deny a sequence. Allow rules have a positive security model and deny everything but the configured sequence.</td>
<td><code>block</code>, <code>allow</code></td>
<td><code>&quot;block&quot;</code></td>
</tr>
<tr>
<td><code>action</code></td>
<td>What firewall action should we do when the rule matches.</td>
<td><code>block</code>,<code>log</code></td>
<td><code>&quot;log&quot;</code></td>
</tr>
<tr>
<td><code>sequence</code></td>
<td>Denotes the operations (from Endpoint Management) that make up the sequence for this rule. We currently only support sequences of length two. The first operation will be the starting endpoint and the second operation will be the ending endpoint.</td>
<td>An array with two valid operation IDs from Endpoint Management</td>
<td><code>[&quot;0d9bf70c-92e1-4bb3-9411-34a3bcc59003&quot;, &quot;b704ab4d-5be0-46e0-9875-b2b3d1ab42f9&quot;]</code></td>
</tr>
<tr>
<td><code>priority</code></td>
<td>Denotes the precedence of this rule in relation to all other rules. Rules with a higher priority value are evaluated before those with a lower value. If two rules have the same priority, they are evaluated in the order in which they were added.</td>
<td>A valid integer</td>
<td><code>10</code></td>
</tr>
<tr>
<td><code>last_updated</code></td>
<td>When this rule was last changed.</td>
<td>A date string</td>
<td><code>2023-05-02T12:06:51.796286Z</code></td>
</tr>
<tr>
<td><code>created_at</code></td>
<td>When this rule was created.</td>
<td>A date string</td>
<td><code>2023-05-02T12:06:51.796286Z</code></td>
</tr>
</tbody>
</table>
<p>You can find an endpoint's operation ID by exporting the schema in <a href="/api-shield/management-and-monitoring/#export-a-schema">Endpoint Management</a> or via the <a href="/api/resources/api_gateway/subresources/operations/methods/list/">API</a>.</p>
<h3 id="list-sequence-rules">List sequence rules</h3>
<p>Use the <code>GET</code> command to list rules.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/seqrules&quot;&#10;</code></pre>
<h3 id="add-a-single-sequence-rule">Add a single sequence rule</h3>
<p>Use the <code>POST</code> command to create a single rule.</p>
<p>This adds a single rule to all existing rules. Priority can be used to place the rule between, before, or after another rule.</p>
<p>The response will reflect the rule that has been written with its ID. In case something is not right with the rule, an appropriate error message with a <code>json</code> path pointing towards the issue will be provided.</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/seqrules/rules&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;title&quot;: &quot;string&quot;,&#10;  &quot;kind&quot;: &quot;block&quot;,&#10;  &quot;action&quot;: &quot;block&quot;,&#10;  &quot;sequence&quot;: [&#10;    &quot;0d9bf70c-92e1-4bb3-9411-34a3bcc59003&quot;,&#10;    &quot;b704ab4d-5be0-46e0-9875-b2b3d1ab42f9&quot;&#10;  ],&#10;  &quot;priority&quot;: 0&#10;}&#x27;&#10;</code></pre>
<h3 id="add-multiple-sequence-rules">Add multiple sequence rules</h3>
<p>Use the <code>PUT</code> command to set up new rules in bulk.</p>
<p>This will overwrite any existing rules and replace them with the rules specified in the body. Setting an empty array for the rules removes all rules.</p>
<p>The response will reflect the rules that have been written with their IDs in case something is not right with the rules, an appropriate error message with a <code>json</code> path pointing towards the issue will be provided.</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/seqrules&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;{&#10;  &quot;rules&quot;: [&#10;    {&#10;      &quot;title&quot;: &quot;&lt;RULE_TITLE&gt;&quot;,&#10;      &quot;kind&quot;: &quot;block&quot;,&#10;      &quot;action&quot;: &quot;block&quot;,&#10;      &quot;sequence&quot;: [&#10;        &quot;0d9bf70c-92e1-4bb3-9411-34a3bcc59003&quot;,&#10;        &quot;b704ab4d-5be0-46e0-9875-b2b3d1ab42f9&quot;&#10;      ],&#10;      &quot;priority&quot;: 0&#10;    }&#10;  ]&#10;}&#x27;&#10;</code></pre>
<h3 id="delete-a-rule">Delete a rule</h3>
<p>Use the <code>DELETE</code> command with its rule ID to delete a rule.</p>
<pre tabindex="0"><code class="language-bash">curl --request DELETE &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/api_gateway/seqrules/rules/d4909253-390f-4956-89fd-92a5b0cd86d8&quot;&#10;</code></pre>
