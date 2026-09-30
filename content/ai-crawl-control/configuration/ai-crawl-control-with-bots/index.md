<p>AI Crawl Control works alongside other Cloudflare products, such as Cloudflare <a href="/bots/">bot solutions</a>. Bot solutions identifies traffic matching patterns of known bots, and can challenge or block the bots as you wish.</p>
<h2 id="order-of-precedence">Order of precedence</h2>
<ul>
<li>AI Crawl Control's AI crawler blocking uses <a href="/waf/custom-rules/">WAF custom rules</a>, which take place before Cloudflare bot solutions.</li>
<li>AI Crawl Control's pay per crawl takes place after Cloudflare bot solutions.</li>
</ul>
<pre><code class="language-mermaid">graph LR&#10;A[Traffic] --&gt; B[WAF custom rules&lt;br&gt;AI Crawl Control: Crawler blocks]&#10;B --&gt; C[Cloudflare&lt;br&gt;Bot Solutions]&#10;C --&gt; D[AI Crawl Control:&lt;br&gt;Pay Per Crawl]&#10;classDef highlight fill:#F6821F,color:white&#10;</code></pre>
<p>For more information on how Cloudflare classifies bot traffic, refer to <a href="/bots/concepts/bot/#ai-bots">AI bots</a>.</p>
<h2 id="examples">Examples</h2>
<p>Consider the following examples.</p>
<h3 id="bot-rule-which-blocks-all-ai-bots-vs-pay-per-crawl">Bot rule which blocks all AI bots vs pay per crawl</h3>
<p>You may have both of the following enabled:</p>
<ul>
<li>A selection of AI crawlers to be charged through AI Crawl Control's pay per crawl</li>
<li>Bot configuration option to <a href="/bots/get-started/bot-fight-mode/#block-ai-bots">Block AI Bots</a>.</li>
</ul>
<p>Since pay per crawl happens after bot solutions, you need to first turn off <strong>Block AI Bots</strong> to ensure pay per crawl works as intended.</p>
