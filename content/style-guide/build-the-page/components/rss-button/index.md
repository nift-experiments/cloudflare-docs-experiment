<h2 id="example">Example</h2>
<pre><code class="language-mdx">import { RSSButton } from &quot;~/components&quot;;&#10;&#10;&lt;RSSButton changelog=&quot;Workers&quot; /&gt;&#10;&lt;br /&gt;&#10;&lt;RSSButton href=&quot;/custom/feed.xml&quot; text=&quot;Custom Feed&quot; icon=&quot;external&quot; /&gt;&#10;</code></pre>
<h2 id="props">Props</h2>
<h3 id="text"><code>text</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p><strong>default:</strong> <code>&quot;Subscribe to RSS&quot;</code></p>
<p>The text to display in the button.</p>
<h3 id="icon"><code>icon</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p><strong>default:</strong> <code>&quot;rss&quot;</code></p>
<p>The icon to display next to the text. Renders via the Nimbus <code>Icon</code> component; accepts any iconify icon name (for example, <code>ph:rss-simple</code>). The default <code>&quot;rss&quot;</code> maps to <code>ph:rss-simple</code>.</p>
<h3 id="changelog-or-href"><code>changelog</code> or <code>href</code></h3>
<p>You must provide either <code>changelog</code> or <code>href</code>, but not both:</p>
<h4 id="changelog"><code>changelog</code></h4>
<p><strong>type:</strong> <code>string</code></p>
<p>The name of the changelog to link to. This will be transformed into a lowercase, hyphen-separated string and used to construct the RSS feed URL in the format <code>/changelog/rss/{changelog}.xml</code>.</p>
<h4 id="href"><code>href</code></h4>
<p><strong>type:</strong> <code>string</code></p>
<p>A custom URL to link to. Use this when you need to link to an RSS feed that doesn't follow the standard changelog URL pattern.</p>
