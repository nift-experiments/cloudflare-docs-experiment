<p>Once you <a href="/fundamentals/api/get-started/create-token/">create your API token</a>, all API requests are authorized in the same way. Cloudflare uses the <a href="https://tools.ietf.org/html/rfc6750#section-2.1">RFC standard</a> <code>Authorization: Bearer &lt;API_TOKEN&gt;</code> interface. An example request is shown below.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID&quot; \&#10;&#45;-header &quot;Authorization: Bearer YQSn-xWAQiiEh9qM58wZNnyQS7FUdoqGIUAbrh7T&quot;&#10;</code></pre>
<p>Never send or store your API token secret in plaintext. Also be sure not to check it into code repositories, especially public ones.</p>
<p>Consider defining <a href="#environment-variables">environment variables</a> for the zone or account ID, as well as for authentication credentials (for example, the API token).</p>
<p>To format JSON output for readability in the command line, you can use a tool like <code>jq</code>, a command-line JSON processor. For more information on obtaining and installing <code>jq</code>, refer to <a href="https://stedolan.github.io/jq/download/">Download jq</a>.</p>
<p>The following example will format the curl JSON output using <code>jq</code>:</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones/$ZONE_ID&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; | jq .&#10;</code></pre>
<h2 id="using-cloudflare-s-apis">Using Cloudflare's APIs</h2>
<p>Every Cloudflare API element is fixed to a version number. The latest version is Version 4. The stable base URL for all Version 4 HTTPS endpoints is: <code>https://api.cloudflare.com/client/v4/</code></p>
<p>For specific guidance on making API calls, refer to the following resources:</p>
<ul>
<li>The product's <a href="/directory/">Developer Docs section</a> for how-to guides.</li>
<li><a href="/api/">API schema docs</a> for request and response payloads for each endpoint.</li>
<li>The first-party libraries for <a href="https://github.com/cloudflare/cloudflare-go">Go</a>, <a href="https://github.com/cloudflare/cloudflare-typescript">TypeScript</a>, <a href="https://github.com/cloudflare/cloudflare-python">Python</a>, or <a href="https://github.com/cloudflare/terraform-provider-cloudflare">HashiCorp's Terraform</a>.</li>
</ul>
<h2 id="query-parameters">Query parameters</h2>
<p>Several Cloudflare endpoints have optional query parameters to filter incoming results, such as <a href="/api/resources/zones/methods/list/">List Zones</a>.</p>
<p>When adding those query parameters, make sure you enclose the URL in double quotes <code>&quot;&quot;</code> (just like the header values), or the API call might error.</p>
<pre><code class="language-bash">curl &quot;https://api.cloudflare.com/client/v4/zones?account.id=$ACCOUNT_ID&quot; \&#10;&#45;-header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;&#10;</code></pre>
<p>You can enclose strings using either single quotes (<code>''</code>) or double quotes (<code>&quot;&quot;</code>). However, using single quotes prevents variable substitution in shells like <code>bash</code>. In the previous example, this would mean that the <code>$ACCOUNT_ID</code> and <code>$CLOUDFLARE_API_TOKEN</code> <a href="#environment-variables">environment variables</a> would not be replaced with their values.</p>
<h3 id="pagination">Pagination</h3>
<p>Sometimes there will be too many results to display via the default page size, for example you might receive the following:</p>
<pre><code class="language-txt">&quot;count&quot;: 1,&#10;&quot;page&quot;: 1,&#10;&quot;per_page&quot;: 20,&#10;&quot;total_count&quot;: 200,&#10;</code></pre>
<p>Two query parameter options exist, which can be combined to paginate across the results.</p>
<ul>
<li><code>page=x</code> enables you to select a specific page.</li>
<li><code>per_page=xx</code> enables you to adjust the number of results displayed on a page. If you select too many, you may get a timeout.</li>
</ul>
<p>An example might be <code>https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records?per_page=100&amp;page=2</code>.</p>
<p>Other options are:</p>
<ul>
<li><code>order</code>: Select the attribute to order by.</li>
<li><code>direction</code>: Either <code>ASC</code> (ascending order) or <code>DESC</code> (descending order).</li>
</ul>
<p>The available options will be listed at the end of the <code>result_info</code> of all endpoints in the <a href="/api/">API documentation</a>.</p>
<h2 id="making-api-calls-on-windows">Making API calls on Windows</h2>
<p>Recent versions of Windows 10 and 11 <a href="https://curl.se/windows/microsoft.html">already include the curl tool</a> used in the developer documentation's API examples. If you are using a different Windows version, refer to <a href="https://curl.se/windows/">Windows downloads</a> in the curl website for more information on obtaining and installing this tool.</p>
<h3 id="using-a-command-prompt-window">Using a Command Prompt window</h3>
<p>To use the Cloudflare API with curl on a Command Prompt window, you must use double quotes (<code>&quot;</code>) as string delimiters.</p>
<p>A typical <code>PATCH</code> request will be similar to the following:</p>
<pre><code class="language-txt">C:\&gt;curl --request PATCH &quot;https://api.cloudflare.com/client/v4/user/invites/{id}&quot; --header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; --header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; --data &quot;{&quot;&quot;status&quot;&quot;: &quot;&quot;accepted&quot;&quot;}&quot;&#10;</code></pre>
<p>To escape a double quote character in a request body (for example, a body specified with <code>-d</code> or <code>--data</code> in a <code>POST</code>/<code>PATCH</code> request), prepend it with another double quote (<code>&quot;</code>) or a backslash (<code>\</code>) character.</p>
<p>To break a single command in two or more lines, use <code>^</code> as the line continuation character at the end of a line:</p>
<pre><code class="language-txt">C:\&gt;curl --request PATCH ^&#10;&quot;https://api.cloudflare.com/client/v4/user/invites/{id}&quot; ^&#10;&#45;-header &quot;X-Auth-Email: &lt;EMAIL&gt;&quot; ^&#10;&#45;-header &quot;X-Auth-Key: &lt;API_KEY&gt;&quot; ^&#10;&#45;-data &quot;{&quot;&quot;status&quot;&quot;: &quot;&quot;accepted&quot;&quot;}&quot;&#10;</code></pre>
<h3 id="using-powershell">Using PowerShell</h3>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/8980.md")
</aside>
<p>PowerShell has specific cmdlets (<code>Invoke-RestMethod</code> and <code>ConvertFrom-Json</code>) for making REST API calls and handling JSON responses. The syntax for these cmdlets is different from the curl examples provided in the developer documentation.</p>
<p>The following example uses the <code>Invoke-RestMethod</code> cmdlet:</p>
<pre><code class="language-powershell">Invoke-RestMethod -URI &quot;https://api.cloudflare.com/client/v4/zones/$Env:ZONE_ID/ssl/certificate_packs?ssl_status=all&quot; -Method &#x27;GET&#x27; -Headers @{&#x27;X-Auth-Email&#x27;=$Env:CLOUDFLARE_EMAIL;&#x27;X-Auth-Key&#x27;=$Env:CLOUDFLARE_API_KEY}&#10;</code></pre>
<pre><code class="language-txt">result      : {@{id=78411cfa-5727-4dc1-8d4a-773d01f17c7c; type=universal; hosts=System.Object[];&#10;              primary_certificate=c173c8a1-9724-4e96-a748-2c4494186098; status=active; certificates=System.Object[];&#10;              created_on=2022-12-09T23:11:06.010263Z; validity_days=90; validation_method=txt;&#10;              certificate_authority=lets_encrypt}}&#10;result_info : @{page=1; per_page=20; total_pages=1; count=1; total_count=1}&#10;success     : True&#10;errors      : {}&#10;messages    : {}&#10;</code></pre>
<p>The command assumes that the environment variables <code>ZONE_ID</code>, <code>CLOUDFLARE_EMAIL</code>, and <code>CLOUDFLARE_API_KEY</code> have been previously defined. For more information, refer to <a href="#environment-variables">Environment variables</a>.</p>
<p>By default, the output will only contain the first level of the JSON object hierarchy (in the above example, the content of objects such as <code>hosts</code> and <code>certificates</code> is not shown). To show additional levels and format the output like the <code>jq</code> tool, you can use the <code>ConvertFrom-Json</code> cmdlet specifying the desired maximum depth (by default, <code>2</code>):</p>
<pre><code class="language-powershell">Invoke-RestMethod -URI &quot;https://api.cloudflare.com/client/v4/zones/$Env:ZONE_ID/ssl/certificate_packs?ssl_status=all&quot; -Method &#x27;GET&#x27; -Headers @{&#x27;X-Auth-Email&#x27;=$Env:CLOUDFLARE_EMAIL;&#x27;X-Auth-Key&#x27;=$Env:CLOUDFLARE_API_KEY} | ConvertTo-Json -Depth 5&#10;</code></pre>
<pre><code class="language-json">{&#10;	&quot;result&quot;: [&#10;		{&#10;			&quot;id&quot;: &quot;78411cfa-5727-4dc1-8d4a-773d01f17c7c&quot;,&#10;			&quot;type&quot;: &quot;universal&quot;,&#10;			&quot;hosts&quot;: [&quot;*.example.com&quot;, &quot;example.com&quot;],&#10;			&quot;primary_certificate&quot;: &quot;c173c8a1-9724-4e96-a748-2c4494186098&quot;,&#10;			&quot;status&quot;: &quot;active&quot;,&#10;			&quot;certificates&quot;: [&#10;				{&#10;					&quot;id&quot;: &quot;c173c8a1-9724-4e96-a748-2c4494186098&quot;,&#10;					&quot;hosts&quot;: [&quot;*.example.com&quot;, &quot;example.com&quot;],&#10;					&quot;issuer&quot;: &quot;LetsEncrypt&quot;,&#10;					&quot;signature&quot;: &quot;ECDSAWithSHA384&quot;,&#10;					&quot;status&quot;: &quot;active&quot;,&#10;					&quot;bundle_method&quot;: &quot;ubiquitous&quot;,&#10;					&quot;zone_id&quot;: &quot;&lt;ZONE_ID&gt;&quot;,&#10;					&quot;uploaded_on&quot;: &quot;2023-02-02T11:20:25.403338Z&quot;,&#10;					&quot;modified_on&quot;: &quot;2022-12-08T00:26:15.577555Z&quot;,&#10;					&quot;expires_on&quot;: &quot;2023-03-07T23:26:12.000000Z&quot;,&#10;					&quot;priority&quot;: null&#10;				}&#10;			],&#10;			&quot;created_on&quot;: &quot;2022-12-09T23:11:06.010263Z&quot;,&#10;			&quot;validity_days&quot;: 90,&#10;			&quot;validation_method&quot;: &quot;txt&quot;,&#10;			&quot;certificate_authority&quot;: &quot;lets_encrypt&quot;&#10;		}&#10;	]&#10;	// (...)&#10;}&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="convertfrom-json-handling-of-datetime-values">ConvertFrom-Json handling of DateTime values</h3>
@markup("md", "content/.markup/bodies/8979.md")
</aside>
<p>You can also use the curl tool in PowerShell. However, in PowerShell <code>curl</code> is an alias to the <code>Invoke-WebRequest</code> cmdlet, which supports a different syntax from the usual curl tool. To use curl, enter <code>curl.exe</code> instead.</p>
<p>A typical <code>PATCH</code> request with curl will be similar to the following:</p>
<pre><code class="language-powershell">curl.exe --request PATCH &quot;https://api.cloudflare.com/client/v4/user/invites/{id}&quot; --header &quot;Authorization: Bearer $Env:CLOUDFLARE_API_TOKEN&quot; --data &#x27;{\&quot;status\&quot;: \&quot;accepted\&quot;}&#x27;&#10;</code></pre>
<p>To escape a double quote (<code>&quot;</code>) character in a request body (specified with <code>-d</code> or <code>--data</code>), prepend it with another double quote (<code>&quot;</code>) or a backslash (<code>\</code>). You must escape double quotes even when using single quotes (<code>'</code>) as string delimiters.</p>
<p>To break a single command in two or more lines, use a backtick (<code>`</code>) character as the line continuation character at the end of a line:</p>
<pre><code class="language-powershell">curl.exe --request PATCH `&#10;&quot;https://api.cloudflare.com/client/v4/user/invites/{id}&quot; `&#10;&#45;-header &quot;X-Auth-Email: $Env:CLOUDFLARE_EMAIL&quot; `&#10;&#45;-header &quot;X-Auth-Key: $Env:CLOUDFLARE_API_KEY&quot; `&#10;&#45;-data &#x27;{\&quot;status\&quot;: \&quot;accepted\&quot;}&#x27;&#10;</code></pre>
<h2 id="environment-variables">Environment variables</h2>
<p>You can define environment variables for values that repeat between commands, such as the zone or account ID. The lifetime of an environment variable can be the current shell session, all future sessions of the current user, or even all future sessions of all users on the machine you are defining them.</p>
<p>You can also use environment variables for keeping authentication credentials (API token, API key, and email) and reusing them in different commands. However, make sure you define these values in the smallest possible scope (either the current shell session only or all new sessions for the current user).</p>
<p>The procedure for setting and referencing environment variables depends on your platform and shell.</p>
<h3 id="define-an-environment-variable">Define an environment variable</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="LinuxPowershellCmd"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8984.md")
</div></div>
<h3 id="reference-an-environment-variable">Reference an environment variable</h3>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="LinuxPowershellCmd"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/8988.md")
</div></div>
