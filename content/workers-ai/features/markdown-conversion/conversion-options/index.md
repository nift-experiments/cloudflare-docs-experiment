<p>By default, the <code>toMarkdown</code> service extracts text content from your files. To further extend the capabilities of the conversion process, you can pass options to the service to control how specific file types are converted.</p>
<p>Options are organized by file type and are all optional.</p>
<h2 id="available-options">Available options</h2>
<h3 id="output">Output</h3>
<pre><code class="language-typescript">{&#10;  output?: {&#10;    format?: &#x27;markdown&#x27; | &#x27;text&#x27;;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li><code>format</code>: controls the format of the converted content. Defaults to <code>markdown</code>. Set to <code>text</code> to receive plain text with Markdown syntax removed.</li>
</ul>
<p>When <code>format</code> is <code>text</code>, the <code>format</code> field of the <a href="/workers-ai/features/markdown-conversion/usage/binding/#conversionresult-definition"><code>ConversionResult</code></a> is also set to <code>text</code>.</p>
<h3 id="images">Images</h3>
<pre><code class="language-typescript">{&#10;  image?: {&#10;    descriptionLanguage?: &#x27;en&#x27; | &#x27;it&#x27; | &#x27;de&#x27; | &#x27;es&#x27; | &#x27;fr&#x27; | &#x27;pt&#x27;;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li><code>descriptionLanguage</code>: controls the language of the AI-generated image descriptions.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15818.md")
</aside>
<h3 id="html">HTML</h3>
<pre><code class="language-typescript">{&#10;  html?: {&#10;    hostname?: string;&#10;    cssSelector?: string;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li>
<p><code>hostname</code>: string to use as a host when resolving relative links inside the HTML.</p>
</li>
<li>
<p><code>cssSelector</code>: string containing a CSS selector pattern to pick specific elements from your HTML. Refer to <a href="/workers-ai/features/markdown-conversion/how-it-works/#html">how HTML is processed</a> for more details.</p>
</li>
</ul>
<h3 id="pdf">PDF</h3>
<pre><code class="language-typescript">{&#10;  pdf?: {&#10;    metadata?: boolean;&#10;  }&#10;}&#10;</code></pre>
<ul>
<li><code>metadata</code>: Previously, all converted PDF files always included metadata information when converted. This option allows you to opt-out of this behavior.</li>
</ul>
<h2 id="examples">Examples</h2>
<h3 id="binding">Binding</h3>
<p>To configure custom options, pass a <code>conversionOptions</code> object inside the second argument of the binding call, like this:</p>
<pre><code class="language-typescript">await env.AI.toMarkdown(..., {&#10;  conversionOptions: {&#10;    html: { ... },&#10;    pdf: { ... },&#10;    ...&#10;   }&#10;})&#10;</code></pre>
<h3 id="rest-api">REST API</h3>
<p>Since the REST API uses file uploads, the request's <code>Content-Type</code> will be <code>multipart/form-data</code>. As such, include a new form field with your stringified object as a value:</p>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/tomarkdown \&#10;  &#45;X POST \&#10;  &#45;H &#x27;Authorization: Bearer {API_TOKEN}&#x27; \&#10;  ...&#10;  &#45;F &#x27;conversionOptions={ &quot;html&quot;: { ... }, ... }&#x27;&#10;</code></pre>
