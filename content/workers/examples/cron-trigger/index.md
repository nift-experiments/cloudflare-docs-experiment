---
cp9:
  canonical: https://developers.cloudflare.com/workers/examples/cron-trigger/
  description: Set a Cron Trigger for your Worker.
  full_title: Setting Cron Triggers · Cloudflare Workers docs
  head_html: <title>Setting Cron Triggers · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Set a Cron Trigger for your Worker."><link rel="canonical" href="https://developers.cloudflare.com/workers/examples/cron-trigger/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/examples/cron-trigger/index.md"><meta property="og:title" content="Setting Cron Triggers · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Set a Cron Trigger for your Worker."><meta property="og:url" content="https://developers.cloudflare.com/workers/examples/cron-trigger/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Example"><meta name="algolia_content_type" content="Example"><meta name="pcx_additional_products" content="Workers"><meta name="pcx_tags" content="Middleware,JavaScript,TypeScript"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/examples/cron-trigger/#page","headline":"Setting Cron Triggers \u00b7 Cloudflare Workers docs","description":"Set a Cron Trigger for your Worker.","url":"https://developers.cloudflare.com/workers/examples/cron-trigger/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["Middleware","JavaScript","TypeScript"]}</script>
  markdown: true
  noindex: false
  route: /workers/examples/cron-trigger/
  schema: 1
---
<p class="article-summary">Set a Cron Trigger for your Worker.</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="workersExamples"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/16482.md")
</div></div>
<h2 id="set-cron-triggers-in-wrangler">Set Cron Triggers in Wrangler</h2>
<p>Refer to <a href="/workers/configuration/cron-triggers/">Cron Triggers</a> for more information on how to add a Cron Trigger.</p>
<p>If you are deploying with Wrangler, set the cron syntax (once per hour as shown below) by adding this to your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16483.md")
</div>
<p>You also can set a different Cron Trigger for each <a href="/workers/wrangler/environments/">environment</a> in your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>. You need to put the <code>[triggers]</code> table under your chosen environment. For example:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/16484.md")
</div>
<h2 id="test-cron-triggers-using-wrangler">Test Cron Triggers using Wrangler</h2>
<p>The recommended way of testing Cron Triggers is using Wrangler.</p>
<p>Cron Triggers can be tested using Wrangler by passing in the <code>--test-scheduled</code> flag to <a href="/workers/wrangler/commands/general/#dev"><code>wrangler dev</code></a>. This will expose a <code>/cdn-cgi/local/scheduled</code> route which can be used to test using a HTTP request. To simulate different cron patterns, a <code>cron</code> query parameter can be passed in.</p>
<pre tabindex="0"><code class="language-sh">npx wrangler dev --test-scheduled&#10;&#10;curl &quot;http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*&quot; # Python Workers&#10;</code></pre>
