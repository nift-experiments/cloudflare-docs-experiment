<p>AI companies use crawlers to collect website content for training language models, generating search answers, and other purposes. A <code>robots.txt</code> file at the root of your domain tells these crawlers which content they should or should not access. When you turn on the managed <code>robots.txt</code> setting, Cloudflare generates and maintains a <code>robots.txt</code> file that instructs known AI crawlers to stay away from your content.</p>
<p><code>robots.txt</code> compliance is voluntary. The file expresses your preferences, but it does not prevent crawlers from accessing your content at a technical level. Some crawler operators may disregard your <code>robots.txt</code> directives (instructions like <code>Disallow: /</code>) and crawl your content regardless.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3537.md")
</aside>
<h2 id="compatibility-with-existing-robots-txt-files">Compatibility with existing <code>robots.txt</code> files</h2>
<p>Cloudflare detects whether your origin server already has a <code>robots.txt</code> file and adjusts accordingly — either merging with your existing file or creating one from scratch.</p>
<h3 id="existing-robots-txt-file">Existing robots.txt file</h3>
<p>If your website already has a <code>robots.txt</code> file — verified by an HTTP <code>200</code> response — Cloudflare will prepend our managed <code>robots.txt</code> before your existing <code>robots.txt</code>, combining both into a single response.</p>
<p>For example, without this feature enabled, the <code>robots.txt</code> content of <code>crawlstop.com</code> would be:</p>
<pre><code class="language-txt">User-agent: *&#10;Disallow: /lp&#10;Disallow: /feedback&#10;Disallow: /langtest&#10;&#10;Sitemap: https://www.crawlstop.com/sitemap.xml&#10;</code></pre>
<p>With the managed <code>robots.txt</code> enabled, Cloudflare will prepend our managed content before your original content, resulting in what you can view at <a href="https://www.crawlstop.com/robots.txt">https://www.crawlstop.com/robots.txt</a>.</p>
<pre><code class="language-txt">&#35; As a condition of accessing this website, you agree to abide by the&#10;&#35; following content signals:&#10;&#10;&#35; (a)  If a content-signal = yes, you may collect content for the&#10;&#35;      corresponding use.&#10;&#35; (b)  If a content-signal = no, you may not collect content for the&#10;&#35;      corresponding use.&#10;&#35; (c)  If the website operator does not include a content signal for a&#10;&#35;      corresponding use, the website operator neither grants nor restricts&#10;&#35;      permission via content signal with respect to the corresponding use.&#10;&#10;&#35; The content signals and their meanings are:&#10;&#10;&#35; search: building a search index and providing search results (e.g., returning&#10;&#35;         hyperlinks and short excerpts from your website&#x27;s contents). Search&#10;&#35;         does not include providing AI-generated search summaries.&#10;&#35; ai-input: inputting content into one or more AI models (e.g., retrieval&#10;&#35;           augmented generation, grounding, or other real-time taking of&#10;&#35;           content for generative AI search answers).&#10;&#35; ai-train: training or fine-tuning AI models.&#10;&#10;&#35; ANY RESTRICTIONS EXPRESSED VIA CONTENT SIGNALS ARE EXPRESS RESERVATIONS OF&#10;&#35; RIGHTS UNDER ARTICLE 4 OF THE EUROPEAN UNION DIRECTIVE 2019/790 ON COPYRIGHT&#10;&#35; AND RELATED RIGHTS IN THE DIGITAL SINGLE MARKET.&#10;&#10;&#35; BEGIN Cloudflare Managed content&#10;&#10;User-Agent: *&#10;Content-signal: search=yes, ai-train=no, use=reference&#10;Allow: /&#10;&#10;User-agent: Amazonbot&#10;Disallow: /&#10;&#10;User-agent: Applebot-Extended&#10;Disallow: /&#10;&#10;User-agent: Bytespider&#10;Disallow: /&#10;&#10;User-agent: CCBot&#10;Disallow: /&#10;&#10;User-agent: ClaudeBot&#10;Disallow: /&#10;&#10;User-agent: Google-Extended&#10;Disallow: /&#10;&#10;User-agent: GPTBot&#10;Disallow: /&#10;&#10;User-agent: meta-externalagent&#10;Disallow: /&#10;&#10;&#35; END Cloudflare Managed Content&#10;User-agent: *&#10;Disallow: /lp&#10;Disallow: /feedback&#10;Disallow: /langtest&#10;&#10;Sitemap: https://www.crawlstop.com/sitemap.xml&#10;</code></pre>
<h3 id="no-robots-txt-file">No robots.txt file</h3>
<p>If your website does not have a <code>robots.txt</code> file, Cloudflare creates a new file with managed <code>Disallow</code> rules for known AI crawlers and serves it for you.</p>
<h2 id="implementation">Implementation</h2>
<p>To implement a <code>robots.txt</code> file on your domain:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/3538.md")
</div>
<h2 id="content-signals-policy">Content Signals Policy</h2>
<p>Content Signals are a set of machine-readable directives in a <code>robots.txt</code> file that categorize how crawlers may use your content. The three categories are <code>search</code> (building a search index), <code>ai-input</code> (feeding content into AI models for real-time answers), and <code>ai-train</code> (training or fine-tuning AI models).</p>
<p>Domains on the Free plan that do not have their own <code>robots.txt</code> file and do not use the managed <code>robots.txt</code> feature will display the Content Signals Policy when a crawler requests the <code>robots.txt</code> file for your domain.</p>
<p>The Content Signals Policy defines these categories but does not express any specific preferences about your content. To set preferences (for example, <code>ai-train=no</code>), turn on the managed <code>robots.txt</code> feature.</p>
<pre><code class="language-txt">&#35; As a condition of accessing this website, you agree to abide by the&#10;&#35; following content signals:&#10;&#10;&#35; (a)  If a content-signal = yes, you may collect content for the&#10;&#35;      corresponding use.&#10;&#35; (b)  If a content-signal = no, you may not collect content for the&#10;&#35;      corresponding use.&#10;&#35; (c)  If the website operator does not include a content signal for a&#10;&#35;      corresponding use, the website operator neither grants nor restricts&#10;&#35;      permission via content signal with respect to the corresponding use.&#10;&#10;&#35; The content signals and their meanings are:&#10;&#10;&#35; search: building a search index and providing search results (e.g., returning&#10;&#35;         hyperlinks and short excerpts from your website&#x27;s contents). Search&#10;&#35;         does not include providing AI-generated search summaries.&#10;&#35; ai-input: inputting content into one or more AI models (e.g., retrieval&#10;&#35;           augmented generation, grounding, or other real-time taking of&#10;&#35;           content for generative AI search answers).&#10;&#35; ai-train: training or fine-tuning AI models.&#10;&#10;&#35; ANY RESTRICTIONS EXPRESSED VIA CONTENT SIGNALS ARE EXPRESS RESERVATIONS OF&#10;&#35; RIGHTS UNDER ARTICLE 4 OF THE EUROPEAN UNION DIRECTIVE 2019/790 ON COPYRIGHT&#10;&#35; AND RELATED RIGHTS IN THE DIGITAL SINGLE MARKET.&#10;</code></pre>
<p>Cloudflare's Content Signals Policy is included by default in the <code>robots.txt</code> file when you turn on <strong>robots.txt setting</strong>.</p>
<p>If you would like to opt out of displaying the policy in your <code>robots.txt</code> file, you can uncheck <strong>Display Content Signals Policy</strong> under <strong>Control AI Crawlers</strong> in your zone's overview.</p>
<div class="nb-dash-button"></div>
<p>Alternatively, you can use <a href="#implementation">Security Settings</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/3536.md")
</aside>
<h2 id="content-use-signal">Content use signal</h2>
<p>Cloudflare is testing <code>content-use</code>, an optional extension to <a href="https://contentsignals.org/">Content Signals</a> that lives in your <code>robots.txt</code>. It adds a fourth field alongside the existing <code>search</code>, <code>ai-input</code>, and <code>ai-train</code> signals to describe what a crawler may keep and reuse after accessing your content. The field takes one of three values, from least to most permissive:</p>
<table>
<thead>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>use=immediate</code></td>
<td>Interact, but store and reuse nothing.</td>
</tr>
<tr>
<td><code>use=reference</code></td>
<td>Index, excerpt, and link back.</td>
</tr>
<tr>
<td><code>use=full</code></td>
<td>Summarize and reproduce.</td>
</tr>
</tbody>
</table>
<p>For customers who have turned on the managed <code>robots.txt</code> setting, Cloudflare adds <code>use=reference</code> to the managed content, in line with the existing default of <code>search=yes,ai-train=no</code>:</p>
<pre><code class="language-txt">User-Agent: *&#10;Content-signal: search=yes, ai-train=no, use=reference&#10;Allow: /&#10;</code></pre>
<h2 id="availability">Availability</h2>
<p>Managed <code>robots.txt</code> for AI crawlers is available on all plans.</p>
