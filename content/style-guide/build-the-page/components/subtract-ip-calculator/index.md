<h2 id="import">Import</h2>
<pre><code class="language-mdx">import { SubtractIPCalculator } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<br />
<div class="nb-interactive-component" data-cf-component="SubtractIPCalculator"></div>
<pre><code class="language-mdx">import { SubtractIPCalculator } from &quot;~/components&quot;;&#10;&#10;&lt;SubtractIPCalculator client:load /&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;SubtractIPCalculator&gt;</code> Props</h2>
<h3 id="defaults"><code>defaults</code></h3>
<p><strong>type:</strong> <code>object</code></p>
<p>An optional object containing <code>base</code> (<code>string</code>) and <code>subtract</code> (<code>string[]</code>) properties, to set default inputs.</p>
<p><strong>example:</strong></p>
<div class="nb-interactive-component" data-cf-component="SubtractIPCalculator"></div>
<pre><code class="language-mdx">import { SubtractIPCalculator } from &quot;~/components&quot;;&#10;&#10;&lt;SubtractIPCalculator&#10;	client:load&#10;	defaults={{&#10;		base: &quot;10.0.0.0/8&quot;,&#10;		subtract: [&quot;10.0.0.0/24&quot;, &quot;10.32.0.0/11&quot;]&#10;	}}&#10;/&gt;&#10;</code></pre>
