<p>This component can help you create a tabbed interface to show related information more efficiently. Use it when there are different ways of getting the same thing done:</p>
<ul>
<li>Dashboard / API / Terraform</li>
<li>Different code syntax styles</li>
<li>Account-level vs zone-level navigation</li>
<li>GRE / IPsec tunnels</li>
</ul>
<h2 id="additional-guidance">Additional guidance</h2>
<p>The primary answer or core instruction should always appear in the main content flow, not exclusively inside a tab or collapsible section.</p>
<p>Use tabs for platform-specific variations (for example, Dashboard versus API versus Terraform) only after stating the general concept. Use Details for supplementary information, not for the primary answer.</p>
<pre><code class="language-mdx">import { Tabs, TabItem } from &quot;~/components&quot;;&#10;&#10;&lt;Tabs&gt;&#10;	&lt;TabItem label=&quot;Stars&quot; icon=&quot;star&quot;&gt;&#10;		Sirius, Vega, Betelgeuse&#10;	&lt;/TabItem&gt;&#10;	&lt;TabItem label=&quot;Moons&quot; icon=&quot;moon&quot;&gt;&#10;		Io, Europa, Ganymede&#10;	&lt;/TabItem&gt;&#10;&lt;/Tabs&gt;&#10;</code></pre>
<h3 id="tab-icons">Tab icons</h3>
<p>Optionally, you can choose a corresponding icon from Starlight’s <a href="https://starlight.astro.build/reference/icons/#all-icons">Icons</a> for tab labels.</p>
<h2 id="synchronize-tabs">Synchronize Tabs</h2>
<p>If you have tabs that follow a particular pattern (Dashboard / API / Terraform), add a <code>syncKey</code> parameter that includes a <code>string</code> value.</p>
<p>We use the following <code>syncKey</code> values in our docs:</p>
<ul>
<li><code>dashPlusAPI</code>: Dashboard / API / Terraform</li>
<li><code>workersExamples</code>: For different code language tabs in the Workers docs (JavaScript, TypeScript, Python, Rust)</li>
</ul>
<h3 id="example">Example</h3>
<pre><code class="language-mdx">import { Tabs, TabItem } from &quot;~/components&quot;;&#10;&#10;&lt;Tabs syncKey=&quot;dashPlusAPI&quot;&gt; &lt;TabItem label=&quot;Dashboard&quot;&gt;&#10;&#10;Dash instructions&#10;&#10;&lt;/TabItem&gt; &lt;TabItem label=&quot;API&quot;&gt;&#10;&#10;API instructions&#10;&#10;&lt;/TabItem&gt; &lt;/Tabs&gt;&#10;</code></pre>
<p>Will synchronize with:</p>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="dashPlusAPI"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/14629.md")
</div></div>
