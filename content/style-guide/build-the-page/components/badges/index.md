<p>Badges are a built-in component provided by <a href="https://nimbus-docs.com/components/badge/">Nimbus</a>. Use them to indicate a product is in beta, for example.</p>
<h2 id="component">Component</h2>
<pre><code class="language-mdx">import { Badge } from &quot;~/components&quot;;&#10;&#10;&lt;Badge text=&quot;Note&quot; variant=&quot;note&quot; /&gt;&#10;&lt;Badge text=&quot;Success&quot; variant=&quot;success&quot; /&gt;&#10;&lt;Badge text=&quot;Tip&quot; variant=&quot;tip&quot; /&gt;&#10;&lt;Badge text=&quot;Caution&quot; variant=&quot;caution&quot; /&gt;&#10;&lt;Badge text=&quot;Danger&quot; variant=&quot;danger&quot; /&gt;&#10;&lt;Badge text=&quot;Default&quot; /&gt;&#10;</code></pre>
<h2 id="sidebar">Sidebar</h2>
<p>Badges can be added to the sidebar via page frontmatter.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Hello World&#10;sidebar:&#10;  badge:&#10;    variant: tip&#10;    text: New&#10;&#45;--&#10;</code></pre>
<p>If you want to add the Beta badge to a product, omit the <code>variant:</code> entry:</p>
<pre><code class="language-mdx">&#45;--&#10;title: Hello World&#10;sidebar:&#10;  badge:&#10;    text: Beta&#10;&#45;--&#10;</code></pre>
