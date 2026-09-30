<h2 id="definition">Definition</h2>
<p>A single term and corresponding definition in the glossary.</p>
<h2 id="used-in">Used in</h2>
<p>Glossary, documentation pages, tooltips.</p>
<h2 id="structure">Structure</h2>
<h3 id="data">Data</h3>
<p>The data underlying our glossary lives with YAML files in the <a href="https://github.com/cloudflare/cloudflare-docs/tree/production/src/content/glossary"><code>/src/content/glossary/*</code></a> folder.</p>
<p>Each file should be structured similar to the following:</p>
<pre><code class="language-yaml">&#45;--&#10;productName: DNS&#10;entries:&#10;  &#45; term: active zone&#10;    general_definition: |-&#10;      a DNS zone that is active on Cloudflare requires changing its nameservers to Cloudflare&#x27;s for management.&#10;    associated_products:&#10;      &#45; Cloudflare One&#10;&#10;  &#45; term: apex domain&#10;    general_definition: |-&#10;      apex domain is used to refer to a domain that does not contain a subdomain part, such as `example.com` (without `www.`). It is also known as &quot;root domain&quot; or &quot;naked domain&quot;.&#10;&#10;  &#45; term: DNS over HTTPS&#10;    general_definition: |-&#10;      DNS over HTTPS (DoH) is a standard for encrypting DNS traffic, preventing tracking and spoofing of DNS queries.&#10;    associated_products:&#10;      &#45; 1.1.1.1&#10;      &#45; Cloudflare One&#10;&#10;  &#45; term: DNS over TLS&#10;    general_definition: |-&#10;      DNS over TLS (DoT) is a standard for encrypting DNS traffic using its own port (853) and TLS encryption.&#10;    associated_products:&#10;      &#45; 1.1.1.1&#10;      &#45; Cloudflare One&#10;</code></pre>
<p>Relevant values include the following:</p>
<ul>
<li>
<p><code>productName</code> string required</p>
<ul>
<li>Core product associated with this file. Should always match the same formatting / styling used in <code>associated_products</code>.</li>
</ul>
</li>
<li>
<p><code>entries</code> object required</p>
<ul>
<li>
<p><code>term</code> string required</p>
<ul>
<li>The glossary term itself.</li>
</ul>
</li>
<li>
<p><code>general_definition</code> string required</p>
<ul>
<li>Definition of the term. Should be general enough to apply to multiple products. Should also start with a lowercase letter unless starting with a proper noun.</li>
</ul>
</li>
<li>
<p><code>associated_products</code> array optional</p>
<ul>
<li>If the term is associated with other products. Any names used should correspond to the <code>productName</code> of that associated file.</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="usage">Usage</h3>
<p>Because of the <a href="#data">structured data</a> associated with our glossaries, we can pull these terms into multiple places.</p>
<h4 id="product-level-glossary">Product-level glossary</h4>
<p>A product-level glossary includes all terms associated with a particular product, which will pull in terms directly in that product's glossary file and any terms that include the product in its <code>associated_products</code>.</p>
<pre><code class="language-mdx">&#45;--&#10;title: Glossary&#10;pcx_content_type: glossary&#10;&#45;--&#10;&#10;import { Glossary } from &quot;~/components&quot;;&#10;&#10;Review the definitions for terms used across Cloudflare&#x27;s DNS documentation.&#10;&#10;&lt;Glossary product=&quot;dns&quot; /&gt;&#10;</code></pre>
<h4 id="glossary-definition">Glossary definition</h4>
<p>Pull glossary definitions directly into your Markdown by using the <code>&lt;GlossaryDefinition&gt;</code> component.</p>
<blockquote>
<div class="nb-glossary-definition"><p>A DNS zone that is active on Cloudflare requires changing its nameservers to Cloudflare's for management.</p></div>
</blockquote>
<p>Is a quoted definition that comes from:</p>
<pre><code class="language-mdx">&lt;GlossaryDefinition term=&quot;active zone&quot; prepend=&quot;An active zone is &quot; /&gt;&#10;</code></pre>
<p>Properties are:</p>
<ul>
<li>
<p><code>term</code> string required</p>
<ul>
<li>Should match a term within an existing glossary YAML file.</li>
</ul>
</li>
<li>
<p><code>prepend</code> string optional</p>
<ul>
<li>Text to add before a definition.</li>
</ul>
</li>
</ul>
<h4 id="glossary-tooltip">Glossary tooltip</h4>
<p>Pull component definitions into a focusable tooltip for a specific phrase by using the <code>&lt;GlossaryTooltip&gt;</code> component.</p>
<p>Here's a <div class="nb-interactive-component" data-cf-component="GlossaryTooltip"></p>
@markup("md", "content/.markup/bodies/14666.md")
</div> example.
<pre><code class="language-mdx">Here&#x27;s a &lt;GlossaryTooltip term=&quot;active zone&quot;&gt;tooltip&lt;/GlossaryTooltip&gt; example.&#10;</code></pre>
<p>Properties are:</p>
<ul>
<li>
<p><code>term</code> string required</p>
<ul>
<li>Should match a term within an existing glossary YAML file.</li>
</ul>
</li>
<li>
<p><code>prepend</code> string optional</p>
<ul>
<li>Text to add before a definition.</li>
</ul>
</li>
<li>
<p><code>link</code> string optional</p>
<ul>
<li>Wraps the inner text in a markdown link, similar to normal markdown formatting.</li>
</ul>
</li>
</ul>
<p>Because of space limitations, the tooltip will always default to the short definition of a term, meaning the definition text before the first line break.</p>
