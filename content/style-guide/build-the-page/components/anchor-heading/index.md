<p>The <code>AnchorHeading</code> component defines headings. Specifically, <code>AnchorHeading</code> performs the following:</p>
<ol>
<li>Generates URL fragments corresponding to headings.</li>
<li>Formats URL fragments into compatible syntax. For example, a <code>&amp;</code> is replaced with a <code>-</code>.</li>
<li>Creates a button to copy the URL at each fragment.</li>
<li>Allows heading fragments to be defined separately from the text of the heading itself.</li>
</ol>
<pre><code class="language-mdx">import { AnchorHeading } from &quot;~/components&quot;;&#10;&#10;&lt;AnchorHeading title=&quot;How to use AnchorHeading&quot; slug=&quot;use-anchorheading&quot; depth={2} /&gt;&#10;</code></pre>
<p>Markdown files (including partials) have this behavior by default, applied via rehype plugins. Therefore, the <code>AnchorHeading</code> component is usually only required when writing headings yourself inside components, or when working on non-markdown files.</p>
<p>To override the ID given to a heading within Markdown, add an MDX comment at the end of the line:</p>
<pre><code class="language-mdx">&#35;# foo {/*bar*/}&#10;{/* HTML: &lt;h2 id=&quot;bar&quot;&gt;foo&lt;/h2&gt; */}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14659.md")
</aside>
