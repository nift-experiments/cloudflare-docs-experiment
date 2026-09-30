---
cp9:
  canonical: https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/
  description: Connect Cloudflare Workers to Upstash for serverless Redis and Kafka integrations.
  full_title: Upstash · Cloudflare Workers docs
  head_html: <title>Upstash · Cloudflare Workers docs</title><meta name="generator" content="Nift"><meta name="description" content="Connect Cloudflare Workers to Upstash for serverless Redis and Kafka integrations."><link rel="canonical" href="https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/index.md"><meta property="og:title" content="Upstash · Cloudflare Workers docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Connect Cloudflare Workers to Upstash for serverless Redis and Kafka integrations."><meta property="og:url" content="https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers"><meta name="algolia_product_filter" content="Workers"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Configuration"><meta name="algolia_content_type" content="Configuration"><meta name="pcx_additional_products" content="Workers"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/#page","headline":"Upstash \u00b7 Cloudflare Workers docs","description":"Connect Cloudflare Workers to Upstash for serverless Redis and Kafka integrations.","url":"https://developers.cloudflare.com/workers/databases/third-party-integrations/upstash/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /workers/databases/third-party-integrations/upstash/
  schema: 1
---
<p><a href="https://upstash.com/">Upstash</a> is a serverless database with Redis* and Kafka API. Upstash also offers QStash, a task queue/scheduler designed for the serverless.</p>
<h2 id="upstash-for-redis">Upstash for Redis</h2>
<p>To set up an integration with Upstash:</p>
<ol>
<li>
<p>You need an existing Upstash database to connect to. <a href="https://docs.upstash.com/redis#create-a-database">Create an Upstash database</a> or <a href="https://docs.upstash.com/redis/howto/connectclient">load data from an existing database to Upstash</a>.</p>
</li>
<li>
<p>Insert some data to your Upstash database. You can add data to your Upstash database in two ways:</p>
<ul>
<li>Use the CLI directly from your Upstash console.</li>
<li>Alternatively, install <a href="https://redis.io/docs/getting-started/installation/">redis-cli</a> locally and run the following commands.</li>
</ul>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">set GB &quot;Ey up?&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">OK&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">set US &quot;Yo, what’s up?&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">OK&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">set NL &quot;Hoi, hoe gaat het?&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-sh">OK&#10;</code></pre>
<ol start="3">
<li>
<p>Configure the Upstash Redis credentials in your Worker:</p>
<p>You need to add your Upstash Redis database URL and token as secrets to your Worker. Get these from your <a href="https://console.upstash.com">Upstash Console</a> under your database details, then add them as secrets using Wrangler:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">&#35; Add the Upstash Redis URL as a secret&#10;npx wrangler secret put UPSTASH_REDIS_REST_URL&#10;&#35; When prompted, paste your Upstash Redis REST URL&#10;&#10;&#35; Add the Upstash Redis token as a secret&#10;npx wrangler secret put UPSTASH_REDIS_REST_TOKEN&#10;&#35; When prompted, paste your Upstash Redis REST token&#10;</code></pre>
<ol start="4">
<li>In your Worker, install the <code>@upstash/redis</code>, a HTTP client to connect to your database and start manipulating data:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @upstash/redis" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @upstash/redis" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @upstash/redis" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @upstash/redis</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @upstash/redis" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="5">
<li>The following example shows how to make a query to your Upstash database in a Worker. The credentials needed to connect to Upstash have been added as secrets to your Worker.</li>
</ol>
<pre tabindex="0"><code class="language-js">import { Redis } from &quot;@upstash/redis/cloudflare&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		const redis = Redis.fromEnv(env);&#10;&#10;		const country = request.headers.get(&quot;cf-ipcountry&quot;);&#10;		if (country) {&#10;			const greeting = await redis.get(country);&#10;			if (greeting) {&#10;				return new Response(greeting);&#10;			}&#10;		}&#10;&#10;		return new Response(&quot;Hello What&#x27;s up!&quot;);&#10;	},&#10;};&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/16853.md")
</aside>
<p>To learn more about Upstash, refer to the <a href="https://docs.upstash.com/redis">Upstash documentation</a>.</p>
<h2 id="upstash-qstash">Upstash QStash</h2>
<p>To set up an integration with Upstash QStash:</p>
<ol>
<li>
<p>Configure the <a href="https://docs.upstash.com/qstash#1-public-api">publicly available HTTP endpoint</a> that you want to send your messages to.</p>
</li>
<li>
<p>Configure the Upstash QStash credentials in your Worker:</p>
<p>You need to add your Upstash QStash token as a secret to your Worker. Get your token from your <a href="https://console.upstash.com">Upstash Console</a> under QStash settings, then add it as a secret using Wrangler:</p>
</li>
</ol>
<pre tabindex="0"><code class="language-sh">&#35; Add the QStash token as a secret&#10;npx wrangler secret put QSTASH_TOKEN&#10;&#35; When prompted, paste your QStash token&#10;</code></pre>
<ol start="3">
<li>In your Worker, install the <code>@upstash/qstash</code>, a HTTP client to connect to your database QStash endpoint:</li>
</ol>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add @upstash/qstash</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @upstash/qstash" aria-label="Copy to clipboard">Copy</button></div></div>
<ol start="4">
<li>Refer to the <a href="https://docs.upstash.com/qstash/quickstarts/cloudflare-workers#3-use-qstash-in-your-handler">Upstash documentation on how to receive webhooks from QStash in your Cloudflare Worker</a>.</li>
</ol>
<p>* Redis is a trademark of Redis Ltd. Any rights therein are reserved to Redis Ltd. Any use by Upstash is for referential purposes only and does not indicate any sponsorship, endorsement or affiliation between Redis and Upstash.</p>
