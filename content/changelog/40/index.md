---
cp9:
  canonical: https://developers.cloudflare.com/changelog/40/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 40 | Cloudflare Docs
  head_html: <title>Changelog - page 40 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/40/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 40"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/40/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/40/#page","headline":"Changelog - page 40 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/40/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/40/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-07-03">Jul 3, 2025</time><div>
<h2 id="post-2025-07-02-hyperdrive-configurable-connection-count"><a href="/changelog/post/2025-07-02-hyperdrive-configurable-connection-count/">Hyperdrive now supports configuring the amount of database connections</a></h2>
<div class="changelog-badges"><span>hyperdrive</span></div><div class="changelog-body"><p>You can now specify the number of connections your Hyperdrive configuration uses to connect to your origin database.</p>
<p>All configurations have a minimum of 5 connections. The maximum connection count for a Hyperdrive configuration depends on the <a href="/hyperdrive/platform/limits/">Hyperdrive limits of your Workers plan</a>.</p>
<p>This feature allows you to right-size your connection pool based on your database capacity and application requirements. You can configure connection counts through the Cloudflare dashboard or API.</p>
<p>Refer to the <a href="/hyperdrive/concepts/connection-pooling/">Hyperdrive configuration documentation</a> for more information.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-01">Jul 1, 2025</time><div>
<h2 id="post-2025-07-01-browser-based-rdp-open-beta"><a href="/changelog/post/2025-07-01-browser-based-rdp-open-beta/">Access RDP securely from your browser — now in open beta</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Browser-based RDP</a> with <a href="/cloudflare-one/access-controls/policies/">Cloudflare Access</a> is now available in open beta for all Cloudflare customers. It enables secure, remote Windows server access without VPNs or RDP clients.</p>
<p>With browser-based RDP, you can:</p>
<ul>
<li><strong>Control how users authenticate to internal RDP resources</strong> with single sign-on (SSO), multi-factor authentication (MFA), and granular access policies.</li>
<li><strong>Record who is accessing which servers and when</strong> to support regulatory compliance requirements and to gain greater visibility in the event of a security event.</li>
<li><strong>Eliminate the need to install and manage software on user devices</strong>. You will only need a web browser.</li>
<li><strong>Reduce your attack surface</strong> by keeping your RDP servers off the public Internet and protecting them from common threats like credential stuffing or brute-force attacks.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/access/browser-based-rdp-access-app.png" alt="Example of a browsed-based RDP Access application" /></p>
<p>To get started, see <a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/rdp/rdp-browser/">Connect to RDP in a browser</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-01">Jul 1, 2025</time><div>
<h2 id="post-2025-07-01-pay-per-crawl"><a href="/changelog/post/2025-07-01-pay-per-crawl/">Introducing Pay Per Crawl (private beta)</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>We are introducing a new feature of <a href="/ai-crawl-control/">AI Crawl Control</a> — Pay Per Crawl. <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl</a> enables site owners to require payment from AI crawlers every time the crawlers access their content, thereby fostering a fairer Internet by enabling site owners to control and monetize how their content gets used by AI.</p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/pay-per-crawl.png" alt="Pay per crawl" /></p>
<p><strong>For Site Owners:</strong></p>
<ul>
<li>Set pricing and select which crawlers to charge for content access</li>
<li>Manage payments via Stripe</li>
<li>Monitor analytics on successful content deliveries</li>
</ul>
<p><strong>For AI Crawler Owners:</strong></p>
<ul>
<li>Use HTTP headers to request and accept pricing</li>
<li>Receive clear confirmations on charges for accessed content</li>
</ul>
<p>Learn more in the <a href="/ai-crawl-control/features/pay-per-crawl/what-is-pay-per-crawl/">Pay Per Crawl documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-01">Jul 1, 2025</time><div>
<h2 id="post-2025-07-01-refresh"><a href="/changelog/post/2025-07-01-refresh/">AI Crawl Control refresh</a></h2>
<div class="changelog-badges"><span>ai-crawl-control</span></div><div class="changelog-body"><p>We redesigned the AI Crawl Control dashboard to provide more intuitive and granular control over AI crawlers.</p>
<ul>
<li>From the new <strong>AI Crawlers</strong> tab: block specific AI crawlers.</li>
<li>From the new <strong>Metrics</strong> tab: view AI Crawl Control metrics.</li>
</ul>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/manage-ai-crawlers.png" alt="Block AI crawlers" /></p>
<p><img src="/assets/upstream/images/changelog/ai-crawl-control/analyze-metrics.png" alt="Analyze AI crawler activity" /></p>
<p>To get started, explore:</p>
<ul>
<li><a href="/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers</a>.</li>
<li><a href="/ai-crawl-control/features/analyze-ai-traffic/">Analyze AI traffic</a>.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-01">Jul 1, 2025</time><div>
<h2 id="post-2025-07-01-radar-bots-insights"><a href="/changelog/post/2025-07-01-radar-bots-insights/">Bot &amp; Crawler Insights in Cloudflare Radar</a></h2>
<div class="changelog-badges"><span>radar</span></div><div class="changelog-body"><h4 id="2025-07-01-radar-bots-insights-web-crawlers-insights">Web crawlers insights</h4>
<p><a href="/radar/"><strong>Radar</strong></a> now offers expanded insights into web crawlers, giving you greater visibility into aggregated trends in crawl and refer activity.</p>
<p>We have introduced the following endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/summary/"><code>/bots/crawlers/summary/{dimension}</code></a>: Returns an overview of crawler HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/subresources/web_crawlers/methods/timeseries_groups/"><code>/bots/crawlers/timeseries_groups/{dimension}</code></a>: Provides time-series data on crawler request distributions across the same dimensions.</li>
</ul>
<p>These endpoints allow analysis across the following dimensions:</p>
<ul>
<li><code>user_agent</code>: Parsed data from the <code>User-Agent</code> header.</li>
<li><code>referer</code>: Parsed data from the <code>Referer</code> header.</li>
<li><code>crawl_refer_ratio</code>: Ratio of HTML page crawl requests to HTML page referrals by platform.</li>
</ul>
<h4 id="2025-07-01-radar-bots-insights-broader-bot-insights">Broader bot insights</h4>
<p>In addition to crawler-specific insights, Radar now provides a broader set of bot endpoints:</p>
<ul>
<li><a href="/api/resources/radar/subresources/bots/"><code>/bots/</code></a>: Lists all bots.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/get/"><code>/bots/{bot_slug}</code></a>: Returns detailed metadata for a specific bot.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries/"><code>/bots/timeseries</code></a>: Time-series data for bot activity.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/summary/"><code>/bots/summary/{dimension}</code></a>: Returns an overview of bot HTTP request distributions across key dimensions.</li>
<li><a href="/api/resources/radar/subresources/bots/methods/timeseries_groups/"><code>/bots/timeseries_groups/{dimension}</code></a>: Provides time-series data on bot request distributions across the same dimensions.</li>
</ul>
<p>These endpoints support filtering and breakdowns by:</p>
<ul>
<li><code>bot</code>: Bot name.</li>
<li><code>bot_operator</code>: The organization or entity operating the bot.</li>
<li><code>bot_category</code>: Classification of bot type.</li>
</ul>
<p>The previously available <code>verified_bots</code> endpoints have now been deprecated in favor of this set of bot insights APIs.
While current data still focuses on verified bots, we plan to expand support for unverified bot traffic in the future.</p>
<p>Learn more about the new Radar bot and crawler insights in our <a href="https://blog.cloudflare.com/ai-search-crawl-refer-ratio-on-radar">blog post</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-07-01">Jul 1, 2025</time><div>
<h2 id="post-2025-07-01-vite-plugin-enhanced-assets-support"><a href="/changelog/post/2025-07-01-vite-plugin-enhanced-assets-support/">Enhanced support for static assets with the Cloudflare Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now use any of Vite's <a href="https://vite.dev/guide/assets">static asset handling</a> features in your Worker as well as in your frontend.
These include importing assets as URLs, importing as strings and importing from the <code>public</code> directory as well as inlining assets.</p>
<p>Additionally, assets imported as URLs in your Worker are now automatically moved to the client build output.</p>
<p>Here is an example that fetches an imported asset using the <a href="/workers/static-assets/binding/#binding">assets binding</a> and modifies the response.</p>
<pre tabindex="0"><code class="language-ts">// Import the asset URL&#10;// This returns the resolved path in development and production&#10;import myImage from &quot;./my-image.png&quot;;&#10;&#10;export default {&#10;	async fetch(request, env) {&#10;		// Fetch the asset using the binding&#10;		const response = await env.ASSETS.fetch(new URL(myImage, request.url));&#10;		// Create a new `Response` object that can be modified&#10;		const modifiedResponse = new Response(response.body, response);&#10;		// Add an additional header&#10;		modifiedResponse.headers.append(&quot;my-header&quot;, &quot;imported-asset&quot;);&#10;&#10;		// Return the modified response&#10;		return modifiedResponse;&#10;	},&#10;};&#10;</code></pre>
<p>Refer to <a href="/workers/vite-plugin/reference/static-assets/">Static Assets</a> in the Cloudflare Vite plugin docs for more info.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-30">Jun 30, 2025</time><div>
<h2 id="post-2025-06-30-warp-ga-android"><a href="/changelog/post/2025-06-30-warp-ga-android/">Cloudflare One Agent for Android (version 2.4.2)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Android Cloudflare One Agent is now available in the <a href="https://play.google.com/store/apps/details?id=com.cloudflare.cloudflareoneagent">Google Play Store</a>. This release
contains improvements and new exciting features, including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">post-quantum cryptography</a>.
By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate <a href="https://blog.cloudflare.com/pq-2024/">protection of post-quantum cryptography</a> without needing to upgrade any of your individual corporate applications or systems.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>QLogs are now disabled by default and can be enabled in the app by turning on <strong>Enable qlogs</strong> under <strong>Settings</strong> &gt; <strong>Advanced</strong> &gt; <strong>Diagnostics</strong> &gt; <strong>Debug Logs</strong>. The QLog setting from previous releases will no longer be respected.</li>
<li>DNS over HTTPS traffic is now included in the WARP tunnel by default.</li>
<li>The WARP client now applies <a href="https://blog.cloudflare.com/pq-2024/">post-quantum cryptography</a> end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">MDM</a>.</li>
<li>Fixed an issue that caused WARP connection failures on ChromeOS devices.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-30">Jun 30, 2025</time><div>
<h2 id="post-2025-06-30-warp-ga-ios"><a href="/changelog/post/2025-06-30-warp-ga-ios/">Cloudflare One Agent for iOS (version 1.11)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the iOS Cloudflare One Agent is now available in the <a href="https://apps.apple.com/us/app/cloudflare-one-agent/id6443476492">iOS App Store</a>. This release
contains improvements and new exciting features, including <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">post-quantum cryptography</a>.
By tunneling your corporate network traffic over Cloudflare, you can now gain the immediate <a href="https://blog.cloudflare.com/pq-2024/">protection of post-quantum cryptography</a> without needing to upgrade any of your individual corporate applications or systems.</p>
<p><strong>Changes and improvements</strong></p>
<ul>
<li>QLogs are now disabled by default and can be enabled in the app by turning on <strong>Enable qlogs</strong> under <strong>Settings</strong> &gt; <strong>Advanced</strong> &gt; <strong>Diagnostics</strong> &gt; <strong>Debug Logs</strong>. The QLog setting from previous releases will no longer be respected.</li>
<li>DNS over HTTPS traffic is now included in the WARP tunnel by default.</li>
<li>The WARP client now applies <a href="https://blog.cloudflare.com/pq-2024/">post-quantum cryptography</a> end-to-end on enabled devices accessing resources behind a Cloudflare Tunnel. This feature can be enabled by <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/parameters/#enable_post_quantum">MDM</a>.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-30">Jun 30, 2025</time><div>
<h2 id="post-2025-06-30-mail-authentication"><a href="/changelog/post/2025-06-30-mail-authentication/">Mail authentication requirements for Email Routing</a></h2>
<div class="changelog-badges"><span>email-service</span></div><div class="changelog-body"><p>The Email Routing platform supports <a href="https://datatracker.ietf.org/doc/html/rfc7208">SPF</a> records and <a href="https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail">DKIM (DomainKeys Identified Mail)</a> signatures and
honors these protocols when the sending domain has them configured. However, if the sending domain doesn't implement them,
we still forward the emails to upstream mailbox providers.</p>
<p>Starting on July 3, 2025, we will require all emails to be authenticated using at least one of the protocols, SPF or DKIM, to
forward them. We also strongly recommend that all senders implement the DMARC protocol.</p>
<p>If you are using a Worker with an Email trigger to receive email messages and forward them upstream, you will need to handle the case where
the forward action may fail due to missing authentication on the incoming email.</p>
<p>SPAM has been a long-standing issue with email. By enforcing mail authentication, we will increase the efficiency of identifying abusive senders and blocking
bad emails.
If you're an email server delivering emails to large mailbox providers, it's likely you already use these protocols; otherwise, please ensure
you have them properly configured.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-30">Jun 30, 2025</time><div>
<h2 id="post-2025-06-30-graceful-byoip-withdrawal"><a href="/changelog/post/2025-06-30-graceful-byoip-withdrawal/">Graceful withdrawal of BYOIP prefixes</a></h2>
<div class="changelog-badges"><span>magic-transit</span></div><div class="changelog-body"><p>Magic Transit customers can now configure AS prepending on their BYOIP prefixes advertised at the Cloudflare edge. This allows for smoother traffic migration and minimizes packet loss when changing providers.</p>
<p>AS prepending makes the Cloudflare route less preferred by increasing the AS path length. You can use this to gradually shift traffic away from Cloudflare before withdrawing a prefix, avoiding abrupt routing changes.</p>
<p>Prepending can be configured via the API or through BGP community values when peering with the Magic Transit routing table. For more information, refer to <a href="/magic-transit/how-to/advertise-prefixes/">Advertise prefixes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-30">Jun 30, 2025</time><div>
<h2 id="post-2025-06-25-getPlatformProxy-support-remote-bindings"><a href="/changelog/post/2025-06-25-getPlatformProxy-support-remote-bindings/">Remote bindings (beta) now works with Next.js — connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">recently announced</a> our public beta for <a href="/workers/local-development/#remote-bindings">remote bindings</a>, which allow you to connect to deployed resources running on your Cloudflare account (like <a href="/r2">R2 buckets</a> or <a href="/d1">D1 databases</a>) while running a local development session.</p>
<p>Now, you can use remote bindings with your Next.js applications through the <a href="https://opennext.js.org/cloudflare/bindings#remote-bindings"><code>@opennextjs/cloudflare</code> adaptor</a> by enabling the experimental feature in your <code>next.config.ts</code>:</p>
<pre tabindex="0"><code class="language-diff">&#45; initOpenNextCloudflareForDev();&#10;&#43; initOpenNextCloudflareForDev({&#10;&#43;  experimental: { remoteBindings: true }&#10;&#43; });&#10;</code></pre>
<p>Then, all you have to do is specify which bindings you want connected to the deployed resource on your Cloudflare account via the <code>experimental_remote</code> flag in your binding definition:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17780.md")</div>
<p>You can then run <code>next dev</code> to start a local development session (or start a preview with <code>opennextjs-cloudflare preview</code>), and all requests to <code>env.MY_BUCKET</code> will be proxied to the remote <code>testing-bucket</code> — rather than the <a href="/workers/local-development/#bindings-during-local-development">default local binding simulations</a>.</p>
<h4 id="2025-06-25-getPlatformProxy-support-remote-bindings-remote-bindings-isr">Remote bindings &amp; ISR</h4>
<p>Remote bindings are also used during the build process, which comes with significant benefits for pages using <a href="https://opennext.js.org/aws/inner_workings/components/server/node#isrssg">Incremental Static Regeneration (ISR)</a>. During the build step for an ISR page, your server executes the page's code just as it would for normal user requests. If a page needs data to display (like fetching user info from <a href="/kv">KV</a>), those requests are actually made. The server then uses this fetched data to render the final HTML.</p>
<p>Data fetching is a critical part of this process, as the finished HTML is only as good as the data it was built with. If the build process can't fetch real data, you end up with a pre-rendered page that's empty or incomplete.</p>
<p><strong>With remote bindings support in OpenNext,</strong> your pre-rendered pages are built with real data from the start. The build process uses any configured remote bindings, and any data fetching occurs against the deployed resources on your Cloudflare account.</p>
<p><strong>Want to learn more?</strong> Get started with <a href="https://opennext.js.org/cloudflare/bindings#remote-bindings">remote bindings and OpenNext</a>.</p>
<p><strong>Have feedback?</strong> Join the discussion in our <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">beta announcement</a> to share feedback or report any issues.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-26">Jun 26, 2025</time><div>
<h2 id="post-2025-06-26-vite-plugin-cross-commands-binding"><a href="/changelog/post/2025-06-26-vite-plugin-cross-commands-binding/">Run and connect Workers in separate dev commands with the Cloudflare Vite plugin</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers can now talk to each other across separate dev commands using service bindings and tail consumers, whether started with <code>vite dev</code> or <code>wrangler dev</code>.</p>
<p>Simply start each Worker in its own terminal:</p>
<pre tabindex="0"><code class="language-sh">&#35; Terminal 1&#10;vite dev&#10;&#10;&#35; Terminal 2&#10;wrangler dev&#10;</code></pre>
<p>This is useful when different teams maintain different Workers, or when each Worker has its own build setup or tooling.</p>
<p>Check out the <a href="/workers/local-development/multi-workers">Developing with multiple Workers</a> guide to learn more about the different approaches and when to use each one.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-25">Jun 25, 2025</time><div>
<h2 id="post-2025-06-24-announcing-sandboxes"><a href="/changelog/post/2025-06-24-announcing-sandboxes/">Run AI-generated code on-demand with Code Sandboxes (new)</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span><span>workflows</span></div><div class="changelog-body"><p>AI is supercharging app development for everyone, but we need a safe way to run untrusted, LLM-written code. We’re introducing <a href="https://www.npmjs.com/package/@cloudflare/sandbox">Sandboxes</a>, which let your Worker run actual processes in a secure, container-based environment.</p>
<pre tabindex="0"><code class="language-ts">import { getSandbox } from &quot;@cloudflare/sandbox&quot;;&#10;export { Sandbox } from &quot;@cloudflare/sandbox&quot;;&#10;&#10;export default {&#10;	async fetch(request: Request, env: Env) {&#10;		const sandbox = getSandbox(env.Sandbox, &quot;my-sandbox&quot;);&#10;		return sandbox.exec(&quot;ls&quot;, [&quot;-la&quot;]);&#10;	},&#10;};&#10;</code></pre>
<h4 id="2025-06-24-announcing-sandboxes-methods">Methods</h4>
<ul>
<li><code>exec(command: string, args: string[], options?: { stream?: boolean })</code>:Execute a command in the sandbox.</li>
<li><code>gitCheckout(repoUrl: string, options: { branch?: string; targetDir?: string; stream?: boolean })</code>: Checkout a git repository in the sandbox.</li>
<li><code>mkdir(path: string, options: { recursive?: boolean; stream?: boolean })</code>: Create a directory in the sandbox.</li>
<li><code>writeFile(path: string, content: string, options: { encoding?: string; stream?: boolean })</code>: Write content to a file in the sandbox.</li>
<li><code>readFile(path: string, options: { encoding?: string; stream?: boolean })</code>: Read content from a file in the sandbox.</li>
<li><code>deleteFile(path: string, options?: { stream?: boolean })</code>: Delete a file from the sandbox.</li>
<li><code>renameFile(oldPath: string, newPath: string, options?: { stream?: boolean })</code>: Rename a file in the sandbox.</li>
<li><code>moveFile(sourcePath: string, destinationPath: string, options?: { stream?: boolean })</code>: Move a file from one location to another in the sandbox.</li>
<li><code>ping()</code>: Ping the sandbox.</li>
</ul>
<p>Sandboxes are still experimental. We're using them to explore how isolated, container-like workloads might scale on Cloudflare — and to help define the developer experience around them.</p>
<p>You can try it today from your Worker, with just a few lines of code. Let us know what you build.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-25">Jun 25, 2025</time><div>
<h2 id="post-2025-06-25-actors-package-alpha"><a href="/changelog/post/2025-06-25-actors-package-alpha/">@cloudflare/actors library - SDK for Durable Objects in beta</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>The new <a href="https://www.npmjs.com/package/@cloudflare/actors">@cloudflare/actors</a> library is now in beta!</p>
<p>The <code>@cloudflare/actors</code> library is a new SDK for Durable Objects and provides a powerful set of abstractions for building real-time, interactive, and multiplayer applications on top of Durable Objects. With beta usage and feedback, <code>@cloudflare/actors</code> will become the recommended way to build on Durable Objects and draws upon Cloudflare's experience building products/features on Durable Objects.</p>
<p>The name &quot;actors&quot; originates from the <a href="/durable-objects/concepts/what-are-durable-objects/#actor-programming-model">actor programming model</a>, which closely ties to how Durable Objects are modelled.</p>
<p>The <code>@cloudflare/actors</code> library includes:</p>
<ul>
<li>Storage helpers for querying embeddeded, per-object SQLite storage</li>
<li>Storage helpers for managing SQL schema migrations</li>
<li>Alarm helpers for scheduling multiple alarms provided a date, delay in seconds, or cron expression</li>
<li><code>Actor</code> class for using Durable Objects with a defined pattern</li>
<li>Durable Objects <a href="https://developers.cloudflare.com/durable-objects/api/base/">Workers API</a> is always available for your application as needed</li>
</ul>
<p>Storage and alarm helper methods can be combined with <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#storage--alarms-with-durableobject-class">any Javascript class</a> that defines your Durable Object, i.e, ones that extend <code>DurableObject</code> including the <code>Actor</code> class.</p>
<pre tabindex="0"><code class="language-js">import { Storage } from &quot;@cloudflare/actors/storage&quot;;&#10;&#10;export class ChatRoom extends DurableObject&lt;Env&gt; {&#10;    storage: Storage;&#10;&#10;    constructor(ctx: DurableObjectState, env: Env) {&#10;        super(ctx, env)&#10;        this.storage = new Storage(ctx.storage);&#10;        this.storage.migrations = [{&#10;            idMonotonicInc: 1,&#10;            description: &quot;Create users table&quot;,&#10;            sql: &quot;CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)&quot;&#10;        }]&#10;    }&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        // Run migrations before executing SQL query&#10;        await this.storage.runMigrations();&#10;&#10;        // Query with SQL template&#10;        let userId = new URL(request.url).searchParams.get(&quot;userId&quot;);&#10;        const query = this.storage.sql`SELECT * FROM users WHERE id = ${userId};`&#10;        return new Response(`${JSON.stringify(query)}`);&#10;    }&#10;}&#10;</code></pre>
<p><code>@cloudflare/actors</code> library introduces the <code>Actor</code> class pattern. <code>Actor</code> lets you access Durable Objects without writing the Worker that communicates with your Durable Object (the Worker is created for you). By default, requests are routed to a Durable Object named &quot;default&quot;.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(&#x27;Hello, World!&#x27;)&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>You can <a href="/durable-objects/get-started/#3-instantiate-and-communicate-with-a-durable-object">route</a> to different Durable Objects by name within your <code>Actor</code> class using <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#actor-with-custom-name"><code>nameFromRequest</code></a>.</p>
<pre tabindex="0"><code class="language-js">export class MyActor extends Actor&lt;Env&gt; {&#10;    static nameFromRequest(request: Request): string {&#10;        let url = new URL(request.url);&#10;        return url.searchParams.get(&quot;userId&quot;) ?? &quot;foo&quot;;&#10;    }&#10;&#10;    async fetch(request: Request): Promise&lt;Response&gt; {&#10;        return new Response(`Actor identifier (Durable Object name): ${this.identifier}`);&#10;    }&#10;}&#10;&#10;export default handler(MyActor);&#10;</code></pre>
<p>For more examples, check out the library <a href="https://github.com/cloudflare/actors?tab=readme-ov-file#getting-started">README</a>. <code>@cloudflare/actors</code> library is a place for more helpers and built-in patterns, like retry handling and Websocket-based applications, to reduce development overhead for common Durable Objects functionality. Please share feedback and what more you would like to see on our <a href="https://discord.com/channels/595317990191398933/773219443911819284">Discord channel</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-23">Jun 23, 2025</time><div>
<h2 id="post-cf1-data-security-analytics-v1"><a href="/changelog/post/cf1-data-security-analytics-v1/">Data Security Analytics in the Zero Trust dashboard</a></h2>
<div class="changelog-badges"><span>dlp</span><span>casb</span><span>cloudflare-one</span></div><div class="changelog-body"><p>Zero Trust now includes <strong>Data security analytics</strong>, providing you with unprecedented visibility into your organization sensitive data.</p>
<p>The new dashboard includes:</p>
<ul>
<li>
<p><strong>Sensitive Data Movement Over Time:</strong></p>
<ul>
<li>See patterns and trends in how sensitive data moves across your environment. This helps understand where data is flowing and identify common paths.</li>
</ul>
</li>
<li>
<p><strong>Sensitive Data at Rest in SaaS &amp; Cloud:</strong></p>
<ul>
<li>View an inventory of sensitive data stored within your corporate SaaS applications (for example, Google Drive, Microsoft 365) and cloud accounts (such as AWS S3).</li>
</ul>
</li>
<li>
<p><strong>DLP Policy Activity:</strong></p>
<ul>
<li>Identify which of your Data Loss Prevention (DLP) policies are being triggered most often.</li>
<li>See which specific users are responsible for triggering DLP policies.</li>
</ul>
</li>
</ul>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/cf1-data-security-analytics-v1.png" alt="Data Security Analytics" /></p>
<p>To access the new dashboard, log in to <a href="https://one.dash.cloudflare.com/">Cloudflare One</a> and go to <strong>Insights</strong> on the sidebar.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-23">Jun 23, 2025</time><div>
<h2 id="post-2025-06-23-user-groups-ga"><a href="/changelog/post/2025-06-23-user-groups-ga/">Cloudflare User Groups &amp; SCIM User Groups are now in GA</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>We're announcing the GA of <strong>User Groups for Cloudflare Dashboard</strong> and <strong>System for Cross Domain Identity Management (SCIM) User Groups</strong>, strengthening our RBAC capabilities with stable, production-ready primitives for managing access at scale.</p>
<p><strong>What's New</strong></p>
<p><strong>User Groups [GA]</strong>: <a href="/fundamentals/manage-members/user-groups/">User Groups</a> are a new Cloudflare IAM primitive that enable administrators to create collections of account members that are treated equally from an access control perspective. User Groups can be assigned permission policies, with individual members in the group inheriting all permissions granted to the User Group. User Groups can be created manually or via our APIs.</p>
<p><strong>SCIM User Groups [GA]</strong>: Centralize &amp; simplify your user and group management at scale by syncing memberships directly from your upstream identity provider (like Okta or Entra ID) to the Cloudflare Platform. This ensures Cloudflare stays in sync with your identity provider, letting you apply Permission Policies to those synced groups directly within the Cloudflare Dashboard.</p>
<p><strong>Stability &amp; Scale</strong>:
These features have undergone extensive testing during the Public Beta period and are now ready for production use across enterprises of all sizes.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17727.md")</aside>
<p>For more info:</p>
<ul>
<li><a href="/fundamentals/manage-members/user-groups/">Get started with User Groups</a></li>
<li><a href="/fundamentals/account/account-security/scim-setup/">Explore our SCIM integration guide</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-20">Jun 20, 2025</time><div>
<h2 id="post-2025-06-20-cni-maintenance-alerts"><a href="/changelog/post/2025-06-20-cni-maintenance-alerts/">CNI maintenance alerts</a></h2>
<div class="changelog-badges"><span>network-interconnect</span></div><div class="changelog-body"><p>Customers using Cloudflare Network Interconnect with the v1 dataplane can now subscribe to maintenance alert emails. These alerts notify you of planned maintenance windows that may affect your CNI circuits.</p>
<p>For more information, refer to <a href="/network-interconnect/monitoring-and-alerts/">Monitoring and alerts</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-20">Jun 20, 2025</time><div>
<h2 id="post-2025-06-20-increased-blob-size-limits-in-Workers-Analytics"><a href="/changelog/post/2025-06-20-increased-blob-size-limits-in-Workers-Analytics/">Increased blob size limits in Workers Analytics Engine</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We’ve increased the total allowed size of <a href="/analytics/analytics-engine/get-started/#2-write-data-points-from-your-worker"><code>blob</code></a> fields on data points written to <a href="/analytics/analytics-engine/">Workers Analytics Engine</a> from <strong>5 KB to 16 KB</strong>.</p>
<p>This change gives you more flexibility when logging rich observability data — such as base64-encoded payloads, AI inference traces, or custom metadata — without hitting request size limits.</p>
<p>You can find full details on limits for queries, filters, payloads, and more <a href="/analytics/analytics-engine/limits/">here in the Workers Analytics Engine limits documentation</a>.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17779.md")</div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-19">Jun 19, 2025</time><div>
<h2 id="post-2025-06-19-autorag-custom-metadata-and-context"><a href="/changelog/post/2025-06-19-autorag-custom-metadata-and-context/">View custom metadata in responses and guide AI-search with context in AutoRAG</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>In <a href="/ai-search/">AutoRAG</a>, you can now view your object's custom metadata in the response from <a href="/ai-search/api/search/workers-binding/"><code>/search</code></a> and <a href="/ai-search/api/search/workers-binding/"><code>/ai-search</code></a>, and optionally add a <code>context</code> field in the custom metadata of an object to provide additional guidance for AI-generated answers.</p>
<p>You can add <a href="/r2/api/workers/workers-api-reference/#r2putoptions">custom metadata</a> to an object when uploading it to your R2 bucket.</p>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-object-s-custom-metadata-in-search-responses">Object's custom metadata in search responses</h4>
<p>When you run a search, AutoRAG now returns any custom metadata associated with the object. This metadata appears in the response inside <code>attributes</code> then <code>file</code> , and can be used for downstream processing.</p>
<p>For example, the <code>attributes</code> section of your search response may look like:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;attributes&quot;: {&#10;		&quot;timestamp&quot;: 1750001460000,&#10;		&quot;folder&quot;: &quot;docs/&quot;,&#10;		&quot;filename&quot;: &quot;launch-checklist.md&quot;,&#10;		&quot;file&quot;: {&#10;			&quot;url&quot;: &quot;https://wiki.company.com/docs/launch-checklist&quot;,&#10;			&quot;context&quot;: &quot;A checklist for internal launch readiness, including legal, engineering, and marketing steps.&quot;&#10;		}&#10;	}&#10;}&#10;</code></pre>
<h4 id="2025-06-19-autorag-custom-metadata-and-context-add-a-context-field-to-guide-llm-answers">Add a <code>context</code> field to guide LLM answers</h4>
<p>When you include a custom metadata field named <code>context</code>, AutoRAG attaches that value to each chunk of the file. When you run an <code>/ai-search</code> query, this <code>context</code> is passed to the LLM and can be used as additional input when generating an answer.</p>
<p>We recommend using the <code>context</code> field to describe supplemental information you want the LLM to consider, such as a summary of the document or a source URL. If you have several different metadata attributes, you can join them together however you choose within the <code>context</code> string.</p>
<p>For example:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;context&quot;: &quot;summary: &#x27;Checklist for internal product launch readiness, including legal, engineering, and marketing steps.&#x27;; url: &#x27;https://wiki.company.com/docs/launch-checklist&#x27;&quot;&#10;}&#10;</code></pre>
<p>This gives you more control over how your content is interpreted, without requiring you to modify the original contents of the file.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-19">Jun 19, 2025</time><div>
<h2 id="post-2025-06-19-autorag-filename-filter"><a href="/changelog/post/2025-06-19-autorag-filename-filter/">Filter your AutoRAG search by file name</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>In <a href="/ai-search/">AutoRAG</a>, you can now <a href="/ai-search/configuration/indexing/metadata/">filter</a> by an object's file name using the <code>filename</code> attribute, giving you more control over which files are searched for a given query.</p>
<p>This is useful when your application has already determined which files should be searched. For example, you might query a PostgreSQL database to get a list of files a user has access to based on their permissions, and then use that list to limit what AutoRAG retrieves.</p>
<p>For example, your search query may look like:</p>
<pre tabindex="0"><code class="language-js">const response = await env.AI.autorag(&quot;my-autorag&quot;).search({&#10;	query: &quot;what is the project deadline?&quot;,&#10;	filters: {&#10;		type: &quot;eq&quot;,&#10;		key: &quot;filename&quot;,&#10;		value: &quot;project-alpha-roadmap.md&quot;,&#10;	},&#10;});&#10;</code></pre>
<p>This allows you to connect your application logic with AutoRAG's retrieval process, making it easy to control what gets searched without needing to reindex or modify your data.</p>
<p>Learn more in AutoRAG's <a href="/ai-search/configuration/indexing/metadata/">metadata filtering documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-19">Jun 19, 2025</time><div>
<h2 id="post-2025-06-23-account-level-dns-analytics-api"><a href="/changelog/post/2025-06-23-account-level-dns-analytics-api/">Account-level DNS analytics now available via GraphQL Analytics API</a></h2>
<div class="changelog-badges"><span>dns</span></div><div class="changelog-body"><p>Authoritative DNS analytics are now available on the <strong>account level</strong> via the <a href="/analytics/graphql-api/">Cloudflare GraphQL Analytics API</a>.</p>
<p>This allows users to query DNS analytics across multiple zones in their account, by using the <code>accounts</code> filter.</p>
<p>Here is an example to retrieve the most recent DNS queries across all zones in your account that resulted in an <code>NXDOMAIN</code> response over a given time frame. Please replace <code>a30f822fcd7c401984bf85d8f2a5111c</code> with your actual account ID.</p>
<pre tabindex="0"><code class="language-graphql">query GetLatestNXDOMAINResponses {&#10;	viewer {&#10;		accounts(filter: { accountTag: &quot;a30f822fcd7c401984bf85d8f2a5111c&quot; }) {&#10;			dnsAnalyticsAdaptive(&#10;				filter: {&#10;					date_geq: &quot;2025-06-16&quot;&#10;					date_leq: &quot;2025-06-18&quot;&#10;					responseCode: &quot;NXDOMAIN&quot;&#10;				}&#10;				limit: 10000&#10;				orderBy: [datetime_DESC]&#10;			) {&#10;				zoneTag&#10;				queryName&#10;				responseCode&#10;				queryType&#10;				datetime&#10;			}&#10;		}&#10;	}&#10;}&#10;</code></pre>
<p>To learn more and get started, refer to the <a href="/dns/additional-options/analytics/#analytics">DNS Analytics documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-19">Jun 19, 2025</time><div>
<h2 id="post-2025-06-17-workers-terraform-sdk-api-fixes"><a href="/changelog/post/2025-06-17-workers-terraform-sdk-api-fixes/">Automate Worker deployments with a simplified SDK and more reliable Terraform provider</a></h2>
<div class="changelog-badges"><span>d1</span><span>workers</span><span>workers-for-platforms</span></div><div class="changelog-body"><h4 id="2025-06-17-workers-terraform-sdk-api-fixes-simplified-worker-deployments-with-our-sdks">Simplified Worker Deployments with our SDKs</h4>
<p>We've simplified the programmatic deployment of Workers via our <a href="/fundamentals/api/reference/sdks/">Cloudflare SDKs</a>. This update abstracts away the low-level complexities of the <code>multipart/form-data</code> upload process, allowing you to focus on your code while we handle the deployment mechanics.</p>
<p>This new interface is available in:</p>
<ul>
<li><a href="https://github.com/cloudflare/cloudflare-typescript">cloudflare-typescript</a> (4.4.1)</li>
<li><a href="https://github.com/cloudflare/cloudflare-python">cloudflare-python</a> (4.3.1)</li>
</ul>
<p>For complete examples, see our guide on <a href="/workers/platform/infrastructure-as-code">programmatic Worker deployments</a>.</p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-the-old-way-manual-api-calls">The Old way: Manual API calls</h4>
<p>Previously, deploying a Worker programmatically required manually constructing a <code>multipart/form-data</code> HTTP request, packaging your code and a separate <code>metadata.json</code> file. This was more complicated and verbose, and prone to formatting errors.</p>
<p>For example, here's how you would upload a Worker script previously with cURL:</p>
<pre tabindex="0"><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/&lt;account_id&gt;/workers/scripts/my-hello-world-script \&#10;  &#45;X PUT \&#10;  &#45;H &#x27;Authorization: Bearer &lt;api_token&gt;&#x27; \&#10;  &#45;F &#x27;metadata={&#10;        &quot;main_module&quot;: &quot;my-hello-world-script.mjs&quot;,&#10;        &quot;bindings&quot;: [&#10;          {&#10;            &quot;type&quot;: &quot;plain_text&quot;,&#10;            &quot;name&quot;: &quot;MESSAGE&quot;,&#10;            &quot;text&quot;: &quot;Hello World!&quot;&#10;          }&#10;        ],&#10;        &quot;compatibility_date&quot;: &quot;$today&quot;&#10;      };type=application/json&#x27; \&#10;  &#45;F &#x27;my-hello-world-script.mjs=@-;filename=my-hello-world-script.mjs;type=application/javascript+module&#x27; &lt;&lt;EOF&#10;export default {&#10;  async fetch(request, env, ctx) {&#10;    return new Response(env.MESSAGE, { status: 200 });&#10;  }&#10;};&#10;EOF&#10;</code></pre>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-after-sdk-interface">After: SDK interface</h4>
<p>With the new SDK interface, you can now define your entire Worker configuration using a single, structured object.</p>
<p>This approach allows you to specify metadata like <code>main_module</code>, <code>bindings</code>, and <code>compatibility_date</code> as clearer properties directly alongside your script content. Our SDK takes this logical object and automatically constructs the complex multipart/form-data API request behind the scenes.</p>
<p>Here's how you can now programmatically deploy a Worker via the <a href="https://github.com/cloudflare/cloudflare-typescript"><code>cloudflare-typescript</code> SDK</a></p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17777.md")</div>
<p>View the complete example here: <a href="https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts">https://github.com/cloudflare/cloudflare-typescript/blob/main/examples/workers/script-upload.ts</a></p>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-terraform-provider-improvements">Terraform provider improvements</h4>
<p>We've also made several fixes and enhancements to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare">Cloudflare Terraform provider</a>:</p>
<ul>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_script"><code>cloudflare_workers_script</code></a> resource in Terraform, which previously was producing a diff even when there were no changes. Now, your <code>terraform plan</code> outputs will be cleaner and more reliable.</li>
<li>Fixed the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_for_platforms_dispatch_namespace"><code>cloudflare_workers_for_platforms_dispatch_namespace</code></a>, where the provider would attempt to recreate the namespace on a <code>terraform apply</code>. The resource now correctly reads its remote state, ensuring stability for production environments and CI/CD workflows.</li>
<li>The <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/workers_route"><code>cloudflare_workers_route</code></a> resource now allows for the <code>script</code> property to be empty, null, or omitted to indicate that pattern should be negated for all scripts (see routes <a href="/workers/configuration/routing/routes">docs</a>). You can now reserve a pattern or temporarily disable a Worker on a route without deleting the route definition itself.</li>
<li>Using <code>primary_location_hint</code> in the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/resources/d1_database"><code>cloudflare_d1_database</code></a> resource will no longer always try to recreate. You can now safely change the location hint for a D1 database without causing a destructive operation.</li>
</ul>
<h4 id="2025-06-17-workers-terraform-sdk-api-fixes-api-improvements">API improvements</h4>
<p>We've also properly documented the <a href="/api/resources/workers/subresources/scripts/subresources/script_and_version_settings">Workers Script And Version Settings</a> in our public OpenAPI spec and SDKs.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-18">Jun 18, 2025</time><div>
<h2 id="post-2025-06-17-new-order-of-enforcement"><a href="/changelog/post/2025-06-17-new-order-of-enforcement/">Gateway will now evaluate Network policies before HTTP policies from July 14th, 2025</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p><a href="/cloudflare-one/traffic-policies/">Gateway</a> will now evaluate <a href="/cloudflare-one/traffic-policies/network-policies/">Network (Layer 4) policies</a> <strong>before</strong> <a href="/cloudflare-one/traffic-policies/http-policies/">HTTP (Layer 7) policies</a>. This change preserves your existing security posture and does not affect which traffic is filtered — but it may impact how notifications are displayed to end users.</p>
<p>This change will roll out progressively between <strong>July 14–18, 2025</strong>. If you use HTTP policies, we recommend reviewing your configuration ahead of rollout to ensure the user experience remains consistent.</p>
<h4 id="2025-06-17-new-order-of-enforcement-updated-order-of-enforcement">Updated order of enforcement</h4>
<p><strong>Previous order:</strong></p>
<ol>
<li>DNS policies</li>
<li>HTTP policies</li>
<li>Network policies</li>
</ol>
<p><strong>New order:</strong></p>
<ol>
<li>DNS policies</li>
<li><strong>Network policies</strong></li>
<li><strong>HTTP policies</strong></li>
</ol>
<h4 id="2025-06-17-new-order-of-enforcement-action-required-review-your-gateway-http-policies">Action required: Review your Gateway HTTP policies</h4>
<p>This change may affect block notifications. For example:</p>
<ul>
<li>You have an <strong>HTTP policy</strong> to block <code>example.com</code> and display a block page.</li>
<li>You also have a <strong>Network policy</strong> to block <code>example.com</code> silently (no client notification).</li>
</ul>
<p>With the new order, the Network policy will trigger first — and the user will no longer see the HTTP block page.</p>
<p>To ensure users still receive a block notification, you can:</p>
<ul>
<li>Add a client notification to your Network policy, or</li>
<li>Use only the HTTP policy for that domain.</li>
</ul>
<hr />
<h4 id="2025-06-17-new-order-of-enforcement-why-we-re-making-this-change">Why we’re making this change</h4>
<p>This update is based on user feedback and aims to:</p>
<ul>
<li>Create a more intuitive model by evaluating network-level policies before application-level policies.</li>
<li>Minimize <a href="/support/troubleshooting/http-status-codes/cloudflare-5xx-errors/error-526/#error-526-in-the-zero-trust-context">526 connection errors</a> by verifying the network path to an origin before attempting to establish a decrypted TLS connection.</li>
</ul>
<hr />
<p>To learn more, visit the <a href="/cloudflare-one/traffic-policies/order-of-enforcement/">Gateway order of enforcement documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-18">Jun 18, 2025</time><div>
<h2 id="post-2025-06-18-log-explorer-ga"><a href="/changelog/post/2025-06-18-log-explorer-ga/">Log Explorer is GA</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p><a href="/log-explorer/">Log Explorer</a> is now GA, providing native observability and forensics for traffic flowing through Cloudflare.</p>
<p>Search and analyze your logs, natively in the Cloudflare dashboard. These logs are also stored in Cloudflare's network, eliminating many of the costs associated with other log providers.</p>
<p><img src="/assets/upstream/images/changelog/log-explorer/log-explorer-dash.png" alt="Log Explorer dashboard" /></p>
<p>With Log Explorer, you can now:</p>
<ul>
<li><strong>Monitor security and performance issues with custom dashboards</strong> – use natural language to define charts for measuring response time, error rates, top statistics and more.</li>
<li><strong>Investigate and troubleshoot issues with Log Search</strong> – use data type-aware search filters or custom sql to investigate detailed logs.</li>
<li><strong>Save time and collaborate with saved queries</strong> – save Log Search queries for repeated use or sharing with other users in your account.</li>
<li><strong>Access Log Explorer at the account and zone level</strong> – easily find Log Explorer at the account and zone level for querying any dataset.</li>
</ul>
<p>For help getting started, refer to <a href="/log-explorer/">our documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-06-18">Jun 18, 2025</time><div>
<h2 id="post-2025-06-18-remote-bindings-beta"><a href="/changelog/post/2025-06-18-remote-bindings-beta/">Remote bindings public beta - Connect to remote resources (D1, KV, R2, etc.) during local development</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Today <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">we announced the public beta</a> of <a href="/workers/local-development/#remote-bindings">remote bindings</a> for local development. With remote bindings, you can now connect to deployed resources like <a href="/r2/">R2 buckets</a> and <a href="/d1/">D1 databases</a> while running Worker code on your local machine. This means you can test your local code changes against real data and services, without the overhead of deploying for each iteration.</p>
<h4 id="2025-06-18-remote-bindings-beta-example-configuration">Example configuration</h4>
<p>To enable remote mode, add <code>&quot;experimental_remote&quot; : true</code> to each binding that you want to rely on a remote resource running on Cloudflare:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17778.md")</div>
<p>When remote bindings are configured, your Worker <strong>still executes locally</strong>, but all binding calls are proxied to the deployed resource that runs on Cloudflare's network.</p>
<p><strong>You can try out remote bindings for local development today with:</strong></p>
<ul>
<li><a href="/workers/local-development/#remote-bindings">Wrangler v4.20.3</a>: Use the <code>wrangler dev --x-remote-bindings</code> command.</li>
<li>The <a href="/workers/local-development/#remote-bindings">Cloudflare Vite Plugin</a>: Refer to the documentation for how to enable in your Vite config.</li>
<li>The <a href="/workers/local-development/#remote-bindings">Cloudflare Vitest Plugin</a>: Refer to the documentation for how to enable in your Vitest config.</li>
</ul>
<p><strong>Have feedback?</strong>
Join the discussion in our <a href="https://github.com/cloudflare/workers-sdk/discussions/9660">beta announcement</a> to share feedback or report any issues.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/39/">Previous</a><span>Page 40 of 50</span><a class="pagination-next" rel="next" href="/changelog/41/">Next</a></nav>
</div>
