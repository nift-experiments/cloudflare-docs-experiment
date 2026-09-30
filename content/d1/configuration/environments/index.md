<p><a href="/workers/wrangler/environments/">Environments</a> are different contexts that your code runs in. Cloudflare Developer Platform allows you to create and manage different environments. Through environments, you can deploy the same project to multiple places under multiple names.</p>
<p>To specify different D1 databases for different environments, use the following syntax in your Wrangler file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7366.md")
</div>
<p>In the code above, the <code>staging</code> environment is using a different database (<code>DATABASE_NAME_1</code>) than the <code>production</code> environment (<code>DATABASE_NAME_2</code>).</p>
<h2 id="anatomy-of-wrangler-file">Anatomy of Wrangler file</h2>
<p>If you need to specify different D1 databases for different environments, your <a href="/workers/wrangler/configuration/">Wrangler configuration file</a> may contain bindings that resemble the following:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7367.md")
</div>
<p>In the above configuration:</p>
<ul>
<li><code>[[env.production.d1_databases]]</code> creates an object <code>production</code> under <code>env</code> with a property <code>d1_databases</code>, where <code>d1_databases</code> is an array of objects, since you can create multiple D1 bindings in case you have more than one database.</li>
<li>Any property below the line in the form <code>&lt;key&gt; = &lt;value&gt;</code> is a property of an object within the <code>d1_databases</code> array.</li>
</ul>
<p>Therefore, the above binding is equivalent to:</p>
<pre><code class="language-json">{&#10;  &quot;env&quot;: {&#10;    &quot;production&quot;: {&#10;      &quot;d1_databases&quot;: [&#10;        {&#10;          &quot;binding&quot;: &quot;DB&quot;,&#10;          &quot;database_name&quot;: &quot;DATABASE_NAME&quot;,&#10;          &quot;database_id&quot;: &quot;DATABASE_ID&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#10;}&#10;</code></pre>
<h3 id="example">Example</h3>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/7368.md")
</div>
<p>The above is equivalent to the following structure in JSON:</p>
<pre><code class="language-json">{&#10;  &quot;env&quot;: {&#10;    &quot;production&quot;: {&#10;      &quot;d1_databases&quot;: [&#10;        {&#10;          &quot;binding&quot;: &quot;BINDING_NAME_2&quot;,&#10;          &quot;database_id&quot;: &quot;UUID_2&quot;,&#10;          &quot;database_name&quot;: &quot;DATABASE_NAME_2&quot;&#10;        }&#10;      ]&#10;    },&#10;    &quot;staging&quot;: {&#10;      &quot;d1_databases&quot;: [&#10;        {&#10;          &quot;binding&quot;: &quot;BINDING_NAME_1&quot;,&#10;          &quot;database_id&quot;: &quot;UUID_1&quot;,&#10;          &quot;database_name&quot;: &quot;DATABASE_NAME_1&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#10;}&#10;</code></pre>
