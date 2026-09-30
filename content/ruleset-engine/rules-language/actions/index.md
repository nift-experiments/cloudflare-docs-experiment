---
cp9:
  canonical: https://developers.cloudflare.com/ruleset-engine/rules-language/actions/
  description: Learn about actions supported by the Rules language, including Block, Skip, and Log.
  full_title: Actions reference · Cloudflare Ruleset Engine docs
  head_html: <title>Actions reference · Cloudflare Ruleset Engine docs</title><meta name="generator" content="Nift"><meta name="description" content="Learn about actions supported by the Rules language, including Block, Skip, and Log."><link rel="canonical" href="https://developers.cloudflare.com/ruleset-engine/rules-language/actions/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/ruleset-engine/rules-language/actions/index.md"><meta property="og:title" content="Actions reference · Cloudflare Ruleset Engine docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Learn about actions supported by the Rules language, including Block, Skip, and Log."><meta property="og:url" content="https://developers.cloudflare.com/ruleset-engine/rules-language/actions/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Ruleset Engine"><meta name="algolia_product_filter" content="Ruleset Engine"><meta name="pcx_content_group" content="Core platform"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Ruleset Engine"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/ruleset-engine/rules-language/actions/#page","headline":"Actions reference \u00b7 Cloudflare Ruleset Engine docs","description":"Learn about actions supported by the Rules language, including Block, Skip, and Log.","url":"https://developers.cloudflare.com/ruleset-engine/rules-language/actions/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /ruleset-engine/rules-language/actions/
  schema: 1
---
<p>The action of a rule tells Cloudflare how to handle matches for the rule <a href="/ruleset-engine/rules-language/expressions/">expression</a>.</p>
<h2 id="supported-actions">Supported actions</h2>
<p>The table below lists the actions available in the Rules language.</p>
<p>Some actions like <em>Block</em>, called terminating actions, will stop the evaluation of the remaining rules. The <em>Skip</em> action will skip the evaluation of <em>some</em> rules when there is a match, but the exact behavior will depend on the rule configuration.</p>
<p>The available actions depend on the <a href="/ruleset-engine/about/phases/">phase</a> where you are configuring the rule. Refer to each product’s documentation for details on the phase(s) supported by that product.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Action</th>
<th>Description</th>
<th>Terminating action?</th>
</tr>
</thead>
<tbody>
<tr>
<td>
        <strong>Non-Interactive Challenge</strong><br />
<br />
        API value:<br />
        <code>js_challenge</code>
</td>
<td>
        <p>
          Useful for ensuring that bots and spam cannot access the requested resource; browsers,
          however, are free to satisfy the challenge automatically.
        </p>
        <p>
          The client that made the request must pass a non-interactive Cloudflare challenge before
          proceeding.
        </p>
        <p>If successful, Cloudflare accepts the matched request; otherwise, it is blocked.</p>
</td>
<td>Yes</td>
</tr>
<tr>
<td>
        <strong>Managed Challenge</strong><br />
<br />
        API value:<br />
        <code>managed_challenge</code>
</td>
<td>
        <p>Helps reduce the lifetimes of human time spent solving CAPTCHAs across the Internet.</p>
        <p>
          Depending on the characteristics of a request, Cloudflare will dynamically choose the appropriate type of challenge from the following actions based on specific criteria:
        </p>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;Show a non-interactive challenge page.&lt;/li&gt;&#10;      &lt;li&gt;Show a custom interactive challenge (such as click a button).&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>Yes</td>
</tr>
<tr>
<td>
        <strong>Interactive Challenge</strong><br />
<br />
        API value:<br />
        <code>challenge</code>
</td>
<td>
        <p>Useful for ensuring that the visitor accessing the site is human, not automated.</p>
        <p>The client that made the request must pass an interactive challenge.</p>
        <p>If successful, Cloudflare accepts the matched request; otherwise, it is blocked.</p>
</td>
<td>Yes</td>
</tr>
<tr>
<td>
        <strong>Block</strong><br />
<br />
        API value:<br />
        <code>block</code>
</td>
<td>
        <p>Matching requests are denied access to the site.</p>
				<p>Depending on the Cloudflare product performing the block action, the HTTP status code can be <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-403/#cloudflare-specific-information"><code>403</code></a> (most security features) or <a href="/support/troubleshooting/http-status-codes/4xx-client-error/error-429/#website-end-users"><code>429</code></a> (for example, rate limiting rules).</p>
				<p>Customers on paid plans can customize the HTML error page displayed to website visitors due to the block action. Refer to <a href="/rules/custom-errors/#error-pages">Error Pages</a> for more information.</p>
				<p>Customers in Pro plans and above can customize the response (HTML, JSON, XML, or plain text) and the response status code for each <a href="/waf/custom-rules/create-dashboard/#configure-a-custom-response-for-blocked-requests">custom rule</a> or <a href="/waf/rate-limiting-rules/create-zone-dashboard/#configure-a-custom-response-for-blocked-requests">rate limiting rule</a> that triggers a block action.</p>
</td>
<td>Yes</td>
</tr>
<tr>
<td>
        <strong>Skip</strong><br />
<br />
        API value:<br />
        <code>skip</code>
</td>
<td>
        <p>
          Allows user to dynamically skip one or more security features or products for a request.
        </p>
        <p>
          Depending on the rule configuration, matching requests will skip the evaluation of one or
          more security features or products:
        </p>
        <p>
          <ul>
<pre tabindex="0"><code>        &lt;li&gt;Skip all remaining rules in the current ruleset&lt;/li&gt;&#10;        &lt;li&gt;Skip all remaining rules in the current phase (zone-level only option)&lt;/li&gt;&#10;        &lt;li&gt;Skip rulesets&lt;/li&gt;&#10;        &lt;li&gt;Skip rules of a ruleset&lt;/li&gt;&#10;        &lt;li&gt;Skip phases&lt;/li&gt;&#10;        &lt;li&gt;Skip specific security products that are not based on the Ruleset Engine&lt;/li&gt;&#10;&#10;      &lt;/ul&gt;&#10;    &lt;/p&gt;&#10;    &lt;p&gt;&#10;      The available skip options depend on the phase where you configure the rule. Refer to each&#10;      product’s documentation for details.&#10;    &lt;/p&gt;&#10;    &lt;p&gt;&#10;      If you configure a rule with the &lt;em&gt;Skip&lt;/em&gt; action at the account level it will only&#10;      affect rules/phases configured at the account level, not at the zone level.&#10;      To skip rules/phases at the zone level you must configure a rule with the &lt;em&gt;Skip&lt;/em&gt;&#10;      action at the zone level.&#10;    &lt;/p&gt;&#10;</code></pre>
</td>
<td>
        No
<br />
        (but some rules may be skipped)
</td>
</tr>
<tr>
<td>
        <strong>Log</strong><br />
<br />
        API value:<br />
        <code>log</code>
</td>
<td>
        <p>Records matching requests in the Cloudflare Logs.</p>
        <p>Only available on Enterprise plans.</p>
        <p>Recommended for validating rules before committing to a more severe action.</p>
</td>
<td>No</td>
</tr>
<tr>
<td>
        <strong>Execute</strong><br />
<br />
        API value:<br />
        <code>execute</code>
</td>
<td>
        <p>
          Executes the rules in the ruleset specified in the rule configuration. You can specify a
          managed ruleset or a custom ruleset to execute.
        </p>
        <p>In the Cloudflare dashboard, this action is not listed in action selection dropdowns.</p>
</td>
<td>No</td>
</tr>
<tr>
<td>
        <strong>Rewrite</strong><br />
<br />
        API value:<br />
        <code>rewrite</code>
</td>
<td>
        <p>
          Rewrites the request (or response) by adjusting the URI path, query string, and/or HTTP request/response headers, according to the rule configuration.
        </p>
        <p>Only available in:</p>
        <ul>
<pre tabindex="0"><code>      &lt;li&gt;&lt;a href=&quot;/rules/transform/&quot;&gt;Transform Rules&lt;/a&gt;, in phases &lt;code&gt;http_request_transform&lt;/code&gt;, &lt;code&gt;http_request_late_transform&lt;/code&gt;, and &lt;code&gt;http_response_headers_transform&lt;/code&gt;. In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, create a Transform Rule.&lt;/li&gt;&#10;      &lt;li&gt;WAF custom rules checking for &lt;a href=&quot;/waf/managed-rules/check-for-exposed-credentials/&quot;&gt;exposed credentials&lt;/a&gt;, in the &lt;code&gt;http_request_firewall_custom&lt;/code&gt; phase at the account level. In the Cloudflare dashboard, this action is called &lt;em&gt;Exposed-Credential-Check Header&lt;/em&gt;.&lt;/li&gt;&#10;&#10;    &lt;/ul&gt;&#10;</code></pre>
</td>
<td>No</td>
</tr>
<tr>
<td>
        <strong>Redirect</strong><br />
<br />
        API value:<br />
        <code>redirect</code>
</td>
<td>
        <p>
          Navigates the user from a source URL to a target URL, according to the rule configuration, by replying with an HTTP redirect.
        </p>
        <p>
          Only available for <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a> and <a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>.
        </p>
        <p>
          In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, create a redirect rule or a bulk redirect rule.
        </p>
</td>
<td>Yes</td>
</tr>
<tr>
<td>
        <strong>Route</strong><br />
<br />
        API value:<br />
        <code>route</code>
</td>
<td>
        <p>
          Adjusts the <code>Host</code> header, Server Name Indication (SNI), resolved hostname, and/or resolved destination port of incoming requests.
        </p>
        <p>
          Only available for <a href="/rules/origin-rules/">Origin Rules</a>, in the <code>http_request_origin</code> phase.
        </p>
        <p>
          In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, create an origin rule.
        </p>
</td>
<td>No</td>
</tr>
<tr>
<td>
        <strong>Set Configuration</strong><br />
<br />
        API value:<br />
        <code>set_config</code>
</td>
<td>
        <p>
          Changes the configuration settings of one or more Cloudflare products.
        </p>
        <p>
          Only available for <a href="/rules/configuration-rules/">Configuration Rules</a>, in the <code>http_config_settings</code> phase.
        </p>
        <p>
          In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, <a href="/rules/configuration-rules/create-dashboard/">create a Configuration Rule</a>.
        </p>
</td>
<td>No</td>
</tr>
<tr>
<td>
        <strong>Compress Response</strong><br />
<br />
        API value:<br />
        <code>compress_response</code>
</td>
<td>
        <p>
          Defines compression settings for delivering responses to website visitors.
        </p>
        <p>
          Only available for <a href="/rules/compression-rules/">Compression Rules</a>, in the <code>http_response_compression</code> phase.
        </p>
        <p>
          In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, <a href="/rules/compression-rules/create-dashboard/">create a compression rule</a>.
        </p>
</td>
<td>No</td>
</tr>
<tr>
<td>
        <strong>Set Cache Settings</strong><br />
<br />
        API value:<br />
        <code>set_cache_settings</code>
</td>
<td>
        <p>
          Cache Rules allows you to customize cache settings on Cloudflare.
        </p>
        <p>
          Only available for <a href="/cache/how-to/cache-rules/">Cache Rules</a>, in the <code>http_request_cache_settings</code> phase.
        </p>
        <p>
          In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, <a href="/cache/how-to/cache-rules/create-dashboard/">create a cache rule</a>.
        </p>
</td>
<td>No</td>
</tr>
<tr>
<td>
        <strong>Serve Error</strong><br />
<br />
        API value:<br />
        <code>serve_error</code>
</td>
<td>
        <p>
          Serves error content to the website visitor, according to the custom error rule configuration.
        </p>
        <p>
          Only available for <a href="/rules/custom-errors/#custom-error-rules">Custom Error Rules</a>, in the <code>http_custom_errors</code> phase.
        </p>
        <p>
          In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, <a href="/rules/custom-errors/create-rules/#create-a-custom-error-rule-dashboard">create a custom error rule</a>.
        </p>
</td>
<td>Yes</td>
</tr>
<tr>
<td>
        <strong>Log custom field</strong><br />
<br />
        API value:<br />
        <code>log_custom_field</code>
</td>
<td>
        <p>
          Configures custom fields for Logpush jobs in a zone.
        </p>
        <p>
          Only available for <a href="/logs/logpush/logpush-job/custom-fields/">custom fields</a>, in the <code>http_log_custom_fields</code> phase.
        </p>
        <p>
          In the Cloudflare dashboard, this action is not listed in action selection dropdowns. To use this action, <a href="/logs/logpush/logpush-job/custom-fields/#enable-custom-fields-via-dashboard">configure custom log fields</a> for Logpush jobs.
        </p>
</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13270.md")
</aside>
