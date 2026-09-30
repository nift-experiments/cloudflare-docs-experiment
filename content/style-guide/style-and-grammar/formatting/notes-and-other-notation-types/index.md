<p>When adding a note to a page, always use this special note formatting. There are three types of formatted notes: <code>note</code>, <code>caution</code>, and <code>tip</code>.</p>
<p>Here is some additional information about notes:</p>
<ul>
<li>The color of the note depends on the type of note: <code>note</code> is blue, <code>caution</code> is yellow, and <code>tip</code> is purple.</li>
<li>For every note type, the header text is optional.</li>
<li>All note types can contain text and additional formatting like lists, code blocks, and images.</li>
</ul>
<p>To learn how notes fit into our content strategy, refer to <a href="/style-guide/documentation-content-strategy/component-attributes/notes-tips-warnings/">Notes/tips/warnings</a>.</p>
<h2 id="note">Note</h2>
<p>Use Note for small additions or when you need to provide extra context that is not essential to the main content.</p>
<p>If you do not provide a header, this aside will default to <code>Note</code>.</p>
<pre><code class="language-mdx">:::note[Header]&#10;Hello, world!&#10;:::&#10;</code></pre>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="header">Header</h3>
@markup("md", "content/.markup/bodies/14677.md")
</aside>
<h2 id="caution-warning">Caution/Warning</h2>
<p>Use Caution to highlight actions that could cause issues for a user.</p>
<p>If you do not provide a header, this aside will default to <code>Warning</code>.</p>
<pre><code class="language-mdx">:::caution[Feature conflict]&#10;If you use feature A and feature B together, your configuration will not work.&#10;:::&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="feature-conflict">Feature conflict</h3>
@markup("md", "content/.markup/bodies/14676.md")
</aside>
<h2 id="tip">Tip</h2>
<p>Use Tip to share best practices or opinionated use cases that do not fit into the main documentation.</p>
<p>If you do not provide a header, this aside will default to <code>Tip</code>.</p>
<pre><code class="language-mdx">:::tip[Best practice]&#10;Cloudflare recommends you use [1.1.1.1](/1.1.1.1/) as your DNS resolver.&#10;:::&#10;</code></pre>
<aside class="nb-aside tip">
<h3 class="nb-aside-title" id="best-practice">Best practice</h3>
@markup("md", "content/.markup/bodies/14675.md")
</aside>
