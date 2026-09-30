<p>Cloudflare’s serverless platform allows you to run code at the edge to build full-stack applications with <a href="/workers/">Workers</a>. A <a href="/workers/runtime-apis/bindings/">binding</a> enables your Worker or Pages Function to interact with resources on the Cloudflare Developer Platform.</p>
<p>To use our Markdown Conversion service directly from your Workers, create an AI binding either in the Cloudflare dashboard (refer to <a href="/pages/functions/bindings/#workers-ai">AI bindings</a> for instructions), or you can update your <a href="/workers/wrangler/configuration/">Wrangler file</a>. Add the following to your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15834.md")
</div>
<h2 id="examples">Examples</h2>
<h3 id="converting-files">Converting files</h3>
<p>In this example, we fetch a PDF document and an image from R2 and feed them both to <code>env.AI.toMarkdown</code>. The result is a list of converted documents. Workers AI models are used automatically to detect and summarize the image.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15835.md")
</div>
<h3 id="getting-supported-file-formats">Getting supported file formats</h3>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15836.md")
</div>
<h2 id="methods">Methods</h2>
<h3 id="async-env-ai-tomarkdown">async env.AI.toMarkdown()</h3>
<p>Takes a document or list of documents in different formats and converts them to Markdown.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15837.md")
</div>
<h4 id="parameter">Parameter</h4>
<ul>
<li>
<p><code>files</code>: <span class="nb-type">MarkdownDocument | MarkdownDocument[]</span>- an
instance of or an array of <code>MarkdownDocument</code>s.</p>
</li>
<li>
<p><code>conversionOptions</code>: <span class="nb-type">ConversionOptions</span>- options
that control how conversion happens. See <a href="/workers-ai/features/markdown-conversion/conversion-options/">Conversion
Options</a> for
further details.</p>
</li>
</ul>
<h4 id="return-values">Return values</h4>
<ul>
<li><code>results</code>:
<span class="nb-type">Promise&lt;ConversionResult | ConversionResult[]&gt;</span>- An instance of
or an array of <code>ConversionResult</code>s.</li>
</ul>
<h4 id="markdowndocument-definition"><code>MarkdownDocument</code> definition</h4>
<ul>
<li>
<p><code>name</code> <span class="nb-type">string</span></p>
<ul>
<li>Name of the document to convert.</li>
</ul>
</li>
<li>
<p><code>blob</code> <span class="nb-type">Blob</span></p>
<ul>
<li>A new <a href="https://developer.mozilla.org/en-US/docs/Web/API/Blob/Blob">Blob</a> object with the document content.</li>
</ul>
</li>
</ul>
<h4 id="conversionresult-definition"><code>ConversionResult</code> definition</h4>
<ul>
<li>
<p><code>id</code> <span class="nb-type">string</span></p>
<ul>
<li>ID associated to this object.</li>
</ul>
</li>
<li>
<p><code>name</code> <span class="nb-type">string</span></p>
<ul>
<li>Name of the converted document. Matches the input name.</li>
</ul>
</li>
<li>
<p><code>format</code> <span class="nb-type">markdown' | 'text' | 'error</span></p>
<ul>
<li>The format of this <code>ConversionResult</code> object. Equals <code>text</code> when you set the <a href="/workers-ai/features/markdown-conversion/conversion-options/#output"><code>output.format</code></a> option to <code>text</code>.</li>
</ul>
</li>
<li>
<p><code>mimetype</code> <span class="nb-type">string</span></p>
<ul>
<li>The detected <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types">mime type</a> of the document.</li>
</ul>
</li>
<li>
<p><code>tokens</code> <span class="nb-type">number</span></p>
<ul>
<li>The estimated number of tokens of the converted document. Not present if <code>format</code> is equal to <code>error</code>.</li>
</ul>
</li>
<li>
<p><code>data</code> <span class="nb-type">string</span></p>
<ul>
<li>The content of the converted document. Not present if <code>format</code> is equal to <code>error</code>.</li>
</ul>
</li>
<li>
<p><code>error</code> <span class="nb-type">string</span></p>
<ul>
<li>The error message explaining why this conversion failed. Only present if <code>format</code> is equal to <code>error</code>.</li>
</ul>
</li>
</ul>
<h3 id="async-env-ai-tomarkdown-transform">async env.AI.toMarkdown().transform()</h3>
<p>This method is similar to <code>env.AI.toMarkdown</code> except that it is exposed through a new handle. It takes the same arguments and returns the same values.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15838.md")
</div>
<h3 id="async-env-ai-tomarkdown-supported">async env.AI.toMarkdown().supported()</h3>
<p>Returns a list of file formats that are currently supported for markdown conversion. See <a href="/workers-ai/features/markdown-conversion/supported-formats/">Supported formats</a> for the full list of file formats that can be converted into Markdown.</p>
<div class="nb-type-script-example">
@markup("md", "content/.markup/bodies/15839.md")
</div>
<h4 id="return-values-1">Return values</h4>
<ul>
<li><code>results</code>: <span class="nb-type">SupportedFormat[]</span>- An array of all
formats supported for markdown conversion.</li>
</ul>
<h4 id="supportedformat-definition"><code>SupportedFormat</code> definition</h4>
<ul>
<li>
<p><code>extension</code> <span class="nb-type">string</span></p>
<ul>
<li>Extension of files in this format.</li>
</ul>
</li>
<li>
<p><code>mimeType</code> <span class="nb-type">string</span></p>
<ul>
<li>The <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types">mime type</a> of files of this format</li>
</ul>
</li>
</ul>
