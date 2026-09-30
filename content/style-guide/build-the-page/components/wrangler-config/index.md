<p>This component can be used to automatically generate a <code>jsonc</code> version of the <code>toml</code> file (or vice versa) of the Cloudflare <a href="/workers/wrangler/configuration/">Wrangler configuration file</a>.</p>
<h2 id="import">Import</h2>
<pre><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;</code></pre>
<h2 id="usage">Usage</h2>
<pre><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerConfig&gt;&#10;</code></pre>
<p>[[d1_databases]]
binding = &quot;DB&quot; # available in your Worker on env.DB
database_name = &quot;prod-d1-tutorial&quot;
database_id = &quot;<unique-ID-for-your-database>&quot;</p>
<pre><code>&lt;/WranglerConfig&gt;&#10;</code></pre>
<h2 id="compatibility-date">Compatibility date</h2>
<p>You should generally use <code>$today</code> for the <code>compatibility_date</code> value for new projects. This magic string is automatically replaced with the current date at build time, ensuring documentation always suggests the latest date. When <code>$today</code> is used, the component also automatically injects a comment above the <code>compatibility_date</code> line (for example, <code># Set this to today's date</code> in TOML and <code>// Set this to today's date</code> in JSONC) so that readers know to keep the value current. If you need to specify a fixed date, you can do so as well, but you may miss out on the latest features and performance improvements. You can disable specific features by using <a href="/workers/configuration/compatibility-flags/">compatibility flags</a>.</p>
<pre><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerConfig&gt;&#10;</code></pre>
<p>{
&quot;name&quot;: &quot;my-worker&quot;,
&quot;compatibility_date&quot;: &quot;$today&quot;
}</p>
<pre><code>&lt;/WranglerConfig&gt;&#10;</code></pre>
<h3 id="minimum-compatibility-dates">Minimum compatibility dates</h3>
<p>Some features require a minimum compatibility date. When documenting these features, use a <code>:::note</code> component to communicate the requirement clearly on the docs page:</p>
<pre><code class="language-mdx">:::note&#10;This feature requires a `compatibility_date` of `2024-09-23` or later.&#10;:::&#10;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/14624.md")
</aside>
<p>The <code>removeSchema</code> prop can be used to remove the <code>$schema</code> reference from the generated JSON file. This can be useful if you want to add snippets of configuration files that are easier to copy paste, and are providing toml as the source config format.</p>
<p>If you provide jsonc as the source config format, the <code>removeSchema</code> prop will be ignored.</p>
<pre><code class="language-mdx">import { WranglerConfig } from &quot;~/components&quot;;&#10;&#10;&lt;WranglerConfig removeSchema&gt;&#10;</code></pre>
<p>[[d1_databases]]
binding = &quot;DB&quot; # available in your Worker on env.DB
database_name = &quot;prod-d1-tutorial&quot;
database_id = &quot;<unique-ID-for-your-database>&quot;</p>
<pre><code>&lt;/WranglerConfig&gt;&#10;</code></pre>
