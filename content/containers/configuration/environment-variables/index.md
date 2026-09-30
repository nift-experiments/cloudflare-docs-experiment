<h2 id="runtime-environment-variables">Runtime environment variables</h2>
<p>The container runtime automatically sets the following variables:</p>
<ul>
<li><code>CLOUDFLARE_APPLICATION_ID</code> - the ID of the Containers application</li>
<li><code>CLOUDFLARE_COUNTRY_A2</code> - the <a href="https://www.iso.org/obp/ui/#search/code/">ISO 3166-1 Alpha 2 code</a> of a country the container is placed in</li>
<li><code>CLOUDFLARE_LOCATION</code> - a name of a location the container is placed in</li>
<li><code>CLOUDFLARE_REGION</code> - a region name</li>
<li><code>CLOUDFLARE_DURABLE_OBJECT_ID</code> - the ID of the Durable Object instance that the container is bound to. You can use this to identify particular container instances on the dashboard.</li>
</ul>
<h2 id="user-defined-environment-variables">User-defined environment variables</h2>
<p>You can set environment variables when defining a Container in your Worker, or when starting a container instance.</p>
<p>For example:</p>
<pre><code class="language-javascript">class MyContainer extends Container {&#10;	defaultPort = 4000;&#10;	envVars = {&#10;		MY_CUSTOM_VAR: &quot;value&quot;,&#10;		ANOTHER_VAR: &quot;another_value&quot;,&#10;	};&#10;}&#10;</code></pre>
<p>More details about defining environment variables and secrets can be found in <a href="/containers/examples/env-vars-and-secrets">this example</a>.</p>
