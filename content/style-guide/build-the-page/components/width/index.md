<p>This component can be used to constrain the width of content, such as text or images.</p>
<h2 id="import">Import</h2>
<pre><code class="language-mdx">import { Width } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre><code class="language-mdx">import { Width } from &quot;~/components&quot;;&#10;&#10;&lt;Width size=&quot;large&quot;&gt;This content will take up 75% of the container width&lt;/Width&gt;&#10;&#10;&lt;Width size=&quot;medium&quot;&gt;&#10;	This content will take up 50% of the container width&#10;&lt;/Width&gt;&#10;&#10;&lt;Width size=&quot;small&quot;&gt;This content will take up 25% of the container width&lt;/Width&gt;&#10;&#10;&lt;Width size=&quot;small&quot; center&gt;&#10;	This content will take up 25% of the container width and be centered&#10;&lt;/Width&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;Width&gt;</code> Props</h2>
<h3 id="size"><code>size</code></h3>
<p><strong>required</strong></p>
<p><strong>type:</strong> <code>&quot;large&quot; | &quot;medium&quot; | &quot;small&quot;</code></p>
<p>Controls the width of the container:</p>
<ul>
<li><code>large</code>: 75% of container width</li>
<li><code>medium</code>: 50% of container width</li>
<li><code>small</code>: 25% of container width</li>
</ul>
<h3 id="center"><code>center</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p>Whether to horizontally center the content.</p>
