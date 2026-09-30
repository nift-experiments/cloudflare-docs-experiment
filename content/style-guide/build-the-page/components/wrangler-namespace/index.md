<p>The <code>WranglerNamespace</code> component documents the available commands for a given namespace.</p>
<p>This is generated using the Wrangler version in the <a href="https://github.com/cloudflare/cloudflare-docs/blob/production/package.json"><code>cloudflare-docs</code> repository</a>.</p>
<h2 id="import">Import</h2>
<pre><code class="language-mdx">import { WranglerNamespace } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre><code class="language-mdx">import { WranglerNamespace } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerNamespace namespace=&quot;d1&quot; /&gt;&#10;</code></pre>
<h2 id="arguments">Arguments</h2>
<ul>
<li><code>namespace</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span>
<ul>
<li>The namespace to pull the related commands from (<code>d1</code>, <code>hyperdrive</code>).</li>
</ul>
</li>
<li><code>headingLevel</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">(default: 2) optional</span>
<ul>
<li>The heading level that the commands should be added at on the page, i.e <code>2</code> for <code>h2</code>.</li>
</ul>
</li>
</ul>
