<p>Use footnotes to add details or context about something without distracting from the main content. We recommend using hover-activated footnotes, but you can also use plain text.</p>
<h3 id="hover-activated-footnotes">Hover-activated footnotes</h3>
<p>To add hover-activated footnotes, use the following syntax:</p>
<pre><code class="language-mdx">This is a sentence with a footnote.[^1]&#10;&#10;[^1]: A footnote adds details or context.&#10;</code></pre>
<p>With this type of footnote, you can add the numbers to the MDX file in any order and they will still display in numerical order on the page.</p>
<p>The hover ability of this type of footnote is powered by <a href="https://atomiks.github.io/tippyjs/">tippy.js</a>.</p>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14678.md")
</aside>
<h3 id="plain-text-footnotes">Plain text footnotes</h3>
<p>To add plain text footnotes, use the syntax in this example:</p>
<pre><code class="language-mdx">This is a sentence with a footnote.&lt;sup&gt;1&lt;/sup&gt;&#10;&#10;&lt;sup&gt;1&lt;/sup&gt; A footnote adds details or context.&#10;</code></pre>
<p>With this type of footnote, you can add the footnote note anywhere on the page. We recommend adding it to the bottom of the section or table where the footnote is referenced or to the bottom of the page.</p>
