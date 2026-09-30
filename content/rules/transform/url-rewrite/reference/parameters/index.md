<p>Static and dynamic URL rewrites have different parameters:</p>
<ul>
<li>A static URL rewrite requires a static value for the target URL.</li>
<li>A dynamic URL rewrite requires an expression that, when evaluated, will define the target URL.</li>
</ul>
<p>A URL rewrite with wildcard patterns is a simplified interface in the Cloudflare dashboard for creating dynamic URL rewrites with <a href="#wildcard-matching-and-replacement">wildcard matching and replacement</a>.</p>
<p>The maximum length of all parameter values in a URL rewrite (combined) is 4,096 characters. For example, you could provide a static value (or an expression) for the URI path with 2,048 characters and a static value (or expression) for the query string with 2,048 characters.</p>
<h2 id="api-information">API information</h2>
<h3 id="static-url-rewrites">Static URL rewrites</h3>
<p>The full syntax of the <code>action_parameters</code> field for a static URL rewrite rule that rewrites both the URI path and the query string is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;uri&quot;: {&#10;    &quot;path&quot;: {&#10;      &quot;value&quot;: &quot;&lt;URI_PATH_VALUE&gt;&quot;&#10;    },&#10;    &quot;query&quot;: {&#10;      &quot;value&quot;: &quot;&lt;QUERY_STRING_VALUE&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>If you are only rewriting the URI path or the query string, omit the <code>query</code> or <code>path</code> parameter, respectively.</p>
<h3 id="dynamic-url-rewrites">Dynamic URL rewrites</h3>
<p>The full syntax of the <code>action_parameters</code> field for a dynamic URL rewrite rule that rewrites both the URI path and the query string is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;uri&quot;: {&#10;    &quot;path&quot;: {&#10;      &quot;expression&quot;: &quot;&lt;URI_PATH_EXPRESSION&gt;&quot;&#10;    },&#10;    &quot;query&quot;: {&#10;      &quot;expression&quot;: &quot;&lt;QUERY_STRING_EXPRESSION&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<p>If you are only rewriting the URI path or the query string, omit the <code>query</code> or <code>path</code> parameter, respectively.</p>
<h4 id="wildcard-matching-and-replacement">Wildcard matching and replacement</h4>
<p>The syntax of a dynamic URL rewrite rule that rewrites both the URI path and the query string based on wildcard matching and replacement is the following:</p>
<pre><code class="language-json">{&#10;	&quot;expression&quot;: &quot;(http.request.full_uri wildcard r\&quot;&lt;REQUEST_URL&gt;\&quot;)&quot;,&#10;	&quot;action_parameters&quot;: {&#10;		&quot;uri&quot;: {&#10;			&quot;path&quot;: {&#10;				&quot;expression&quot;: &quot;wildcard_replace(http.request.uri.path, r\&quot;&lt;PATH_TARGET_PATH&gt;\&quot;, r\&quot;&lt;PATH_REWRITE_TO&gt;\&quot;)&quot;&#10;			},&#10;			&quot;query&quot;: {&#10;				&quot;expression&quot;: &quot;wildcard_replace(http.request.uri.query, r\&quot;&lt;QUERY_TARGET_QUERY&gt;\&quot;, r\&quot;&lt;QUERY_REWRITE_TO&gt;\&quot;)&quot;&#10;			}&#10;		}&#10;	},&#10;	&quot;action&quot;: &quot;rewrite&quot;&#10;	// ...&#10;}&#10;</code></pre>
<p>The <code>&lt;REQUEST_URL&gt;</code>, <code>&lt;PATH_TARGET_PATH&gt;</code>, <code>&lt;PATH_REWRITE_TO&gt;</code>, <code>&lt;QUERY_TARGET_QUERY&gt;</code>, and <code>&lt;QUERY_REWRITE_TO&gt;</code> value placeholders correspond to the fields available in the Cloudflare dashboard when you select the <strong>Wildcard pattern</strong> option. For more information, refer to <a href="/rules/transform/url-rewrite/create-dashboard/#wildcard-pattern-parameters">Wildcard pattern parameters</a>.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13184.md")
</aside>
<h3 id="different-url-rewrite-types-in-the-same-rule">Different URL rewrite types in the same rule</h3>
<p>The same rule can have different types of URL rewrites for the URI path and the query string. For example, a single rule can perform a <strong>dynamic</strong> URL rewrite of the URI path and a <strong>static</strong> URL rewrite of the query string. The syntax of such a rule would be the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;uri&quot;: {&#10;    &quot;path&quot;: {&#10;      &quot;expression&quot;: &quot;&lt;URI_PATH_EXPRESSION&gt;&quot;&#10;    },&#10;    &quot;query&quot;: {&#10;      &quot;value&quot;: &quot;&lt;QUERY_STRING_VALUE&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
