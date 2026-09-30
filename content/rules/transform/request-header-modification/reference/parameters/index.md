<p>To set an HTTP request header via API, set the following parameters in the <code>action_parameters</code> field:</p>
<ul>
<li>
<p><strong>operation</strong>: <code>set</code></p>
</li>
<li>
<p>Include one of the following parameters to define a static or dynamic value:</p>
<ul>
<li><strong>value</strong>: Specifies a static value for the HTTP request header.</li>
<li><strong>expression</strong>: Specifies the expression that defines a value for the HTTP request header.</li>
</ul>
</li>
</ul>
<p>To remove an HTTP request header via API, set the following parameter in the <code>action_parameters</code> field:</p>
<ul>
<li><strong>operation</strong>: <code>remove</code></li>
</ul>
<p>For step-by-step instructions, refer to <a href="/rules/transform/request-header-modification/create-api/">Create a request header transform rule via API</a>.</p>
<h2 id="static-header-value-parameters">Static header value parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to define a static HTTP request header value is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;set&quot;,&#10;      &quot;value&quot;: &quot;&lt;URI_PATH_VALUE&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="dynamic-header-value-parameters">Dynamic header value parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to define a dynamic HTTP request header value using an expression is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;set&quot;,&#10;      &quot;expression&quot;: &quot;&lt;EXPRESSION&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13180.md")
</aside>
<h2 id="header-removal-parameters">Header removal parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to remove an HTTP request header is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;remove&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="different-header-modifications-in-the-same-rule">Different header modifications in the same rule</h2>
<p>The same rule can modify different HTTP request headers using different operations (set or remove a header). For example, a single rule can set the value of a header and remove a different header. The syntax of such a rule could be the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME_1&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;set&quot;,&#10;      &quot;value&quot;: &quot;&lt;HEADER_VALUE_1&gt;&quot;&#10;    },&#10;    &quot;&lt;HEADER_NAME_2&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;remove&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
