<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="recommendation-avoid-inline-badges">Recommendation: Avoid inline badges</h3>
@markup("md", "content/.markup/bodies/14638.md")
</aside>
<h2 id="component">Component</h2>
<p>To adopt this styling in a React component, apply the <code>sl-badge</code> class to a <code>span</code> element.</p>
<pre><code class="language-mdx">import { InlineBadge } from &#x27;~/components&#x27;;&#10;&#10;&#35;## Alpha &lt;InlineBadge preset=&quot;alpha&quot; /&gt;&#10;&#10;&#35;## Beta &lt;InlineBadge preset=&quot;beta&quot; /&gt;&#10;&#10;&#35;## Deprecated &lt;InlineBadge preset=&quot;deprecated&quot; /&gt;&#10;&#10;&#35;## Early Access &lt;InlineBadge preset=&quot;early-access&quot; /&gt;&#10;&#10;&#35;## Legacy &lt;InlineBadge preset=&quot;legacy&quot; /&gt;&#10;&#10;&#35;## Default &lt;InlineBadge text=&quot;Default&quot; /&gt;&#10;</code></pre>
<h2 id="inputs">Inputs</h2>
<p>Either <code>preset</code> or <code>text</code> and <code>variant</code> must be specified.</p>
<h3 id="presets">Presets</h3>
<ul>
<li>
<p><code>alpha</code></p>
<ul>
<li><strong>Text</strong>: <code>Alpha</code></li>
<li><strong>Variant</strong> <code>success</code></li>
</ul>
</li>
<li>
<p><code>beta</code></p>
<ul>
<li><strong>Text</strong>: <code>Beta</code></li>
<li><strong>Variant</strong> <code>caution</code></li>
</ul>
</li>
<li>
<p><code>deprecated</code></p>
<ul>
<li><strong>Text</strong>: <code>Deprecated</code></li>
<li><strong>Variant</strong> <code>danger</code></li>
</ul>
</li>
<li>
<p><code>early-access</code></p>
<ul>
<li><strong>Text</strong>: <code>Early Access</code></li>
<li><strong>Variant</strong> <code>note</code></li>
</ul>
</li>
<li>
<p><code>legacy</code></p>
<ul>
<li><strong>Text</strong>: <code>Legacy</code></li>
<li><strong>Variant</strong> <code>danger</code></li>
</ul>
</li>
</ul>
<h3 id="text">Text</h3>
<p>Any string.</p>
<h3 id="variant">Variant</h3>
<ul>
<li>
<p><code>note</code></p>
<ul>
<li><strong>Color</strong>: Blue</li>
</ul>
</li>
<li>
<p><code>tip</code></p>
<ul>
<li><strong>Color</strong>: Purple</li>
</ul>
</li>
<li>
<p><code>danger</code></p>
<ul>
<li><strong>Color</strong>: Red</li>
</ul>
</li>
<li>
<p><code>caution</code></p>
<ul>
<li><strong>Color</strong>: Orange</li>
</ul>
</li>
<li>
<p><code>success</code></p>
<ul>
<li><strong>Color</strong>: Green</li>
</ul>
</li>
</ul>
