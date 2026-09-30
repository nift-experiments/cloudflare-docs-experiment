<p>Use the conventions described below throughout Cloudflare product content.</p>
<p><a href="/style-guide/style-and-grammar/formatting/code-block-guidelines/">Learn about code block formatting guidelines</a></p>
<h2 id="angle-brackets">Angle brackets ( <code>&lt;</code> and <code>&gt;</code> )</h2>
<p>Use angle brackets to denote placeholders for variables you want the user to enter (except in <a href="/style-guide/api-content-strategy/guidelines-for-curl-commands/#request-guidelines">API URLs and API authentication headers</a>, where you should use the <code>$ZONE_ID</code> / <code>$CLOUDFLARE_API_TOKEN</code> format). Placeholder text should have all capital letters and use underscores (<code>_</code>) to separate words.</p>
<p>Examples:</p>
<pre><code>{&#10;  &quot;description&quot;: &quot;&lt;RULE_DESCRIPTION&gt;&quot;&#10;}&#10;</code></pre>
<pre><code>https://&lt;YOUR_DOMAIN&gt;.cloudflare.com&#10;</code></pre>
<p>Angle brackets that contain numbers separated by an ellipsis represent a range of values associated with a bit or single name - for example, AO <code>&lt;0...3&gt;</code>.</p>
<h2 id="square-brackets-and">Square brackets ( <code>[</code> and <code>]</code> )</h2>
<p>Square brackets enclose optional items.</p>
<p>Example:</p>
<p>Specify a subsearch that starts with this search command: <code>tag=dns query [search tag=malware].</code></p>
<h2 id="curly-braces-and">Curly braces ( <code>{</code> and <code>}</code> )</h2>
<p>As a general rule, do not use curly braces for URL or variable placeholders. Instead, refer to <a href="#angle-brackets---and--">angle brackets</a>.</p>
<p>Curly braces are acceptable around parameter names when referring to a specific API schema path (for example, <code>/api/v4/{account_id}</code>). However, in API examples (<code>curl</code> blocks or <a href="/style-guide/build-the-page/components/api-request/"><code>APIRequest</code></a> blocks) use shell variables instead (for example, <code>$ACCOUNT_ID</code>). The <code>APIRequest</code> component handles this automatically for variables in the API operation's URL path. For more information, refer to <a href="/style-guide/api-content-strategy/guidelines-for-curl-commands/">Guidelines for cURL commands</a>.</p>
<h2 id="section"><blockquote>
</blockquote></h2>
<p>The &gt; symbol leads you through nested menu items and dialog box options to a final action. The sequence <strong>Options &gt; Settings &gt; General</strong> directs you to pull down the <strong>Options</strong> menu, select the <strong>Settings</strong> item, and select <strong>General</strong> from the last dialog box. Do not use bold formatting for the &gt; symbol.</p>
<h2 id="tip-icon">Tip icon</h2>
<p>This icon denotes a tip, which alerts you to advisory information.</p>
<h2 id="note-icon">Note icon</h2>
<p>This icon denotes a note, which alerts you to important information.</p>
<h2 id="info-icon">Info icon</h2>
<p>This icon denotes info, which alerts you to important information.</p>
<h2 id="notice-icon">Notice icon</h2>
<p>This icon denotes a notice, which alerts you to take precautions to avoid data loss, loss of signal integrity, or degradation of performance.</p>
<h2 id="caution-icon">Caution icon</h2>
<p>This icon denotes a caution, which advises you to take precautions to avoid injury.</p>
<h2 id="blue-text">Blue text</h2>
<p>Text in this color indicates a link.</p>
<h2 id="bold"><strong>Bold</strong></h2>
<p>Use <strong>bold</strong> when referring to a clickable action or to highlight a title or name in the UI. Bold text denotes items that you must select or click in the software, identifiers in the UI, or parameter names.</p>
<p>Do not use bold for programs.</p>
<p>In nested menus, use bold for the word not the symbol.</p>
<p>Example: <strong>Dashboard</strong> &gt; <strong>This</strong> &gt; <strong>That</strong></p>
<h2 id="italics"><em>Italics</em></h2>
<p>Use <em>italics</em> when referring to an option that customers can select from, like in dropdown menus.</p>
<p>Do not use italics when referring to the state of a toggle - for example, enabled/disabled should not be italicized.</p>
<h2 id="monospace"><code>Monospace</code></h2>
<p><code>`text in between backticks`</code></p>
<p>Text in this font denotes text or characters that you should enter from the keyboard, sections of code, programming examples, and syntax examples. This font is also used for the proper names of drives, paths, directories, programs, subprograms, devices, functions, operations, variables, files, API commands, and extensions.</p>
<h3 id="examples-of-elements-we-monospace">Examples of elements we monospace</h3>
<table>
<thead>
<tr>
<th>Element</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td>IP addresses and ranges</td>
<td>Change your system + DNS servers to use <code>127.0.1.1</code>.</td>
</tr>
<tr>
<td>Port numbers</td>
<td>Requests are redirected through the HTTP service (port <code>80</code>).</td>
</tr>
<tr>
<td>API commands</td>
<td>The endpoint supports <code>GET</code> for JSON format.</td>
</tr>
<tr>
<td>Terminal commands</td>
<td>Run the command <code>wrangler login</code>.</td>
</tr>
<tr>
<td>Attribute names and values</td>
<td><code>type</code>, <code>name</code></td>
</tr>
<tr>
<td>Class names</td>
<td><code>button-primary</code></td>
</tr>
<tr>
<td>Command-line utility names</td>
<td><code>wrangler</code>, <code>npm</code>, <code>node</code>, <code>cloudflared</code></td>
</tr>
<tr>
<td>Data types</td>
<td>(<code>string</code>, <code>number</code>, <code>int64</code>)</td>
</tr>
<tr>
<td>Defined (constant) values for an element or attribute</td>
<td><code>&lt;A_BINDING_NAME&gt;</code></td>
</tr>
<tr>
<td>DNS record types</td>
<td>The bot will default to looking for <code>AAAA</code> records. <br/>However, you may use regular formatting (for example, AAAA) if there are multiple inline occurrences or if the text is a hyperlink.</td>
</tr>
<tr>
<td>Enum (enumerator) names (depending on language)</td>
<td><code>type ContentTypeMapElem</code></td>
</tr>
<tr>
<td>Environment variable names</td>
<td><code>&lt;A_BINDING_NAME&gt;</code></td>
</tr>
<tr>
<td>Element names, including angle brackets (XML and HTML).</td>
<td><code>&lt;span&gt;</code>, <code>&lt;form&gt;</code>, <code>&lt;input&gt;</code>, <code>&lt;code&gt;</code></td>
</tr>
<tr>
<td>Filenames, filename extensions (if used), and paths</td>
<td><code>wrangler.toml</code>, <code>wrangler.jsonc</code></td>
</tr>
<tr>
<td>Folders and directories</td>
<td><code>~/Downloads/Cloudflare_CA.crt</code></td>
</tr>
<tr>
<td>HTTP verbs</td>
<td><code>POST</code>, <code>GET</code>, <code>HEAD</code>, <code>PUT</code>,<code>DELETE</code></td>
</tr>
<tr>
<td>HTTP status codes</td>
<td><code>400</code>, <code>200</code>, <code>500</code><br/>However, error ranges using <code>x</code> placeholders should not be monospaced: 5xx, 1xxxx.</td>
</tr>
<tr>
<td>HTTP content-type values</td>
<td><code>text/html</code>, <code>application/javascript; charset=utf-8</code></td>
</tr>
<tr>
<td>HTTP header names</td>
<td><code>Content-Length</code></td>
</tr>
<tr>
<td>URLs that are used as input or output in commands and code</td>
<td><code>VERSION-dot-SERVICE-dot-PROJECT_ID.REGION_ID.r.appspot.com</code></td>
</tr>
<tr>
<td>IAM role names</td>
<td><code>roles/storage.admin</code></td>
</tr>
<tr>
<td>Language keywords</td>
<td><code>in</code>, <code>await</code></td>
</tr>
<tr>
<td>Method and function names</td>
<td><code>handleRequest</code></td>
</tr>
<tr>
<td>Namespace aliases</td>
<td><code>numpy</code></td>
</tr>
<tr>
<td>Placeholder variables</td>
<td><code>&lt;YOUR_BUILD_DIR&gt;</code></td>
</tr>
<tr>
<td>Query parameter names and values</td>
<td><code>/api/v4/{account_id}</code></td>
</tr>
<tr>
<td>Text input</td>
<td><code>&quot;Hello Worker&quot;</code></td>
</tr>
</tbody>
</table>
