<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><span>All products</span><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<section class="changelog-feed" aria-label="Changelog entries">
<article class="changelog-entry">
<time datetime="2025-08-26">Aug 26, 2025</time><div>
<h2 id="post-2025-08-26-vectorize-list-vectors"><a href="/changelog/post/2025-08-26-vectorize-list-vectors/">List all vectors in a Vectorize index with the new list-vectors operation</a></h2>
<div class="changelog-badges"><span>vectorize</span></div><div class="changelog-body"><p>You can now list all vector identifiers in a Vectorize index using the new <code>list-vectors</code> operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.</p>
<p>The operation is available via Wrangler CLI and REST API. Refer to the <a href="/vectorize/best-practices/list-vectors/">list-vectors best practices guide</a> for detailed usage guidance.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-25">Aug 25, 2025</time><div>
<h2 id="post-2025-08-25-secrets-store-ai-gateway"><a href="/changelog/post/2025-08-25-secrets-store-ai-gateway/">Manage and deploy your AI provider keys through Bring Your Own Key (BYOK) with AI Gateway, now powered by Cloudflare Secrets Store</a></h2>
<div class="changelog-badges"><span>secrets-store</span><span>ai-gateway</span><span>ssl</span></div><div class="changelog-body"><p>Cloudflare Secrets Store is now integrated with AI Gateway, allowing you to store, manage, and deploy your AI provider keys in a secure and seamless configuration through <a href="https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/">Bring Your Own Key</a>. Instead of passing your AI provider keys directly in every request header, you can centrally manage each key with Secrets Store and deploy in your gateway configuration using only a reference, rather than passing the value in plain text.</p>
<p>You can now create a secret directly from your AI Gateway <a href="http://dash.cloudflare.com/?to=/:account/ai-gateway">in the dashboard</a> by navigating into your gateway -&gt; <strong>Provider Keys</strong> -&gt; <strong>Add</strong>.</p>
<p><img src="/assets/upstream/images/ssl/add-secret-ai-gateway.png" alt="Import repo or choose template" /></p>
<p>You can also create your secret with the newly available <strong>ai_gateway</strong> scope via <a href="https://developers.cloudflare.com/workers/wrangler/commands/">wrangler</a>, the <a href="http://dash.cloudflare.com/?to=/:account/secrets-store">Secrets Store dashboard</a>, or the <a href="https://developers.cloudflare.com/api/resources/secrets_store/">API</a>.</p>
<p>Then, pass the key in the request header using its Secrets Store reference:</p>
<pre><code class="language-bash">curl -X POST https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic/v1/messages \&#10; &#45;-header &#x27;cf-aig-authorization: ANTHROPIC_KEY_1 \&#10; &#45;-header &#x27;anthropic-version: 2023-06-01&#x27; \&#10; &#45;-header &#x27;Content-Type: application/json&#x27; \&#10; &#45;-data  &#x27;{&quot;model&quot;: &quot;claude-3-opus-20240229&quot;, &quot;messages&quot;: [{&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: &quot;What is Cloudflare?&quot;}]}&#x27;&#10;</code></pre>
<p>Or, using Javascript:</p>
<pre><code>import Anthropic from &#x27;@anthropic-ai/sdk&#x27;;&#10;&#10;&#10;const anthropic = new Anthropic({&#10; apiKey: &quot;ANTHROPIC_KEY_1&quot;,&#10; baseURL: &quot;https://gateway.ai.cloudflare.com/v1/&lt;ACCOUNT_ID&gt;/my-gateway/anthropic&quot;,&#10;});&#10;&#10;&#10;const message = await anthropic.messages.create({&#10; model: &#x27;claude-3-opus-20240229&#x27;,&#10; messages: [{role: &quot;user&quot;, content: &quot;What is Cloudflare?&quot;}],&#10; max_tokens: 1024&#10;});&#10;</code></pre>
<p>For more information, check out the <a href="https://blog.cloudflare.com/ai-gateway-aug-2025-refresh">blog</a>!</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-25">Aug 25, 2025</time><div>
<h2 id="post-2025-08-25-ai-prompt-protection"><a href="/changelog/post/2025-08-25-ai-prompt-protection/">New DLP topic based detection entries for AI prompt protection</a></h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You now have access to a comprehensive suite of capabilities to secure your organization's use of generative AI. AI prompt protection introduces four key features that work together to provide deep visibility and granular control.</p>
<ol>
<li><strong>Prompt Detection for AI Applications</strong></li>
</ol>
<p>DLP can now natively detect and inspect user prompts submitted to popular AI applications, including <strong>Google Gemini</strong>, <strong>ChatGPT</strong>, <strong>Claude</strong>, and <strong>Perplexity</strong>.</p>
<ol start="2">
<li><strong>Prompt Analysis and Topic Classification</strong></li>
</ol>
<p>Our DLP engine performs deep analysis on each prompt, applying <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">topic classification</a>. These topics are grouped into two evaluation categories:</p>
<pre><code>    - **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.&#10;&#10;    - **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.&#10;</code></pre>
<p>To help you apply these topics quickly, we have also released five new predefined profiles (for example, AI Prompt: AI Security, AI Prompt: PII) that bundle these new topics.</p>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-detection-entry.png" alt="DLP" /></p>
<ol start="3">
<li>
<p><strong>Granular Guardrails</strong></p>
<p>You can now build guardrails using Gateway HTTP policies with <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a>. Apply a DLP profile containing an <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topic detection</a> to individual AI applications (for example, <code>ChatGPT</code>) and specific user actions (for example, <code>SendPrompt</code>) to block sensitive prompts.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-policy.png" alt="DLP" /></p>
<ol start="4">
<li>
<p><strong>Full Prompt Logging</strong></p>
<p>To aid in incident investigation, an optional setting in your Gateway policy allows you to <a href="/cloudflare-one/data-loss-prevention/dlp-policies/logging-options/#log-generative-ai-prompt-content">capture prompt logs</a> to store the full interaction of prompts that trigger a policy match. To make investigations easier, logs can be filtered by <code>conversation_id</code>, allowing you to reconstruct the full context of an interaction that led to a policy violation.</p>
</li>
</ol>
<p><img src="/assets/upstream/images/changelog/dlp/ai-prompt-log.png" alt="DLP" /></p>
<p>AI prompt protection is now available in open beta. To learn more about it, read the <a href="https://blog.cloudflare.com/ai-prompt-protection/#closing-the-loop-logging">blog</a> or refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-25">Aug 25, 2025</time><div>
<h2 id="post-2025-08-25-waf-release"><a href="/changelog/post/2025-08-25-waf-release/">WAF Release - 2025-08-25</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week, critical vulnerabilities were disclosed that impact widely used open-source infrastructure, creating high-risk scenarios for code execution and operational disruption.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>Apache HTTP Server – Code Execution (CVE-2024-38474): A flaw in Apache HTTP Server allows attackers to achieve remote code execution, enabling full compromise of affected servers. This vulnerability threatens the confidentiality, integrity, and availability of critical web services.</p>
</li>
<li>
<p>Laravel (CVE-2024-55661): A security flaw in Laravel introduces the potential for remote code execution under specific conditions. Exploitation could provide attackers with unauthorized access to application logic and sensitive backend data.</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities pose severe risks to enterprise environments and open-source ecosystems. Remote code execution enables attackers to gain deep system access, steal data, disrupt services, and establish persistent footholds for broader intrusions. Given the widespread deployment of Apache HTTP Server and Laravel in production systems, timely patching and mitigation are critical.</p>
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
        <code class="nb-rule-id" title="c550282a0f7343ca887bdab528050359">28050359</code>
</td>
<td>100822_BETA</td>
<td>WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058</td>
<td>N/A</td>
<td>Disabled</td>
<td>This was merged in to the original rule "WordPress:Plugin:WPBookit - Remote Code Execution - CVE:CVE-2025-6058" (ID: <code class="nb-rule-id" title="9b5c5e13d2ca4253a89769f2194f7b2d">194f7b2d</code>)</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="456b1e8f827b4ed89fb4a54b3bdcdbad">3bdcdbad</code>
</td>
<td>100831</td>
<td>Apache HTTP Server - Code Execution - CVE:CVE-2024-38474</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7dcc01e1dd074e42a26c8ca002eaac5b">02eaac5b</code>
</td>
<td>100846</td>
<td>Laravel - Remote Code Execution - CVE:CVE-2024-55661</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-25">Aug 25, 2025</time><div>
<h2 id="post-2025-08-25-workers-assets-javascript-content-type"><a href="/changelog/post/2025-08-25-workers-assets-javascript-content-type/">Content type returned in Workers Assets for Javascript files is now `text/javascript`</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>JavaScript asset responses have been updated to use the <code>text/javascript</code> Content-Type header instead of <code>application/javascript</code>. While both MIME types are widely supported by browsers, the HTML Living Standard explicitly recommends <code>text/javascript</code> as the preferred type going forward.</p>
<p>This change improves:</p>
<ul>
<li>Standards alignment: Ensures consistency with the HTML spec and modern web platform guidance.</li>
<li>Interoperability: Some developer tools, validators, and proxies expect text/javascript and may warn or behave inconsistently with application/javascript.</li>
<li>Future-proofing: By following the spec-preferred MIME type, we reduce the risk of deprecation warnings or unexpected behavior in evolving browser environments.</li>
<li>Consistency: Most frameworks, CDNs, and hosting providers now default to text/javascript, so this change matches common ecosystem practice.</li>
</ul>
<p>Because all major browsers accept both MIME types, this update is backwards compatible and should not cause breakage.</p>
<p>Users will see this change on the next deployment of their assets.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-22">Aug 22, 2025</time><div>
<h2 id="post-2025-08-22-kv-performance-improvements"><a href="/changelog/post/2025-08-22-kv-performance-improvements/">Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance</a></h2>
<div class="changelog-badges"><span>kv</span></div><div class="changelog-body"><p>Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.</p>
<p><img src="/assets/upstream/images/kv/changelog/kv-hybrid-providers-performance-improvements.png" alt="Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker." /></p>
<h4 id="2025-08-22-kv-performance-improvements-performance-improvements">Performance improvements</h4>
<p>The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:</p>
<ul>
<li><strong>p95 latency</strong>: Reduced from ~150ms to ~50ms (67% decrease)</li>
<li><strong>p99 latency</strong>: Reduced from ~350ms to ~250ms (29% decrease)</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-22">Aug 22, 2025</time><div>
<h2 id="post-2025-08-22-audit-logs-v2-logpush"><a href="/changelog/post/2025-08-22-audit-logs-v2-logpush/">Audit logs (version 2) - Logpush Beta Release</a></h2>
<div class="changelog-badges"><span>audit-logs</span></div><div class="changelog-body"><p><a href="/logs/logpush/logpush-job/datasets/account/audit_logs_v2/">Audit Logs v2 dataset</a> is now available via Logpush.</p>
<p>This expands on earlier releases of Audit Logs v2 in the <a href="/changelog/2025-03-27-automatic-audit-logs-beta-release/">API</a> and <a href="/changelog/2025-07-29-audit-logs-v2-ui-beta/">Dashboard UI</a>.</p>
<p>We recommend creating a new Logpush job for the Audit Logs v2 dataset.</p>
<p>Timelines for General Availability (GA) of Audit Logs v2 and the retirement of Audit Logs v1 will be shared in upcoming updates.</p>
<p>For more details on Audit Logs v2, refer to the <a href="https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/">Audit Logs documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-22">Aug 22, 2025</time><div>
<h2 id="post-2025-08-22-dedicated-egress-ip-logpush"><a href="/changelog/post/2025-08-22-dedicated-egress-ip-logpush/">Dedicated Egress IP for Logpush</a></h2>
<div class="changelog-badges"><span>logs</span></div><div class="changelog-body"><p>Cloudflare Logpush can now deliver logs from using fixed, dedicated egress IPs. By routing Logpush traffic through a Cloudflare zone enabled with <a href="/smart-shield/configuration/dedicated-egress-ips/">Aegis IP</a>, your log destination only needs to allow Aegis IPs making setup more secure.</p>
<p>Highlights:</p>
<ul>
<li>Fixed egress IPs ensure your destination only accepts traffic from known addresses.</li>
<li>Works with any supported Logpush destination.</li>
<li>Recommended to use a dedicated zone as a proxy for easier management.</li>
</ul>
<p>To get started, work with your Cloudflare account team to provision Aegis IPs, then configure your Logpush job to deliver logs through the proxy zone. For full setup instructions, refer to the <a href="/logs/logpush/logpush-job/enable-destinations/egress-ip/">Logpush documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-22">Aug 22, 2025</time><div>
<h2 id="post-2025-08-22-waf-release"><a href="/changelog/post/2025-08-22-waf-release/">WAF Release - 2025-08-22</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><table style="width: 100%">
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
        <code class="nb-rule-id" title="0f3b6b9377334707b604be925fcca5c8">5fcca5c8</code>
</td>
<td>100850</td>
<td>Command Injection - Generic 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="36b0532eb3c941449afed2d3744305c4">744305c4</code>
</td>
<td>100851</td>
<td>Remote Code Execution - Java Deserialization</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5d3c0d0958d14512bd2a7d902b083459">2b083459</code>
</td>
<td>100852</td>
<td>Command Injection - Generic 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>    
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6e2f7a696ea74c979e7d069cefb7e5b9">efb7e5b9</code>
</td>
<td>100853</td>
<td>Remote Code Execution - Common Bash Bypass Beta</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="735666d7268545a5ae6cfd0b78513ad7">78513ad7</code>
</td>
<td>100854</td>
<td>XSS - Generic JavaScript</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="82780ba6f5df49dcb8d09af0e9a5daac">e9a5daac</code>
</td>
<td>100855</td>
<td>Command Injection - Generic 4</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8e305924a7dc4f91a2de931a480f6093">480f6093</code>
</td>
<td>100856</td>
<td>PHP Object Injection</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1d34e0d05c10473ca824e66fd4ae0a33">d4ae0a33</code>
</td>
<td>100857</td>
<td>Generic - Parameter Fuzzing</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="b517e4b79d7a47fbb61f447b1121ee45">1121ee45</code>
</td>
<td>100858</td>
<td>Code Injection - Generic 4</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1f9accf629dc42cb84a7a14420de01e3">20de01e3</code>
</td>
<td>100859</td>
<td>SQLi - UNION - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="e95939eacf7c4484b47101d5c0177e21">c0177e21</code>
</td>
<td>100860</td>
<td>Command Injection - Generic 5</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="7b426e6f456043f4a21c162085f4d7b3">85f4d7b3</code>
</td>
<td>100861</td>
<td>Command Execution - Generic</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5fac82bd1c03463fb600cfa83fa8ee7f">3fa8ee7f</code>
</td>
<td>100862</td>
<td>GraphQL Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="ab2cb1f2e2ad4da6a2685b1dc7a41d4b">c7a41d4b</code>
</td>
<td>100863</td>
<td>Command Injection - Generic 6</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="549b4fe1564a448d848365d565e3c165">65e3c165</code>
</td>
<td>100864</td>
<td>Code Injection - Generic 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="8ef3c3f91eef46919cc9cb6d161aafdc">161aafdc</code>
</td>
<td>100865</td>
<td>PHP Object Injection - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="57e8ba867e6240d2af8ea0611cc3c3f8">1cc3c3f8</code>
</td>
<td>100866</td>
<td>SQLi - LIKE 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a967a167874b42b6898be46e48ac2221">48ac2221</code>
</td>
<td>100867</td>
<td>SQLi - DROP - 2</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="cf79a868cc934bcc92b86ff01f4eec13">1f4eec13</code>
</td>
<td>100868</td>
<td>Code Injection - Generic 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="97a52405eaae47ae9627dbb22755f99e">2755f99e</code>
</td>
<td>100869</td>
<td>Command Injection - Generic 7</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5b3ce84c099040c6a25cee2d413592e2">413592e2</code>
</td>
<td>100870</td>
<td>Command Injection - Generic 8</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="5940a9ace2f04d078e35d435d2dd41b5">d2dd41b5</code>
</td>
<td>100871</td>
<td>SQLi - LIKE 3</td>
<td>N/A</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-22">Aug 22, 2025</time><div>
<h2 id="post-2025-08-22-workflows-python-beta"><a href="/changelog/post/2025-08-22-workflows-python-beta/">Build durable multi-step applications in Python with Workflows (now in beta)</a></h2>
<div class="changelog-badges"><span>workflows</span><span>workers</span></div><div class="changelog-body"><p>You can now build <a href="/workflows/">Workflows</a> using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the <a href="/workers/languages/python/">Python Workers</a> runtime.</p>
<p>Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable <a href="/workflows/python/dag/">DAG (Directed Acyclic Graph) workflows</a>, where you can define complex dependencies between steps using the depends parameter.</p>
<p>Here’s a simple example:</p>
<pre><code class="language-python">from workers import Response, WorkflowEntrypoint&#10;&#10;class PythonWorkflowStarter(WorkflowEntrypoint):&#10;    async def run(self, event, step):&#10;        @step.do(&quot;my first step&quot;)&#10;        async def my_first_step():&#10;            &#35; do some work&#10;            return &quot;Hello Python!&quot;&#10;&#10;        await my_first_step()&#10;&#10;        await step.sleep(&quot;my-sleep-step&quot;, &quot;10 seconds&quot;)&#10;&#10;        @step.do(&quot;my second step&quot;)&#10;        async def my_second_step():&#10;            &#35; do some more work&#10;            return &quot;Hello again!&quot;&#10;&#10;        await my_second_step()&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        await self.env.MY_WORKFLOW.create()&#10;        return Response(&quot;Hello Workflow creation!&quot;)&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17831.md")</aside>
<p>Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.</p>
<p>To learn more and get started, refer to <a href="/workflows/python/">Python Workflows documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-21">Aug 21, 2025</time><div>
<h2 id="post-2025-08-21-durable-objects-get-by-name"><a href="/changelog/post/2025-08-21-durable-objects-get-by-name/">New getByName() API to access Durable Objects</a></h2>
<div class="changelog-badges"><span>durable-objects</span><span>workers</span></div><div class="changelog-body"><p>You can now create a client (a <a href="/durable-objects/api/stub/">Durable Object stub</a>) to a Durable Object with the new <code>getByName</code> method, removing the need to convert Durable Object names to IDs and then create a stub.</p>
<pre><code class="language-js">// Before: (1) translate name to ID then (2) get a client &#10;const objectId = env.MY_DURABLE_OBJECT.idFromName(&quot;foo&quot;); // or .newUniqueId()&#10;const stub = env.MY_DURABLE_OBJECT.get(objectId); &#10;&#10;// Now: retrieve client to Durable Object directly via its name &#10;const stub = env.MY_DURABLE_OBJECT.getByName(&quot;foo&quot;);&#10;&#10;// Use client to send request to the remote Durable Object&#10;const rpcResponse = await stub.sayHello();&#10;</code></pre>
<p>Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.</p>
<p>To learn more, visit the Durable Objects <a href="/durable-objects/api/namespace/#getbyname">API Documentation</a> or the <a href="/durable-objects/get-started/">getting started guide</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-21">Aug 21, 2025</time><div>
<h2 id="post-2025-08-21-byoip-dedicated-egress-ip"><a href="/changelog/post/2025-08-21-byoip-dedicated-egress-ip/">Gateway BYOIP Dedicated Egress IPs now available.</a></h2>
<div class="changelog-badges"><span>gateway</span></div><div class="changelog-body"><p>Enterprise Gateway users can now use Bring Your Own IP (BYOIP) for dedicated egress IPs.</p>
<p>Admins can now onboard and use their own IPv4 or IPv6 prefixes to egress traffic from Cloudflare, delivering greater control, flexibility, and compliance for network traffic.</p>
<p>Get started by following the <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP onboarding process</a>. Once your IPs are onboarded, go to <strong>Gateway</strong> &gt; <strong>Egress policies</strong> and select or create an egress policy. In <strong>Select an egress IP</strong>, choose <em>Use dedicated egress IPs (Cloudflare or BYOIP)</em>, then select your BYOIP address from the dropdown menu.</p>
<p><img src="/assets/upstream/images/gateway/Gateway-byoip-dedicated-egress-ips.png" alt="Screenshot of a dropdown menu adding a BYOIP IPv4 address as a dedicated egress IP in a Gateway egress policy" /></p>
<p>For more information, refer to <a href="/cloudflare-one/traffic-policies/egress-policies/dedicated-egress-ips/#bring-your-own-ip-address-byoip">BYOIP for dedicated egress IPs</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-19">Aug 19, 2025</time><div>
<h2 id="post-2025-08-19-event-subscriptions"><a href="/changelog/post/2025-08-19-event-subscriptions/">Subscribe to events from Cloudflare services with Queues</a></h2>
<div class="changelog-badges"><span>queues</span></div><div class="changelog-body"><p>You can now subscribe to events from other Cloudflare services (for example, <a href="/kv/">Workers KV</a>, <a href="/workers-ai">Workers AI</a>, <a href="/workers">Workers</a>) and consume those events via <a href="/queues/">Queues</a>, allowing you to build custom workflows, integrations, and logic in response to account activity.</p>
<p><img src="/assets/upstream/images/queues/queues-event-subscriptions.png" alt="Event subscriptions architecture" /></p>
<p>Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products can publish structured events to a queue, which you can then consume with <a href="/workers/">Workers</a> or <a href="/queues/configuration/pull-consumers/">pull via HTTP from anywhere</a>.</p>
<p>To create a subscription, use the dashboard or <a href="/workers/wrangler/commands/queues/#queues-subscription-create">Wrangler</a>:</p>
<pre><code class="language-bash">npx wrangler queues subscription create my-queue --source r2 --events bucket.created&#10;</code></pre>
<p>An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. Events follow a consistent structure:</p>
<pre><code class="language-json">{&#10;  &quot;type&quot;: &quot;cf.r2.bucket.created&quot;,&#10;  &quot;source&quot;: {&#10;    &quot;type&quot;: &quot;r2&quot;&#10;  },&#10;  &quot;payload&quot;: {&#10;    &quot;name&quot;: &quot;my-bucket&quot;,&#10;    &quot;location&quot;: &quot;WNAM&quot;&#10;  },&#10;  &quot;metadata&quot;: {&#10;    &quot;accountId&quot;: &quot;f9f79265f388666de8122cfb508d7776&quot;,&#10;    &quot;eventTimestamp&quot;: &quot;2025-07-28T10:30:00Z&quot;&#10;  }&#10;}&#10;</code></pre>
<p>Current <a href="/queues/event-subscriptions/events-schemas/">event sources</a> include <a href="/r2/">R2</a>, <a href="/kv/">Workers KV</a>, <a href="/workers-ai/">Workers AI</a>, <a href="/workers/ci-cd/builds/">Workers Builds</a>, <a href="/vectorize/">Vectorize</a>, <a href="/r2/data-migration/super-slurper/">Super Slurper</a>, and <a href="/workflows/">Workflows</a>. More sources and events are on the way.</p>
<p>For more information on event subscriptions, available events, and how to get started, refer to our <a href="/queues/event-subscriptions/">documentation</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-19">Aug 19, 2025</time><div>
<h2 id="post-2025-08-19-improved-wrangler-error-screen"><a href="/changelog/post/2025-08-19-improved-wrangler-error-screen/">Easier debugging in Workers with improved Wrangler error screen</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Wrangler's error screen has received several improvements to enhance your debugging experience!</p>
<p>The error screen now features a refreshed design thanks to <a href="https://www.npmjs.com/package/youch">youch</a>, with support for both light and dark themes, improved source map resolution logic that handles missing source files more reliably, and better error cause display.</p>
<table>
<thead>
<tr>
<th>Before</th>
<th>After (Light)</th>
<th>After (Dark)</th>
</tr>
</thead>
<tbody>
<tr>
<td><img src="/assets/upstream/images/workers/changelog/old-error-screen.png" alt="Old error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-light.png" alt="New light theme error screen" /></td>
<td><img src="/assets/upstream/images/workers/changelog/new-error-screen-dark.png" alt="New dark theme error screen" /></td>
</tr>
</tbody>
</table>
<p>Try it out now with <code>npx wrangler@latest dev</code> in your Workers project.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-18">Aug 18, 2025</time><div>
<h2 id="post-2025-08-18-waf-release"><a href="/changelog/post/2025-08-18-waf-release/">WAF Release - 2025-08-18</a></h2>
<div class="changelog-badges"><span>waf</span></div><div class="changelog-body"><p><strong>This week's update</strong></p>
<p>This week, a series of critical vulnerabilities were discovered impacting core enterprise and open-source infrastructure. These flaws present a range of risks, providing attackers with distinct pathways for remote code execution, methods to breach internal network boundaries, and opportunities for critical data exposure and operational disruption.</p>
<p><strong>Key Findings</strong></p>
<ul>
<li>
<p>SonicWall SMA (CVE-2025-32819, CVE-2025-32820, CVE-2025-32821): A remote authenticated attacker with SSLVPN user privileges can bypass path traversal protections. These vulnerabilities enable a attacker to bypass security checks to read, modify, or delete arbitrary files. An attacker with administrative privileges can escalate this further, using a command injection flaw to upload malicious files, which could ultimately force the appliance to reboot to its factory default settings.</p>
</li>
<li>
<p>Ms-Swift Project (CVE-2025-50460): An unsafe deserialization vulnerability exists in the Ms-Swift project's handling of YAML configuration files. If an attacker can control the content of a configuration file passed to the application, they can embed a malicious payload that will execute arbitrary code and it can be executed during deserialization.</p>
</li>
<li>
<p>Apache Druid (CVE-2023-25194): This vulnerability in Apache Druid allows an attacker to cause the server to connect to a malicious LDAP server. By sending a specially crafted LDAP response, the attacker can trigger an unrestricted deserialization of untrusted data. If specific &quot;gadgets&quot; (classes that can be abused) are present in the server's classpath, this can be escalated to achieve Remote Code Execution (RCE).</p>
</li>
<li>
<p>Tenda AC8v4 (CVE-2025-51087, CVE-2025-51088): Vulnerabilities allow an authenticated attacker to trigger a stack-based buffer overflow. By sending malformed arguments in a request to specific endpoints, an attacker can crash the device or potentially achieve arbitrary code execution.</p>
</li>
<li>
<p>Open WebUI (CVE-2024-7959): This vulnerability allows a user to change the OpenAI URL endpoint to an arbitrary internal network address without proper validation. This flaw can be exploited to access internal services or cloud metadata endpoints, potentially leading to remote command execution if the attacker can retrieve instance secrets or access sensitive internal APIs.</p>
</li>
<li>
<p>BentoML (CVE-2025-54381): The vulnerability exists in the serialization/deserialization handlers for multipart form data and JSON requests, which automatically download files from user-provided URLs without proper validation of internal network addresses. This allows attackers to fetch from unintended internal services, including cloud metadata and localhost.</p>
</li>
<li>
<p>Adobe Experience Manager Forms (CVE-2025-54254): An Improper Restriction of XML External Entity Reference ('XXE') vulnerability that could lead to arbitrary file system read in Adobe AEM (≤6.5.23).</p>
</li>
</ul>
<p><strong>Impact</strong></p>
<p>These vulnerabilities affect core infrastructure, from network security appliances like SonicWall to data platforms such as Apache Druid and ML frameworks like BentoML. The code execution and deserialization flaws are particularly severe, offering deep system access that allows attackers to steal data, disrupt services, and establish a foothold for broader intrusions. Simultaneously, SSRF and XXE vulnerabilities undermine network boundaries, exposing sensitive internal data and creating pathways for lateral movement. Beyond data-centric threats, flaws in edge devices like the Tenda router introduce the tangible risk of operational disruption, highlighting a multi-faceted threat to the security and stability of key enterprise systems.</p>
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
        <code class="nb-rule-id" title="326ebb56d46a4c269bb699d3418d9a3b">418d9a3b</code>
</td>
<td>100574</td>
<td>SonicWall SMA - Remote Code Execution - CVE:CVE-2025-32819, CVE:CVE-2025-32820, CVE:CVE-2025-32821</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="69f4f161dec04aca8a73a3231e6fefdb">1e6fefdb</code>
</td>
<td>100576</td>
<td>Ms-Swift Project - Remote Code Execution - CVE:CVE-2025-50460</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="d62935357ff846d9adefb58108ac45b3">08ac45b3</code>
</td>
<td>100585</td>
<td>Apache Druid - Remote Code Execution - CVE:CVE-2023-25194</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="4f6148a760804bf8ad8ebccfe4855472">e4855472</code>
</td>
<td>100834</td>
<td>Tenda AC8v4 - Auth Bypass - CVE:CVE-2025-51087, CVE:CVE-2025-51088</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="1474121b01ba40629f8246f8022ab542">022ab542</code>
</td>
<td>100835</td>
<td>Open WebUI - SSRF - CVE:CVE-2024-7959</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="96abffdb7e224ce69ddf89eb6339f132">6339f132</code>
</td>
<td>100837</td>
<td>SQLi - OOB</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="a0b20ec638d14800a1d6827cb83d2625">b83d2625</code>
</td>
<td>100841</td>
<td>BentoML - SSRF - CVE:CVE-2025-54381</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="40fd793035c947c5ac75add1739180d2">739180d2</code>
</td>
<td>100841A</td>
<td>BentoML - SSRF - CVE:CVE-2025-54381 - 2</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="08dcb20b9acf47e3880a0b886ab910c2">6ab910c2</code>
</td>
<td>100841B</td>
<td>BentoML - SSRF - CVE:CVE-2025-54381 - 3</td>
<td>Log</td>
<td>Disabled</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="309cfb7eeb42482e9ad896f12197ec51">2197ec51</code>
</td>
<td>100845</td>
<td>Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
<tr>
<td>Cloudflare Managed Ruleset</td>
<td>
        <code class="nb-rule-id" title="6e039776c2d6418ab6e8f05196f34ce3">96f34ce3</code>
</td>
<td>100845A</td>
<td>Adobe Experience Manager Forms - XSS - CVE:CVE-2025-54254 - 2</td>
<td>Log</td>
<td>Block</td>
<td>This is a New Detection</td>
</tr>
</tbody>
</table>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-15">Aug 15, 2025</time><div>
<h2 id="post-2025-08-15-sftp"><a href="/changelog/post/2025-08-15-sftp/">SFTP support for SSH with Cloudflare Access for Infrastructure</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/">SSH with Cloudflare Access for Infrastructure</a> now supports SFTP. It is compatible with SFTP clients, such as Cyberduck.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-15">Aug 15, 2025</time><div>
<h2 id="post-2025-08-15-asnum-support-in-custom-rules"><a href="/changelog/post/2025-08-15-asnum-support-in-custom-rules/">Steer Traffic by AS Number in Load Balancing Custom Rules</a></h2>
<div class="changelog-badges"><span>load-balancing</span></div><div class="changelog-body"><p>You can now create more granular, network-aware Custom Rules in Cloudflare Load Balancing using the Autonomous System Number (ASN) of an incoming request.</p>
<p>This allows you to steer traffic with greater precision based on the network source of a request. For example, you can route traffic from specific Internet Service Providers (ISPs) or enterprise customers to dedicated infrastructure, optimize performance, or enforce compliance by directing certain networks to preferred data centers.</p>
<p><img src="/assets/upstream/images/changelog/load-balancing/asnum-custom-rule.png" alt="Create a Load Balancing Custom Rule using AS Num" /></p>
<p>To get started, create a <a href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/">Custom Rule</a> in your Load Balancer and select <strong>AS Num</strong> from the <strong>Field</strong> dropdown.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-15">Aug 15, 2025</time><div>
<h2 id="post-2025-08-15-extended-retention"><a href="/changelog/post/2025-08-15-extended-retention/">Extended retention</a></h2>
<div class="changelog-badges"><span>log-explorer</span></div><div class="changelog-body"><p>Customers can now rely on Log Explorer to meet their log retention compliance requirements.</p>
<p>Contract customers can choose to store their logs in Log Explorer for up to two years, at an additional cost of $0.10 per GB per month. Customers interested in this feature can contact their account team to have it added to their contract.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-15">Aug 15, 2025</time><div>
<h2 id="post-2025-08-15-brand-protection-bulk-endpoint"><a href="/changelog/post/2025-08-15-brand-protection-bulk-endpoint/">Save time with bulk query creation in Brand Protection</a></h2>
<div class="changelog-badges"><span>security-center</span></div><div class="changelog-body"><p><a href="/security-center/brand-protection/">Brand Protection</a> detects domains that may be impersonating your brand — from common misspellings (<code>cloudfalre.com</code>) to malicious concatenations (<code>cloudflare-okta.com</code>). Saved search queries run continuously and alert you when suspicious domains appear.</p>
<p>You can now create and save multiple queries in a single step, streamlining setup and management. Available now via the <a href="/api/resources/brand_protection/subresources/queries/methods/bulk/">Brand Protection bulk query creation API</a>.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-15">Aug 15, 2025</time><div>
<h2 id="post-2025-08-15-terraform-v5.8.4-provider"><a href="/changelog/post/2025-08-15-terraform-v5.8.4-provider/">Terraform v5.8.4 now available</a></h2>
<div class="changelog-badges"><span>fundamentals</span><span>terraform</span></div><div class="changelog-body"><p>Earlier this year, we announced the launch of the new <a href="/changelog/2025-02-03-terraform-v5-provider/">Terraform v5 Provider</a>. We are aware of the high number of <a href="https://github.com/cloudflare/terraform-provider-cloudflare">issues</a> reported by the Cloudflare Community related to the v5 release. We have committed to releasing improvements on a two week cadence to ensure stability and reliability.</p>
<p>One key change we adopted in recent weeks is a pivot to more comprehensive, test-driven development. We are still evaluating individual issues, but are also investing in much deeper testing to drive our stabilization efforts. We will subsequently be investing in comprehensive migration scripts. As a result, you will see several of the highest traffic APIs have been stabilized in the most recent release, and are supported by comprehensive acceptance tests.</p>
<p>Thank you for continuing to raise issues. We triage them weekly and they help make our products stronger.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-changes">Changes</h4>
- Resources stabilized:
  - `cloudflare_argo_smart_routing`
  - `cloudflare_bot_management`
  - `cloudflare_list`
  - `cloudflare_list_item`
  - `cloudflare_load_balancer`
  - `cloudflare_load_balancer_monitor`
  - `cloudflare_load_balancer_pool`
  - `cloudflare_spectrum_application`
  - `cloudflare_managed_transforms`
  - `cloudflare_url_normalization_settings`
  - `cloudflare_snippet`
  - `cloudflare_snippet_rules`
  - `cloudflare_zero_trust_access_application`
  - `cloudflare_zero_trust_access_group`
  - `cloudflare_zero_trust_access_identity_provider`
  - `cloudflare_zero_trust_access_mtls_certificate`
  - `cloudflare_zero_trust_access_mtls_hostname_settings`
  - `cloudflare_zero_trust_access_policy`
  - `cloudflare_zone`
- Multipart handling restored for `cloudflare_snippet`
- `cloudflare_bot_management` diff issues resolves when running `terraform plan` and `terraform apply`
- Other bug fixes
<p>For a more detailed look at all of the changes, refer to the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/releases/tag/v5.8.4">changelog</a> in GitHub.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-issues-closed">Issues Closed</h4>
- [#5017: 'Uncaught Error: No such module' using cloudflare_snippets](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5017)
- [#5701: cloudflare_workers_script migrations for Durable Objects not recorded in tfstate; cannot be upgraded between versions](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5701)
- [#5640: cloudflare_argo_smart_routing importing doesn't read the actual value](https://github.com/cloudflare/terraform-provider-cloudflare/issues/5640)
<p>If you have an unaddressed issue with the provider, we encourage you to check the <a href="https://github.com/cloudflare/terraform-provider-cloudflare/issues">open issues</a> and open a new one if one does not already exist for what you are experiencing.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-upgrading">Upgrading</h4>
<p>We suggest holding off on migration to v5 while we work on stabilization. This will help you avoid any blocking issues while the Terraform resources are actively being stabilized.</p>
<p>If you'd like more information on migrating to v5, please make use of the <a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs/guides/version-5-upgrade">migration guide</a>. We have provided automated migration scripts using Grit which simplify the transition. These migration scripts do not support implementations which use Terraform modules, so customers making use of modules need to migrate manually. Please make use of <code>terraform plan</code> to test your changes before applying, and let us know if you encounter any additional issues by reporting to our <a href="https://github.com/cloudflare/terraform-provider-cloudflare">GitHub repository</a>.</p>
<h4 id="2025-08-15-terraform-v5.8.4-provider-for-more-info">For more info</h4>
<ul>
<li><a href="https://registry.terraform.io/providers/cloudflare/cloudflare/latest/docs">Terraform provider</a></li>
<li><a href="/terraform/">Documentation on using Terraform with Cloudflare</a></li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-15">Aug 15, 2025</time><div>
<h2 id="post-2025-08-15-nodejs-fs"><a href="/changelog/post/2025-08-15-nodejs-fs/">The Node.js and Web File System APIs in Workers</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>Implementations of the <a href="https://nodejs.org/docs/latest/api/fs.html"><code>node:fs</code> module</a> and the <a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_Access_API">Web File System API</a> are now available in Workers.</p>
<h4 id="2025-08-15-nodejs-fs-using-the-node-fs-module">Using the <code>node:fs</code> module</h4>
<p>The <code>node:fs</code> module provides access to a virtual file system in Workers. You can use it to read and write files, create directories, and perform other file system operations.</p>
<p>The virtual file system is ephemeral with each individual request havig its own isolated temporary file space. Files written to the file system will not persist across requests and will not be shared across requests or across different Workers.</p>
<p>Workers running with the <code>nodejs_compat</code> compatibility flag will have access to the <code>node:fs</code> module by default when the compatibility date is set to <code>2025-09-01</code> or later. Support for the API can also be enabled using the <code>enable_nodejs_fs_module</code> compatibility flag together with the <code>nodejs_compat</code> flag. The <code>node:fs</code> module can be disabled using the <code>disable_nodejs_fs_module</code> compatibility flag.</p>
<pre><code class="language-js">import fs from &quot;node:fs&quot;;&#10;&#10;const config = JSON.parse(fs.readFileSync(&quot;/bundle/config.json&quot;, &quot;utf-8&quot;));&#10;&#10;export default {&#10;	async fetch(request) {&#10;		return new Response(`Config value: ${config.value}`);&#10;	},&#10;};&#10;</code></pre>
<p>There are a number of initial limitations to the <code>node:fs</code> implementation:</p>
<ul>
<li>The glob APIs (e.g. <code>fs.globSync(...)</code>) are not implemented.</li>
<li>The file watching APIs (e.g. <code>fs.watch(...)</code>) are not implemented.</li>
<li>The file timestamps (modified time, access time, etc) are only partially supported. For now, these will always return the Unix epoch.</li>
</ul>
<p>Refer to the <a href="https://nodejs.org/docs/latest/api/fs.html">Node.js documentation</a> for more information on the <code>node:fs</code> module and its APIs.</p>
<h4 id="2025-08-15-nodejs-fs-the-web-file-system-api">The Web File System API</h4>
<p>The Web File System API provides access to the same virtual file system as the <code>node:fs</code> module, but with a different API surface. The Web File System API is only available in Workers running with the <code>enable_web_file_system</code> compatibility flag. The <code>nodejs_compat</code> compatibility flag is not required to use the Web File System API.</p>
<pre><code class="language-js">const root = navigator.storage.getDirectory();&#10;&#10;export default {&#10;	async fetch(request) {&#10;		const tmp = await root.getDirectoryHandle(&quot;/tmp&quot;);&#10;		const file = await tmp.getFileHandle(&quot;data.txt&quot;, { create: true });&#10;		const writable = await file.createWritable();&#10;		const writer = writable.getWriter();&#10;		await writer.write(&quot;Hello, World!&quot;);&#10;		await writer.close();&#10;&#10;		return new Response(&quot;File written successfully!&quot;);&#10;	},&#10;};&#10;</code></pre>
<p>As there are still some parts of the Web File System API that are not fully standardized, there may be some differences between the Workers implementation and the implementations in browsers.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-15">Aug 15, 2025</time><div>
<h2 id="post-2025-08-15-static-assets-redirect-url"><a href="/changelog/post/2025-08-15-static-assets-redirect-url/">Workers Static Assets: Corrected handling of double slashes in redirect rule paths</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p><a href="/workers/static-assets/">Static Assets</a>: Fixed a bug in how <a href="https://developers.cloudflare.com/workers/static-assets/redirects/">redirect rules</a> defined in your Worker's <code>_redirects</code> file are processed.</p>
<p>If you're serving Static Assets with a <code>_redirects</code> file containing a rule like <code>/ja/* /:splat</code>, paths with double slashes were previously misinterpreted as external URLs. For example, visiting <code>/ja//example.com</code> would incorrectly redirect to <code>https://example.com</code> instead of <code>/example.com</code> on your domain. This has been fixed and double slashes now correctly resolve as local paths. Note: <a href="/pages/">Cloudflare Pages</a> was not affected by this issue.</p>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-14">Aug 14, 2025</time><div>
<h2 id="post-2025-08-08-support-long-branch-names-preview-aliases"><a href="/changelog/post/2025-08-08-support-long-branch-names-preview-aliases/">Workers per-branch preview URLs now support long branch names</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We've updated <a href="/workers/versions-and-deployments/preview-urls/">preview URLs</a> for Cloudflare Workers to support long branch names.</p>
<p>Previously, branch and Worker names exceeding the 63-character DNS limit would cause alias generation to fail, leaving pull requests without aliased preview URLs. This particularly impacted teams relying on descriptive branch naming.</p>
<p>Now, Cloudflare automatically truncates long branch names and appends a unique hash, ensuring every pull request gets a working preview link.</p>
<h4 id="2025-08-08-support-long-branch-names-preview-aliases-how-it-works">How it works</h4>
<ul>
<li><strong>63 characters or less</strong>: <code>&lt;branch-name&gt;-&lt;worker-name&gt;</code> → Uses actual branch name as is</li>
<li><strong>64 characters or more</strong>: <code>&lt;truncated-branch-name&gt;--&lt;hash&gt;-&lt;worker-name&gt;</code> → Uses truncated name with 4-character hash</li>
<li><strong>Hash generation</strong>: The hash is derived from the full branch name to ensure uniqueness</li>
<li><strong>Stable URLs</strong>: The same branch always generates the same hash across all commits</li>
</ul>
<h4 id="2025-08-08-support-long-branch-names-preview-aliases-requirements-and-compatibility">Requirements and compatibility</h4>
<ul>
<li><strong>Wrangler 4.30.0 or later</strong>: This feature requires updating to wrangler@4.30.0+</li>
<li><strong>No configuration needed</strong>: Works automatically with existing preview URL setups</li>
</ul>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-14">Aug 14, 2025</time><div>
<h2 id="post-2025-07-01-Access-Supports-Customer-Metadata-Boundary"><a href="/changelog/post/2025-07-01-Access-Supports-Customer-Metadata-Boundary/">Cloudflare Access Logging supports the Customer Metadata Boundary (CMB)</a></h2>
<div class="changelog-badges"><span>access</span></div><div class="changelog-body"><p>Cloudflare Access logs now support the <a href="/data-localization/metadata-boundary/">Customer Metadata Boundary (CMB)</a>. If you have configured the CMB for your account, all Access logging will respect that configuration.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17615.md")</aside>
</div>
</div></article>
<article class="changelog-entry">
<time datetime="2025-08-14">Aug 14, 2025</time><div>
<h2 id="post-2025-08-14-new-python-handlers"><a href="/changelog/post/2025-08-14-new-python-handlers/">Python Workers handlers now live in an entrypoint class</a></h2>
<div class="changelog-badges"><span>workers</span></div><div class="changelog-body"><p>We are changing how Python Workers are structured by default. Previously, handlers were defined at the top-level of a module as <code>on_fetch</code>, <code>on_scheduled</code>, etc. methods, but now they live in an entrypoint class.</p>
<p>Here's an example of how to now define a Worker with a fetch handler:</p>
<pre><code class="language-python">from workers import Response, WorkerEntrypoint&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        return Response(&quot;Hello World!&quot;)&#10;</code></pre>
<p>To keep using the old-style handlers, you can specify the <code>disable_python_no_global_handlers</code> compatibility flag in your wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/17785.md")</div>
<p>Consult the <a href="/workers/languages/python/">Python Workers documentation</a> for more details.</p>
</div>
</div></article>
</section>
<nav class="pagination" aria-label="Changelog pages"><a rel="prev" href="/changelog/36/">Previous</a><span>Page 37 of 50</span><a class="pagination-next" rel="next" href="/changelog/38/">Next</a></nav>
</div>
