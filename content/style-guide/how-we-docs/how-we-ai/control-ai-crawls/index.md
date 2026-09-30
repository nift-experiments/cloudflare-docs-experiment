<p>Allowing AI crawlers to crawl your documentation enables end users to extract useful information from their preferred AI tool. For example, it enables users to ask tools like ChatGPT or Gemini questions about your documentation, rather than reading entire pages. However, it is important to control how the AI crawlers interact with your site for optimal results.</p>
<h2 id="instruct-ai-crawlers-to-crawl-correct-pages">Instruct AI crawlers to crawl correct pages</h2>
<p>You should first consider which pages you want AI crawlers to crawl. You may wish the AI crawler to access most of your pages, but there may be certain exceptions.</p>
<h3 id="use-robots-txt-to-control-ai-crawlers">Use <code>robots.txt</code> to control AI crawlers</h3>
<p>You can use the <code>robots.txt</code> file to control which pages AI crawlers can access. This is a simple text file which instructs crawlers to follow certain rules. The crawler is not forced to follow them, but many crawlers operated by major companies such as Google and OpenAI respect <code>robots.txt</code> files. Refer to <a href="/bots/additional-configurations/managed-robots-txt/">robots.txt setting</a> for more information.</p>
<p>For example, you can add the following to your <code>robots.txt</code> file to prevent AI crawlers from accessing a beta product called &quot;Product A&quot;, located in <code>/docs-site/product-a/</code>:</p>
<pre><code class="language-txt">User-agent: *&#10;Disallow: `/product-a/`&#10;</code></pre>
<p>By specifying explicit disallow conditions in your <code>robots.txt</code> file, you allow access to most of your pages, with only a small number of exceptions.</p>
<p>Refer to <a href="https://developers.cloudflare.com/robots.txt">https://developers.cloudflare.com/robots.txt</a> as an example.</p>
<h3 id="use-security-control-to-completely-block-access">Use security control to completely block access</h3>
<p>Sometimes, you may wish to completely block crawlers from accessing a certain page. You cannot solely rely on <code>robots.txt</code> to block access, as crawlers are not forced to follow <code>robots.txt</code> files.</p>
<p>To ensure complete blocking, you can use security controls, such as Cloudflare's <a href="/ai-crawl-control/">AI Crawl Control</a>, <a href="/bots/">bot solutions</a>, or some other security tool.</p>
<div class="nb-example"><h3 class="nb-component-title" id="case-study-github-preview-sites">Case study: GitHub preview sites</h3>
@markup("md", "content/.markup/bodies/14674.md")
</div>
<h2 id="action-points">Action points</h2>
<ul>
<li>Identify pages you want AI crawlers to access.</li>
<li>If you wish to guide AI crawlers, use <code>robots.txt</code> to instruct AI crawlers.</li>
<li>If you wish to completely block access to certain pages from AI crawlers, use security controls such as Cloudflare's <a href="/ai-crawl-control/">AI Crawl Control</a>, <a href="/bots/">bot solutions</a>, or some other security tool to completely block access to certain pages.</li>
<li>If your documentation site generates preview sites, make sure these sites are not being accessed by AI crawlers to improve your end user experience.</li>
</ul>
