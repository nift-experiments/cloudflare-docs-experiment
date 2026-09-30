<p>This component can be used to display entries from the <a href="/changelog/">changelog</a> for a given product or product area.</p>
<h2 id="import">Import</h2>
<pre><code class="language-mdx">import { ProductChangelog } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre><code class="language-mdx">import { ProductChangelog } from &quot;~/components&quot;;&#10;&#10;&lt;ProductChangelog product=&quot;workers&quot; /&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;ProductChangelog&gt;</code> Props</h2>
<p>The <code>product</code> and <code>area</code> props cannot be used at the same time.</p>
<h3 id="product"><code>product</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The name of the product.</p>
<h3 id="area"><code>area</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The name of the product area.</p>
<h3 id="hideentry"><code>hideEntry</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The id of a specific entry to hide.</p>
<h3 id="publish-future-dated-entry"><code>publish_future_dated_entry</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p><strong>default:</strong> <code>false</code></p>
<p>Set to <code>true</code> to show future-dated entries (used for WAF scheduled changelogs).</p>
<h3 id="numberofentries"><code>numberOfEntries</code></h3>
<p><strong>type:</strong> <code>number</code></p>
<p>Limits the number of entries shown.</p>
