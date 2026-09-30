<p>Use <code>&lt;DirectoryListing /&gt;</code> to display the directory of a specific folder, which appears as a list of links.</p>
<h2 id="usage">Usage</h2>
<pre><code class="language-mdx">import { DirectoryListing } from &quot;~/components&quot;;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;Default&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; /&gt;&#10;&#10;&lt;br /&gt;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;maxDepth&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; maxDepth={2} /&gt;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;Descriptions&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; descriptions /&gt;&#10;&#10;&lt;p&gt;&#10;	&lt;strong&gt;Button&lt;/strong&gt;&#10;&lt;/p&gt;&#10;&lt;DirectoryListing folder=&quot;workers/wrangler&quot; button /&gt;&#10;</code></pre>
<h2 id="props">Props</h2>
<h3 id="folder"><code>folder</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>The folder path to list contents from. If not provided, defaults to the current page's path.</p>
<h3 id="button"><code>button</code></h3>
<p><strong>type:</strong> <code>boolean</code>
<strong>default:</strong> <code>false</code></p>
<p>When enabled, displays the listing as a 3-column grid of button-style cards (sorted alphabetically) instead of a bullet list. The cards match the style of our <a href="/style-guide/build-the-page/components/link-cards/"><code>LinkCard</code></a> component.</p>
<h3 id="descriptions"><code>descriptions</code></h3>
<p><strong>type:</strong> <code>boolean</code>
<strong>default:</strong> <code>false</code></p>
<p>When enabled, shows the <a href="/style-guide/build-the-page/frontmatter/">frontmatter <code>description</code></a> field for each page in the listing.</p>
<h3 id="maxdepth"><code>maxDepth</code></h3>
<p><strong>type:</strong> <code>number</code>
<strong>default:</strong> <code>1</code></p>
<p>Controls how many levels of nested pages to display. A value of <code>1</code> shows only direct children, while higher values will show deeper nesting levels.</p>
<h3 id="tag"><code>tag</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>Optionally, filter the listing to only pages with a specific tag.</p>
<h2 id="associated-content-types">Associated content types</h2>
<ul>
<li><a href="/style-guide/documentation-content-strategy/content-types/navigation/">Navigation</a></li>
</ul>
