<p>When you want to provide additional information in context, but you do not want it to clutter up the more important content, use <code>&lt;Details&gt;</code> to add a collapsible container.</p>
<pre><code class="language-mdx">import { Details } from &quot;~/components&quot;;&#10;&#10;&lt;Details header=&quot;Open me!&quot;&gt;Hello, world!&lt;/Details&gt;&#10;</code></pre>
<p>You can specify the default configuration of each instance of the <code>&lt;Details&gt;</code> component (that is, whether it is open or closed by default).</p>
<pre><code class="language-mdx">import { Details } from &quot;~/components&quot;;&#10;&#10;&lt;Details header=&quot;Close me!&quot; open={true}&gt;&#10;	Long piece of code example.&#10;&lt;/Details&gt;&#10;</code></pre>
<h2 id="additional-guidance">Additional guidance</h2>
<p>The primary answer or core instruction should always appear in the main content flow, not exclusively inside a tab or collapsible section.</p>
<p>Use tabs for platform-specific variations (for example, Dashboard versus API versus Terraform) only after stating the general concept. Use Details for supplementary information, not for the primary answer.</p>
<h2 id="properties">Properties</h2>
<ul>
<li>
<p><code>header</code> <span class="nb-type">string</span> <span class="nb-metainfo">required</span></p>
</li>
<li>
<p><code>id</code> <span class="nb-type">string</span> <span class="nb-metainfo">optional</span></p>
<p>Adds a specific <code>id</code> to the HTML element</p>
</li>
<li>
<p><code>open</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional</span></p>
</li>
</ul>
