---
cp9:
  canonical: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/
  description: Configure per-hostname settings such as URL rewriting and custom headers.
  full_title: Custom metadata · Cloudflare for Platforms docs
  head_html: <title>Custom metadata · Cloudflare for Platforms docs</title><meta name="generator" content="Nift"><meta name="description" content="Configure per-hostname settings such as URL rewriting and custom headers."><link rel="canonical" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/index.md"><meta property="og:title" content="Custom metadata · Cloudflare for Platforms docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Configure per-hostname settings such as URL rewriting and custom headers."><meta property="og:url" content="https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Cloudflare for Platforms"><meta name="algolia_product_filter" content="Cloudflare for Platforms"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Cloudflare for SaaS"><meta name="pcx_tags" content="JSON,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/#page","headline":"Custom metadata \u00b7 Cloudflare for Platforms docs","description":"Configure per-hostname settings such as URL rewriting and custom headers.","url":"https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["JSON","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /cloudflare-for-platforms/cloudflare-for-saas/domain-support/custom-metadata/
  schema: 1
---
<p>You may wish to configure per-hostname (customer) settings beyond the scale of Rules or Rate Limiting.</p>
<p>To do this, you will first need to reach out to your account team to enable access to Custom Metadata. After configuring custom metadata, you can use it in the following ways:</p>
<ul>
<li>Read the metadata JSON from <a href="/workers/">Cloudflare Workers</a> (requires access to Workers) to define per-hostname behavior.</li>
<li>Use custom metadata values in <a href="/ruleset-engine/rules-language/expressions/">rule expressions</a> of different Cloudflare security products to define the rule scope.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4103.md")
</aside>
<hr />
<h2 id="examples">Examples</h2>
<ul>
<li>Per-customer URL rewriting — for example, customers 1-10,000 fetch assets from server A, 10,001-20,000 from server B, etc.</li>
<li>Adding custom headers — for example, <code>X-Customer-ID: $number</code> based on the metadata you provided</li>
<li>Setting HTTP Strict Transport Security (“HSTS”) headers on a per-customer basis</li>
</ul>
<p>Please speak with your Solutions Engineer to discuss additional logic and requirements.</p>
<h2 id="submitting-custom-metadata">Submitting custom metadata</h2>
<p>You may add custom metadata to Cloudflare via the Custom Hostnames API. This data can be added via a <a href="/api/resources/custom_hostnames/methods/edit/"><code>PATCH</code> request</a> to the specific hostname ID to set metadata for that hostname, for example:</p>
<pre tabindex="0" class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_hostnames/{custom_hostname_id} \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;ssl&quot;: {&#10;    &quot;method&quot;: &quot;http&quot;,&#10;    &quot;type&quot;: &quot;dv&quot;&#10;  },&#10;  &quot;custom_metadata&quot;: {&#10;    &quot;customer_id&quot;: &quot;12345&quot;,&#10;    &quot;redirect_to_https&quot;: true,&#10;    &quot;security_tag&quot;: &quot;low&quot;&#10;  }&#10;}&#x27;</code></pre>
<p>Changes to metadata will propagate across Cloudflare's edge within 30 seconds.</p>
<hr />
<h2 id="accessing-custom-metadata-from-a-cloudflare-worker">Accessing custom metadata from a Cloudflare Worker</h2>
<p>The metadata object will be accessible on each request using the <code>request.cf.hostMetadata</code> property. You can then read the data, and customize any behavior on it using the Worker.</p>
<p>In the example below we will use the user_id in the Worker that was submitted using the API call above <code>&quot;custom_metadata&quot;:{&quot;customer_id&quot;:&quot;12345&quot;,&quot;redirect_to_https&quot;: true,&quot;security_tag&quot;:&quot;low&quot;}</code>, and set a request header to send the <code>customer_id</code> to the origin:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/4104.md")
</div>
<h2 id="accessing-custom-metadata-in-a-rule-expression">Accessing custom metadata in a rule expression</h2>
<p>Use the <a href="/ruleset-engine/rules-language/fields/reference/cf.hostname.metadata/"><code>cf.hostname.metadata</code></a> field to access the metadata object in rule expressions. To obtain the different values from the JSON object, use the <a href="/ruleset-engine/rules-language/functions/#lookup_json_string"><code>lookup_json_string</code></a> function.</p>
<p>The following rule expression defines that there will be a rule match if the <code>security_tag</code> value in custom metadata contains the value <code>low</code>:</p>
<pre tabindex="0"><code class="language-txt">lookup_json_string(cf.hostname.metadata, &quot;security_tag&quot;) eq &quot;low&quot;&#10;</code></pre>
<hr />
<h2 id="best-practices">Best practices</h2>
<ul>
<li>Ensure that the JSON schema used is fixed: changes to the schema without corresponding Cloudflare Workers changes will potentially break websites, or fall back to any defined “default” behavior</li>
<li>Prefer a flat JSON structure</li>
<li>Use string keys in snake_case (rather than camelCase or PascalCase)</li>
<li>Use proper booleans (true/false rather than <code>true</code> or <code>1</code> or <code>0</code>)</li>
<li>Use numbers to represent integers instead of strings (<code>1</code> or <code>2</code> instead of <code>&quot;1&quot;</code> or <code>&quot;2&quot;</code>)</li>
<li>Define fallback behaviour in the non-presence of metadata</li>
<li>Define fallback behaviour if a key or value in the metadata are unknown</li>
</ul>
<p>General guidance is to follow <a href="https://google.github.io/styleguide/jsoncstyleguide.xml">Google's JSON Style guide</a> where appropriate.</p>
<hr />
<h2 id="limitations">Limitations</h2>
<p>There are some limitations to the metadata that can be provided to Cloudflare:</p>
<ul>
<li>It must be valid JSON.</li>
<li>Any origin resolution — for example, directing requests for a given hostname to a specific backend — must be provided as a hostname that exists within Cloudflare's DNS (even for non-authoritative setups). Providing an IP address directly will cause requests to error.</li>
<li>The total payload must not exceed 4 KB.</li>
<li>It requires a Cloudflare Worker that knows how to process the schema and trigger logic based on the contents.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/4102.md")
</aside>
<h3 id="terraform-support">Terraform support</h3>
<p><a href="/terraform/">Terraform</a> only allows maps of a single type, so Cloudflare's Terraform support for custom metadata for custom hostnames is limited to string keys and values.</p>
