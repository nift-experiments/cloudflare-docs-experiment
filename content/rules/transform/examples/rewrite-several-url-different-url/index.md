<p class="article-summary">Create a URL rewrite rule (part of Transform Rules) to rewrite any requests for `/images/&lt;FOLDER1&gt;/&lt;FOLDER2&gt;/&lt;FILENAME&gt;` to `/img/&lt;FILENAME&gt;`.</p>
<p>To rewrite paths like <code>/images/&lt;FOLDER1&gt;/&lt;FOLDER2&gt;/&lt;FILENAME&gt;</code> — where <code>&lt;FOLDER1&gt;</code>, <code>&lt;FOLDER2&gt;</code>, and <code>&lt;FILENAME&gt;</code> can vary — to <code>/img/&lt;FILENAME&gt;</code>, create a URL rewrite rule with a dynamic rewrite of the path component:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/13167.md")
</div>
<p>For example, this rule would rewrite the <code>/images/nature/animals/tiger.png</code> path to <code>/img/tiger.png</code>.</p>
