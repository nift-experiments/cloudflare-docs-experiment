---
cp9:
  canonical: https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/
  description: New updates and improvements at Cloudflare.
  full_title: New DLP topic based detection entries for AI prompt protection · Changelog
  head_html: <title>New DLP topic based detection entries for AI prompt protection · Changelog</title><meta name="generator" content="Nift"><meta name="description" content="New updates and improvements at Cloudflare."><link rel="canonical" href="https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/"><link rel="sitemap" href="/sitemap-index.xml"><meta property="og:title" content="New DLP topic based detection entries for AI prompt protection · Changelog"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="New updates and improvements at Cloudflare."><meta property="og:url" content="https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/"><meta property="image" content="https://developers.cloudflare.com/og-changelog.png"><meta property="og:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-changelog.png"><meta name="pcx_content_type" content="Changelog entry"><meta name="algolia_content_type" content="Changelog entry"><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/#page","headline":"New DLP topic based detection entries for AI prompt protection \u00b7 Changelog","description":"New updates and improvements at Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2025-08-25-ai-prompt-protection/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: false
  noindex: false
  route: /changelog/post/2025-08-25-ai-prompt-protection/
  schema: 1
---
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
<pre tabindex="0"><code>    - **Content:** PII, Source Code, Credentials and Secrets, Financial Information, and Customer Data.&#10;&#10;    - **Intent:** Jailbreak attempts, requests for malicious code, or attempts to extract PII.&#10;</code></pre>
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
