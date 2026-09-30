<p>Cloudflare docs pages are authored in MDX, which is Markdown extended with JSX components. Every page is a <code>.mdx</code> file with a <a href="/style-guide/build-the-page/frontmatter/">frontmatter</a> block at the top, followed by the body content.</p>
<h2 id="body-content">Body content</h2>
<p>The body is standard Markdown. Use it for headings, paragraphs, lists, tables, links, and code:</p>
<pre><code class="language-md">&#35;# A heading&#10;&#10;A paragraph with a [link](/style-guide/) and `inline code`.&#10;&#10;&#45; A list item&#10;&#45; Another list item&#10;</code></pre>
<p>Refer to the <a href="/style-guide/style-and-grammar/formatting/">formatting</a> section for the rules that govern how to write each of these elements.</p>
<h2 id="import-components">Import components</h2>
<p>Components add formatting that plain Markdown cannot, such as tabs, asides, and collapsible sections. Import them from <code>~/components</code> after the frontmatter block, then add them anywhere in the body:</p>
<pre><code class="language-mdx">&#45;--&#10;title: Example page&#10;&#45;--&#10;&#10;import { Aside } from &quot;~/components&quot;;&#10;&#10;&lt;Aside type=&quot;note&quot;&gt;This is an aside.&lt;/Aside&gt;&#10;</code></pre>
<p>Refer to the <a href="/style-guide/build-the-page/components/">components</a> section for the props and requirements of each component.</p>
<h2 id="escape-special-characters">Escape special characters</h2>
<p>MDX treats <code>{</code>, <code>}</code>, <code>&lt;</code>, and <code>&gt;</code> as syntax. When these characters are part of your content rather than code, wrap them in backticks so they render literally:</p>
<pre><code class="language-md">Set the value to `{&quot;key&quot;: &quot;value&quot;}`.&#10;</code></pre>
<p>Characters inside a fenced code block are already literal and do not need escaping.</p>
<h2 id="code-blocks">Code blocks</h2>
<p>Open a fenced code block with a lowercase language identifier so the code is highlighted correctly. Use <code>txt</code> for generic output that has no language:</p>
<pre><code class="language-md">&#10;</code></pre>
<p>const value = 1;</p>
<pre><code>&#10;</code></pre>
<p>Deployment complete.</p>
<pre><code>&#10;</code></pre>
