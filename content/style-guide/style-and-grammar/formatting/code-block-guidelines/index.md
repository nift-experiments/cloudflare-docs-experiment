<p>To create a code block:</p>
<ul>
<li>Use triple-grave characters (<code>```</code>) as a fence, and enter a <a href="#languages">language</a> name after the first <code>```</code> fence</li>
<li>Indent lines by four spaces or one tab</li>
</ul>
<p><a href="/style-guide/style-and-grammar/formatting/code-conventions-and-format/">Learn about conventions for code blocks</a></p>
<p><a href="#add-special-formatting">Learn about code block special formatting and functionality</a></p>
<p>Here is an example of a JSON code block:</p>
<pre><code>&#10;</code></pre>
<p>{
&quot;firstName&quot;: &quot;John&quot;,
&quot;lastName&quot;: &quot;Smith&quot;,
&quot;age&quot;: 25
}</p>
<pre><code>&#10;</code></pre>
<p>The rendered output looks like this:</p>
<pre><code class="language-json">{&#10;	&quot;firstName&quot;: &quot;John&quot;,&#10;	&quot;lastName&quot;: &quot;Smith&quot;,&#10;	&quot;age&quot;: 25&#10;}&#10;</code></pre>
<h3 id="add-output">Add output</h3>
<p>To add the output of your code block, create a second code block below the first and add the <code>output</code> property to the opening code fence, like this:</p>
<pre><code class="language-sh">npx wrangler vectorize create tutorial-index --dimensions=3 --metric=cosine&#10;</code></pre>
<pre><code class="language-txt">✅ Successfully created index &#x27;tutorial-index&#x27;&#10;&#10;[[vectorize]]&#10;binding = &quot;VECTORIZE_INDEX&quot; # available in your Worker on env.VECTORIZE_INDEX&#10;index_name = &quot;tutorial-index&quot;&#10;</code></pre>
<pre><code class="language-mdx">&#10;</code></pre>
<p>npx wrangler vectorize create tutorial-index --dimensions=3 --metric=cosine</p>
<pre><code>&#10;</code></pre>
<p>✅ Successfully created index 'tutorial-index'</p>
<p>[[vectorize]]
binding = &quot;VECTORIZE_INDEX&quot; # available in your Worker on env.VECTORIZE_INDEX
index_name = &quot;tutorial-index&quot;</p>
<pre><code>&#10;</code></pre>
<h2 id="languages">Languages</h2>
<p>To define the language of your code block, enter the name of the language after the first <code>```</code> fence.</p>
<p>Language names must be lowercase. For example, use <code>javascript</code>, not <code>JavaScript</code>.</p>
<p>Use <code>txt</code> (aliases: <code>text</code>, <code>plaintext</code>) when there is no appropriate syntax language.</p>
<h3 id="terminal-commands">Terminal commands</h3>
<ul>
<li>
<p>Use the <code>sh</code> or <code>bash</code> language for commands executed in the Linux/macOS terminal, including:</p>
<ul>
<li>One-line commands</li>
<li>Commands that span multiple lines (usually each line ends with a <code>\</code>)</li>
<li>Commands for specific shells (for example, a command specifically for the <code>zsh</code> shell)</li>
</ul>
</li>
<li>
<p>Use the <code>powershell</code> language for Windows PowerShell commands. When rendered, these blocks will have a <code>PowerShell</code> title.</p>
</li>
<li>
<p>Use the <code>txt</code> language for Windows console commands.</p>
</li>
</ul>
<p>The <strong>Copy to clipboard</strong> button, available in the top-right corner of each code block, will copy the entire content of the code block, including any command output included in the block.</p>
<p>Do not include a prefix (<code>$</code>, <code>%</code>, <code>PS&gt;</code>, <code>C:\&gt;</code>, or similar) before a command so that the user can run the command immediately after copying and pasting without having to remove the prefix. Similarly, do not write the folder where the command is being executed unless it is an essential part of the explanation.</p>
<h3 id="json">JSON</h3>
<p>Use <code>json</code> for JSON code blocks or JSON fragments.</p>
<p>Multi-line curl commands with a JSON body should use the <code>sh</code> or <code>bash</code> syntax highlighting, as stated in <a href="#terminal-commands">Terminal commands</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14682.md")
</aside>
<h2 id="add-special-formatting">Add special formatting</h2>
<p>You can add special formatting to code blocks, such as collapsed sections, line numbers, and highlighting. Here is a showcase of some of the functionality. You can find more options at <a href="https://expressive-code.com/">Expressive Code</a>, a project by Astro.</p>
<pre><code class="language-mdx">&#10;</code></pre>
<p>Write-Output &quot;This one has a title&quot;</p>
<pre><code>&#10;</code></pre>
<p>// Collapsing
const foo = {
1: 1,
2: 2,
3: 3,
};</p>
<pre><code>&#10;</code></pre>
<p>// Line numbers
const foo = &quot;bar&quot;;
const bar = &quot;baz&quot;;</p>
<pre><code>&#10;</code></pre>
<p>// Example with wrap
function getLongString() {
return &quot;This is a very long string that will most probably not fit into the available space unless the container is extremely wide&quot;;
}</p>
<pre><code>&#10;</code></pre>
<p>function demo() {
console.log(&quot;These are inserted and deleted marker types&quot;);
// The return statement uses the default marker type
return true;
}</p>
<pre><code>&#10;</code></pre>
<p>function thisIsJavaScript() {
// This entire block gets highlighted as JavaScript,
// and we can still add diff markers to it!</p>
<ul>
<li>console.log('Old code to be removed')</li>
</ul>
<ul>
<li>console.log('New and shiny code!')
}</li>
</ul>
<pre><code>&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/14681.md")
</aside>
<h2 id="workers-playground">Workers Playground</h2>
<p>If you add the <code>playground</code> option to the opening code fence for a Worker example, it will add a &quot;Run Worker in Playground&quot; link that will take the user to the <a href="/workers/playground/">Worker's playground</a>.</p>
<h3 id="live-demo">Live demo</h3>
<pre><code class="language-js">export default {&#10;	fetch() {&#10;		return new Response(&quot;Test!&quot;);&#10;	},&#10;};&#10;</code></pre>
<h3 id="how-to-use">How to use</h3>
<pre><code class="language-mdx">&#10;</code></pre>
<pre><code>fetch() {&#10;	return new Response(&quot;Test!&quot;);&#10;},&#10;</code></pre>
<p>};</p>
<pre><code>&#10;</code></pre>
<h2 id="graphql-api-explorer">GraphQL API Explorer</h2>
<p>Add <code>graphql-api-explorer</code> to the opening code fence to create a <code>graphql</code> code block with a <strong>Run in GraphQL API Explorer</strong> button that leads to <a href="https://graphql.cloudflare.com/explorer">GraphQL API Explorer</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14680.md")
</aside>
<pre><code class="language-mdx">&#10;</code></pre>
<p>query ASingleDatasetExample($zoneTag: string, $start: Time, $end: Time) {
viewer {
zones(filter: { zoneTag: $zoneTag }) {
firewallEventsAdaptive(
filter: { datetime_gt: $start, datetime_lt: $end }
limit: 2
orderBy: [datetime_DESC]
) {
action
datetime
host: clientRequestHTTPHost
}
}
}
}</p>
<pre><code>&#10;</code></pre>
<h3 id="variables">Variables</h3>
<p>In the GraphQL API Explorer, the <strong>Variables</strong> section is automatically filled based on the names and types of the variables defined in your query:</p>
<ul>
<li>Variables that include <code>start</code> and are of type <code>Time</code> are set to six hours before the current time</li>
<li>Variables that include <code>end</code> and are of type <code>Time</code> are set to the current time</li>
<li>Variables that include <code>start</code> and are of type <code>Date</code> are set to 24 hours before the current date</li>
<li>Variables that include <code>end</code> and are of type <code>Date</code> are set to the current date</li>
<li>Variables that include <code>zoneTag</code> and are of type <code>string</code> are set to &quot;ZONE_ID&quot;</li>
<li>Variables that include <code>accountTag</code> and are of type <code>string</code> are set to &quot;ACCOUNT_ID&quot;</li>
<li>Variables that include <code>id</code> and are of type <code>string</code> are set to &quot;REPLACE_WITH_ID&quot;</li>
<li>Variables that include <code>limit</code> and are of type <code>int</code> are set to 100</li>
<li>Any other variable with a type of <code>string</code> is set to &quot;REPLACE_WITH_STRING&quot;</li>
</ul>
<p>You can also add custom variables by setting their values as a JSON string in the <code>graphql-api-explorer</code> metadata. The custom variables will be merged with the automatically populated variables.</p>
<p>In the following example, the custom value is <code>custom-variable</code>:</p>
<pre><code class="language-mdx">&#10;</code></pre>
<p>query GraphqlExample($zoneTag: string, $start: Time, $end: Time) {
viewer {
zones(filter: { zoneTag: $zoneTag }) {
...
}
}
}</p>
<pre><code>&#10;</code></pre>
<p>So, the <strong>Variables</strong> would look something like this:</p>
<pre><code class="language-txt">{&quot;zoneTag&quot;:&quot;ZONE_ID&quot;, &quot;start&quot;:&quot;2025-09-11T14:00:00Z&quot;, &quot;end&quot;:&quot;2025-09-11T20:00:00Z&quot;, &quot;uId&quot;:&quot;custom-variable&quot;}&#10;</code></pre>
