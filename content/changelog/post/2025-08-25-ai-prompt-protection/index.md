<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>August 25, 2025</time><h2 id="post-title">New DLP topic based detection entries for AI prompt protection</h2>
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
</div></article></div>
