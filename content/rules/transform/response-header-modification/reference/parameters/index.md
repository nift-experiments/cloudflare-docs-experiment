<p>To set an HTTP response header, overwriting any headers with the same name, use the following parameters in the <code>action_parameters</code> field:</p>
<ul>
<li><strong>operation</strong>: <code>set</code></li>
<li>Include one of the following parameters to define a static or dynamic value:
<ul>
<li><strong>value</strong>: Specifies a static value for the HTTP response header.</li>
<li><strong>expression</strong>: Specifies the expression that defines a value for the HTTP response header.</li>
</ul>
</li>
</ul>
<p>To add an HTTP response header, keeping any existing headers with the same name, use the following parameters in the <code>action_parameters</code> field:</p>
<ul>
<li><strong>operation</strong>: <code>add</code></li>
<li>Include one of the following parameters to define a static or dynamic value:
<ul>
<li><strong>value</strong>: Specifies a static value for the HTTP response header.</li>
<li><strong>expression</strong>: Specifies the expression that defines a value for the HTTP response header.</li>
</ul>
</li>
</ul>
<p>To remove an HTTP response header, set the following parameter in the <code>action_parameters</code> field:</p>
<ul>
<li><strong>operation</strong>: <code>remove</code></li>
</ul>
<h2 id="static-header-value-parameters">Static header value parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to define a static HTTP response header value is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;&lt;set|add&gt;&quot;,&#10;      &quot;value&quot;: &quot;&lt;URI_PATH_VALUE&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="dynamic-header-value-parameters">Dynamic header value parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to define a dynamic HTTP response header value using an expression is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;&lt;set|add&gt;&quot;,&#10;      &quot;expression&quot;: &quot;&lt;EXPRESSION&gt;&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/13182.md")
</aside>
<h2 id="header-removal-parameters">Header removal parameters</h2>
<p>The full syntax of the <code>action_parameters</code> field to remove an HTTP response header is the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;remove&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h2 id="different-header-modifications-in-the-same-rule">Different header modifications in the same rule</h2>
<p>The same rule can modify different HTTP response headers using different operations. For example, a single rule can set the value of a header and remove a different header. The syntax of such a rule could be the following:</p>
<pre><code class="language-json">&quot;action_parameters&quot;: {&#10;  &quot;headers&quot;: {&#10;    &quot;&lt;HEADER_NAME_1&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;set&quot;,&#10;      &quot;value&quot;: &quot;&lt;HEADER_VALUE_1&gt;&quot;&#10;    },&#10;    &quot;&lt;HEADER_NAME_2&gt;&quot;: {&#10;      &quot;operation&quot;: &quot;remove&quot;&#10;    }&#10;  }&#10;}&#10;</code></pre>
