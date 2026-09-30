<p>A navigation page is a sub-landing page that points a reader deeper into a specific area of the documentation. It carries almost no prose of its own: a short introduction and an automatically generated listing of the child pages under it. The tone is brief and functional.</p>
<h2 id="when-to-use-it">When to use it</h2>
<p>Write a navigation page when an area of the documentation has enough child pages that a reader needs a signposted entry point into them. It is not:</p>
<ul>
<li><strong>An overview.</strong> An overview introduces a product and orients a new reader with prose, whereas a navigation page mainly signposts the child pages under it.</li>
<li><strong>A concept.</strong> A concept explains how something works, whereas a navigation page explains nothing and only routes the reader onward.</li>
</ul>
<p>For the full comparison, refer to <a href="/style-guide/documentation-content-strategy/content-types/">Content types</a>.</p>
<h2 id="title-description">Title &amp; description</h2>
<ul>
<li><strong>Title</strong>: name the section or area the page fronts, matching the heading a reader clicked to arrive.</li>
<li><strong>Description</strong>: invite the reader to explore the area, and name the key topics the child pages cover.</li>
</ul>
<h2 id="scaffold-this-page">Scaffold this page</h2>
<p>Copy this skeleton and adapt it to your area:</p>
<pre><code>&#45;--&#10;title: &lt;Section or area name&gt;&#10;description: Explore &lt;area&gt;, covering &lt;the key topics the child pages cover&gt;.&#10;pcx_content_type: navigation&#10;sidebar:&#10;  order: 10&#10;products:&#10;  &#45; product-a&#10;&#45;--&#10;&#10;import { DirectoryListing } from &quot;~/components&quot;;&#10;&#10;Introduce the area in one or two sentences, then let the listing route the reader to the child pages.&#10;&#10;&lt;DirectoryListing /&gt;&#10;</code></pre>
<h2 id="component-guidance">Component guidance</h2>
<ul>
<li><a href="/style-guide/build-the-page/components/directory-listing/"><strong>DirectoryListing</strong></a> carries the body of the page: it displays the child pages of a folder as a list of links, generated automatically so the listing stays current as pages are added or removed.</li>
<li><strong>What does not fit:</strong> substantive explanation or procedures. A navigation page holds no content of its own, so put explanations on the pages it links to.</li>
</ul>
<h2 id="frontmatter">Frontmatter</h2>
<pre><code class="language-yaml">pcx_content_type: navigation&#10;products:&#10;  &#45; product-a&#10;  &#45; product-b&#10;</code></pre>
<p>For more details, refer to <a href="/style-guide/build-the-page/frontmatter/custom-properties/#pcx_content_type"><code>pcx_content_type</code></a>.</p>
<h2 id="examples">Examples</h2>
<ul>
<li><a href="/logs/logpush/logpush-job/enable-destinations/">Logs: Enable destinations</a></li>
<li><a href="/cloudflare-one/networks/connectors/cloudflare-tunnel/get-started/">Cloudflare Tunnel: Get started</a></li>
</ul>
<h2 id="writing-for-ai-and-agents">Writing for AI and agents</h2>
<ul>
<li><strong>Automatic listing.</strong> Use DirectoryListing rather than a hand-written list, so the routes an agent follows are always the current child pages.</li>
<li><strong>No orphaned content.</strong> Keep explanations and procedures off the navigation page, because an agent that lands here should be routed onward, not asked to read.</li>
<li><strong>Descriptive child titles.</strong> The listing shows each child page's title, so write those titles to stand alone, because they are the only signal a reader or agent has when choosing where to go.</li>
</ul>
