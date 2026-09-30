---
cp9:
  canonical: https://developers.cloudflare.com/changelog/7/
  description: New updates and improvements at Cloudflare.
  full_title: Changelog - page 7 | Cloudflare Docs
  head_html: <title>Changelog - page 7 | Cloudflare Docs</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/7/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="Changelog - page 7"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/7/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/changelog/7/#page","headline":"Changelog - page 7 | Cloudflare Docs","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/7/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/7/
  schema: 1
---
<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2026-07-31">Jul 31, 2026</time><div>
<h2 id="post-2026-07-31-warp-macos-beta"><a href="/changelog/post/2026-07-31-warp-macos-beta/">Cloudflare One Client for macOS (version 2026.7.1210.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.</li>
<li>Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.</li>
<li>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search domain</a> parsing failure no longer prevents connection.</li>
<li>Fixed a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a> issue where the tunnel could stall while uploading at a high rate.</li>
<li>Fixed being unable to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch organizations</a> when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed the Home Screen dropdown popup not anchoring correctly.</li>
<li>Fixed a crash during dialog dismissal.</li>
<li>Increased tolerance for configurations with a large number of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.</li>
<li>Fixed the WARP client stealing window focus (for example, during reauth).</li>
<li>Fixed a client crash when connecting to a captive portal over Wi-Fi.</li>
<li>Fixed the system tray icon showing &quot;disconnected&quot; while the UI showed &quot;connected&quot;.</li>
<li>A successful re-authentication will cause the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to be re-evaluated.</li>
<li>Improved <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">dashboard-managed client updates</a> by running the updater only when needed.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-31">Jul 31, 2026</time><div>
<h2 id="post-2026-07-31-warp-windows-beta"><a href="/changelog/post/2026-07-31-warp-windows-beta/">Cloudflare One Client for Windows (version 2026.7.1210.1)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new Beta release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/">beta releases downloads page</a>.</p>
<p>This beta release includes the following changes and improvements:</p>
<ul>
<li>Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.</li>
<li>Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.</li>
<li>A <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes">DNS search domain</a> parsing failure no longer prevents connection.</li>
<li>Fixed a <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol">MASQUE</a> issue where the tunnel could stall while uploading at a high rate.</li>
<li>Fixed being unable to <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/">switch organizations</a> when the client was stuck in the &quot;Device not in organization&quot; state.</li>
<li>Fixed the Home Screen dropdown popup not anchoring correctly.</li>
<li>Fixed a crash during dialog dismissal.</li>
<li>Increased tolerance for configurations with a large number of <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/">local domain fallback</a> resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.</li>
<li>Fixed a networking issue where IPv6 multicast routes were being assigned to the WARP tunnel interface.</li>
<li>Fixed fatal errors on UI load on Windows 10.</li>
<li>Fixed a crash during Windows notification initialization.</li>
<li>Made the Windows <a href="/cloudflare-one/reusable-components/posture-checks/client-checks/domain-joined/">domain-joined posture check</a> more reliable.</li>
<li>Fixed orphaned credentials left behind on multi-user uninstall.</li>
<li>A successful re-authentication will cause the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/">device profile</a> to be re-evaluated.</li>
<li>Improved <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/">dashboard-managed client updates</a> by running the updater only when needed.</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-30">Jul 30, 2026</time><div>
<h2 id="post-2026-07-30-mcp-portal-code-mode-policies"><a href="/changelog/post/2026-07-30-mcp-portal-code-mode-policies/">Admins can turn on Code Mode by default for MCP portal users</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/">MCP server portals</a> now support four Code Mode policies: <em>Off</em>, <em>Opt-in</em>, <em>On by default</em>, and <em>Enforced</em>. Admins can choose whether Code Mode is unavailable, optional, enabled by default, or required for every session.</p>
<p>Existing portals retain their current behavior. Portals that previously allowed Code Mode use <em>Opt-in</em>, while portals that did not allow Code Mode use <em>Off</em>. New portals also use <em>Opt-in</em> by default.</p>
<p>Clients turn on Code Mode for an <em>Opt-in</em> portal with <code>?codemode=search_and_execute</code>. The <em>On by default</em> policy lets clients opt out with <code>?codemode=off</code>, which avoids nested code execution when a client runs its own Code Mode implementation. The <em>Off</em> and <em>Enforced</em> policies ignore client overrides.</p>
<p>The Cloudflare API exposes these policies through the <code>code_mode</code> field:</p>
<pre tabindex="0"><code class="language-json">{&#10;	&quot;code_mode&quot;: &quot;default_on&quot;&#10;}&#10;</code></pre>
<p>The supported values are <code>off</code>, <code>opt_in</code>, <code>default_on</code>, and <code>enforced</code>. The previous <code>allow_code_mode</code> boolean is deprecated.</p>
<p>For configuration details and client behavior, refer to <a href="/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode-policies">Code Mode policies</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-30">Jul 30, 2026</time><div>
<h2 id="post-2026-07-30-ai-search-agent-sdks"><a href="/changelog/post/2026-07-30-ai-search-agent-sdks/">Use AI Search with the Agents SDK, AI SDK, and LangChain</a></h2>
<div class="changelog-badges"><span>ai-search</span></div><div class="changelog-body"><p>You can now use <a href="/ai-search/">AI Search</a> directly from popular agent frameworks, adding grounded retrieval to an existing app instead of calling the REST API by hand. The new <a href="/ai-search/agent-sdks/">Agents</a> section has guides for the <a href="/ai-search/agent-sdks/ai-sdk/">Vercel AI SDK</a>, <a href="/ai-search/agent-sdks/langchain/">LangChain</a>, and the <a href="/ai-search/agent-sdks/agents-sdk/">Cloudflare Agents SDK</a>. The AI SDK integration is a new package, and the LangChain integration is a new retriever in the existing <code>langchain-cloudflare</code> package.</p>
<h4 id="2026-07-30-ai-search-agent-sdks-vercel-ai-sdk">Vercel AI SDK</h4>
<p>The <a href="https://www.npmjs.com/package/ai-search-provider"><code>ai-search-provider</code></a> package connects AI Search to the AI SDK, and targets AI SDK v6 (<code>ai@^6</code>). Pass <code>instance.chat()</code> to <code>generateText</code> or <code>streamText</code> to generate a response grounded in your indexed content, with the retrieved chunks returned as <code>sources</code>. You can also expose <code>instance.search()</code> as a tool for agent loops.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17688.md")</div>
<h4 id="2026-07-30-ai-search-agent-sdks-langchain">LangChain</h4>
<p>The <code>langchain-cloudflare</code> package (<a href="https://pypi.org/project/langchain-cloudflare/">PyPI</a>, <a href="https://github.com/cloudflare/langchain-cloudflare">GitHub</a>) provides <code>CloudflareAISearchRetriever</code>, a standard LangChain retriever backed by AI Search. Use it on its own, wrap it with <code>create_retriever_tool</code> to give an agent a search tool, or drop it into a RAG chain. It works with REST credentials or a Worker binding inside a Python Worker.</p>
<pre tabindex="0"><code class="language-python">from langchain_cloudflare import CloudflareAISearchRetriever&#10;&#10;retriever = CloudflareAISearchRetriever(&#10;    account_id=ACCOUNT_ID,&#10;    api_token=API_TOKEN,&#10;    instance_name=&quot;knowledge-base&quot;,&#10;    retrieval_type=&quot;hybrid&quot;,&#10;)&#10;&#10;docs = retriever.invoke(&quot;How do I configure Workers AI?&quot;)&#10;</code></pre>
<h4 id="2026-07-30-ai-search-agent-sdks-cloudflare-agents-sdk">Cloudflare Agents SDK</h4>
<p>The <a href="/agents/">Cloudflare Agents SDK</a> could already reach AI Search through the Workers binding. The new <a href="/ai-search/agent-sdks/agents-sdk/">guide</a> walks through building a stateful chat agent that provisions its own instance, indexes content, and searches it from a tool.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17689.md")</div>
<p>For the full walkthroughs, including creating an instance and indexing content, refer to the <a href="/ai-search/agent-sdks/">Agents</a> guides.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-30">Jul 30, 2026</time><div>
<h2 id="post-2026-07-30-workers-builds-nodejs-24"><a href="/changelog/post/2026-07-30-workers-builds-nodejs-24/">Node.js 24 is now the default for Workers Builds</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers Builds now uses Node.js 24.18.0 by default. The build image preinstalls Node.js 22.23.2 and 24.18.0.</p>
<p>You can continue to override the default with the <code>NODE_VERSION</code> environment variable, an <code>.nvmrc</code> file, or a <code>.node-version</code> file. For more information, refer to <a href="/workers/ci-cd/builds/build-image/#overriding-default-versions">Override default versions</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-29">Jul 29, 2026</time><div>
<h2 id="post-2026-07-29-waf-release"><a href="/changelog/post/2026-07-29-waf-release/">WAF Release - 2026-07-29</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p>This release introduces new rules and updates existing threat signatures to provide targeted protections for vulnerabilities in Nuxt Server Island components and Alibaba Fastjson deserialization routines, alongside enhanced protections for cloud metadata Server-Side Request Forgery (SSRF) and obfuscated command injection attempts.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Nuxt Server Island - RCE(GHSA-9473-5f9j-94wq): An unauthenticated vulnerability in Nuxt Server Islands where remote attackers can supply arbitrary component names or props to endpoints. Manipulating these parameters allows unauthenticated component Remote Code Execution (RCE) on the server.</p>
</li>
<li>
<p>Alibaba Fastjson JSONType Remote Code Execution: A unauthenticated remote code execution vulnerability in Alibaba Fastjson (≤ 1.2.83) during JSON deserialization. Under default configurations, attackers can execute arbitrary system commands, bypassing traditional classpath and gadget-based defenses.</p>
</li>
<li>
<p>Generic Protections (SSRF &amp; Command Injection): Added improved detection logic targeting Server-Side Request Forgery (SSRF) in cloud-hosted applications, alongside new rules targeting obfuscated command injection patterns across request parameters.</p>
</li>
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
				<code class="nb-rule-id" title="54e1733b10da4a599e06c6fbc2e84e2d">c2e84e2d</code>
</td>
<td>N/A</td>
<td>SSRF - Cloud - Beta</td>
<td>Log</td>
<td>Block</td>
<td>
				This is an improved detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="95a84ab1645a49c685648c17761e7a4c">761e7a4c</code>
</td>
<td>N/A</td>
<td>Command Injection - Obfuscation</td>
<td>Log</td>
<td>Block</td>            
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="58df9693db4d454a8764fcda7347c892">7347c892</code>
</td>
<td>N/A</td>
<td>Alibaba Fastjson JSONType Remote Code Execution - Body</td>
<td>Log</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="6159ead63d284147943dc5a18ec012ea">8ec012ea</code>
</td>
<td>N/A</td>
<td>Nuxt Server Island - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.This was labeled as Generic Rules - RCE.
</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="dcf635ab2e744e1a994443973590a4ad">3590a4ad</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
				<code class="nb-rule-id" title="d3852d0891634686a46114069c6dff1c">9c6dff1c</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
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
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="6ad9f2049b094c608be0f8adcfe1a93c">cfe1a93c</code>
</td>
<td>N/A</td>
<td>Generic Rules - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>	
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="5bdf578fff504b8cbe3b7f699ab5ed95">9ab5ed95</code>
</td>
<td>N/A</td>
<td>Generic Rules - XSS</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
<tr>
<td>Cloudflare Free Ruleset</td>
<td>
				<code class="nb-rule-id" title="7ecac499d14a4750aa58c1e21b7f9c67">1b7f9c67</code>
</td>
<td>N/A</td>
<td>File Upload - RCE</td>
<td>N/A</td>
<td>Block</td>
<td>
				This is a new detection.
</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-28">Jul 28, 2026</time><div>
<h2 id="post-2026-07-28-improved-record-display-format"><a href="/changelog/post/2026-07-28-improved-record-display-format/">Improved DoH JSON formatting for additional record types</a></h2>
<div class="changelog-badges"><span>1.1.1.1</span></div><div class="changelog-body"><p>Cloudflare is rolling out updated formatting for the <code>data</code> field in the 1.1.1.1 <a href="/1.1.1.1/encryption/dns-over-https/make-api-requests/dns-json/">DoH JSON API</a> (<code>application/dns-json</code>). During the roll out responses may use either the old or new format.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17613.md")</aside>
<h4 id="2026-07-28-improved-record-display-format-human-readable-display-for-additional-record-types">Human-readable display for additional record types</h4>
<p>Several record types previously returned their <code>data</code> field in <a href="https://datatracker.ietf.org/doc/html/rfc3597">RFC 3597</a> generic hex encoding (<code>\# &lt;length&gt; &lt;hex&gt;</code>). These now use standard presentation format:</p>
<pre tabindex="0"><code class="language-txt">CAA:        0 issue &quot;letsencrypt.org&quot;&#10;NAPTR:      100 10 &quot;s&quot; &quot;SIP+D2U&quot; &quot;&quot; _sip._udp.example.com.&#10;RP:         admin.example.com. txt.example.com.&#10;IPSECKEY:   10 1 2 192.0.2.1 AwEA...&#10;SVCB:       1 target.example.com. alpn=h2&#10;HTTPS:      1 . alpn=h3,h2 ipv4hint=192.0.2.1&#10;TLSA:       3 1 1 aabbccdd...&#10;SSHFP:      1 2 aabbccdd...&#10;OPENPGPKEY: AwEA...&#10;</code></pre>
<h4 id="2026-07-28-improved-record-display-format-numeric-dnssec-algorithm-identifiers">Numeric DNSSEC algorithm identifiers</h4>
<p>DNSSEC-related records now use numeric algorithm identifiers as defined in <a href="https://datatracker.ietf.org/doc/html/rfc4034">RFC 4034</a> instead of mnemonic names. This affects <code>RRSIG</code>, <code>DS</code>, <code>CDS</code>, <code>DNSKEY</code>, and <code>CDNSKEY</code> records. For example, <code>RSASHA256</code> becomes <code>8</code>, <code>ECDSAP256SHA256</code> becomes <code>13</code>, and <code>ED25519</code> becomes <code>15</code>. DS digest types also change from mnemonic to numeric: <code>SHA-256</code> becomes <code>2</code>.</p>
<pre tabindex="0"><code class="language-txt">RRSIG:  A RSASHA256 2 300 ...&#10;DS:     12345 RSASHA256 SHA-256 aabb...&#10;DNSKEY: 257 3 RSASHA256 AwEA...&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">RRSIG:  A 8 2 300 ...&#10;DS:     12345 8 2 aabb...&#10;DNSKEY: 257 3 8 AwEA...&#10;</code></pre>
<h4 id="2026-07-28-improved-record-display-format-other-formatting-changes">Other formatting changes</h4>
<p><code>HINFO</code> character-strings are now individually quoted to remove ambiguity when values contain spaces:</p>
<pre tabindex="0"><code class="language-txt">&quot;data&quot;: &quot;Intel Xeon Linux&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-txt">&quot;data&quot;: &quot;\&quot;Intel Xeon\&quot; \&quot;Linux\&quot;&quot;&#10;</code></pre>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-28">Jul 28, 2026</time><div>
<h2 id="post-2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28"><a href="/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/">Cloudflare MCP servers support the new MCP 2026-07-28 Specification</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Cloudflare's <a href="/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers">product-specific MCP servers</a> now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.</p>
<p>The <code>/mcp</code> endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.</p>
<p>Use <code>/mcp</code> for new connections. Historical <code>/sse</code> URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-28">Jul 28, 2026</time><div>
<h2 id="post-2026-07-28-human-in-the-loop"><a href="/changelog/post/2026-07-28-human-in-the-loop/">Browser Run adds structured handoff for Human in the Loop</a></h2>
<div class="changelog-badges"><span>browser-run</span></div><div class="changelog-body"><p><a href="/browser-run/">Browser Run</a> now supports structured handoff for <a href="/browser-run/features/human-in-the-loop/">Human in the Loop</a> workflows. Using Cloudflare-specific <a href="/browser-run/features/human-in-the-loop/#cloudflare-cdp-commands">CDP commands</a>, your agent can signal that it needs help, a human steps in through <a href="/browser-run/features/live-view/">Live View</a> to handle the task, and the agent resumes once the work is done.</p>
<p>For agents running multi-step browser workflows, a single login wall or unexpected prompt can fail the entire run. Previously, scripts had to manage human intervention manually by sharing a Live View URL and polling for completion. Structured handoff replaces this with a formal pause-and-resume flow.</p>
<p>The following example requests human intervention for a login page and waits for the human to finish before continuing:</p>
<pre tabindex="0"><code class="language-js">const cdp = await page.createCDPSession();&#10;&#10;// Get Live View URL for the human operator&#10;const { devtoolsFrontendUrl } = await cdp.send(&quot;Cloudflare.getLiveView&quot;, {&#10;	mode: &quot;tab&quot;,&#10;});&#10;console.log(`Human input needed: ${devtoolsFrontendUrl}`);&#10;&#10;// Request human intervention and wait for completion&#10;const handoffComplete = new Promise((resolve) =&gt; {&#10;	cdp.once(&quot;Cloudflare.handoffComplete&quot;, resolve);&#10;});&#10;&#10;await cdp.send(&quot;Cloudflare.handoff&quot;, {&#10;	instructions: &quot;Please log in with your credentials&quot;,&#10;	timeout: 600000,&#10;});&#10;&#10;const result = await handoffComplete;&#10;console.log(result.success ? &quot;Handoff complete&quot; : `Failed: ${result.reason}`);&#10;</code></pre>
<p>Refer to the <a href="/browser-run/features/human-in-the-loop/">Human in the Loop documentation</a> for the full API reference, examples, and best practices.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-28">Jul 28, 2026</time><div>
<h2 id="post-2026-07-28-gateway-maximum-dns-ttl"><a href="/changelog/post/2026-07-28-gateway-maximum-dns-ttl/">Control Cloudflare Gateway DNS caching with a maximum TTL setting</a></h2>
<div class="changelog-badges"><span>cloudflare-one</span><span>gateway</span></div><div class="changelog-body"><p>You can now set a maximum time-to-live (TTL) for DNS responses returned by Gateway. When an upstream DNS record has a TTL that exceeds the configured maximum, Gateway caps it to your specified value. This ensures that DNS policy changes - such as blocking a newly identified malicious domain - take effect faster across all clients.</p>
<p><img src="/assets/upstream/images/changelog/cloudflare-one/gateway-max-ttl-traffic-settings.png" alt="The maximum DNS TTL setting in Traffic policies &gt; Traffic settings, showing a numeric input field that accepts values between 60 and 36,000 seconds" /></p>
<p>The setting is available at two levels:</p>
<ul>
<li><strong>Account level</strong> - In <strong>Traffic Policies</strong> &gt; <strong>Traffic Settings</strong>, under <strong>Proxy and inspection</strong>. This sets the default cap for all DNS locations.</li>
<li><strong>Per-location</strong> - Each <a href="/cloudflare-one/networks/resolvers-proxies/">DNS location</a> can inherit the account setting, disable the cap, or override it with a custom value.</li>
</ul>
<p>Two new fields are also available in DNS logs: <code>upstream_record_ttls</code> (the original TTL from the upstream response) and <code>applied_max_ttl</code> (the cap Gateway applied). These appear in the DNS logs column picker and in Logpush datasets.</p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/dns-policies/maximum-dns-ttl/">Maximum DNS TTL</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-28">Jul 28, 2026</time><div>
<h2 id="post-2026-07-28-start-active-span"><a href="/changelog/post/2026-07-28-start-active-span/">Workers tracing — write custom spans with new startActiveSpan() and span.end() runtime APIs</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>The Workers runtime now provides built-in <code>tracing.startActiveSpan()</code> and <code>span.end()</code> APIs, allowing you to write custom spans for operations that last beyond a single callback — for example, instrumenting a stream pipeline where the span should stay open until the stream is fully consumed.</p>
<p>This augments the <a href="/changelog/post/2026-06-16-custom-spans/">existing API for writing custom spans</a>, <code>tracing.enterSpan()</code>, which automatically ends a span when its callback is returned. With <code>startActiveSpan()</code>, the span remains open after the callback returns, and you call <code>span.end()</code> when the work is complete:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17808.md")</div>
<p>For more details, refer to the <a href="/workers/observability/traces/custom-spans/">custom spans documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-28">Jul 28, 2026</time><div>
<h2 id="post-2026-07-28-models-require-workers-paid"><a href="/changelog/post/2026-07-28-models-require-workers-paid/">Select models now require the Workers Paid plan</a></h2>
<div class="changelog-badges"><span>workers-ai</span></div><div class="changelog-body"><p>We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer <code>429</code> and <code>3040</code> (Out of Capacity) errors.</p>
<p>The following models now require the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a>:</p>
<ul>
<li><a href="/workers-ai/models/kimi-k2.6/"><code>@cf/moonshotai/kimi-k2.6</code></a></li>
<li><a href="/workers-ai/models/kimi-k2.7-code/"><code>@cf/moonshotai/kimi-k2.7-code</code></a></li>
<li><a href="/workers-ai/models/glm-5.2/"><code>@cf/zai-org/glm-5.2</code></a></li>
</ul>
<p>On the Workers Free plan, requests to these models now return a <code>403</code> HTTP error (<a href="/workers-ai/platform/errors/">internal error <code>5035</code></a>) prompting you to upgrade. The Workers Paid plan starts at $5 per month and still includes the 10,000 free Neurons per day allocation, with usage beyond that billed at each <a href="/workers-ai/platform/pricing/">model's pricing</a>.</p>
<p>Many models remain available on the Workers Free plan, including:</p>
<ul>
<li><a href="/workers-ai/models/glm-4.7-flash/"><code>@cf/zai-org/glm-4.7-flash</code></a></li>
<li><a href="/workers-ai/models/gemma-4-26b-a4b-it/"><code>@cf/google/gemma-4-26b-a4b-it</code></a></li>
<li><a href="/workers-ai/models/nemotron-3-120b-a12b/"><code>@cf/nvidia/nemotron-3-120b-a12b</code></a></li>
</ul>
<p>For the full list, refer to the <a href="/workers-ai/models/">Workers AI model catalog</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-27">Jul 27, 2026</time><div>
<h2 id="post-2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2"><a href="/changelog/post/2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2/">Agents SDK adds MCP Specification 2026-07-28 support</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>Agents SDK v0.20.0 adds client and server support for the <a href="https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/">MCP 2026-07-28 release candidate</a>. Workers can serve tools, prompts, resources, and elicitation without an MCP transport session or Durable Object. Agents can connect to both MCP 2026-07-28 servers and existing legacy servers.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-client-support">Client support</h4>
<p>The MCP client manager now uses <code>@modelcontextprotocol/client</code>. For each connection, it probes for MCP 2026-07-28 support with <code>server/discover</code>. If the server does not support the stateless protocol, the client continues with the legacy <code>initialize</code> handshake on the same connection. Existing <code>addMcpServer</code> calls do not need a protocol-version setting or separate clients for each protocol generation.</p>
<p>For stateless requests, elicitation uses <code>input_required</code> through multi-round-trip requests (MRTR). The legacy path uses the same form and URL handlers for pushed requests. The SDK collects input, retries the original operation, and resolves the original <code>callTool</code>, <code>getPrompt</code>, or <code>readResource</code> promise with its final result.</p>
<p>OAuth callbacks now validate issuer metadata through the v2 SDK. Discovery state and issuer-bound credentials persist across browser redirects and Durable Object hibernation.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-run-stateless-servers">Run stateless servers</h4>
<p><code>createMcpHandler</code> now accepts a factory that returns a server from <code>@modelcontextprotocol/server</code>. The factory creates an isolated server for each request.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17681.md")</div>
<p>The isolated <code>agents/mcp/server</code> entry keeps <code>McpAgent</code>, <code>WorkerTransport</code>, MCP client transports, and SDK v1 modules out of stateless server bundles.</p>
<p>The Workers wrapper validates present browser Origins, supports explicit delegation to trusted Origin middleware, and exposes request handling plus typed change notifications.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-backward-compatibility">Backward compatibility</h4>
<p>The same <code>createMcpHandler(createServer)(request, env, ctx)</code> route serves MCP 2026-07-28 clients and legacy clients that use stateless requests. You do not need separate routes or tool definitions for ordinary tools, prompts, and resources.</p>
<p><code>McpAgent</code> is deprecated and feature-frozen. Migrate existing <code>McpAgent</code> servers to the stateless handler at your earliest convenience. If a server depends on protocol sessions, RPC, pushed server-to-client requests, standalone streams, or replay, use the <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">migration guide</a> to design stateless equivalents and run both routes while clients transition.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-migrate-existing-sdk-v1-servers">Migrate existing SDK v1 servers</h4>
<p>Upgrade the Agents SDK:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Move ordinary SDK v1 server definitions into an SDK v2 factory and serve them with <code>createMcpHandler</code>. The handler's default legacy compatibility means most stateless deployments need only one route.</p>
<p>If an existing <code>McpAgent</code> server still needs sessionful features, add the stateless path beside it. Use <code>isLegacyRequest()</code> to send only legacy traffic to the existing route:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17682.md")</div>
<p>Migrate the remaining sessionful features, allow existing sessions to drain, then remove the legacy route. Refer to <a href="/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/">Migrate to MCP SDK v2</a> for package changes, compatibility limits, and rollout steps.</p>
<h4 id="2026-07-27-agents-sdk-v0.20.0-mcp-sdk-v2-deprecations-in-v0-20-0">Deprecations in v0.20.0</h4>
<p>This release deprecates the following Agents SDK APIs:</p>
<table>
<thead>
<tr>
<th>Deprecated API</th>
<th>Replacement</th>
<th>Status</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>McpAgent</code></td>
<td>Use an SDK v2 factory with <code>createMcpHandler</code> for stateless servers. Use the migration guide to replace stateful features before removing a legacy route.</td>
<td>Feature-frozen. No removal version is announced.</td>
</tr>
<tr>
<td><code>createMcpHandler(v1Server, options)</code></td>
<td>Move the server to an SDK v2 factory and call <code>createMcpHandler(factory, options)</code>. Use <code>createLegacyMcpHandler</code> only as a temporary bridge for sessionful features.</td>
<td>Scheduled for removal in the next major version.</td>
</tr>
<tr>
<td><code>MCPClientManager.callTool(params, resultSchema, options)</code> and the equivalent <code>withX402Client</code> overload</td>
<td>Use <code>callTool(params, options)</code> or <code>callTool(confirm, params, options)</code>.</td>
<td>Compatibility overload. No removal version is announced.</td>
</tr>
</tbody>
</table>
<p>The MCP 2026-07-28 draft separately deprecates Roots, Sampling, Logging, the old HTTP+SSE transport, and Dynamic Client Registration.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-27">Jul 27, 2026</time><div>
<h2 id="post-2026-07-27-audit-logs-v2-resource-history"><a href="/changelog/post/2026-07-27-audit-logs-v2-resource-history/">Audit Logs v2 — Resource History</a></h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p>Audit Logs v2 now includes <strong>Resource History</strong>. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.</p>
<p>Resource History uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.</p>
<p><img src="/assets/upstream/images/changelog/audit-logs/Audit_logs_v2_resource_history.png" alt="Resource History in Audit Logs v2" /></p>
<p><strong>Dashboard:</strong></p>
<ol>
<li>Go to <strong>Manage Account</strong> &gt; <strong>Audit Logs</strong>.</li>
<li>Open any audit log entry.</li>
<li>Select the <strong>History</strong> tab to see the full history for that resource.</li>
<li>Select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.</li>
</ol>
<p><strong>API:</strong></p>
<p>Use the History endpoint to retrieve the change history for any audit log entry:</p>
<pre tabindex="0"><code class="language-txt">GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history&#10;</code></pre>
<p>The endpoint is also available for organization-scoped audit logs at <code>/organizations/{organization_id}/logs/audit/{id}/history</code>.</p>
<p>For more information, refer to the <a href="/fundamentals/account/account-security/audit-logs/#resource-history">Resource History documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-27">Jul 27, 2026</time><div>
<h2 id="post-2026-07-21-integration-test-harness"><a href="/changelog/post/2026-07-21-integration-test-harness/">Run integration tests against your Worker's production build</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler now provides <code>createTestHarness()</code>, an API for running integration tests against Workers built with <a href="/workers/testing/test-harness/configure/#configure-worker-projects">Wrangler or the Cloudflare Vite plugin</a> from any Node.js test runner.</p>
<p>The test harness starts a local Worker server with <a href="/workers/wrangler/api/#createtestharness">helpers for dispatching requests, resetting storage, and inspecting runtime logs</a>.</p>
<p>This is useful for tests that need to:</p>
<ul>
<li><a href="/workers/testing/test-harness/interact-with-workers/#test-route-dispatch-across-workers">Route requests across multiple Workers</a></li>
<li><a href="/workers/testing/test-harness/integrations/#mock-service-worker">Mock outbound <code>fetch()</code> requests</a> with Node.js request mocking libraries such as <a href="https://mswjs.io/">MSW</a></li>
<li><a href="/workers/testing/test-harness/integrations/#playwright">Run Playwright tests against a Worker</a></li>
</ul>
<p>For example, this test starts two Workers and mocks an upstream API:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17807.md")</div>
<p>Cloudflare now recommends <code>createTestHarness()</code> for integration tests instead of <a href="/workers/testing/unstable_startworker/"><code>unstable_startWorker()</code></a> or <a href="/workers/wrangler/api/#unstable_dev"><code>unstable_dev()</code></a>. To start a development server programmatically, use the Vite <a href="https://vite.dev/guide/api-javascript.html#createserver"><code>createServer()</code></a> API with the <a href="/workers/vite-plugin/">Cloudflare Vite plugin</a>.</p>
<p>For more information about <code>createTestHarness()</code>, refer to the <a href="/workers/testing/test-harness/">Integration test harness guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-24">Jul 24, 2026</time><div>
<h2 id="post-2026-07-24-r2-sippy-azure-s3-compatible-support"><a href="/changelog/post/2026-07-24-r2-sippy-azure-s3-compatible-support/">Sippy now supports Azure Blob Storage and S3-compatible storage providers</a></h2>
<div class="changelog-badges"><span>r2</span></div><div class="changelog-body"><p><a href="/r2/data-migration/sippy/">Sippy</a> can now incrementally migrate data from Azure Blob Storage and any S3-compatible object storage provider to <a href="/r2/">Cloudflare R2</a>, in addition to Amazon S3 and Google Cloud Storage. Sippy copies objects to R2 as your application requests them, so you can start serving data from R2 without first moving your entire dataset or paying migration-specific egress fees.</p>
<h4 id="2026-07-24-r2-sippy-azure-s3-compatible-support-enable-sippy">Enable Sippy</h4>
<p>Run the following command and follow the prompts to select and configure your source storage provider:</p>
<pre tabindex="0"><code class="language-sh">npx wrangler r2 bucket sippy enable &lt;BUCKET_NAME&gt;&#10;</code></pre>
<p>For Azure Blob Storage, provide your storage account name, container name, and either an account key or a shared access signature (SAS) token with read and list permissions. For an S3-compatible provider, provide the S3 API endpoint URL and read-only Access Key ID and Secret Access Key.</p>
<p><img src="/assets/upstream/images/r2/sippy-azure-source-configuration.png" alt="Azure Blob Storage source configuration in the R2 dashboard" /></p>
<p>After you enable Sippy, requests for objects that are not yet in R2 are served from your source bucket and copied to R2. Subsequent requests for those objects are served from R2.</p>
<p>For setup instructions and credential requirements, refer to the <a href="/r2/data-migration/sippy/">Sippy documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-24">Jul 24, 2026</time><div>
<h2 id="post-2026-07-24-durable-object-instance-observability"><a href="/changelog/post/2026-07-24-durable-object-instance-observability/">Filter Durable Object logs and traces by instance ID</a></h2>
<div class="changelog-badges"><span>workers</span><span>durable-objects</span></div><div class="changelog-body"><p><a href="/workers/observability/logs/workers-logs/">Workers Logs</a> and <a href="/workers/observability/exporting-opentelemetry-data/">OpenTelemetry</a> spans for <a href="/durable-objects/">Durable Object</a> requests include the Durable Object instance ID.</p>
<p>Use <code>$workers.durableObjectId</code> to filter logs for a specific instance. Root and child spans include the same ID in <code>cloudflare.durable_object.id</code>.</p>
<p><img src="/assets/upstream/images/changelog/workers/observability/2026-07-24-durable-object-trace-filter.png" alt="Query Builder filtering traces by Durable Object instance ID" /></p>
<p>Use these fields to isolate a specific instance and correlate its logs and traces.</p>
<p>For more information, refer to <a href="/durable-objects/observability/metrics-and-analytics/">Durable Objects metrics and analytics</a> and <a href="/workers/observability/traces/spans-and-attributes/">Workers tracing spans and attributes</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-24">Jul 24, 2026</time><div>
<h2 id="post-2026-07-24-skip-superseded-builds"><a href="/changelog/post/2026-07-24-skip-superseded-builds/">Workers Builds now skips superseded queued builds</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Workers Builds now automatically skips a queued build when a newer build for the same build trigger is also queued.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-23">Jul 23, 2026</time><div>
<h2 id="post-2026-07-23-ai-sdk-v6-v7-support"><a href="/changelog/post/2026-07-23-ai-sdk-v6-v7-support/">Agents SDK packages support AI SDK v6 and v7</a></h2>
<div class="changelog-badges"><span>agents</span></div><div class="changelog-body"><p>The <code>agents</code>, <code>@cloudflare/ai-chat</code>, <code>@cloudflare/codemode</code>, and <code>@cloudflare/think</code> packages now support AI SDK v6 and v7. Existing applications can remain on v6 when updating these packages. Applications can also adopt v7 without changing the Cloudflare Agents APIs they use.</p>
<p>The supported peer ranges are <code>ai@^6 || ^7</code> and <code>@ai-sdk/react@^3 || ^4</code>. Use matching major versions: pair AI SDK v6 with <code>@ai-sdk/react</code> v3, or pair AI SDK v7 with <code>@ai-sdk/react</code> v4.</p>
<p>To install the latest packages with AI SDK v7:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/ai-chat@latest @cloudflare/codemode@latest @cloudflare/think@latest ai@^7 @ai-sdk/react@^4" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Think normalizes streaming, tool completion events, and telemetry across both AI SDK versions. Existing v6 applications do not need to migrate these integrations before updating Think.</p>
<p>For setup and usage details, refer to the <a href="/agents/harnesses/think/">Think documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-22">Jul 22, 2026</time><div>
<h2 id="post-2026-07-22-mcp-codemode-updates"><a href="/changelog/post/2026-07-22-mcp-codemode-updates/">Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs</a></h2>
<div class="changelog-badges"><span>agents</span><span>workers</span></div><div class="changelog-body"><p>This release reduces repeated MCP schema conversion and adds an opt-out for Think's automatic MCP tool exposure. It also lets non-AI-SDK hosts invoke the durable Code Mode runtime directly.</p>
<h4 id="2026-07-22-mcp-codemode-updates-control-direct-mcp-tool-exposure-in-think">Control direct MCP tool exposure in Think</h4>
<p>Agents SDK MCP clients now reuse converted input and output schemas while a live connection keeps the same tool catalog. This avoids converting every MCP JSON Schema to Zod again for each model turn.</p>
<p><code>@cloudflare/think</code> also adds <code>includeMcpTools</code>. Set it to <code>false</code> when you expose MCP tools through Code Mode or another mechanism outside Think's automatic tool set:</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17679.md")</div>
<p>This setting skips Think's automatic <code>getAITools()</code> call. MCP registration, restoration, discovery, raw catalog access, direct calls, and Code Mode connectors continue to work.</p>
<p>Use <a href="/agents/model-context-protocol/apis/client-api/#thismcplisttools"><code>listTools()</code></a> when you only need the raw MCP catalog. For connector setup, refer to <a href="/agents/tools/codemode/mcp/">Use MCP tools with Code Mode</a>.</p>
<h4 id="2026-07-22-mcp-codemode-updates-invoke-the-code-mode-runtime-without-the-ai-sdk">Invoke the Code Mode runtime without the AI SDK</h4>
<p><code>@cloudflare/codemode@latest</code> adds <code>execute()</code>, <code>search()</code>, and <code>describe()</code> to the durable runtime handle. MCP servers and other hosts can now execute code and discover connector methods without adapting the runtime to an AI SDK tool.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/17680.md")</div>
<p>Search and describe results include <code>requiresApproval: true</code> for protected connector methods. Resolve a paused execution with the existing <code>approve()</code> and <code>reject()</code> methods.</p>
<p>For setup and exact method types, refer to <a href="/agents/tools/codemode/durable-runtime/">Create a durable Code Mode runtime</a> and the <a href="/agents/tools/codemode/api-reference/">Code Mode API reference</a>.</p>
<h4 id="2026-07-22-mcp-codemode-updates-upgrade">Upgrade</h4>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre tabindex="0"><code data-nb-pm-code>npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre tabindex="0"><code data-nb-pm-code>bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest" aria-label="Copy to clipboard">Copy</button></div></div>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-22">Jul 22, 2026</time><div>
<h2 id="post-2026-07-21-warp-linux-ga"><a href="/changelog/post/2026-07-21-warp-linux-ga/">Cloudflare One Client for Linux (version 2026.6.880.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Linux Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-22">Jul 22, 2026</time><div>
<h2 id="post-2026-07-21-warp-macos-ga"><a href="/changelog/post/2026-07-21-warp-macos-ga/">Cloudflare One Client for macOS (version 2026.6.880.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the macOS Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-22">Jul 22, 2026</time><div>
<h2 id="post-2026-07-21-warp-windows-ga"><a href="/changelog/post/2026-07-21-warp-windows-ga/">Cloudflare One Client for Windows (version 2026.6.880.0)</a></h2>
<div class="changelog-badges"><span>cloudflare-one-client</span></div><div class="changelog-body"><p>A new GA release for the Windows Cloudflare One Client is now available on the <a href="/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/">stable releases downloads page</a>.</p>
<p>This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-21">Jul 21, 2026</time><div>
<h2 id="post-2026-07-21-account-role-api-deprecated"><a href="/changelog/post/2026-07-21-account-role-api-deprecated/">Account Role API deprecated</a></h2>
<div class="changelog-badges"><span>fundamentals</span></div><div class="changelog-body"><p>The <a href="/api/resources/accounts/subresources/roles/">Account Roles API</a> is deprecated and is being replaced by the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a>. An end of life date has not yet been established.</p>
<h4 id="2026-07-21-account-role-api-deprecated-what-you-need-to-do">What you need to do</h4>
<p>Review the <a href="/api/resources/iam/subresources/permission_groups/">Permission Groups API</a> documentation; the response schema differs from the legacy Roles response.</p>
<h4 id="2026-07-21-account-role-api-deprecated-highlights">Highlights</h4>
<ul>
<li>Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.</li>
<li>The legacy <code>Role</code> response includes a top-level <code>description</code> and a <code>permissions</code> object keyed by resource type with edit/read flags.</li>
<li>The <code>PermissionGroup</code> response replaces those with a <code>meta</code> object containing <code>label</code> and <code>scopes</code>. Individual permissions are not returned as part of the permission group.</li>
<li>The new API supports the <a href="/fundamentals/api/get-started/create-token/">API Token</a> authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.</li>
</ul>
<p>For more information, refer to <a href="/fundamentals/api/reference/deprecations/">API deprecations</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2026-07-21">Jul 21, 2026</time><div>
<h2 id="post-2026-07-21-devin-outposts"><a href="/changelog/post/2026-07-21-devin-outposts/">Run Devin on Cloudflare using Devin Outposts</a></h2>
<div class="changelog-badges"><span>sandbox</span></div><div class="changelog-body"><p><a href="https://docs.devin.ai/onboard-devin/outposts">Devin Outposts</a> lets you run Devin agents on Cloudflare. Each Devin session runs in its own isolated sandbox backed by <a href="/containers/">Cloudflare Containers</a>, so agents can execute code and use development tooling in an isolated environment.</p>
<p>Use Devin Outposts when you want Devin sessions to run on Cloudflare managed infrastructure, with each session isolated from the others.</p>
<p><img src="/assets/upstream/images/changelog/sandbox/devin-outposts.jpg" alt="Devin interface showing Cloudflare selected as an Outposts virtual environment" /></p>
<p>To get started, refer to <a href="/sandbox/tutorials/devin-outposts/">Run Devin on Cloudflare using Devin Outposts</a>.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/6/">Previous</a><span>Page 7 of 50</span><a class="pagination-next" rel="next" href="/changelog/8/">Next</a></nav>
</div>
