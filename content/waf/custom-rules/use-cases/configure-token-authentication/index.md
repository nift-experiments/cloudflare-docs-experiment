<p>Token authentication allows you to restrict access to documents, files, and media to select users without requiring them to register. This helps protect paid/restricted content from leeching and unauthorized sharing.</p>
<p>There are two options to configure token authentication: via Cloudflare Workers or via custom rules.</p>
<h2 id="option-1-configure-using-cloudflare-workers">Option 1: Configure using Cloudflare Workers</h2>
<p>Refer to the following Cloudflare Workers resources for two different implementations of token authentication:</p>
<ul>
<li>The <a href="/workers/examples/signing-requests/">Sign requests</a> example.</li>
<li>The <a href="/workers/examples/auth-with-headers/">Auth with headers</a> template.</li>
</ul>
<p>To get started with Workers, refer to <a href="/workers/get-started/quickstarts/">Templates</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15462.md")
</aside>
<h2 id="option-2-configure-using-custom-rules">Option 2: Configure using custom rules</h2>
<p>Use the Rules language <a href="/ruleset-engine/rules-language/functions/#hmac-validation"><code>is_timed_hmac_valid_v0()</code></a> HMAC validation function to validate hash-based message authentication code (HMAC) tokens in a custom rule expression.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15461.md")
</aside>
<p>To validate token authentication, <a href="/waf/custom-rules/create-dashboard/">create a custom rule</a> with a call to the <code>is_timed_hmac_valid_v0()</code> function in the rule expression. You can use an action such as <em>Block</em>.</p>
<h3 id="example-rule">Example rule</h3>
<p>This example illustrates a rule that blocks any visitor that does not pass HMAC key validation on a specific hostname and URL path. Details required for token authentication include:</p>
<ul>
<li>The secret key for generating and validating the HMAC (for example, <code>mysecrettoken</code>)</li>
<li>The path you wish to authenticate (for example, <code>downloads.example.com/images/cat.jpg</code>)</li>
<li>The name of the query string parameter containing the token (for example, <code>verify</code>)</li>
<li>The token lifetime in seconds (for example, 3 hours = 10,800 seconds)</li>
</ul>
<p>Consider the following example URL:</p>
<pre><code class="language-txt">downloads.example.com/images/cat.jpg?verify=1484063787-9JQB8vP1z0yc5DEBnH6JGWM3mBmvIeMrnnxFi3WtJLE%3D&#10;</code></pre>
<p>Where:</p>
<ul>
<li><code>/images/cat.jpg</code> represents the path to the asset — the HMAC message to authenticate.</li>
<li><code>?verify=</code> is the separator between the path to the asset and the timestamp when the HMAC token was issued.</li>
<li><code>1484063787</code> represents the timestamp when the token was issued, expressed as UNIX time in seconds.</li>
<li><code>9JQB8vP1z0yc5DEBnH6JGWM3mBmvIeMrnnxFi3WtJLE%3D</code> is a Base64-encoded MAC.</li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15460.md")
</aside>
<p>The expression for the custom rule would be similar to the following:</p>
<pre><code class="language-txt">(http.host eq &quot;downloads.example.com&quot; and not is_timed_hmac_valid_v0(&quot;mysecrettoken&quot;, http.request.uri, 10800, http.request.timestamp.sec, 8))&#10;</code></pre>
<p>The components of this example custom rule (using the previous example URL) include:</p>
<ul>
<li>Token secret key = <code>mysecrettoken</code></li>
<li>Token lifetime = <code>10800</code> (10,800 seconds = 3 hours)</li>
<li><code>http.request.uri</code> = <code>/images/cat.jpg?verify=1484063787-9JQB8vP1z0yc5DEBnH6JGWM3mBmvIeMrnnxFi3WtJLE%3D</code></li>
<li><code>http.request.timestamp.sec</code> = <code>1484071925</code> (for example)</li>
<li>Separator length: <code>len(&quot;?verify=&quot;)</code> = <code>8</code></li>
</ul>
<p>The <a href="/ruleset-engine/rules-language/functions/#hmac-validation"><code>is_timed_hmac_valid_v0()</code></a> function compares the value of a MAC generated using the <code>mysecrettoken</code> secret key to the value encoded in <code>http.request.uri</code>.</p>
<p>If the MAC values match and if the token has not expired yet, according to the following formula:</p>
<pre><code class="language-txt">http.request.timestamp.sec &lt; (&lt;TIMESTAMP_ISSUED&gt; + 10800)&#10;</code></pre>
<p>Then the token is valid and the <code>is_timed_hmac_valid_v0()</code> function returns <code>true</code>.</p>
<hr />
<h2 id="hmac-token-generation">HMAC token generation</h2>
<p>The following examples show how you could generate tokens at your origin server for the path validated using the custom rule described in the previous section:</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15468.md")
</div></div>
<p>This will generate a URL parameter such as the following:</p>
<pre><code class="language-txt">verify=1484063787-9JQB8vP1z0yc5DEBnH6JGWM3mBmvIeMrnnxFi3WtJLE%3D&#10;</code></pre>
<p>You will need to append this parameter to the URL you are protecting:</p>
<pre><code class="language-txt">/images/cat.jpg?verify=1484063787-9JQB8vP1z0yc5DEBnH6JGWM3mBmvIeMrnnxFi3WtJLE%3D&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15459.md")
</aside>
<h3 id="test-the-generated-token-parameter">Test the generated token parameter</h3>
<p>If you are on an Enterprise plan, you can test if URLs are being generated correctly on the origin server by doing the following:</p>
<ol>
<li>Set the custom rule action to <em>Log</em>.</li>
<li>Check the sampled logs in <a href="/waf/analytics/security-events/">Security Events</a>.</li>
</ol>
<hr />
<h2 id="protect-several-paths-using-the-same-secret">Protect several paths using the same secret</h2>
<p>You can use the same secret key to protect several URI paths.</p>
<p>This is illustrated in the previous example, where <code>http.request.uri</code> is passed as the <a href="/ruleset-engine/rules-language/functions/#messagemac"><code>MessageMAC</code></a> argument to the validation function.</p>
<p>Since <code>http.request.uri</code> includes the path to the asset and that value is extracted for each request, the validation function evaluates all request URIs to <code>downloads.example.com</code> using the same secret key.</p>
<p>Note that while you can use the same secret key to authenticate several paths, you must generate an HMAC token for each unique message you want to authenticate.</p>
<h2 id="protect-an-entire-uri-path-prefix-with-a-single-signature">Protect an entire URI path prefix with a single signature</h2>
<p>You can protect an entire fixed-length URI path prefix with a single HMAC signature (it would also use the same secret). To achieve this, supply a URI path prefix (instead of the full URI path) and the original query string as the <a href="/ruleset-engine/rules-language/functions/#messagemac"><code>MessageMAC</code></a> argument for the <a href="/ruleset-engine/rules-language/functions/#hmac-validation"><code>is_timed_hmac_valid_v0()</code></a> function.</p>
<p>Use the <a href="/ruleset-engine/rules-language/functions/#substring"><code>substring()</code></a> function to obtain the prefix from the full URI path.</p>
<p>In the following example, the URI path prefix requiring a single HMAC signature is always 51 characters long (<code>x</code> is a character placeholder):</p>
<pre><code class="language-txt">/case-studies/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/&#10;</code></pre>
<p>In this case, you would need to use a different HMAC signature for every different URI path prefix of length 51.</p>
<p>If you wanted to block requests for case study files failing the HMAC validation, you could create a custom rule similar to the following:</p>
<div class="nb-example"><h3 class="nb-component-title" id="example">Example</h3>
@markup("md", "content/.markup/bodies/15469.md")
</div>
<p>Example URI paths of valid incoming requests:</p>
<pre><code class="language-txt">/case-studies/12345678-90ab-4cde-f012-3456789abcde/foobar-report.pdf?1755877101-5WOroVcDINdl2%2BQZxZFHJcJ6l%2Fep4HGIrX3DtSXzWO0%3D&#10;/case-studies/12345678-90ab-4cde-f012-3456789abcde/acme-corp.pdf?1755877101-5WOroVcDINdl2%2BQZxZFHJcJ6l%2Fep4HGIrX3DtSXzWO0%3D&#10;/case-studies/768bf477-22d5-4545-857d-b155510119ff/another-company-report.pdf?1755878057-jeMS5S1F3MIgxvL61UmiX4vODiWtuLfcPV6q%2B0Y3Rig%3D&#10;</code></pre>
<p>The first two URI paths can use the same HMAC signature because they share the same 51-character prefix (<code>/case-studies/12345678-90ab-4cde-f012-3456789abcde/</code>) that is validated by the custom rule.</p>
<p>The third URI path needs a different HMAC signature, since the prefix is different.</p>
