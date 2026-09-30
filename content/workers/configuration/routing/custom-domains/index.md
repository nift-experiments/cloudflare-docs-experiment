---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/routing/custom-domains/
  description: Connect a Cloudflare Worker to a domain or subdomain with automatic DNS and certificate management.
  full_title: Custom Domains · Cloudflare Workers docs
  head_html: <title>Custom Domains · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect a Cloudflare Worker to a domain or subdomain with automatic DNS and certificate management."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/routing/custom-domains/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/routing/custom-domains/index.md"><meta property="og:title" content="Custom Domains · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect a Cloudflare Worker to a domain or subdomain with automatic DNS and certificate management."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/routing/custom-domains/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/configuration/routing/custom-domains/#page","headline":"Custom Domains \u00b7 Cloudflare Workers docs","description":"Connect a Cloudflare Worker to a domain or subdomain with automatic DNS and certificate management.","url":"https://developers.cloudflare.com/workers/configuration/routing/custom-domains/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/routing/custom-domains/
  schema: 1
---
<h2 id="background">Background</h2>
<p>Custom Domains allow you to connect your Worker to a domain or subdomain, without having to make changes to your DNS settings or perform any certificate management. After you set up a Custom Domain for your Worker, Cloudflare will create DNS records and issue necessary certificates on your behalf. The created DNS records will point directly to your Worker. Unlike <a href="/workers/configuration/routing/routes/#set-up-a-route">Routes</a>, Custom Domains point all paths of a domain or subdomain to your Worker.</p>
<p>Custom Domains are routes to a domain or subdomain (such as <code>example.com</code> or <code>shop.example.com</code>) within a Cloudflare zone where the Worker is the origin.</p>
<p>Custom Domains are recommended if you want to connect your Worker to the Internet and do not have an application server that you want to always communicate with. If you do have external dependencies, you can create a <code>Request</code> object with the target URI, and use <code>fetch()</code> to reach out.</p>
<p>Custom Domains can stack on top of each other. For example, if you have Worker A attached to <code>app.example.com</code> and Worker B attached to <code>api.example.com</code>, Worker A can call <code>fetch()</code> on <code>api.example.com</code> and invoke Worker B.</p>
<p><img src="/assets/upstream/images/workers/learning/custom-domains-subrequest.png" alt="Custom Domains can stack on top of each other, like any external dependencies" /></p>
<p>Custom Domains can also be invoked within the same zone via <code>fetch()</code>, unlike Routes.</p>
<h2 id="add-a-custom-domain">Add a Custom Domain</h2>
<p>To add a Custom Domain, you must have:</p>
<ol>
<li>An <a href="/dns/zone-setups/">active Cloudflare zone</a>.</li>
<li>A Worker to invoke.</li>
</ol>
<p>Custom Domains can be attached to your Worker via the Cloudflare dashboard, <a href="/workers/configuration/routing/custom-domains/#set-up-a-custom-domain-in-your-wrangler-configuration-file">Wrangler</a> or the <a href="/api/resources/workers/subresources/domains/methods/list/">API</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16836.md")
</aside>
<h3 id="set-up-a-custom-domain-in-the-dashboard">Set up a Custom Domain in the dashboard</h3>
<p>To set up a Custom Domain in the dashboard:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16837.md")
</div>
<p>After you have added the domain or subdomain, Cloudflare will create a new DNS record for you. You can add multiple Custom Domains.</p>
<h3 id="require-sign-in-for-a-custom-domain">Require sign-in for a Custom Domain</h3>
<p>To require visitors to sign in before they can access a Custom Domain, use <a href="/workers/configuration/cloudflare-access/#protect-a-specific-hostname-custom-domain-or-path">Cloudflare Access</a>.</p>
<p>You can protect a Custom Domain with hostname-based Access, or protect the Worker itself across its routes, Custom Domains, <code>workers.dev</code> hostname, and previews. For more information, refer to <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<h3 id="set-up-a-custom-domain-in-your-wrangler-configuration-file">Set up a Custom Domain in your Wrangler configuration file</h3>
<p>To configure a Custom Domain in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, add the <code>custom_domain=true</code> option on each pattern under <code>routes</code>. For example, to configure a Custom Domain:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16838.md")
</div>
<p>To configure multiple Custom Domains:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16839.md")
</div>
<h2 id="worker-to-worker-communication">Worker to Worker communication</h2>
<p>On the same zone, the only way for a Worker to communicate with another Worker running on a <a href="/workers/configuration/routing/routes/#set-up-a-route">route</a>, or on a <a href="/workers/configuration/routing/routes/#_top"><code>workers.dev</code></a> subdomain, is via <a href="/workers/runtime-apis/bindings/service-bindings/">service bindings</a>.</p>
<p>On the same zone, if a Worker is attempting to communicate with a target Worker running on a Custom Domain rather than a route, the limitation is removed. Fetch requests sent on the same zone from one Worker to another Worker running on a Custom Domain will succeed without a service binding.</p>
<p>For example, consider the following scenario, where both Workers are running on the <code>example.com</code> Cloudflare zone:</p>
<ul>
<li><code>worker-a</code> running on the <a href="/workers/configuration/routing/routes/#set-up-a-route">route</a> <code>auth.example.com/*</code>.</li>
<li><code>worker-b</code> running on the <a href="/workers/configuration/routing/routes/#set-up-a-route">route</a> <code>shop.example.com/*</code>.</li>
</ul>
<p>If <code>worker-a</code> sends a fetch request to <code>worker-b</code>, the request will fail, because of the limitation on same-zone fetch requests. <code>worker-a</code> must have a service binding to <code>worker-b</code> for this request to resolve.</p>
<pre tabindex="0"><code class="language-js">export default {&#10;	fetch(request) {&#10;		// This will fail&#10;		return fetch(&quot;https://shop.example.com&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>However, if <code>worker-b</code> was instead set up to run on the Custom Domain <code>shop.example.com</code>, the fetch request would succeed.</p>
<h2 id="request-matching-behaviour">Request matching behaviour</h2>
<p>Custom Domains do not support <a href="/dns/manage-dns-records/reference/wildcard-dns-records/">wildcard DNS records</a>. An incoming request must exactly match the domain or subdomain your Custom Domain is registered to. Other parts (path, query parameters) of the URL are not considered when executing this matching logic. For example, if you create a Custom Domain on <code>api.example.com</code> attached to your <code>api-gateway</code> Worker, a request to either <code>api.example.com/login</code> or <code>api.example.com/user</code> would invoke the same <code>api-gateway</code> Worker.</p>
<p><img src="/assets/upstream/images/workers/platform/triggers/custom-domains-api-gateway.png" alt="Custom Domains follow standard DNS ordering and matching logic" /></p>
<h2 id="interaction-with-routes">Interaction with Routes</h2>
<p>A Worker running on a Custom Domain is treated as an origin. Any Workers running on routes before your Custom Domain can optionally call the Worker registered on your Custom Domain by issuing <code>fetch(request)</code> with the incoming <code>Request</code> object. That means that you are able to set up Workers to run before a request gets to your Custom Domain Worker. In other words, you can chain together two Workers in the same request.</p>
<p>For example, consider the following workflow:</p>
<ol>
<li>A Custom Domain for <code>api.example.com</code> points to your <code>api-worker</code> Worker.</li>
<li>A route added to <code>api.example.com/auth</code> points to your <code>auth-worker</code> Worker.</li>
<li>A request to <code>api.example.com/auth</code> will trigger your <code>auth-worker</code> Worker.</li>
<li>Using <code>fetch(request)</code> within the <code>auth-worker</code> Worker will invoke the <code>api-worker</code> Worker, as if it was a normal application server.</li>
</ol>
<pre tabindex="0"><code class="language-js">export default {&#10;	fetch(request) {&#10;		const url = new URL(request.url);&#10;		if (url.searchParams.get(&quot;auth&quot;) !== &quot;SECRET_TOKEN&quot;) {&#10;			return new Response(null, { status: 401 });&#10;		} else {&#10;			// This will invoke `api-worker`&#10;			return fetch(request);&#10;		}&#10;	},&#10;};&#10;</code></pre>
<h2 id="certificates">Certificates</h2>
<p>Creating a Custom Domain will also generate an <a href="/ssl/edge-certificates/advanced-certificate-manager/">Advanced Certificate</a> on your target zone for your target hostname.</p>
<p>These certificates are generated with default settings. To override these settings, delete the generated certificate and create your own certificate in the Cloudflare dashboard. Refer to <a href="/ssl/edge-certificates/advanced-certificate-manager/manage-certificates/">Manage advanced certificates</a> for instructions.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16835.md")
</aside>
<h2 id="redirect-between-www-and-root-domain">Redirect between www and root domain</h2>
<p>Because Custom Domains require an exact hostname match, a Worker attached to <code>example.com</code> will not receive requests sent to <code>www.example.com</code>, and vice versa. To make both versions of your domain work, set up a redirect rule:</p>
<ul>
<li><a href="/rules/url-forwarding/examples/redirect-www-to-root/">Redirect from www to root</a></li>
<li><a href="/rules/url-forwarding/examples/redirect-root-to-www/">Redirect from root to www</a></li>
</ul>
<p>You also need a <a href="/dns/manage-dns-records/how-to/create-dns-records/">proxied DNS record</a> for the hostname you are redirecting <em>from</em>, so that Cloudflare can apply the redirect rule.</p>
<ul>
<li>For www to root: Add a proxied DNS <code>A</code> record for <code>www</code> pointing to <code>192.0.2.0</code>, or a proxied <code>AAAA</code> record pointing to <code>100::</code></li>
<li>For root to www: Add a proxied DNS <code>A</code> record for your root domain pointing to <code>192.0.2.0</code>, or a proxied <code>AAAA</code> record pointing to <code>100::</code></li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16834.md")
</aside>
<h2 id="migrate-from-routes">Migrate from Routes</h2>
<p>If you are currently invoking a Worker using a <a href="/workers/configuration/routing/routes/">route</a> with <code>/*</code>, and you have a CNAME record pointing to <code>100::</code> or similar, a Custom Domain is a recommended replacement.</p>
<h3 id="migrate-from-routes-via-the-dashboard">Migrate from Routes via the dashboard</h3>
<p>To migrate the route <code>example.com/*</code>:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16840.md")
</div>
<h3 id="migrate-from-routes-via-wrangler">Migrate from Routes via Wrangler</h3>
<p>To migrate the route <code>example.com/*</code> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/16842.md")
</div>
