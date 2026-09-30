<div class="nb-description">
@markup("md", "content/.markup/bodies/8720.md")
</div>
<p><a href="https://openfeature.dev/">OpenFeature</a> is the CNCF standard for feature flag interfaces. It provides a vendor-neutral API so you can switch between flag providers without changing evaluation code.</p>
<p>Flagship provides official OpenFeature-compatible SDKs for TypeScript, Python, and Go. The source code is available on <a href="https://github.com/cloudflare/flagship">GitHub</a>.</p>
<table>
<thead>
<tr>
<th>SDK</th>
<th>Package</th>
<th>Runtime</th>
<th>Evaluation modes</th>
</tr>
</thead>
<tbody>
<tr>
<td>TypeScript</td>
<td><a href="https://www.npmjs.com/package/@cloudflare/flagship"><code>@cloudflare/flagship</code></a></td>
<td>Workers, Node.js, browsers</td>
<td>Workers binding, HTTP, browser prefetch cache</td>
</tr>
<tr>
<td>Python</td>
<td><a href="https://pypi.org/project/cloudflare-flagship/"><code>cloudflare-flagship</code></a></td>
<td>Python server applications</td>
<td>HTTP</td>
</tr>
<tr>
<td>Go</td>
<td><a href="https://pkg.go.dev/github.com/cloudflare/flagship/sdks/go"><code>github.com/cloudflare/flagship/sdks/go</code></a></td>
<td>Go server applications</td>
<td>HTTP</td>
</tr>
</tbody>
</table>
<h2 id="sdks">SDKs</h2>
<p>Flagship SDKs are organized by language. The TypeScript SDK has separate setup guides for server-side and browser usage because they use different OpenFeature packages and runtime behavior.</p>
<ul>
<li><a href="/flagship/sdk/server-provider/">TypeScript Server SDK</a> — For Workers, Node.js, and other server-side JavaScript runtimes.</li>
<li><a href="/flagship/sdk/client-provider/">TypeScript Client SDK</a> — For browser applications that need synchronous OpenFeature web SDK evaluation.</li>
<li><a href="/flagship/sdk/python/">Python SDK</a> — For Python server applications.</li>
<li><a href="/flagship/sdk/go/">Go SDK</a> — For Go server applications.</li>
</ul>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8719.md")
</aside>
<h2 id="installation">Installation</h2>
<p>For TypeScript server-side usage:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/flagship @openfeature/server-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/flagship @openfeature/server-sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For TypeScript browser usage:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">bun</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm i @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm i @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn add @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn add @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm add @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm add @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>bun add @cloudflare/flagship @openfeature/web-sdk</code></pre><button type="button" data-nb-pm-copy data-nb-command="bun add @cloudflare/flagship @openfeature/web-sdk" aria-label="Copy to clipboard">Copy</button></div></div>
<p>For Python:</p>
<pre><code class="language-sh">uv add cloudflare-flagship&#10;</code></pre>
<p>For Go:</p>
<pre><code class="language-sh">go get github.com/cloudflare/flagship/sdks/go&#10;</code></pre>
<h2 id="next-steps">Next steps</h2>
<ul>
<li>Set up the <a href="/flagship/sdk/server-provider/">server provider</a> for Workers, Node.js, or other server-side runtimes.</li>
<li>Set up the <a href="/flagship/sdk/client-provider/">client provider</a> for browser applications.</li>
<li>Set up the <a href="/flagship/sdk/python/">Python SDK</a> for Python server applications.</li>
<li>Set up the <a href="/flagship/sdk/go/">Go SDK</a> for Go server applications.</li>
</ul>
