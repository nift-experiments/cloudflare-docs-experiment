---
cp9:
  canonical: https://developers.cloudflare.com/changelog/product-group/core-platform/8/
  description: '2025-04-09'
  full_title: Core platform changelog - page 8 | Cloudflare Docs
  head_html: <title>Core platform changelog - page 8 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="2025-04-09"><link rel="canonical" href="https://developers.cloudflare.com/changelog/product-group/core-platform/8/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Core platform changelog - page 8"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="2025-04-09"><meta property="og:url" content="https://developers.cloudflare.com/changelog/product-group/core-platform/8/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/product-group/core-platform/8/#page","headline":"Core platform changelog - page 8 | Cloudflare Docs","description":"2025-04-09","url":"https://developers.cloudflare.com/changelog/product-group/core-platform/8/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/product-group/core-platform/8/
  schema: 1
---
<h1 id="changelog">Changelog</h1>

<h2 id="cloudflare-snippets-are-now-generally-available"><a href="/changelog/post/2025-04-09-snippets-ga/">Cloudflare Snippets are now Generally Available</a></h2>
<p><em>2025-04-09</em></p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga.png" alt="Cloudflare Snippets are now GA" /></p>
<p><a href="/rules/snippets/">Cloudflare Snippets</a> are now generally available at no extra cost across all paid plans — giving you a fast, flexible way to programmatically control HTTP traffic using lightweight JavaScript.</p>
<p>You can now use Snippets to modify HTTP requests and responses with confidence, reliability, and scale. Snippets are production-ready and deeply integrated with Cloudflare Rules, making them ideal for everything from quick dynamic header rewrites to advanced routing logic.</p>
<p>What's new:</p>
<ul>
<li><strong>Snippets are now GA</strong> – Available at no extra cost on all Pro, Business, and Enterprise plans.</li>
<li><strong>Ready for production</strong> – Snippets deliver a production-grade experience built for scale.</li>
<li><strong>Part of the Cloudflare Rules platform</strong> – Snippets inherit request modifications from other Cloudflare products and support sequential execution, allowing you to run multiple Snippets on the same request and apply custom modifications step by step.</li>
<li><strong>Trace integration</strong> – Use <a href="/rules/trace-request/">Cloudflare Trace</a> to see which Snippets were triggered on a request — helping you understand traffic flow and debug more effectively.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/rules/snippets-ga-trace.gif" alt="Snippets shown in Cloudflare Trace results" /></p>
<p>Learn more in the <a href="https://blog.cloudflare.com/snippets/">launch blog post</a>.</p>


<h2 id="register-and-renew-ai-and-shop-domains-at-cost"><a href="/changelog/post/2025-03-27-ai-domains-available/">Register and renew .ai and .shop domains at cost</a></h2>
<p><em>2025-03-27T10:00:00</em></p>
<p><img src="/assets/upstream/images/changelog/registrar/2025-03-27-ai-domains-available.png" alt="Example search for .ai domains" /></p>
<p>Cloudflare Registrar now supports <code>.ai</code> and <code>.shop</code> domains. These are two of our most highly-requested top-level domains (TLDs) and are great additions to the <a href="https://domains.cloudflare.com/tlds">300+ other TLDs we support</a>.</p>
<p>Starting today, customers can:</p>
<ul>
<li>Register and renew these domains <em>at cost</em> without any markups or add-on fees</li>
<li>Enjoy best-in-class security and performance with native integrations with Cloudflare DNS, CDN, and SSL services like one-click DNSSEC</li>
<li>Combat domain hijacking with <a href="https://www.cloudflare.com/products/registrar/custom-domain-protection/">Custom Domain Protection</a> (available on enterprise plans)</li>
</ul>
<p>We can't wait to see what AI and e-commerce projects you deploy on Cloudflare. To get started, transfer your domains to Cloudflare or <a href="https://domains.cloudflare.com/">search for new ones to register</a>.</p>


<h2 id="audit-logs-version-2-beta-release"><a href="/changelog/post/2025-03-27-automatic-audit-logs-beta-release/">Audit logs (version 2) - Beta Release</a></h2>
<p><em>2025-03-27</em></p>
<p>The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.</p>
<p>Availability: Audit logs (version 2) is now in Beta, with support limited to <strong>API access</strong>.</p>
<p>Use the following API endpoint to retrieve audit logs:</p>
<pre tabindex="0"><code class="language-js">GET https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/logs/audit?since=&lt;date&gt;&amp;before=&lt;date&gt;&#10;</code></pre>
<p>You can access detailed documentation for audit logs (version 2) Beta API release <a href="https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/">here</a>.</p>
<p><strong>Key Improvements in the Beta Release:</strong></p>
<ul>
<li>
<p><strong>Automated &amp; standardized logging</strong>: Logs are now generated automatically using a standardized system, replacing manual, team-dependent logging. This ensures consistency across all Cloudflare services.</p>
</li>
<li>
<p><strong>Expanded product coverage</strong>: Increased audit log coverage from 75% to 95%. Key API endpoints such as <code>/accounts</code>, <code>/zones</code>, and <code>/organizations</code> are now included.</p>
</li>
<li>
<p><strong>Granular filtering</strong>: Logs now follow a uniform format, enabling precise filtering by actions, users, methods, and resources—allowing for faster and more efficient investigations.</p>
</li>
<li>
<p><strong>Enhanced context and traceability</strong>: Each log entry now includes detailed context, such as the authentication method used, the interface (API or Dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for better traceability.</p>
</li>
<li>
<p><strong>Comprehensive activity capture</strong>: Expanded logging to include GET requests and failed attempts, ensuring that all critical activities are recorded.</p>
</li>
</ul>
<p><strong>Known Limitations in Beta</strong></p>
<ul>
<li>Error handling for the API is not implemented.</li>
<li>There may be gaps or missing entries in the available audit logs.</li>
<li>UI is unavailable in this Beta release.</li>
<li>System-level logs and User-Activity logs are not included.</li>
</ul>
<p>Support for these features is coming as part of the GA release later this year. For more details, including a sample audit log, check out our blog post: <a href="https://blog.cloudflare.com/introducing-automatic-audit-logs/">Introducing Automatic Audit Logs</a></p>


<h2 id="updates-to-account-home-quick-actions-traffic-insights-workers-projects-and-more"><a href="/changelog/post/2025-03-26-account-home-updates/">Updates to Account Home - Quick actions, traffic insights, Workers projects, and more</a></h2>
<p><em>2025-03-26T06:00:00</em></p>
<p><img src="/assets/upstream/images/changelog/fundamentals/2025-03-26-account-home-updates.png" alt="Updated Account Home" /></p>
<p>Recently, Account Home has been updated to streamline your workflows:</p>
<ul>
<li>
<p><strong>Recent Workers projects</strong>: You'll now find your projects readily accessible from a new <code>Developer Platform</code> tab on Account Home. See recently-modified projects and explore what you can work our developer-focused products.</p>
</li>
<li>
<p><strong>Traffic and security insights</strong>: Get a snapshot of domain performance at a glance with key metrics and trends.</p>
</li>
<li>
<p><strong>Quick actions</strong>: You can now perform common actions for your account, domains, and even Workers in just 1-2 clicks from the 3-dot menu.</p>
</li>
<li>
<p><strong>Keep starred domains front and center</strong>: Now, when you filter for starred domains on Account Home, we'll save your preference so you'll continue to only see starred domains by default.</p>
</li>
</ul>
<p>We can't wait for you to take the new Account Home for a spin.</p>
<p>For more info:</p>
<ul>
<li><a href="https://dash.cloudflare.com/">Try the updated Account Home</a></li>
<li><a href="/fundamentals/manage-domains/star-zones/">Documentation on starred domains</a></li>
</ul>


<h2 id="dozens-of-cloudflare-terraform-provider-resources-now-have-proper-drift-detection"><a href="/changelog/post/2025-03-21-resource-force-replacement-bug/">Dozens of Cloudflare Terraform Provider resources now have proper drift detection</a></h2>
<p><em>2025-03-21</em></p>
<p>In <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, dozens of resources now have proper drift detection. Before this fix, these resources would indicate they needed to be updated or replaced — even if there was no real change. Now, you can rely on your <code>terraform plan</code> to only show what resources are expected to change.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>API Shield</li>
<li>Argo Smart Routing</li>
<li>Argo Tiered Caching</li>
<li>Bot Management</li>
<li>BYOIP</li>
<li>D1</li>
<li>DNS</li>
<li>Email Routing</li>
<li>Hyperdrive</li>
<li>Observatory</li>
<li>Pages</li>
<li>R2</li>
<li>Rules</li>
<li>SSL/TLS</li>
<li>Waiting Room</li>
<li>Workers</li>
<li>Zero Trust</li>
</ul>


<h2 id="cloudflare-terraform-provider-now-properly-redacts-sensitive-values"><a href="/changelog/post/2025-03-21-sensitive-values-redacted/">Cloudflare Terraform Provider now properly redacts sensitive values</a></h2>
<p><em>2025-03-21</em></p>
<p>In the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform Provider</a> versions 5.2.0 and above, sensitive properties of resources are redacted in logs. Sensitive properties in <a href="https://raw.githubusercontent.com/cloudflare/api-schemas/refs/heads/main/openapi.yaml">Cloudflare's OpenAPI Schema</a> are now annotated with <code>x-sensitive: true</code>. This results in proper auto-generation of the corresponding Terraform resources, and prevents sensitive values from being shown when you run Terraform commands.</p>
<p>This issue affected <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">resources</a> related to these products and features:</p>
<ul>
<li>Alerts and Audit Logs</li>
<li>Device API</li>
<li>DLP</li>
<li>DNS</li>
<li>Magic Visibility</li>
<li>Magic WAN</li>
<li>TLS Certs and Hostnames</li>
<li>Tunnels</li>
<li>Turnstile</li>
<li>Workers</li>
<li>Zaraz</li>
</ul>


<h2 id="one-click-logpush-setup-with-r2-object-storage"><a href="/changelog/post/2025-03-06-oneclick-logpush/">One-click Logpush Setup with R2 Object Storage</a></h2>
<p><em>2025-03-06</em></p>
<p>We’ve streamlined the <a href="/logs/logpush/">Logpush</a> setup process by integrating R2 bucket creation directly into the Logpush workflow!</p>
<p>Now, you no longer need to navigate multiple pages to manually create an R2 bucket or copy credentials. With this update, you can seamlessly <strong>configure a Logpush job to R2 in just one click</strong>, reducing friction and making setup faster and easier.</p>
<p>This enhancement makes it easier for customers to adopt Logpush and R2.</p>
<p>For more details refer to our <a href="/logs/logpush/logpush-job/enable-destinations/r2/">Logs</a> documentation.</p>


<h2 id="increased-cloudflare-rules-limits"><a href="/changelog/post/2025-02-12-rules-upgraded-limits/">Increased Cloudflare Rules limits</a></h2>
<p><em>2025-02-12</em></p>
<p>We have upgraded and streamlined <a href="/rules/">Cloudflare Rules</a> limits across all plans, simplifying rule management and improving scalability for everyone.</p>
<p><strong>New limits by product:</strong></p>
<ul>
<li><a href="/rules/url-forwarding/bulk-redirects/">Bulk Redirects</a>
<ul>
<li>Free: <strong>20</strong> → <strong>10,000</strong> URL redirects across lists</li>
<li>Pro: <strong>500</strong> → <strong>25,000</strong> URL redirects across lists</li>
<li>Business: <strong>500</strong> → <strong>50,000</strong> URL redirects across lists</li>
<li>Enterprise: <strong>10,000</strong> → <strong>1,000,000</strong> URL redirects across lists</li>
</ul>
</li>
<li><a href="/rules/cloud-connector/">Cloud Connector</a>
<ul>
<li>Free: <strong>5</strong> → <strong>10</strong> connectors</li>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> connectors</li>
</ul>
</li>
<li><a href="/rules/custom-errors/">Custom Errors</a>
<ul>
<li>Pro: <strong>5</strong> → <strong>25</strong> error assets and rules</li>
<li>Business: <strong>20</strong> → <strong>50</strong> error assets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> error assets and rules</li>
</ul>
</li>
<li><a href="/rules/snippets/">Snippets</a>
<ul>
<li>Pro: <strong>10</strong> → <strong>25</strong> code snippets and rules</li>
<li>Business: <strong>25</strong> → <strong>50</strong> code snippets and rules</li>
<li>Enterprise: <strong>50</strong> → <strong>300</strong> code snippets and rules</li>
</ul>
</li>
<li><a href="/cache/how-to/cache-rules/">Cache Rules</a>, <a href="/rules/configuration-rules/">Configuration Rules</a>, <a href="/rules/compression-rules/">Compression Rules</a>, <a href="/rules/origin-rules/">Origin Rules</a>, <a href="/rules/url-forwarding/single-redirects/">Single Redirects</a>, and <a href="/rules/transform/">Transform Rules</a>
<ul>
<li>Enterprise: <strong>125</strong> → <strong>300</strong> rules</li>
</ul>
</li>
</ul>
<aside class="nb-aside note">
<h4 class="nb-aside-title" id="2025-02-12-rules-upgraded-limits-gradual-rollout">Gradual rollout</h4>
@markup("md", "content/.markup/bodies/17745.md")</aside>


<h2 id="custom-errors-beta-stored-assets-account-level-rules"><a href="/changelog/post/2025-02-11-custom-errors-beta/">Custom Errors (beta): Stored Assets & Account-level Rules</a></h2>
<p><em>2025-02-11</em></p>
<p>We're introducing <a href="/rules/custom-errors/">Custom Errors</a> (beta), which builds on our existing Custom Error Responses feature with new asset storage capabilities.</p>
<p>This update allows you to store externally hosted error pages on Cloudflare and reference them in custom error rules, eliminating the need to supply inline content.</p>
<p>This brings the following new capabilities:</p>
<ul>
<li><strong>Custom error assets</strong> – Fetch and store external error pages at the edge for use in error responses.</li>
<li><strong>Account-Level custom errors</strong> – Define error handling rules and assets at the account level for consistency across multiple zones. Zone-level rules take precedence over account-level ones, and assets are not shared between levels.</li>
</ul>
<p>You can use Cloudflare API to upload your existing assets for use with Custom Errors:</p>
<pre tabindex="0"><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/custom_pages/assets&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;name&quot;: &quot;maintenance&quot;,&#10;  &quot;description&quot;: &quot;Maintenance template page&quot;,&#10;  &quot;url&quot;: &quot;https://example.com/&quot;&#10;}&#x27;&#10;</code></pre>
<p>You can then reference the stored asset in a Custom Error rule:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/rulesets/phases/http_custom_errors/entrypoint&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &#x27;Content-Type: application/json&#x27; \&#10;&#45;-data &#x27;{&#10;  &quot;rules&quot;: [&#10;		{&#10;			&quot;action&quot;: &quot;serve_error&quot;,&#10;			&quot;action_parameters&quot;: {&#10;				&quot;asset_name&quot;: &quot;maintenance&quot;,&#10;				&quot;content_type&quot;: &quot;text/html&quot;,&#10;				&quot;status_code&quot;: 503&#10;			},&#10;			&quot;enabled&quot;: true,&#10;			&quot;expression&quot;: &quot;http.request.uri.path contains \&quot;error\&quot;&quot;&#10;		}&#10;	]&#10;}&#x27;&#10;</code></pre>


<h2 id="terraform-v5-provider-is-now-generally-available"><a href="/changelog/post/2025-02-03-terraform-v5-provider/">Terraform v5 Provider is now generally available</a></h2>
<p><em>2025-02-03</em></p>
<p><img src="/assets/upstream/images/changelog/2024-02-03-terraform-v5-screenshot.png" alt="Screenshot of Terraform defining a Zone" /></p>
<p>Cloudflare's v5 Terraform Provider is now generally available. With this release, Terraform resources are now automatically generated based on OpenAPI Schemas. This change brings alignment across our SDKs, API documentation, and now Terraform Provider. The new provider boosts coverage by increasing support for API properties to 100%, adding 25% more resources, and more than 200 additional data sources. Going forward, this will also reduce the barriers to bringing more resources into Terraform across the broader Cloudflare API. This is a small, but important step to making more of our platform manageable through GitOps, making it easier for you to manage Cloudflare just like you do your other infrastructure.</p>
<p>The Cloudflare Terraform Provider v5 is a ground-up rewrite of the provider and introduces breaking changes for some resource types. Please refer to the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">upgrade guide</a> for best practices, or the <a href="https://blog.cloudflare.com/automatically-generating-cloudflares-terraform-provider/">blog post on automatically generating Cloudflare's Terraform Provider</a> for more information about the approach.</p>
<p>For more info</p>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="https://developers.cloudflare.com/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>


<h2 id="new-snippets-code-editor"><a href="/changelog/post/2025-01-29-snippets-code-editor/">New Snippets Code Editor</a></h2>
<p><em>2025-01-29</em></p>
<p>The new <a href="/rules/snippets/">Snippets</a> code editor lets you edit Snippet code and rule in one place, making it easier to test and deploy changes without switching between pages.</p>
<p><img src="/assets/upstream/images/changelog/rules/snippets-new-editor.png" alt="New Snippets code editor" /></p>
<p>What’s new:</p>
<ul>
<li><strong>Single-page editing for code and rule</strong> – No need to jump between screens.</li>
<li><strong>Auto-complete &amp; syntax highlighting</strong> – Get suggestions and avoid mistakes.</li>
<li><strong>Code formatting &amp; refactoring</strong> – Write cleaner, more readable code.</li>
</ul>
<p>Try it now in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/snippets">Rules &gt; Snippets</a>.</p>


<h2 id="new-rules-overview-interface"><a href="/changelog/post/2025-01-09-rules-overview/">New Rules Overview Interface</a></h2>
<p><em>2025-01-09</em></p>
<p><strong>Rules Overview</strong> gives you a single page to manage all your <a href="/rules/">Cloudflare Rules</a>.</p>
<p>What you can do:</p>
<ul>
<li><strong>See all your rules in one place</strong> – No more clicking around.</li>
<li><strong>Find rules faster</strong> – Search by name.</li>
<li><strong>Understand execution order</strong> – See how rules run in sequence.</li>
<li><strong>Debug easily</strong> – Use <a href="/rules/trace-request/">Trace</a> without switching tabs.</li>
</ul>
<p>Check it out in <a href="https://dash.cloudflare.com/?to=/:account/:zone/rules/overview">Rules &gt; Overview</a>.</p>


<h2 id="troubleshoot-tunnels-with-diagnostic-logs"><a href="/changelog/post/2024-12-19-diagnostic-logs/">Troubleshoot tunnels with diagnostic logs</a></h2>
<p><em>2024-12-19</em></p>
<p>The latest <code>cloudflared</code> build <a href="https://github.com/cloudflare/cloudflared/releases/tag/2024.12.2">2024.12.2</a> introduces the ability to collect all the diagnostic logs needed to troubleshoot a <code>cloudflared</code> instance.</p>
<p>A diagnostic report collects data from a single instance of <code>cloudflared</code> running on the local machine and outputs it to a <code>cloudflared-diag</code> file.</p>
<p>For more information, refer to <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/troubleshoot-tunnels/diag-logs/">Diagnostic logs</a>.</p>


<h2 id="terraform-support-for-snippets"><a href="/changelog/post/2024-12-11-terraform-snippets/">Terraform Support for Snippets</a></h2>
<p><em>2024-12-11</em></p>
<p>Now, you can manage <a href="/rules/snippets/">Cloudflare Snippets</a> with <a href="/terraform/">Terraform</a>. Use infrastructure-as-code to deploy and update Snippet code and rules without manual changes in the dashboard.</p>
<p>Example Terraform configuration:</p>
<pre tabindex="0"><code class="language-tf">resource &quot;cloudflare_snippet&quot; &quot;my_snippet&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	name = &quot;my_test_snippet_1&quot;&#10;	main_module = &quot;file1.js&quot;&#10;	files {&#10;		name = &quot;file1.js&quot;&#10;		content = file(&quot;file1.js&quot;)&#10;	}&#10;}&#10;&#10;resource &quot;cloudflare_snippet_rules&quot; &quot;cookie_snippet_rule&quot; {&#10;	zone_id  = &quot;&lt;ZONE_ID&gt;&quot;&#10;	rules {&#10;		enabled = true&#10;		expression = &quot;http.cookie eq \&quot;a=b\&quot;&quot;&#10;		description = &quot;Trigger snippet on specific cookie&quot;&#10;		snippet_name = &quot;my_test_snippet_1&quot;&#10;	}&#10;	depends_on = [cloudflare_snippet.my_snippet]&#10;}&#10;</code></pre>
<p>Learn more in the <a href="/rules/snippets/create-terraform/">Configure Snippets using Terraform</a> documentation.</p>


<h2 id="cloud-connector-now-supports-r2"><a href="/changelog/post/2024-11-22-cloud-connector-r2/">Cloud Connector Now Supports R2</a></h2>
<p><em>2024-11-22</em></p>
<p>Now, you can use <a href="/rules/cloud-connector/">Cloud Connector</a> to route traffic to your <a href="/r2/">R2 buckets</a> based on URLs, headers, geolocation, and more.</p>
<p>Example setup:</p>
<pre tabindex="0"><code class="language-bash">curl --request PUT \&#10;&quot;https://api.cloudflare.com/client/v4/zones/{zone_id}/cloud_connector/rules&quot; \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;&#45;-header &quot;Content-Type: application/json&quot; \&#10;&#45;-data &#x27;[&#10;  {&#10;    &quot;expression&quot;: &quot;http.request.uri.path wildcard \&quot;/images/*\&quot;&quot;,&#10;    &quot;provider&quot;: &quot;cloudflare_r2&quot;,&#10;    &quot;description&quot;: &quot;Connect to R2 bucket containing images&quot;,&#10;    &quot;parameters&quot;: {&#10;      &quot;host&quot;: &quot;mybucketcustomdomain.example.com&quot;&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<p>Get started using <a href="/rules/cloud-connector/">Cloud Connector</a> documentation.</p>


<h2 id="simplified-ui-for-url-rewrites"><a href="/changelog/post/2024-10-23-url-rewrites-wildcard/">Simplified UI for URL Rewrites</a></h2>
<p><em>2024-10-23</em></p>
<p>It’s now easy to create <strong>wildcard-based <a href="/rules/transform/url-rewrite/">URL Rewrites</a></strong>. No need for complex functions—just define your patterns and go.</p>
<p><img src="/assets/upstream/images/rules/transform/create-url-rewrite-rule.png" alt="Rules Overview Interface" /></p>
<p>What’s improved:</p>
<ul>
<li><strong>Full wildcard support</strong> – Create rewrite patterns using intuitive interface.</li>
<li><strong>Simplified rule creation</strong> – No need for complex functions.</li>
</ul>
<p>Try it via <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">creating a Rewrite URL rule in the dashboard</a>.</p>


<h2 id="new-fields-added-to-gateway-related-datasets-in-cloudflare-logs"><a href="/changelog/post/2024-10-08-new-gateway-fields/">New fields added to Gateway-related datasets in Cloudflare Logs</a></h2>
<p><em>2024-10-08</em></p>
<p>Cloudflare has introduced new fields to two Gateway-related datasets in Cloudflare Logs:</p>
<ul>
<li>
<p><strong>Gateway HTTP</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>CategoryIDs</code>, <code>CategoryNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
<li>
<p><strong>Gateway Network</strong>: <code>ApplicationIDs</code>, <code>ApplicationNames</code>, <code>DestinationIPContinentCode</code>, <code>DestinationIPCountryCode</code>, <code>ProxyEndpoint</code>, <code>SourceIPContinentCode</code>, <code>SourceIPCountryCode</code>, <code>TransportProtocol</code>, <code>VirtualNetworkID</code>, and <code>VirtualNetworkName</code>.</p>
</li>
</ul>


<h2 id="ai-crawl-control"><a href="/changelog/post/2024-09-23-ai-audit-launch/">AI Crawl Control</a></h2>
<p><em>2024-09-23</em></p>
<p>Every site on Cloudflare now has access to <a href="/ai-crawl-control/"><strong>AI Audit</strong></a>, which summarizes the crawling behavior of popular and known AI services.</p>
<p>You can use this data to:</p>
<ul>
<li>Understand how and how often crawlers access your site (and which content is the most popular).</li>
<li>Block specific AI bots accessing your site.</li>
<li>Use Cloudflare to enforce your <code>robots.txt</code> policy via an automatic WAF rule.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/ai-crawl-control-overview.png" alt="View AI bot activity with AI Audit" /></p>
<p>To get started, explore <a href="/ai-crawl-control/">AI audit</a>.</p>


<h2 id="new-rules-templates-for-one-click-rule-creation"><a href="/changelog/post/2024-09-05-rules-templates/">New Rules Templates for One-Click Rule Creation</a></h2>
<p><em>2024-09-05</em></p>
<p>Now, you can create <strong>common rule configurations</strong> in just <strong>one click</strong> using Rules Templates.</p>
<p><img src="/assets/upstream/images/changelog/rules/rules-templates.gif" alt="Rules Templates" /></p>
<p>What you can do:</p>
<ul>
<li><strong>Pick a pre-built rule</strong> – Choose from a library of templates.</li>
<li><strong>One-click setup</strong> – Deploy best practices instantly.</li>
<li><strong>Customize as needed</strong> – Adjust templates to fit your setup.</li>
</ul>
<p>Template cards are now also available directly in the rule builder for each product.</p>
<p>Need more ideas? Check out the <a href="/rules/examples/">Examples gallery</a> in our documentation.</p>


<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/product-group/core-platform/7/">Previous</a><span>Page 8 of 8</span></nav>
