<p>Our <a href="/changelog/">changelogs</a> are published to <a href="/fundamentals/new-features/available-rss-feeds/">various RSS feeds</a> with HTML in the <code>&lt;description&gt;</code> tag.</p>
<p>In feeds with multiple products, such as the global or product-area feeds, the products associated with a given entry are in the <code>&lt;category&gt;</code> tag.</p>
<p>A single product will also appear in the custom <code>&lt;product&gt;</code> tag for legacy reasons, but we recommend you use the <code>&lt;category&gt;</code></p>
<h2 id="example-xml">Example XML</h2>
<pre><code class="language-xml">&lt;rss version=&quot;2.0&quot;&gt;&#10;	&lt;channel&gt;&#10;		&lt;title&gt;Cloudflare changelogs&lt;/title&gt;&#10;		&lt;description&gt;Updates to various Cloudflare products&lt;/description&gt;&#10;		&lt;link&gt;https://developers.cloudflare.com/changelog/&lt;/link&gt;&#10;		&lt;item&gt;&#10;			&lt;title&gt;Agents, Workers, Workflows - Build AI Agents with Example Prompts&lt;/title&gt;&#10;			&lt;link&gt;https://developers.cloudflare.com/changelog/2025-02-14-example-ai-prompts/&lt;/link&gt;&#10;			&lt;guid isPermaLink=&quot;true&quot;&gt;https://developers.cloudflare.com/changelog/2025-02-14-example-ai-prompts/&lt;/guid&gt;&#10;			&lt;description&gt;&#10;				&lt;p&gt;&#10;					We&#x27;ve added an &lt;a href=&quot;https://developers.cloudflare.com/workers/get-started/prompting/&quot;&gt;example prompt&lt;/a&gt; to help you get started with building AI agents and applications on Cloudflare ...&#10;				&lt;/p&gt;&#10;			&lt;/description&gt;&#10;			&lt;pubDate&gt;Fri, 14 Feb 2025 19:00:00 GMT&lt;/pubDate&gt;&#10;			&lt;product&gt;Agents&lt;/product&gt;&#10;			&lt;category&gt;Agents&lt;/category&gt;&#10;			&lt;category&gt;Workers&lt;/category&gt;&#10;			&lt;category&gt;Workflows&lt;/category&gt;&#10;		&lt;/item&gt;&#10;	&lt;/channel&gt;&#10;&lt;/rss&gt;&#10;</code></pre>
<h2 id="related-resources">Related resources</h2>
<p>You can surface RSS feeds in several different providers, including:</p>
<ul>
<li><a href="https://slack.com/help/articles/218688467-Add-RSS-feeds-to-Slack">Slack</a></li>
<li><a href="https://learn.microsoft.com/en-us/microsoftteams/m365-custom-connectors">Microsoft Teams</a></li>
<li><a href="https://developers.google.com/workspace/chat/quickstart/webhooks">Google Chat</a></li>
</ul>
