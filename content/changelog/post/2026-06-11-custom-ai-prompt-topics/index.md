<div class="changelog-landing"><header class="catalog-hero"><h1>Changelog</h1><p>New updates and improvements at Cloudflare.</p></header>
<div class="changelog-tools"><a href="/changelog/rss/index.xml">View RSS feeds</a><a href="/changelog/rss/index.xml">Subscribe to RSS</a></div>
<article class="changelog-detail"><a href="/changelog/">← Back to all posts</a>
<time>June 11, 2026</time><h2 id="post-title">Define custom topics for AI prompt protection</h2>
<div class="changelog-badges"><span>dlp</span></div><div class="changelog-body"><p>You can now define custom topics for AI prompt protection. Predefined <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a> cover common content and intent categories such as PII, source code, and jailbreak attempts. Custom topics let you detect unique or proprietary concepts that are not included in predefined categories.</p>
<p>You describe a custom topic in natural language, and Cloudflare DLP detects whether a prompt matches that topic based on context rather than specific keywords. For example, a topic that describes confidential merger discussions matches a prompt that paraphrases the deal, even when the prompt never uses the word merger or names the companies involved. To detect literal values such as internal codenames or product identifiers, use a <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#custom-wordlist-datasets">custom wordlist or pattern entry</a> instead.</p>
<p>Custom topics run through the same <a href="/cloudflare-one/traffic-policies/http-policies/#granular-controls">application granular controls</a> path as predefined AI prompt topics. Custom topics are available for ChatGPT, Google Gemini, Perplexity, and Claude.</p>
<h4 id="create-a-custom-ai-prompt-topic">Create a custom AI prompt topic</h4>
<ol>
<li>In the <a href="https://dash.cloudflare.com/">Cloudflare dashboard</a>, go to <strong>Zero Trust</strong> &gt; <strong>Data loss prevention</strong> &gt; <strong>Detection entries</strong>.</li>
<li>Select <strong>AI prompt topics</strong>, then select <strong>Custom Prompt Topic</strong>.</li>
<li>Describe the topic in natural language. Be specific about the concept you want to detect. For example, describe unreleased product roadmap details or confidential customer contract terms.</li>
<li>Add this detection entry to an existing DLP profile, or <a href="/cloudflare-one/data-loss-prevention/dlp-profiles/#build-a-custom-profile">create a new DLP profile</a>.</li>
<li>Use the profile in a Gateway HTTP policy to log or block prompts that match the topic.</li>
</ol>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/17715.md")</aside>
<p>For more information, refer to <a href="/cloudflare-one/data-loss-prevention/detection-entries/configure-detection-entries/#ai-prompt-topics">AI prompt topics</a>.</p>
</div></article></div>
