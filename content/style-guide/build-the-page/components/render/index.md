<p>The <code>Render</code> component allows us to include a &quot;partial&quot;, a reusable Markdown snippet, onto a page.</p>
<p>It also accepts parameters that can be used as variables within the partial, so that even content which needs slight differences between usages can be turned into a partial.</p>
<h2 id="component">Component</h2>
<pre><code class="language-mdx">import { Render } from &quot;~/components&quot;;&#10;&#10;&#10;Hello, world!&#10;</code></pre>
<h3 id="inputs">Inputs</h3>
<ul>
<li>
<p><code>file</code> <span class="nb-type">string</span></p>
<p>This should be the name of the partial, without the containing directory or file extension. For example, <code>/partials/style-guide/hello.mdx</code> would be <code>file=&quot;hello&quot;</code>.</p>
</li>
<li>
<p><code>product</code> <span class="nb-type">string</span></p>
<p>This should be the folder within <code>src/partials</code>.</p>
</li>
<li>
<p><code>params</code> <span class="nb-type">object</span> <span class="nb-metainfo">optional</span></p>
<p>If you wish to substitute values inside your partial, you can use pass params which can be referenced in your partial. Refer to <a href="#properties">properties</a>.</p>
</li>
</ul>
<h2 id="properties">Properties</h2>
<h3 id="defining-expected-properties-in-frontmatter">Defining expected properties in frontmatter</h3>
<p>Anything defined in the <code>params</code> property of the <code>Render</code> component is available inside the partial, using <a href="https://mdxjs.com/docs/using-mdx/">JavaScript expressions</a>.</p>
<p>To protect against required properties being missed, any partial that relies on <code>params</code> should also define <code>params</code> in the partial's frontmatter. This should be an array of strings, matching the property names you expect.</p>
<pre><code class="language-mdx">&#45;--&#10;params:&#10;  &#45; product&#10;&#45;--&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14630.md")
</aside>
<p>For each of the below examples, you can open the dropdown to view the partial's content.</p>
<h3 id="properties-as-a-plain-string">Properties as a plain string</h3>
<p>The below example would render <code>Hello, world!</code>.</p>
<details class="nb-details"><summary>simple-props.mdx</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14631.md")
</div></details>
<pre><code class="language-mdx">import { Render } from &quot;~/components&quot;;&#10;&#10;&#10;Hello, world!&#10;</code></pre>
<h3 id="properties-in-markdown-syntax">Properties in Markdown syntax</h3>
<p>When using JavaScript expressions, you are now &quot;inside JSX&quot; and cannot use traditional Markdown syntax. Similarly, you cannot use a JavaScript expression inside Markdown syntax.</p>
<p>Ideally, you should not use Markdown syntax, such as <code>**strong**</code> or <code>[text](link)</code>, with properties. If using JSX is not feasible, there is a <a href="/style-guide/build-the-page/components/markdown/"><code>Markdown</code></a> component that will take a <code>text</code> property.</p>
<p>The <a href="https://mdxjs.com/table-of-components/#components">MDX documentation</a> includes a mapping of common Markdown syntax to their equivalent JSX elements.</p>
<h4 id="strong">Strong</h4>
<details class="nb-details"><summary>strong-in-props.mdx</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14632.md")
</div></details>
<pre><code class="language-mdx">import { Render } from &quot;~/components&quot;;&#10;&#10;&#10;&#42;*Don&#x27;t do this!**&#10;&#10;&#42;*Text**&#10;&#10;&#42;*Do this!**&#10;&#10;&lt;strong&gt;Text&lt;/strong&gt;&#10;</code></pre>
<h4 id="links">Links</h4>
<details class="nb-details"><summary>link-in-props.mdx</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14633.md")
</div></details>
<pre><code class="language-mdx">import { Render } from &quot;~/components&quot;;&#10;&#10;&#10;&#42;*Don&#x27;t do this!**&#10;&#10;This will link to `/style-guide/build-the-page/components/%7Bprops.link%7D`.&#10;&#10;[Markdown link](/style-guide/build-the-page/components/render/#links)&#10;&#10;&#42;*Do this!**&#10;&#10;This will link to `style-guide/components/render/#links`.&#10;&#10;&lt;p&gt;&#10;	&lt;a href=&quot;/style-guide/build-the-page/components/render/#links&quot;&gt;JSX link&lt;/a&gt;&#10;&lt;/p&gt;&#10;</code></pre>
<h4 id="images">Images</h4>
<details class="nb-details"><summary>image-in-props.mdx</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14634.md")
</div></details>
<pre><code class="language-mdx">import { Render } from &quot;~/components&quot;;&#10;&#10;&#10;&#42;*Don&#x27;t do this!**&#10;&#10;`![Alt text](/logo.svg)`&#10;&#10;&#42;*Do this!**&#10;&#10;&lt;img src=&quot;/logo.svg&quot; alt=&quot;Alt text&quot; /&gt;&#10;</code></pre>
<h4 id="code-blocks">Code blocks</h4>
<details class="nb-details"><summary>code-in-props.mdx</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/14635.md")
</div></details>
<pre><code class="language-mdx">import { Render } from &quot;~/components&quot;;&#10;&#10;&#10;import { Code } from &quot;~/components&quot;;&#10;&#10;&#35;### Inline&#10;&#10;&#42;*Don&#x27;t do this!**&#10;&#10;`export const foo = &#x27;bar&#x27;;`&#10;&#10;&#42;*Do this!**&#10;&#10;&lt;p&gt;&#10;	&lt;code&gt;export const foo = &#x27;bar&#x27;;&lt;/code&gt;&#10;&lt;/p&gt;&#10;&#10;&lt;hr /&gt;&#10;&#10;&#35;### Codeblocks&#10;&#10;&#42;*Don&#x27;t do this!**&#10;</code></pre>
<p>{
&quot;export const foo = 'bar';&quot;;
}</p>
<pre><code>&#10;&#42;*Do this!**&#10;&#10;&lt;Code code=&quot;export const foo = &amp;#x27;bar&amp;#x27;;&quot; lang=&quot;js&quot; /&gt;&#10;</code></pre>
