<p>The <code>ResourcesBySelector</code> component allows you to pull in documentation resources based on the <code>pcx_content_type</code> and <code>products</code> frontmatter properties.</p>
<h2 id="component">Component</h2>
<pre><code class="language-mdx">import { ResourcesBySelector } from &quot;~/components&quot;;&#10;&#10;&lt;ResourcesBySelector&#10;	directory=&quot;workers/examples/&quot;&#10;	types={[&quot;example&quot;]}&#10;	filterables={[&quot;products&quot;]}&#10;/&gt;&#10;</code></pre>
<h3 id="inputs">Inputs</h3>
<ul>
<li>
<p><code>directory</code> <span class="nb-type">string</span></p>
<p>The directory to search for resources in, relative to <code>src/content/docs/</code>. For example, for Workers tutorials, <code>directory=&quot;workers/tutorials/&quot;</code>.</p>
</li>
<li>
<p><code>filterables</code> <span class="nb-type">string[]</span></p>
<p>An array of frontmatter properties to show in the frontend filter dropdown. For example, <code>filterables={[&quot;products&quot;]}</code> will allow users to filter based on each pages' <code>products</code> frontmatter.</p>
</li>
<li>
<p><code>types</code> <span class="nb-type">string[]</span></p>
<p>An array of <code>pcx_content_type</code> values to filter which content gets pulled into the component. For example, <code>types={[&quot;example&quot;]}</code>.</p>
</li>
<li>
<p><code>products</code> <span class="nb-type">string[]</span> <span class="nb-metainfo">optional</span></p>
<p>An array of <code>products</code> values to filter which content gets pulled into the component. For example, <code>products={[&quot;D1&quot;]}</code>.</p>
</li>
<li>
<p><code>showDescriptions</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional (default true)</span></p>
<p>If set to <code>false</code>, will only show the titles of associated pages, not the showDescriptions</p>
</li>
<li>
<p><code>showLastUpdated</code> <span class="nb-type">boolean</span> <span class="nb-metainfo">optional (default false)</span></p>
<p>If set to <code>true</code>, will add the last updated date, which is added in the <a href="/style-guide/build-the-page/frontmatter/custom-properties/#properties"><code>updated</code> frontmatter value</a>.</p>
</li>
</ul>
