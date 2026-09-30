---
cp9:
  canonical: https://developers.cloudflare.com/workers/configuration/routing/workers-dev/
  description: Deploy Cloudflare Workers on a workers.dev subdomain for quick testing and personal projects.
  full_title: workers.dev · Cloudflare Workers docs
  head_html: <title>workers.dev · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Deploy Cloudflare Workers on a workers.dev subdomain for quick testing and personal projects."><link rel="canonical" href="https://developers.cloudflare.com/workers/configuration/routing/workers-dev/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/configuration/routing/workers-dev/index.md"><meta property="og:title" content="workers.dev · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Deploy Cloudflare Workers on a workers.dev subdomain for quick testing and personal projects."><meta property="og:url" content="https://developers.cloudflare.com/workers/configuration/routing/workers-dev/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/configuration/routing/workers-dev/#page","headline":"workers.dev \u00b7 Cloudflare Workers docs","description":"Deploy Cloudflare Workers on a workers.dev subdomain for quick testing and personal projects.","url":"https://developers.cloudflare.com/workers/configuration/routing/workers-dev/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/configuration/routing/workers-dev/
  schema: 1
---
<p>Cloudflare Workers accounts come with a <code>workers.dev</code> subdomain that is configurable in the Cloudflare dashboard. Your <code>workers.dev</code> subdomain allows you getting started quickly by deploying Workers without first onboarding your custom domain to Cloudflare.</p>
<p>It's recommended to run production Workers on a <a href="/workers/configuration/routing/">Workers route or custom domain</a>, rather than on your <code>workers.dev</code> subdomain. Your <code>workers.dev</code> subdomain is treated as a <a href="https://www.cloudflare.com/plans/">Free website</a> and is intended for personal or hobby projects that aren't business-critical.</p>
<h2 id="configure-workers-dev">Configure <code>workers.dev</code></h2>
<p><code>workers.dev</code> subdomains take the format: <code>&lt;YOUR_ACCOUNT_SUBDOMAIN&gt;.workers.dev</code>. To change your <code>workers.dev</code> subdomain:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Select <strong>Change</strong> next to <strong>Your subdomain</strong>.</li>
</ol>
<p>All Workers are assigned a <code>workers.dev</code> route when they are created or renamed following the syntax <code>&lt;YOUR_WORKER_NAME&gt;.&lt;YOUR_SUBDOMAIN&gt;.workers.dev</code>. The <a href="/workers/wrangler/configuration/#inheritable-keys"><code>name</code></a> field in your Worker configuration is used as the subdomain for the deployed Worker.</p>
<h2 id="manage-access-to-workers-dev">Manage access to <code>workers.dev</code></h2>
<p>When enabled, your <code>workers.dev</code> URL is available publicly. To require visitors to sign in before they can access a <code>workers.dev</code> URL, use <a href="/workers/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
<p>Access can protect one Worker's production <code>workers.dev</code> URL, preview URLs, or both. You can also protect all Workers or all Worker previews in an account.</p>
<p>To use details about the signed-in user in your Worker, use <a href="/workers/configuration/cloudflare-access/#read-authenticated-user-identity-with-ctxaccess"><code>ctx.access</code></a>. You can also read the <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#user-identity">user's identity</a> from the validated JWT or the <code>/cdn-cgi/access/get-identity</code> endpoint.</p>
<h2 id="disabling-workers-dev">Disabling <code>workers.dev</code></h2>
<h3 id="disabling-workers-dev-in-the-dashboard">Disabling <code>workers.dev</code> in the dashboard</h3>
<p>To disable the <code>workers.dev</code> route for a Worker:</p>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Workers &amp; Pages</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>In <strong>Overview</strong>, select your Worker.</li>
<li>Go to <strong>Settings</strong> &gt; <strong>Domains &amp; Routes</strong>.</li>
<li>On <code>workers.dev</code> click &quot;Disable&quot;.</li>
<li>Confirm you want to disable.</li>
</ol>
<h3 id="disabling-workers-dev-in-the-wrangler-configuration-file">Disabling <code>workers.dev</code> in the Wrangler configuration file</h3>
<p>To disable the <code>workers.dev</code> route for a Worker, include the following in your Worker's <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16824.md")
</div>
<p>When you redeploy your Worker with this change, the <code>workers.dev</code> route will be disabled. Preview URLs default to matching your <code>workers_dev</code> setting unless explicitly configured. If you explicitly enabled Preview URLs, <a href="/workers/versions-and-deployments/preview-urls/#toggle-preview-urls-enable-or-disable">disable them separately</a>.</p>
<p>If you do not specify <code>workers_dev = false</code> but add a <a href="/workers/wrangler/configuration/#routes"><code>routes</code> component</a> to your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>, the value of <code>workers_dev</code> will be inferred as <code>false</code> on the next deploy.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/16823.md")
</aside>
<h2 id="limitations">Limitations</h2>
<p>When deploying a Worker with a <code>workers.dev</code> subdomain enabled, your Worker name must meet the following requirements:</p>
<ul>
<li>Must be 63 characters or less</li>
<li>Must contain only alphanumeric characters (<code>a-z</code>, <code>A-Z</code>, <code>0-9</code>) and dashes (<code>-</code>)</li>
<li>Cannot start or end with a dash (<code>-</code>)</li>
</ul>
<p>These restrictions apply because the Worker name is used as a DNS label in your <code>workers.dev</code> URL. DNS labels have a maximum length of 63 characters and cannot begin or end with a dash.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16822.md")
</aside>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="https://blog.cloudflare.com/announcing-workers-dev">Announcing <code>workers.dev</code></a></li>
<li><a href="/workers/wrangler/configuration/#types-of-routes">Wrangler routes configuration</a></li>
</ul>
