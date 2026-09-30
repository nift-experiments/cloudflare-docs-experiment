---
cp9:
  canonical: https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/
  description: Fields and operators for load balancing rule expressions.
  full_title: Supported fields and operators · Cloudflare Load Balancing docs
  head_html: <title>Supported fields and operators · Cloudflare Load Balancing docs</title><meta name="generator" content="Nift"><meta name="description" content="Fields and operators for load balancing rule expressions."><link rel="canonical" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/index.md"><meta property="og:title" content="Supported fields and operators · Cloudflare Load Balancing docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Fields and operators for load balancing rule expressions."><meta property="og:url" content="https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Load Balancing"><meta name="algolia_product_filter" content="Load Balancing"><meta name="pcx_content_group" content="Application performance"><meta name="pcx_content_type" content="Reference"><meta name="algolia_content_type" content="Reference"><meta name="pcx_additional_products" content="Load Balancing"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/#page","headline":"Supported fields and operators \u00b7 Cloudflare Load Balancing docs","description":"Fields and operators for load balancing rule expressions.","url":"https://developers.cloudflare.com/load-balancing/additional-options/load-balancing-rules/reference/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /load-balancing/additional-options/load-balancing-rules/reference/
  schema: 1
---
<p>The fields that are supported by load balancing rules depend on whether Cloudflare proxies the traffic going through your load balancer or not.</p>
<p>If you use the wrong set of fields, you might see unexpected behaviors. For best results, use the fields associated with your traffic's <a href="/load-balancing/understand-basics/proxy-modes/">proxy status</a>.</p>
<p>Also, some Load Balancing rules fields are available on the Expression Builder - as described in <a href="/load-balancing/additional-options/load-balancing-rules/expressions/#working-with-expressions">Load Balancing expressions</a> - while others can only be configured manually, via API or <a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">Expression Editor</a></p>
<h2 id="expression-builder-field-sets">Expression Builder field sets</h2>
<p>Consider the following table to know how the fields available in the <a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-builder">Expression Builder</a> are grouped.</p>
<table>
<thead>
<tr>
<th>Field Set</th>
<th>Section in Expression Builder</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#fields-supported-regardless-of-proxy">Fields supported regardless of proxy</a></td>
<td><code>BOTH</code></td>
<td>Values that are always accessible regardless of the load balancer proxy status.</td>
</tr>
<tr>
<td><a href="#proxied-only-fields">Proxied-only fields</a></td>
<td><code>PROXIED ONLY</code></td>
<td>Values accessible only when the load balancer is proxied.</td>
</tr>
<tr>
<td><a href="#unproxied-only-fields">Unproxied-only fields</a></td>
<td><code>NON-PROXIED ONLY</code></td>
<td>Values accessible only when the load balancer is not proxied (DNS-only traffic).</td>
</tr>
</tbody>
</table>
<p><img src="/assets/upstream/images/load-balancing/proxy-status.png" alt="Choose load balancer fields based on the proxy status header" /></p>
<h2 id="fields-supported-regardless-of-proxy">Fields supported regardless of proxy</h2>
<p>Regardless of your traffic <a href="/load-balancing/understand-basics/proxy-modes/">proxy status</a>, Load Balancing rules can access values for the following fields:</p>
<table style="width:100%">
<thead>
<tr>
<th style="width:40%">Field</th>
<th style="width:20%">Name in Expression Builder</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr id="field-cf-load-balancer-name">
<td valign="top">
				<code>cf.load_balancer.name</code>
<br />
				`Bytes`
</td>
<td>
				<code>Load Balancer Name</code>
</td>
<td>
				<p>Represents the name of the load balancer executing these rules.</p>
				<p>
					Example value:
<br />
					<code class="InlineCode">lb.example.com</code>
				</p>
</td>
</tr>
<tr id="field-cf-load-balancer-region">
<td valign="top">
				<code>cf.load_balancer.region</code>
<br />
				`Bytes`
</td>
<td>
				<code>Load Balancer Region</code>
</td>
<td>
				<p>
					Provides the{" "}
					<a href="/load-balancing/reference/region-mapping-api/#list-of-load-balancer-regions">
						region name
					</a>{" "}
					of the data center processing the request.
				</p>
				<p>
					Example value:
<br />
					<code class="InlineCode">ENAM</code>
				</p>
</td>
</tr>
<tr id="field-ip-src">
<td valign="top">
				<code>ip.src</code>
<br />
				`IP address`
</td>
<td>
				<code>IP Source Address</code>
</td>
<td>
				<p>
					If proxied, this field provides the client TCP IP address, which may
					be adjusted to reflect the actual address of the client by using HTTP
					headers such as <code>X-Forwarded-For</code> or <code>X-Real-IP</code>
					.
				</p>
				<p>
					If unproxied (DNS-only), this field provides the ECS source address,
					if available. If not available, it provides the client resolver IP
					address.
				</p>
				<p>
					<strong>Deprecation Warning:</strong> In the future, this field will
					always be set to the client resolver IP address for unproxied
					requests. To check for the presence of ECS and use the ECS IP, see the
					fields{" "}
					<a href="#field-dns-rr-opt-client">
						<code>dns.rr.opt.client</code>
					</a>{" "}
					and{" "}
					<a href="#field-dns-rr-opt-client-addr">
						<code>dns.rr.opt.client.addr</code>
					</a>
					, respectively.
				</p>
				<p>
					Example value:
<br />
					<code class="InlineCode">1.2.3.4</code>
				</p>
</td>
</tr>
<tr id="field-asnum">
<td valign="top">
				<code>ip.src.asnum</code>
<br />
				`Number`
</td>
<td>
				<code>AS Number</code>
</td>
<td>
				<p>
					The 16-bit or 32-bit integer representing the Autonomous System (AS)
					number associated with the client IP address.
				</p>
				<p>
					Example value:
<br />
					<code class="InlineCode">13335</code>
				</p>
</td>
</tr>
</tbody>
</table>
<h2 id="proxied-only-fields">Proxied-only fields</h2>
<p>If your traffic is proxied through Cloudflare, you have access to all the fields listed under <a href="#fields-supported-regardless-of-proxy">Fields supported regardless of proxy</a> in addition to the following fields:</p>
<p>Many of these fields are referenced from the <a href="/ruleset-engine/rules-language/fields/reference/">Rules language documentation</a>.</p>
<table style="width:100%">
<thead>
<tr>
<th style="width:40%">Field</th>
<th style="width:20%">Name in Expression Builder</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr id="field-http-cookie">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.cookie/"><code>http.cookie</code></a><br />`String`</td>
<td>(<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">Manual entry only</a>)</td>
<td>
        <p>Represents the entire cookie as a string.</p>
        <p>
        Example value:
<br /><code class="InlineCode">session=8521F670545D7865F79C3D7BEDC29CCE;-background=light</code>
        </p>
</td>
</tr>
<tr id="field-http-host">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.host/"><code>http.host</code></a><br />`String`</td>
<td>(<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">Manual entry only</a>)</td>
<td>
        <p>Represents the hostname used in the full request URI.</p>
        <p>
        Example value:
<br /><code class="InlineCode">www.example.org</code>
        </p>
</td>
</tr>
<tr id="field-http-referer">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.referer/"><code>http.referer</code></a><br />`String`</td>
<td>(<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">Manual entry only</a>)</td>
<td>
        <p>Represents the HTTP Referer request header, which contains the address of the web page that linked to the currently requested page.</p>
        <p>
        Example value:
<br /><code class="InlineCode">Referer: htt&shy;ps://developer.example.org/en-US/docs/Web/JavaScript</code>
        </p>
</td>
</tr>
<tr id="field-http-request-headers">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.headers/"><code>http.request.headers</code></a><br />`Map<Array<String>>`</td>
<td><code>Header</code></td>
<td>
        <p>Represents HTTP request headers as a Map (or associative array).</p>
        <p>The keys of the associative array are the names of HTTP request headers <strong>converted to lowercase</strong>.</p>
        <p>When there are repeating headers, the array includes them in the order they appear in the request.</p>
        <p>
        <em><em>Decoding:</em></em> no decoding performed
<br /><em>Whitespace:</em> preserved
<br /><em>Non-ASCII:</em> preserved
        </p>
        <p>
        Example:
<br /><code class="InlineCode">any(http.request.headers["content-type"][*] == "application/json")</code>
        </p>
        <p>
        Example value:
<br /><code class="InlineCode">`{"content-type": ["application/json"]}`</code>
        </p>
</td>
</tr>
<tr id="field-http-request-method">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.method/"><code>http.request.method</code></a><br />`String`</td>
<td><code>Request Method</code></td>
<td>
        <p>Represents the HTTP method, returned as a string of uppercase characters.</p>
        <p>
        Example value:
<br /><code class="InlineCode">GET</code>
        </p>
</td>
</tr>
<tr id="field-http-request-timestamp-sec">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.timestamp.sec/"><code>http.request.timestamp.sec</code></a><br />`Integer`</td>
<td><code>Timestamp</code></td>
<td>
        <p>Represents the timestamp when Cloudflare received the request, expressed as Unix time in seconds. This value is 10 digits long.</p>
        <p>
        Example value:
<br /><code class="InlineCode">1484063137</code>
        </p>
</td>
</tr>
<tr id="field-http-request-uri">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri/"><code>http.request.uri</code></a><br />`String`</td>
<td><code>URI</code></td>
<td>
        <p>Represents the URI path and query string of the request.</p>
        <p>
        Example value:
<br /><code class="InlineCode">/articles/index?section=539061&expand=comments</code>
        </p>
</td>
</tr>
<tr id="field-http-request-uri-args">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.args/"><code>http.request.uri.args</code></a><br />`Map<Array<String>>`</td>
<td>(<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">Manual entry only</a>)</td>
<td>
        <p>Represents the HTTP URI arguments associated with a request as a Map (associative array).</p>
        <p>When an argument repeats, then the array contains multiple items in the order they appear in the request.</p>
        <p>
        The values are not pre-processed and retain the original case used in the request.
        </p>
        <p>
        <em>Decoding:</em> no decoding performed
<br /><em>Non-ASCII:</em> preserved
        </p>
        <p>
        Example:
<br /><code class="InlineCode">any(http.request.uri.args["search"][*] == "red+apples")</code>
        </p>
        <p>
        Example value:
<br /><code class="InlineCode">`{"search": ["red+apples"]}`</code>
        </p>
</td>
</tr>
<tr id="field-http-request-uri-args-names">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.args.names/"><code>http.request.uri.args.names</code></a><br />`Array<String>`</td>
<td>(<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">Manual entry only</a>)</td>
<td>
        <p>Represents the names of the arguments in the HTTP URI query string. The names are not pre-processed and retain the original case used in the request.</p>
        <p>When a name repeats, the array contains multiple items in the order that they appear in the request.</p>
        <p>
        <em>Decoding:</em> no decoding performed
<br /><em>Non-ASCII:</em> preserved
        </p>
        <p>
        Example:
<br /><code class="InlineCode">any(http.request.uri.args.names[*] == "search")</code>
        </p>
        <p>
        Example value:
<br /><code class="InlineCode">["search"]</code>
        </p>
</td>
</tr>
<tr id="field-http-request-uri-args-values">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.args.values/"><code>http.request.uri.args.values</code></a><br />`Array<String>`</td>
<td>(<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">Manual entry only</a>)</td>
<td>
        <p>Represents the values of arguments in the HTTP URI query string. The values are not pre-processed and retain the original case used in the request. They are in the same order as in the request.</p>
        <p>Duplicated values are listed multiple times.</p>
        <p>
        <em>Decoding:</em> no decoding performed
<br /><em>Non-ASCII:</em> preserved
        </p>
        <p>
        Example:
<br /><code class="InlineCode">any(http.request.uri.args.values[*] == "red+apples")</code>
        </p>
        <p>
        Example value:
<br /><code class="InlineCode">["red+apples"]</code>
        </p>
</td>
</tr>
<tr id="field-http-request-uri-path">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.path/"><code>http.request.uri.path</code></a><br />`String`</td>
<td><code>URI Path</code></td>
<td>
        <p>Represents the URI path of the request.</p>
        <p>
        Example value:
<br /><code class="InlineCode">/articles/index</code>
        </p>
</td>
</tr>
<tr id="field-http-request-uri-query">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.uri.query/"><code>http.request.uri.query</code></a><br />`String`</td>
<td><code>URI Query</code></td>
<td>
        <p>Represents the entire query string, without the <code class="InlineCode">?</code> delimiter.</p>
        <p>
        Example value:
<br /><code class="InlineCode">section=539061&expand=comments</code>
        </p>
</td>
</tr>
<tr id="field-http-request-version">
<td valign="top"><a href="/ruleset-engine/rules-language/fields/reference/http.request.version/"><code>http.request.version</code></a><br />`String`</td>
<td><code>HTTP Version</code></td>
<td>
        <p>Represents the version of the HTTP protocol used. Use this field when you require different checks for different versions.</p>
        <p>
        Example Values:
            <ul>
<pre tabindex="0"><code>          &lt;li&gt;&lt;code class=&quot;InlineCode&quot;&gt;HTTP/1.1&lt;/code&gt;&lt;/li&gt;&#10;          &lt;li&gt;&lt;code class=&quot;InlineCode&quot;&gt;HTTP/3&lt;/code&gt;&lt;/li&gt;&#10;&#10;        &lt;/ul&gt;&#10;    &lt;/p&gt;&#10;</code></pre>
</td>
</tr>
</tbody>
</table>
<h2 id="unproxied-only-fields">Unproxied-only fields</h2>
<p>If your traffic is not proxied through Cloudflare, you have access to all the fields listed under <a href="#fields-supported-regardless-of-proxy">Fields supported regardless of proxy</a> in addition to the following fields:</p>
<table style="width:100%">
<thead>
<tr>
<th style="width:40%">Field</th>
<th style="width:20%">Name in Expression Builder</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr id="field-dns-qry-name">
<td valign="top">
				<code>dns.qry.name</code>
<br />
				`Bytes`
</td>
<td>
				<code>Query Name</code>
</td>
<td>
				<p>Represents the query name asked.</p>
				<p>
					Example value:
<br />
					<code class="InlineCode">example.com.</code>
				</p>
</td>
</tr>
<tr id="field-dns-qry-name-len">
<td valign="top">
				<code class>dns.qry.name.len</code>
<br />
				`Integer`
</td>
<td>
				<code>Query Name Length</code>
</td>
<td>
				<p>Represents the length in bytes of the query name.</p>
				<p>
					Example value:
<br />
					<code class="InlineCode">123</code>
				</p>
</td>
</tr>
<tr id="field-dns-qry-qu">
<td valign="top">
				<code>dns.qry.qu</code>
<br />
				`Boolean`
</td>
<td>
				<code>Question</code>
</td>
<td>
				<p>
					When <code>true</code>, this field indicates that the received DNS
					message was a question.
				</p>
</td>
</tr>
<tr id="field-dns-qry-type">
<td valign="top">
				<code>dns.qry.type</code>
<br />
				`Integer`
</td>
<td>
				<code>Query Type</code>
</td>
<td>
				<p>
					Represents the numeric value of the{" "}
					<a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">
						DNS query type
					</a>
					.
				</p>
				<p>Example Values:</p>
				<ul>
<pre tabindex="0"><code>				&lt;li&gt;&#10;					&lt;code class=&quot;InlineCode&quot;&gt;1&lt;/code&gt;&amp;nbsp;(A record)&#10;				&lt;/li&gt;&#10;				&lt;li&gt;&#10;					&lt;code class=&quot;InlineCode&quot;&gt;28&lt;/code&gt;&amp;nbsp;(AAAA record)&#10;				&lt;/li&gt;&#10;&#10;			&lt;/ul&gt;&#10;</code></pre>
</td>
</tr>
<tr id="field-dns-rr-opt-client">
<td valign="top">
				<code class>dns.rr.opt.client</code>
<br />
				`Boolean`
</td>
<td>
				(
				<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">
					Manual entry only
				</a>
				)
</td>
<td>
				<p>
					When <code>true</code>, this field indicates that the EDNS Client
					Subnet (ECS) address was sent with the DNS request.
				</p>
</td>
</tr>
<tr id="field-dns-rr-opt-client-addr">
<td valign="top">
				<code class>dns.rr.opt.client.addr</code>
<br />
				`String`
</td>
<td>
				(
				<a href="/load-balancing/additional-options/load-balancing-rules/expressions/#expression-editor">
					Manual entry only
				</a>
				)
</td>
<td>
				<p>
					If present, this field represents the ECS address sent with the DNS
					request.
				</p>
				<p>
					Example value:
<br />
					<code class="InlineCode">1.2.3.0</code>
				</p>
</td>
</tr>
</tbody>
</table>
<h2 id="operators-and-grouping-symbols">Operators and grouping symbols</h2>
<ul>
<li>
<p><strong>Comparison operators</strong> specify how values defined in an expression must relate to the actual HTTP request value for the expression to return true.</p>
</li>
<li>
<p><strong>Logical operators</strong> combine two expressions to form a compound expression and use order of precedence to determine how an expression is evaluated.</p>
</li>
<li>
<p><strong>Grouping symbols</strong> allow you to organize expressions, enforce operator precedence, and nest expressions.</p>
</li>
</ul>
<p>For examples and usage, refer to <a href="/ruleset-engine/rules-language/operators/">Operators and grouping symbols</a> in the Rules language documentation.</p>
