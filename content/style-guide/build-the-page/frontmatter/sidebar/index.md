<h2 id="labels">Labels</h2>
<p>Labels are controlled by frontmatter properties on a given page, which vary depending on if you are configuring a group or a link.</p>
<h3 id="links">Links</h3>
<p>In order of precedence:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14615.md")
</div>
<h4 id="on-an-index-page">On an index page</h4>
<p>Index page labels default to <code>Overview</code> if <code>sidebar.label</code> is not defined.</p>
<p><code>title</code> is not taken into consideration due to <code>title</code> being used in group labelling.</p>
<h3 id="groups">Groups</h3>
<p>In order of precedence:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/14616.md")
</div>
<h3 id="example">Example</h3>
<p>For example, given the following pages:</p>
<pre><code class="language-mdx">&#45;--&#10;title: Bar&#10;sidebar:&#10;  label: IndexTitle&#10;  group:&#10;    label: GroupTitle&#10;&#45;--&#10;</code></pre>
<pre><code class="language-mdx">&#45;--&#10;title: Baz&#10;sidebar:&#10;  label: PageTitle&#10;&#45;--&#10;</code></pre>
<p>The sidebar structure will look like:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/14617.md")&#10;&#10;&#10;</pre>
<p>If we remove the <code>sidebar</code> property from both, it will now look like this:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/14618.md")&#10;&#10;&#10;</pre>
<h2 id="ordering">Ordering</h2>
<p>Both links and groups use the <code>sidebar.order</code> frontmatter property to configure their ordering, where groups are ordered based on the index page's order.</p>
<p>If <code>sidebar.order</code> is not specified, it will fallback to alphabetical ordering.</p>
<p>For example, given the following pages:</p>
<pre><code class="language-mdx">&#45;--&#10;title: Alpha&#10;sidebar:&#10;  order: 3&#10;&#45;--&#10;</code></pre>
<pre><code class="language-mdx">&#45;--&#10;title: Beta&#10;sidebar:&#10;  order: 2&#10;&#45;--&#10;</code></pre>
<p>The sidebar structure will look like:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/14619.md")&#10;&#10;&#10;</pre>
<p>If we remove the <code>sidebar</code> property from both, it will now look like this:</p>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/14620.md")&#10;&#10;&#10;</pre>
<h2 id="hiding-pages">Hiding pages</h2>
<p>There are three properties that can be used for hiding pages from the sidebar.</p>
<h3 id="hiding-individual-pages">Hiding individual pages</h3>
<h4 id="hidden"><code>hidden</code></h4>
<p>This property should only be used when the page is <strong>not</strong> an index page for a group.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Placeholder&#10;sidebar:&#10;  hidden: true&#10;&#45;--&#10;</code></pre>
<h4 id="group-hideindex"><code>group.hideIndex</code></h4>
<p>Since index pages are relied on to configure the label and sort order of groups, we have a special property that still makes the page available to our sidebar component and allows us to remove it after labelling and ordering groups.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Placeholder&#10;sidebar:&#10;  group:&#10;    hideIndex: true&#10;&#45;--&#10;&#10;import { DirectoryListing } from &quot;~/components&quot;;&#10;&#10;&lt;DirectoryListing /&gt;&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14614.md")
</aside>
<h3 id="hiding-child-pages-of-a-group">Hiding child pages of a group</h3>
<p>To make a group render as if it was a single page, which links to the index page, use the top-level <code>hideChildren</code> property.</p>
<h2 id="badges">Badges</h2>
<h3 id="links-1">Links</h3>
<p>To specify a badge next to the link, use the <code>sidebar.badge</code> property.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Example&#10;sidebar:&#10;  badge: New!&#10;&#45;--&#10;</code></pre>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/14621.md")&#10;&#10;&#10;</pre>
<h3 id="groups-1">Groups</h3>
<p>To specify a badge next to the group label, use the <code>sidebar.group.badge</code> inside the group's <code>index.mdx</code> frontmatter.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Examples&#10;sidebar:&#10;  group:&#10;    badge: New!&#10;&#45;--&#10;</code></pre>
<pre class="nb-file-tree">&#10;&#10;&#10;@markup("md", "content/.markup/bodies/14622.md")&#10;&#10;&#10;</pre>
<h3 id="automatic-beta-badges">Automatic &quot;Beta&quot; badges</h3>
<p>A &quot;Beta&quot; badge is automatically added to sidebar links and groups whose URL matches a directory entry with a &quot;Beta&quot; availability status.
This badge is <strong>not</strong> controlled by frontmatter — it is derived from the product availability data associated with the entry in <code>src/content/directory/</code>.</p>
