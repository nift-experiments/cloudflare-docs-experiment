<p class="article-summary">Create a transform rule to rewrite the URL format `/posts/&lt;YYYY&gt;-&lt;MM&gt;-&lt;DD&gt;-&lt;TITLE&gt;` to the new format `/posts/&lt;YYYY&gt;/&lt;MM&gt;/&lt;DD&gt;/&lt;TITLE&gt;`.</p>
<p>To rewrite the URLs of a blog archive that follow the URL format <code>/posts/&lt;YYYY&gt;-&lt;MM&gt;-&lt;DD&gt;-&lt;TITLE&gt;</code> to the new format <code>/posts/&lt;YYYY&gt;/&lt;MM&gt;/&lt;DD&gt;/&lt;TITLE&gt;</code>, create the following URL rewrite rule:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13171.md")
</div>
<p>The function <code>regex_replace()</code> also allows you to extract parts of the URL using regular expressions' capture groups. Create capture groups by putting part of the regular expression in parentheses. Then, reference a capture group using <code>${&lt;NUMBER&gt;}</code> in the replacement string, where <code>&lt;NUMBER&gt;</code> is the number of the capture group.</p>
