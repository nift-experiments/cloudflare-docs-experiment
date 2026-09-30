---
cp9:
  canonical: https://developers.cloudflare.com/changelog/6/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 6 | Cloudflare Docs
  head_html: <title>Changelog - page 6 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/6/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 6"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/6/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/6/#page","headline":"Changelog - page 6 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/6/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/6/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-08-07">Aug 7, 2026</time><div>
<h2 id="post-2026-08-07-waf-release"><a href="/changelog/post/2026-08-07-waf-release/">WAF Release - 2026-08-07</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release updates WordPress XSS rule metadata in the Cloudflare Managed Ruleset and Cloudflare Free Ruleset to identify XSS2Shell (CVE-2026-64638). It also disables the Command Injection - Obfuscation rule.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-64638: A pre-authentication reflected cross-site scripting vulnerability affecting the WordPress login screen. Exploitation requires social engineering and explicit interaction by the target user. Under additional conditions, it may be escalated to remote code execution.</li>
</ul>
<p><strong>Impact</strong></p>
<p>The WordPress changes update rule metadata only; detection behavior and actions remain unchanged.</p>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d3852d0891634686a46114069c6dff1c">9c6dff1c</code>
</td>
<td>N/A</td>
<td>Wordpress - XSS - CVE:CVE-2026-64638</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="5bdf578fff504b8cbe3b7f699ab5ed95">9ab5ed95</code>
</td>
<td>N/A</td>
<td>Wordpress - XSS - CVE:CVE-2026-64638</td>
<td>Block</td>
<td>N/A</td>
<td>Rule metadata description refined. Detection unchanged.</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="95a84ab1645a49c685648c17761e7a4c">761e7a4c</code>
</td>
<td>N/A</td>
<td>Command Injection - Obfuscation</td>
<td>Block</td>
<td>Disabled</td>
<td>Detection logic has been deprecated</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-06">Aug 6, 2026</time><div>
<h2 id="post-2026-08-06-public-endpoint-custom-domains-and-namespaces"><a href="/changelog/post/2026-08-06-public-endpoint-custom-domains-and-namespaces/">AI Search makes it easier to build a search engine for your data</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p><a href="/ai-search/">AI Search</a> gets you from a data source to a working search endpoint quickly. This release adds what you need to put that endpoint in front of real users: your own domain, authentication, and one endpoint across several instances. It also adds crawling for sites without a complete sitemap, so your index covers everything you want it to find.</p>
<p>Each of the following is a new option. The previous behavior is still the default, so nothing changes until you change it.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-serve-search-from-your-own-domain">Serve search from your own domain</h4>
<p>A <a href="/ai-search/configuration/retrieval/public-endpoint/">public endpoint</a> is a URL that a site or app can query directly, with no authentication in front of it. By default that URL is a generated hostname on <code>search.ai.cloudflare.com</code>. You can now serve the same endpoint from a <a href="/ai-search/configuration/retrieval/public-endpoint/custom-domains/">custom domain</a>, a hostname in a zone that you own:</p>
<pre tabindex="0"><code class="language-txt">https://search.example.com/search&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-restrict-who-can-query-your-content">Restrict who can query your content</h4>
<p>Once your endpoint is on your own domain, you can put <a href="/ai-search/configuration/retrieval/public-endpoint/cloudflare-access/">Cloudflare Access</a> in front of it. For example, you usually want to give <code>/mcp</code> to specific agents rather than to anyone who finds the URL. Agents authenticate with an Access service token, and people who open the endpoint in a browser sign in through your identity provider.</p>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-search-several-instances-from-one-url">Search several instances from one URL</h4>
<p>A namespace can expose its own <a href="/ai-search/configuration/retrieval/public-endpoint/namespace/">public endpoint</a> with <code>/search</code>, <code>/chat/completions</code>, and <code>/mcp</code> paths that fan out across the instances you choose:</p>
<pre tabindex="0"><code class="language-bash">curl https://ns-&lt;NAMESPACE_ENDPOINT_ID&gt;.search.ai.cloudflare.com/search \&#10;  &#45;-header &quot;Content-Type: application/json&quot; \&#10;  &#45;-data &#x27;{&#10;    &quot;messages&quot;: [{ &quot;content&quot;: &quot;How do I configure AI Search?&quot;, &quot;role&quot;: &quot;user&quot; }],&#10;    &quot;ai_search_options&quot;: { &quot;instance_ids&quot;: [&quot;docs&quot;, &quot;support&quot;] }&#10;  }&#x27;&#10;</code></pre>
<h4 id="2026-08-06-public-endpoint-custom-domains-and-namespaces-index-your-sites-without-a-sitemap">Index your sites without a sitemap</h4>
<p>Website data sources support a new <code>discover</code> <a href="/ai-search/configuration/data-source/website/parse-types/">parse type</a>. It starts at the source URL and collects pages from both your sitemaps and the links it finds while crawling:</p>
<pre tabindex="0"><code class="language-bash">curl -X POST &quot;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/ai-search/instances&quot; \&#10;  &#45;H &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot; \&#10;  &#45;H &quot;Content-Type: application/json&quot; \&#10;  &#45;d &#x27;{&#10;    &quot;id&quot;: &quot;my-ai-search&quot;,&#10;    &quot;type&quot;: &quot;web-crawler&quot;,&#10;    &quot;source&quot;: &quot;example.com&quot;,&#10;    &quot;source_params&quot;: {&#10;      &quot;web_crawler&quot;: {&#10;        &quot;parse_type&quot;: &quot;discover&quot;,&#10;        &quot;discover_options&quot;: { &quot;source&quot;: &quot;links&quot;, &quot;limit&quot;: 5000, &quot;depth&quot;: 3 }&#10;      }&#10;    }&#10;  }&#x27;&#10;</code></pre>
<p>To learn more, refer to the <a href="/ai-search/">AI Search documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-06">Aug 6, 2026</time><div>
<h2 id="post-2026-08-06-kitesurf"><a href="/changelog/post/2026-08-06-kitesurf/">Introducing Kitesurf, an agent-first browser on Browser Run</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/kitesurf/">Kitesurf</a> is Cloudflare's new stateless, highly scalable browser that runs entirely on top of <a href="/workers/">Workers</a> and is designed for AI agents. It is available for free while in beta.</p>
<p>Compared to Chromium, Kitesurf uses 3–7× less CPU and memory for common agentic tasks like screenshots and HTML extraction, so you can run more sessions and scale better for bursty, AI-driven workloads.</p>
<p>Your existing clients already work. To opt in, add the <code>browser=kitesurf</code> parameter to any Browser Run <a href="/browser-run/cdp/">CDP</a> or <a href="/browser-run/quick-actions/">Quick Action</a> endpoint:</p>
<pre tabindex="0"><code class="language-sh">curl -X POST &#x27;https://api.cloudflare.com/client/v4/accounts/&lt;ACCOUNT_ID&gt;/browser-run/screenshot?browser=kitesurf&#x27; \&#10;  &#45;H &#x27;Authorization: Bearer &lt;API_TOKEN&gt;&#x27; \&#10;  &#45;H &#x27;Content-Type: application/json&#x27; \&#10;  &#45;d &#x27;{&#10;    &quot;url&quot;: &quot;https://example.com&quot;&#10;  }&#x27; \&#10;  &#45;-output &quot;screenshot.png&quot;&#10;</code></pre>
<p>You can also explore Kitesurf without writing any code in the <a href="https://kitesurf.cloudflare.app/">public playground</a>.</p>
<p>For more information, refer to the <a href="/browser-run/kitesurf/">Kitesurf documentation</a> and the <a href="https://blog.cloudflare.com/kitesurf">blog announcement</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-06">Aug 6, 2026</time><div>
<h2 id="post-2026-08-05-user-insights"><a href="/changelog/post/2026-08-05-user-insights/">Track AI spend and catch anomalous usage with User Insights</a></h2>
<div class="changelog-badges"><span>ai-gateway</span></div><div class="changelog-body"><p>AI Gateway now includes User Insights, a dashboard that gives you two things at once: clear visibility into how much your organization spends on AI, and a security signal that surfaces users whose usage suddenly looks abnormal. It works on the traffic already flowing through your gateway, so there is no additional setup.</p>
<p>On the spend side, User Insights shows organization-wide totals for cost, requests, tokens, and adoption, and lets you drill into an individual user to see their spend, top models and providers, cache hit rate, and more. To attribute usage to individual users, add a user identifier with custom metadata or put your gateway behind Cloudflare Access.</p>
<p>On the security side, User Insights baselines each user's normal usage from their 95th percentile (p95) session cost over the last 30 days, then flags sessions that exceed both that baseline and an organization-level threshold. A sudden jump above a user's own pattern is often the first sign of a compromised credential or a misbehaving agent, so you can investigate before it shows up on your bill.</p>
<p>User Insights is available to all AI Gateway customers at no additional cost.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-05">Aug 5, 2026</time><div>
<h2 id="post-2026-08-05-access-user-id-metadata"><a href="/changelog/post/2026-08-05-access-user-id-metadata/">Identity-aware controls are now available in AI Gateway</a></h2>
<div class="changelog-badges"><span>ai-gateway</span><span>access</span></div><div class="changelog-body"><p>AI Gateway now integrates with Cloudflare Access, giving you two new capabilities:</p>
<ul>
<li><strong>Protect your gateway endpoint.</strong> Put your AI Gateway behind Access so you can set policies that control who is allowed to call a specific gateway's endpoint.</li>
<li><strong>Identity-aware controls.</strong> When traffic reaches AI Gateway through an Access-protected custom domain, AI Gateway can use the authenticated user's Access identity in logs, analytics, routing, and spend controls.</li>
</ul>
<p>With identity-aware controls, you can set spend limits by authenticated user, control which gateways different users can access, filter logs by user, and build policies without passing user IDs from the client application. AI Gateway adds the verified Access user ID to request metadata as <code>cf.user_id</code>.</p>
<p>For setup instructions, refer to <a href="/ai-gateway/configuration/cloudflare-access/">Cloudflare Access</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-05">Aug 5, 2026</time><div>
<h2 id="post-2026-08-04-oauth-consent-shields"><a href="/changelog/post/2026-08-04-oauth-consent-shields/">Improved publisher verification details on OAuth consent screens</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>OAuth consent screens now display a shield icon with explanatory text beneath the consent screen title. Each shield icon indicates who owns the application and whether its domain ownership is verified.</p>
<ul>
<li><strong>Green filled shield</strong>: Cloudflare owns and manages the application.</li>
<li><strong>Blue outlined shield</strong>: A third-party application with verified ownership of its domain.</li>
<li><strong>Amber filled shield</strong>: A third-party application without verified ownership of a domain.</li>
</ul>
<p>Domain verification only confirms that the application owner controls the displayed domain.</p>
<p>For more information, refer to <a href="/fundamentals/oauth/authorizing-an-application/">Authorizing an application</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-agent-tracing"><a href="/changelog/post/2026-08-04-agent-tracing/">Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations.</p>
<p>Turn on Workers tracing in your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17683.md")</div>
<p>Think and Flue applications emit agent traces automatically. For direct AI SDK calls, wrap the AI SDK namespace once. <code>wrapAISDK()</code> supports AI SDK v6 and v7. This AI SDK v7 example also supplies the agent identity:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17684.md")</div>
<p>Message and tool payload recording is off by default. Turn it on only when the payloads are safe to store:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17685.md")</div>
<p>Open the <a href="https://dash.cloudflare.com/?to=/:account/agents"><strong>Agents</strong> tab</a> in the Cloudflare dashboard to inspect sessions, replay conversations, and view trace waterfalls. For advanced setup, privacy controls, and trace structure, refer to <a href="/agents/runtime/operations/observability/tracing/">Agent tracing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-build-and-deploy-on-push"><a href="/changelog/post/2026-08-04-build-and-deploy-on-push/">Build and deploy Artifacts repos on every push</a></h2>
<div class="changelog-badges"><span>artifacts</span><span>workflows</span></div><div class="changelog-body"><p>You can now run your CI/CD pipeline on your <a href="/artifacts/">Artifacts</a> repo by defining a CI <a href="/workflows/">Workflow</a> with the <a href="https://github.com/cloudflare/ci">CI SDK</a>, automatically triggered on Artifacts push events.</p>
<p>This allows you to:</p>
<ul>
<li>Automatically build and deploy application code stored in Artifacts.</li>
<li>Run linting, type checking, tests, and other checks on every push.</li>
<li>Reuse dependencies when the lockfile (i.e. <code>pnpm-lock.yaml</code>) has not changed.</li>
<li>Stop deployment when a check or build fails.</li>
<li>Restrict API token access to the deployment step.</li>
<li>Deploy the output to a <a href="/workers/">Worker</a> or a <a href="/cloudflare-for-platforms/workers-for-platforms/">Workers for Platforms</a> User Worker.</li>
</ul>
<p>Define your CI steps with <code>@cloudflare/ci</code>. Each <code>ci.runner()</code> spins up an isolated sandbox, and the <code>cache</code> option reuses installed dependencies across each sandboxed step in your CI job.</p>
<p>Point <code>cache.inputs</code> at your lockfile (i.e. <code>pnpm-lock.yaml</code>, <code>bun.lock</code>), and the install step only runs again when that lockfile changes:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17690.md")</div>
<p>To start the Workflow automatically after each push, add a <code>cf.artifacts.repo.pushed</code> trigger to your Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17691.md")</div>
<p>To learn more, refer to <a href="/artifacts/guides/build-and-deploy-on-push/">Build and deploy Artifacts repos</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-free-dashboard-button"><a href="/changelog/post/2026-08-04-free-dashboard-button/">Create Free accounts from the dashboard</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>You can now create standalone Free accounts directly from the Cloudflare dashboard using the new <strong>Create Account</strong> button. This feature is currently available to all users.</p>
<p>When creating a Free account:</p>
<ul>
<li>You can create up to <strong>5 Free accounts</strong>.</li>
<li>Your user account must have at least <strong>7 days of tenure</strong> to be eligible.</li>
<li>The account is created immediately and ready to use.</li>
</ul>
<p>To create a Free account, go to the <a href="https://dash.cloudflare.com/"><strong>Cloudflare dashboard</strong></a> and select <strong>Create Account</strong> from either the account switcher in the top left (where your account name appears) or from the <strong>Accounts</strong> page.</p>
<h4 id="2026-08-04-free-dashboard-button-limitations">Limitations</h4>
* This feature can only be used to create a Cloudflare Free account. To create an Enterprise Account under your existing contract, please contact Cloudflare Support. 
* All users can create a Cloudflare Free account, however, Enterprises wish to restrict this action to only Super Administrators. We will deliver this improvement in a future release. 
<h4 id="2026-08-04-free-dashboard-button-next-steps">Next steps</h4>
<p>After creating your Free account, you can:</p>
<ul>
<li><a href="/billing/get-started/create-billing-profile/">Add a payment method</a> to enable additional Cloudflare products and services.</li>
<li><a href="/billing/get-started/update-billing-info/">Update billing information</a> to manage payment methods, billing address, or tax IDs.</li>
<li><a href="/billing/understand/how-billing-works/">Review how Cloudflare billing works</a> to understand the billing lifecycle and charge types.</li>
<li><a href="/fundamentals/organizations/for-enterprise/">Assign accounts to an Enterprise Organization</a> to centrally manage multiple accounts from a single dashboard.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-index-capacity-20-million"><a href="/changelog/post/2026-08-04-index-capacity-20-million/">Vectorize indexes now support up to 20 million vectors</a></h2>
<div class="changelog-badges"><span>vectorize</span></div><div class="changelog-body"><p>You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.</p>
<p>Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the <a href="/vectorize/platform/limits/">Vectorize limits documentation</a> for complete details.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-waf-release"><a href="/changelog/post/2026-08-04-waf-release/">WAF Release - 2026-08-04</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new rules and updates Microsoft SharePoint RCE alongside enhanced SSRF cloud protection rule actions.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>CVE-2026-50522: An insecure deserialization vulnerability in Microsoft SharePoint Server. This may allow an unauthenticated attacker to execute arbitrary code using crafted requests.</li>
<li>CVE-2026-66066: An improper input processing vulnerability in Ruby on Rails Active Storage image variant transformations. This may allow an unauthenticated attacker to perform arbitrary file reads and achieve Remote Code Execution (RCE) using maliciously crafted payload requests.</li>
<li>Generic Cloud Protections: Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications.</li>
</ul>
<table style="width: 100%">
<thead>
<tr>
<th>Ruleset</th>
<th>Rule ID</th>
<th>Legacy Rule ID</th>
<th>Description</th>
<th>Previous Action</th>
<th>New Action</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="91aee93c31944828bf86f068052b07cf">052b07cf</code>
</td>
<td>N/A</td>
<td>Microsoft SharePoint - Remote Code Execution - CVE:CVE-2026-50522</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="89d0243997d24c6ea1d610a23a5b40d6">3a5b40d6</code>
</td>
<td>N/A</td>
<td>Rails - Arbitrary File Read & RCE - CVE:CVE-2026-66066</td>
<td>Block</td>
<td>Block</td>
<td>
				This was labeled as File Upload - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="98bfd6bb46074d5b8d1c4b39743a63ec">743a63ec</code>
</td>
<td>N/A</td>
<td>SSRF - Local - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="ecd26d61a75e46f6a4449a06ab8af26f">ab8af26f</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - 2 - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="281a1b7086b84db7a695220725ba9d7c">25ba9d7c</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud</td>
<td>Disabled</td>
<td>Block</td>
<td>
				We are changing the action for this rule from Disabled to BLOCK
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="158177dec2504acdba1f2da201a076eb">01a076eb</code>
</td>
<td>N/A</td>
<td>SSRF - Local - Beta</td>
<td>Disabled</td>
<td> - </td>
<td>
				This detection has been removed.
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-local-tracing"><a href="/changelog/post/2026-08-04-local-tracing/">AI agents can debug Workers with local tracing</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><code>wrangler dev</code> and <code>vite dev</code> automatically capture structured OpenTelemetry traces and correlated console logs during local Worker invocations.</p>
<h4 id="2026-08-04-local-tracing-debug-with-ai-agents">Debug with AI agents</h4>
<p>When the tooling detects an AI agent session, it prints a terminal hint pointing to the <a href="/workers/local-development/local-explorer/#api">Local Explorer API</a> at <code>/cdn-cgi/local/explorer/api</code>. The API serves an OpenAPI schema and exposes a read-only observability query endpoint for discovering telemetry, querying traces and logs, and inspecting binding state.</p>
<p>The agent can identify the exact failing operation, fix the code, rerun the request, and verify the result. This debug loop requires no deployment or temporary logs.</p>
<h4 id="2026-08-04-local-tracing-inspect-traces-in-local-explorer">Inspect traces in Local Explorer</h4>
<p>Humans can inspect the same <a href="/workers/observability/traces/">traces</a> and correlated console logs in the Local Explorer browser UI. Each trace shows spans, timing, attributes, and errors.</p>
<p><img src="/assets/upstream/images/workers/observability/local-trace-failed-request.png" alt="Local Explorer showing a failed Worker trace with spans, timing, and errors" /></p>
<p>Automatic spans cover handler calls, outbound <code>fetch()</code> calls, and binding calls. Custom spans appear alongside these automatic spans.</p>
<p>For more details, refer to the <a href="/workers/local-development/local-explorer/">Local Explorer documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-nodejs-compat-default"><a href="/changelog/post/2026-08-04-nodejs-compat-default/">Node.js compatibility is now enabled by default</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers now enable the <code>nodejs_compat</code> and <code>nodejs_compat_v2</code> compatibility
flags by default for <a href="/workers/configuration/compatibility-dates/">compatibility dates</a>
of <code>2026-08-04</code> or later. These flags are not used for these compatibility
dates because the compatibility date enables the same behavior.</p>
<p>This means all <a href="/workers/runtime-apis/nodejs/">Node.js built-in APIs</a> supported
by the Workers runtime are available by default, including <code>node:crypto</code>,
<code>node:buffer</code>, <code>node:stream</code>, <code>node:net</code>, <code>node:dns</code>, <code>node:fs</code>, <code>node:http</code>,
and more. npm packages that depend on these APIs will work without additional
configuration.</p>
<p>Workers using an earlier compatibility date are not affected. They can still
opt in by adding <code>nodejs_compat</code> to <code>compatibility_flags</code>.</p>
<p>New projects do not need to add either flag. Existing projects can update their
compatibility date without removing them. Wrangler, Miniflare, the Cloudflare
Vite plugin, and Vitest Pool Workers ignore these redundant flags when starting
the runtime.</p>
<p>To turn off Node.js compatibility completely, remove any <code>nodejs_compat</code> and
<code>nodejs_compat_v2</code> flags. Then add both of the following flags:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17813.md")</div>
<p>For more information, refer to the <a href="/workers/runtime-apis/nodejs/">Node.js compatibility documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-04">Aug 4, 2026</time><div>
<h2 id="post-2026-08-04-wrangler-login-device-flow"><a href="/changelog/post/2026-08-04-wrangler-login-device-flow/">Log in to Wrangler without a local callback server</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><code>wrangler login</code> now supports the <a href="https://www.rfc-editor.org/rfc/rfc8628">OAuth 2.0 Device Authorization Grant</a>. Pass <code>--device</code> to authenticate without starting a temporary callback server on <code>localhost:8976</code>:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler login --device&#10;</code></pre>
<p>Wrangler prints a verification URL and a short user code, opens the URL in your default browser with the code already filled in, and polls Cloudflare for an access token while you approve the request:</p>
<pre tabindex="0"><code class="language-sh"> ⛅️ wrangler 4.119.0&#10;────────────────────&#10;Attempting to login via OAuth Device Authorization Grant...&#10;To authorize Wrangler, please visit:&#10;&#10;  https://dash.cloudflare.com/oauth2/device&#10;&#10;and enter the code:&#10;&#10;  jPqK6Qvs&#10;&#10;You have 5 minutes to approve this request.&#10;&#10;Opening a link in your default browser: https://dash.cloudflare.com/oauth2/device?user_code=jPqK6Qvs&#10;Successfully logged in.&#10;</code></pre>
<p>The default login flow needs your browser to reach <code>localhost:8976</code>, which is not always possible from containers, remote SSH sessions, or GitHub Codespaces. Previously these environments required forwarding ports or fetching the callback URL with <code>curl</code> from a second terminal session. Because <code>--device</code> has no callback server, those workarounds are no longer necessary.</p>
<p>Since the plain verification URL and user code are both printed to the terminal, you can also approve the request from a phone or another machine. Pass <code>--browser=false</code> to stop Wrangler from opening a browser at all.</p>
<p>Available in Wrangler version 4.119.0 or later. For more information, refer to <a href="/workers/wrangler/commands/general/#login"><code>wrangler login</code></a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-03">Aug 3, 2026</time><div>
<h2 id="post-2026-08-03-eager-redirect-cookie-setting"><a href="/changelog/post/2026-08-03-eager-redirect-cookie-setting/">Control authorization cookies for multi-domain Access applications</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access administrators can now control whether a self-hosted application preemptively sets authorization cookies across its public hostnames.</p>
<p>Previously, Access automatically used eager redirects for applications with five or fewer hostnames. Applications with more than five hostnames received cookies as users visited each hostname. Administrators can now choose either behavior, regardless of the number of hostnames.</p>
<p>The new <strong>Eager redirect cookie</strong> setting is turned on by default for new applications. After a user signs in, Access redirects the browser through each hostname and sets a <code>CF_Authorization</code> cookie. This supports applications that need to make requests across hostnames before the user visits each one.</p>
<p>For applications with many hostnames, the redirect chain can cause sign-in loops in some browsers. Turn off the setting to issue the cookie only when a user visits each hostname.</p>
<p>To configure the setting, refer to <a href="/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/#eager-redirect-cookie">Authorization cookie</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-03">Aug 3, 2026</time><div>
<h2 id="post-2026-08-03-cloudflare-computer"><a href="/changelog/post/2026-08-03-cloudflare-computer/">Preview: @cloudflare/computer agent runtime</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>We're releasing an early preview of <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code></a>, an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.</p>
<p><code>@cloudflare/computer</code> provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.</p>
<p>Install the package via npm:</p>
<pre tabindex="0"><code class="language-sh">npm install @cloudflare/computer&#10;</code></pre>
<p>Instantiate a <code>Workspace</code> inside any Durable Object to give your agent a filesystem and execution runtime:</p>
<pre tabindex="0"><code class="language-ts">import { Workspace } from &quot;@cloudflare/computer&quot;;&#10;&#10;export class Agent {&#10;	workspace = new Workspace({&#10;		storage: this.ctx.storage,&#10;	});&#10;}&#10;</code></pre>
<p>Several execution backends are included or you can write your own:</p>
<ul>
<li><strong>Isolate runtime</strong> — fast, horizontally scalable execution via <code>just-bash</code> and Dynamic Workers, ideal for file manipulation and data processing.</li>
<li><strong>Container runtime</strong> — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.</li>
</ul>
<p>The AI SDK-compatible toolkit provides common agent tools (<code>read</code>, <code>write</code>, <code>edit</code>, <code>ls</code>, <code>exec</code>) and guides the model to choose the appropriate backend for each task.</p>
<p>For more examples, including a step-by-step tutorial, visit the <a href="https://github.com/cloudflare/computer"><code>@cloudflare/computer</code> repository</a>.</p>
<p>Read the announcement blog post for more details: <a href="https://blog.cloudflare.com/cloudflare-computer/">Your agent needs a computer, not a container</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-03">Aug 3, 2026</time><div>
<h2 id="post-2026-08-03-fallback-pool-analytics"><a href="/changelog/post/2026-08-03-fallback-pool-analytics/">See fallback pool traffic separately in load balancing analytics</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>Load balancing analytics now shows traffic served by your <a href="/load-balancing/understand-basics/health-details/#fallback-pools">fallback pool</a> separately from traffic routed to the same pool by normal steering.</p>
<p>Previously, requests were grouped by pool name alone. If the pool acting as your fallback also received traffic through your steering policy, both appeared as a single series, so it was not obvious from the graph whether Cloudflare was still making health-based routing decisions or had fallen back to the pool of last resort. Because the fallback pool ignores health, that distinction matters when you are diagnosing an outage or reviewing how much traffic was shed.</p>
<p>Fallback traffic is now labeled with the pool name followed by <code>(Fallback)</code>. A pool named <code>eu-west</code>, for example, is shown as <code>eu-west (Fallback)</code>. This label appears as its own entry in:</p>
<ul>
<li><strong>Requests over time</strong>, as a separate series in the chart.</li>
<li><strong>Pool distribution</strong>, as a separate segment.</li>
<li><strong>Top endpoints</strong>, as a separate card for the pool.</li>
</ul>
<p>The <strong>Latency</strong> view and the health event <strong>Logs</strong> are unchanged.</p>
<p>To see this, go to <strong>Traffic</strong> &gt; <strong>Load Balancing Analytics</strong> for a zone. The same breakdown appears in the analytics view for an individual load balancer under <strong>Load Balancing</strong> at the account level.</p>
<p>Refer to <a href="/load-balancing/reference/load-balancing-analytics/">load balancing analytics</a> to learn more.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-03">Aug 3, 2026</time><div>
<h2 id="post-2026-08-03-pipelines-billing-enabled"><a href="/changelog/post/2026-08-03-pipelines-billing-enabled/">Billing is now enabled for Pipelines</a></h2>
<div class="changelog-badges"><span>pipelines</span></div><div class="changelog-body"><p>Billing is now enabled for <a href="/pipelines/">Cloudflare Pipelines</a> on non-enterprise accounts. Pipelines usage beyond the included free tier will appear on your next invoice.</p>
<p>Pipelines charges based on two usage dimensions. Ingress into a Pipeline stream remains free regardless of volume:</p>
<ul>
<li><strong>SQL transforms</strong>: $0.04 / GB for stateless transforms (filter, reshape, unnest, cast, compute).</li>
<li><strong>Sinks (egress)</strong>: $0.03 / GB for JSON output, $0.06 / GB for Parquet or Iceberg output.</li>
</ul>
<p>Workers Paid plans include 50 GB / month for both SQL transforms and sinks. Standard <a href="/r2/pricing/">R2 storage and operations</a> charges apply for data written to R2 buckets, and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges apply when writing to Iceberg tables.</p>
<p>For example, a pipeline that ingests 500 GB of event data per month, uses a SQL transform to filter and reshape it, and writes 300 GB to an R2 Data Catalog Iceberg table would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Streams</td>
<td>500 GB</td>
<td>Unlimited</td>
<td>0 GB</td>
<td>$0.00</td>
</tr>
<tr>
<td>SQL transforms</td>
<td>500 GB</td>
<td>50 GB</td>
<td>450 GB</td>
<td>$18.00</td>
</tr>
<tr>
<td>Sinks (Iceberg)</td>
<td>300 GB</td>
<td>50 GB</td>
<td>250 GB</td>
<td>$15.00</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$33.00</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/pipelines/platform/pricing/">Pipelines pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-03">Aug 3, 2026</time><div>
<h2 id="post-2026-08-03-r2-data-catalog-billing-enabled"><a href="/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/">Billing is now enabled for R2 Data Catalog</a></h2>
<div class="changelog-badges"><span>r2</span><span>r2-data-catalog</span></div><div class="changelog-body"><p>Billing is now enabled for <a href="/r2-data-catalog/">R2 Data Catalog</a> on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 Data Catalog charges based on two dimensions, in addition to standard <a href="/r2/pricing/">R2 storage and operations</a>:</p>
<ul>
<li><strong>Catalog operations</strong>: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.</li>
<li><strong>Compaction</strong>: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when <a href="/r2-data-catalog/table-maintenance/">automatic compaction</a> is turned on for a table.</li>
</ul>
<p>Each dimension includes a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.</p>
<p>For example, a single Iceberg table with 50 GB of data, 500,000 catalog operations per month, and compaction turned on that processes 20 GB across 200,000 files would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>Catalog operations</td>
<td>500,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td>Compaction (data processed)</td>
<td>20 GB</td>
<td>10 GB</td>
<td>10 GB</td>
<td>$0.05</td>
</tr>
<tr>
<td>Compaction (objects)</td>
<td>200,000</td>
<td>1,000,000</td>
<td>0</td>
<td>$0.00</td>
</tr>
<tr>
<td><strong>Total (Data Catalog)</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$0.05</strong></td>
</tr>
</tbody>
</table>
<p>Standard R2 storage charges ($0.015 / GB-month) apply separately for the 50 GB of data stored.</p>
<p>For full pricing details and billing examples, refer to <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-03">Aug 3, 2026</time><div>
<h2 id="post-2026-08-03-r2-sql-billing-enabled"><a href="/changelog/post/2026-08-03-r2-sql-billing-enabled/">Billing is now enabled for R2 SQL</a></h2>
<div class="changelog-badges"><span>r2-sql</span></div><div class="changelog-body"><p>Billing is now enabled for <a href="/r2-sql/">R2 SQL</a> on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.</p>
<p>R2 SQL charges based on a single dimension:</p>
<ul>
<li><strong>Data scanned</strong>: $0.0025 / GB ($2.50 / TB) of compressed data read from R2 to execute your query.</li>
</ul>
<p>All plans include 10 GB of data scanned per month. Each query is billed for a minimum of 10 MB of data scanned. R2 SQL pricing is additive to standard <a href="/r2/pricing/">R2 storage and operations</a> and <a href="/r2-data-catalog/platform/pricing/">R2 Data Catalog</a> charges. R2 does not charge for egress, so there is no additional data transfer cost.</p>
<p>For example, a user who stores 500 GB of Parquet data in R2 Data Catalog and runs queries that scan a total of 50 GB of compressed data during the month would be billed as follows:</p>
<table>
<thead>
<tr>
<th>Dimension</th>
<th>Usage</th>
<th>Included</th>
<th>Billable</th>
<th>Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td>R2 storage</td>
<td>500 GB-month</td>
<td>10 GB-month</td>
<td>490 GB-month</td>
<td>$7.35</td>
</tr>
<tr>
<td>R2 SQL (data scanned)</td>
<td>50 GB</td>
<td>10 GB</td>
<td>40 GB</td>
<td>$0.10</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td></td>
<td><strong>$7.45</strong></td>
</tr>
</tbody>
</table>
<p>For full pricing details and billing examples, refer to <a href="/r2-sql/platform/pricing/">R2 SQL pricing</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-08-03">Aug 3, 2026</time><div>
<h2 id="post-2026-08-03-python-javascript-rpc"><a href="/changelog/post/2026-08-03-python-javascript-rpc/">Python and JavaScript Workers can now call each other via RPC</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>You can now call methods between Python and JavaScript Workers using <a href="/workers/runtime-apis/rpc/">Workers RPC</a>. This works through <a href="/workers/runtime-apis/bindings/service-bindings/rpc/">Service bindings</a> without extra dependencies, schema definitions, or serialization code.</p>
<p>Cross-language RPC calls behave like ordinary function calls. Exceptions propagate to the call site. You can pass <a href="https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm#supported_types">structured cloneable types</a> as parameters or return values, and Pyodide Foreign Function Interface (FFI) automatically converts types between languages.</p>
<h4 id="2026-08-03-python-javascript-rpc-call-a-typescript-worker-from-python">Call a TypeScript Worker from Python</h4>
<p>Define a method in a TypeScript Worker:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17809.md")</div>
<p>Call it from a Python Worker through a Service binding:</p>
<pre tabindex="0"><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def fetch(self, request):&#10;		rpc = self.env.RPC&#10;		result = await rpc.add(42, 144)&#10;		return Response.json({&quot;result&quot;: result})&#10;</code></pre>
<p>Configure the Service binding in the Python Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17810.md")</div>
<h4 id="2026-08-03-python-javascript-rpc-call-a-python-worker-from-javascript">Call a Python Worker from JavaScript</h4>
<p>Define a method in a Python Worker:</p>
<pre tabindex="0"><code class="language-python">from workers import WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;	async def highlight_code(self, code: str, language: str) -&gt; dict:&#10;		from pygments.formatters import HtmlFormatter&#10;		from pygments import highlight&#10;		from pygments.lexers import get_lexer_by_name&#10;&#10;		lexer = get_lexer_by_name(language, stripall=True)&#10;		formatter = HtmlFormatter(linenos=True, cssclass=&quot;highlight&quot;, style=&quot;monokai&quot;)&#10;		highlighted_html = highlight(code, lexer, formatter)&#10;		css = formatter.get_style_defs(&quot;.highlight&quot;)&#10;&#10;		return {&#10;			&quot;html&quot;: highlighted_html,&#10;			&quot;css&quot;: css&#10;		}&#10;</code></pre>
<p>Call it from a JavaScript Worker through a Service binding:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17811.md")</div>
<p>Configure the Service binding in the JavaScript Worker's Wrangler configuration:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17812.md")</div>
<p>For more details on the announcement, read the <a href="https://blog.cloudflare.com/python-workers-rpc/">blog post</a>.</p>
<p>For more information, refer to the <a href="/workers/runtime-apis/rpc/">Workers RPC documentation</a> and the <a href="/workers/languages/python/">Python Workers overview</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-31">Jul 31, 2026</time><div>
<h2 id="post-2026-07-31-mcp-portal-manual-oauth"><a href="/changelog/post/2026-07-31-mcp-portal-manual-oauth/">Static OAuth client credentials for MCP server portals</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.</p>
<p>When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the <code>client_secret_post</code> and <code>client_secret_basic</code> token endpoint authentication methods.</p>
<p>Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.</p>
<p>For setup instructions, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials">Configure manual OAuth credentials</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-31">Jul 31, 2026</time><div>
<h2 id="post-2026-07-31-br-dashboard-playground"><a href="/changelog/post/2026-07-31-br-dashboard-playground/">Browser Run adds a Playground to the Cloudflare dashboard</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> now includes a Playground in the Cloudflare dashboard. Use it to try Quick Actions against a live browser without creating a Worker, installing an SDK, or deploying code first.</p>
<p>The Playground helps you test a target URL or raw HTML input, tune viewport and page-load settings, preview the output, and copy working code for the same request.</p>
<p><img src="/images/browser-run/playground.png" alt="Browser Run Playground in the Cloudflare dashboard showing a generated screenshot preview and output settings" /></p>
<p>With the Playground, you can:</p>
<ul>
<li>Capture visuals as <a href="/browser-run/quick-actions/screenshot-endpoint/">screenshots</a> or <a href="/browser-run/quick-actions/pdf-endpoint/">PDFs</a>.</li>
<li>Generate multiple output formats in one request with the <a href="/browser-run/quick-actions/snapshot/">snapshot endpoint</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/content-endpoint/">HTML</a>, <a href="/browser-run/quick-actions/markdown-endpoint/">Markdown</a>, <a href="/browser-run/quick-actions/links-endpoint/">links</a>, or <a href="/browser-run/quick-actions/scrape-endpoint/">scraped data</a>.</li>
<li>Extract <a href="/browser-run/quick-actions/json-endpoint/">structured data with AI</a> using a prompt and optional JSON Schema.</li>
</ul>
<p>You can also configure desktop, laptop, tablet, mobile, or custom viewport sizes, set browser scale, choose page-load conditions, set timeouts, and wait for selectors before running a request.</p>
<p>Select <strong>Show Code</strong> to generate the same request as cURL, TypeScript SDK, Python, or Workers Binding code. For example, a screenshot request can be copied as a Workers Binding call:</p>
<pre tabindex="0"><code class="language-ts">interface Env {&#10;	BROWSER: BrowserRun;&#10;}&#10;&#10;export default {&#10;	async fetch(request, env): Promise&lt;Response&gt; {&#10;		return await env.BROWSER.quickAction(&quot;screenshot&quot;, {&#10;			url: &quot;https://developers.cloudflare.com&quot;,&#10;			viewport: {&#10;				width: 1920,&#10;				height: 1080,&#10;			},&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<p>Requests made in the Playground incur <a href="/browser-run/pricing/">Browser Run charges</a>. AI extraction also incurs Workers AI charges.</p>
<p>To try the Playground, go to <strong>Browser Run</strong> in the Cloudflare dashboard and select <strong>Playground</strong>.</p>
<div class="nb-dash-button"></div>
<p>For more information, refer to the <a href="/browser-run/quick-actions/">Quick Actions documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-31">Jul 31, 2026</time><div>
<h2 id="post-2026-07-30-rotate-stream-broadcast-keys"><a href="/changelog/post/2026-07-30-rotate-stream-broadcast-keys/">Rotate Stream broadcast keys for live inputs</a></h2>
<div class="changelog-badges"><span>stream</span></div><div class="changelog-body"><p>You can now rotate the broadcast credentials for a Stream live input without changing the live input identifier.</p>
<p>Use key rotation when live input credentials may have been shared with the wrong audience, exposed in client code or a screenshare, or need to be refreshed as part of your security process. Rotating keys revokes the old credentials, disconnects broadcasts using stale credentials, and returns refreshed credentials in the API response.</p>
<p>To rotate keys for a live input, make a <code>POST</code> request to the <code>rotate_keys</code> endpoint:</p>
<pre tabindex="0"><code class="language-bash">curl --request POST \&#10;https://api.cloudflare.com/client/v4/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/rotate_keys \&#10;&#45;-header &quot;Authorization: Bearer &lt;API_TOKEN&gt;&quot;&#10;</code></pre>
<p>Live input responses now also include <code>keysRotatedAt</code>, which indicates when the live input keys were last rotated. This field is omitted for live inputs whose keys have never been rotated.</p>
<p>For endpoint details, refer to <a href="/api/resources/stream/subresources/live_inputs/methods/rotate_keys/">Rotate keys for a live input</a>. For usage guidance, refer to <a href="/stream/stream-live/start-stream-live/#manage-live-inputs">Manage live inputs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-31">Jul 31, 2026</time><div>
<h2 id="post-2026-07-31-wrangler-startup-profile-summary"><a href="/changelog/post/2026-07-31-wrangler-startup-profile-summary/">Inspect Worker startup performance with Wrangler</a></h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p><code>wrangler check startup</code> now reports your Worker's raw and compressed bundle sizes. It also summarizes local CPU activity during startup directly in your terminal.</p>
<p>Large bundles and costly startup work can introduce cold-start latency, so use this command to find code and large dependencies that slow your Worker before it handles requests.</p>
<p>The summary includes sampled, active, garbage collection, and idle time. Wrangler continues to save a <code>.cpuprofile</code> file for detailed flamegraph analysis in Chrome DevTools or VS Code.</p>
<pre tabindex="0"><code class="language-bash">⛅️ wrangler 4.116.0&#10;───────────────────────────────────────────────&#10;├ Building your Worker&#10;│ Worker Built! 🎉&#10;│&#10;├ Analysing&#10;│ Startup phase analysed&#10;│&#10;│ Bundle: 7171.25 KiB / gzip: 2197.00 KiB&#10;│&#10;│ Local startup profile:&#10;│   Profile window: 70.3 ms&#10;│   Sampled time: 70.3 ms&#10;│   Active: 38.5 ms (including 3.7 ms garbage collection)&#10;│   Idle: 31.8 ms&#10;│   Samples: 36&#10;│&#10;│ CPU Profile has been written to worker-startup.cpuprofile. Load it into the Chrome DevTools profiler (or directly in VSCode) to view a flamegraph.&#10;│&#10;│ Note that the CPU Profile was measured on your Worker running locally on your machine, which has a different CPU than when your Worker runs on Cloudflare.&#10;│&#10;│ As such, CPU Profile can be used to understand where time is spent at startup, but the overall startup time in the profile should not be expected to exactly match what your Worker&#x27;s startup time will be when deploying to Cloudflare.&#10;</code></pre>
<p>The profile runs locally, so its duration will differ from startup time on Cloudflare. For authoritative startup time, deploy your Worker or upload a version.</p>
<p>Available in Wrangler version 4.116.0 or later. For more information, refer to <a href="/workers/wrangler/commands/workers/#startup"><code>wrangler check startup</code></a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/5/">Previous</a><span>Page 6 of 50</span><a class="pagination-next" rel="next" href="/changelog/7/">Next</a></nav>
</div>
