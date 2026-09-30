<h2 id="typescript-examples">TypeScript examples</h2>
<p>The <code>TypeScriptExample</code> component uses <a href="https://github.com/bloomberg/ts-blank-space"><code>ts-blank-space</code></a> to remove TypeScript-specific syntax from your example and provide a JavaScript tab. This reduces maintenance burden by only having a single example to maintain.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14626.md")
</aside>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14625.md")
</aside>
<h2 id="component">Component</h2>
<pre><code class="language-mdx">import { TypeScriptExample } from &quot;~/components&quot;;&#10;&#10;&lt;TypeScriptExample code={{&#10;  collapse: &quot;1-2&quot;&#10;}}&gt;&#10;</code></pre>
<p>// comment to demonstrate
// collapsible sections
interface Environment {
KV: KVNamespace;
}</p>
<p>async fetch(req, env, ctx): Promise<Response> {
if (req !== &quot;POST&quot;) {
return new Response(&quot;Method Not Allowed&quot;, {
status: 405,
headers: {
&quot;Allow&quot;: &quot;POST&quot;
}
});
}</p>
<pre><code>await env.KV.put(&quot;foo&quot;, &quot;bar&quot;);&#10;&#10;return new Response();&#10;</code></pre>
<p>}
} satisfies ExportedHandler<Environment></p>
<pre><code>&lt;/TypeScriptExample&gt;&#10;</code></pre>
<h2 id="props"><code>&lt;TypeScriptExample&gt;</code> Props</h2>
<h3 id="filename"><code>filename</code></h3>
<p><strong>type:</strong> <code>string</code></p>
<p>An optional filename, ending in <code>.ts</code>.</p>
<p><code>.ts</code> will be replaced by <code>.js</code> for the JavaScript tab.</p>
<h3 id="playground"><code>playground</code></h3>
<p><strong>type:</strong> <code>boolean</code></p>
<p>If set to <code>true</code>, a <a href="/style-guide/style-and-grammar/formatting/code-block-guidelines/#workers-playground"><code>Run Worker in Playground</code></a> button will appear on the JavaScript tab.</p>
<h3 id="code"><code>code</code></h3>
<p><strong>type</strong>: <code>object</code></p>
<p>Props to pass to the <a href="https://docs.astro.build/en/reference/api-reference/#code-">Astro <code>Code</code> component</a>.</p>
<p>These props will apply to both code blocks and so options like <code>collapse</code> may not work as expected, as lines may be removed from the TypeScript code.</p>
