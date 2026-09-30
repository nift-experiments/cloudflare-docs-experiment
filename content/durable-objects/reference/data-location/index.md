---
cp9:
  canonical: https://developers.cloudflare.com/durable-objects/reference/data-location/
  description: Restrict Durable Objects to specific jurisdictions or provide location hints to control where data is stored and processed.
  full_title: Data location · Cloudflare Durable Objects docs
  head_html: <title>Data location · Cloudflare Durable Objects docs</title><meta name="generator" content="Nift"><meta name="description" content="Restrict Durable Objects to specific jurisdictions or provide location hints to control where data is stored and processed."><link rel="canonical" href="https://developers.cloudflare.com/durable-objects/reference/data-location/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/durable-objects/reference/data-location/index.md"><meta property="og:title" content="Data location · Cloudflare Durable Objects docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="Restrict Durable Objects to specific jurisdictions or provide location hints to control where data is stored and processed."><meta property="og:url" content="https://developers.cloudflare.com/durable-objects/reference/data-location/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Durable Objects"><meta name="algolia_product_filter" content="Durable Objects"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Concept"><meta name="algolia_content_type" content="Concept"><meta name="pcx_additional_products" content="Durable Objects"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/durable-objects/reference/data-location/#page","headline":"Data location \u00b7 Cloudflare Durable Objects docs","description":"Restrict Durable Objects to specific jurisdictions or provide location hints to control where data is stored and processed.","url":"https://developers.cloudflare.com/durable-objects/reference/data-location/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}</script>
  markdown: true
  noindex: false
  route: /durable-objects/reference/data-location/
  schema: 1
---
<h2 id="restrict-durable-objects-to-a-jurisdiction">Restrict Durable Objects to a jurisdiction</h2>
<p>Jurisdictions are used to create <span class="nb-glossary-tooltip" title="Durable Object">Durable Objects</span> that only run and store data within a region to comply with local regulations such as the <a href="https://gdpr-info.eu/">GDPR</a> or <a href="https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/">FedRAMP</a>.</p>
<p>Workers may still access Durable Objects constrained to a jurisdiction from anywhere in the world. The jurisdiction constraint only controls where the Durable Object itself runs and persists data. Consider using <a href="/data-localization/regional-services/">Regional Services</a> to control the regions from which Cloudflare responds to requests.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="logging">Logging</h3>
@markup("md", "content/.markup/bodies/8156.md")
</aside>
<p>Durable Objects can be restricted to a specific jurisdiction by creating a <a href="/durable-objects/api/namespace/"><code>DurableObjectNamespace</code></a> restricted to a jurisdiction. All <a href="/durable-objects/api/id/">Durable Object ID methods</a> are valid on IDs within a namespace restricted to a jurisdiction.</p>
<pre tabindex="0"><code class="language-js">const euSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;);&#10;const euId = euSubnamespace.newUniqueId();&#10;</code></pre>
<ul>
<li>It is possible to have the same name represent different IDs in different jurisdictions.</li>
</ul>
<pre tabindex="0"><code class="language-js">const euId1 = env.MY_DURABLE_OBJECT.idFromName(&quot;my-name&quot;);&#10;const euId2 = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;).idFromName(&quot;my-name&quot;);&#10;console.assert(!euId1.equal(euId2), &quot;This should always be true&quot;);&#10;</code></pre>
<ul>
<li>You will run into an error if the jurisdiction on your <a href="/durable-objects/api/namespace/"><code>DurableObjectNamespace</code></a> and the jurisdiction on <a href="/durable-objects/api/id"><code>DurableObjectId</code></a> are different.</li>
<li>You will not run into an error if the <a href="/durable-objects/api/namespace/"><code>DurableObjectNamespace</code></a> is not associated with a jurisdiction.</li>
<li>All <a href="/durable-objects/api/id/">Durable Object ID methods</a> are valid on IDs within a namespace restricted to a jurisdiction.</li>
</ul>
<pre tabindex="0"><code class="language-js">const euSubnamespace = env.MY_DURABLE_OBJECT.jurisdiction(&quot;eu&quot;);&#10;const euId = euSubnamespace.idFromName(name);&#10;const stub = env.MY_DURABLE_OBJECT.get(euId);&#10;</code></pre>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="use-durableobjectnamespace-jurisdiction">Use `DurableObjectNamespace.jurisdiction`</h3>
@markup("md", "content/.markup/bodies/8155.md")
</aside>
<h3 id="supported-locations">Supported locations</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td>eu</td>
<td>The European Union</td>
</tr>
<tr>
<td>us</td>
<td>The United States</td>
</tr>
<tr>
<td>fedramp</td>
<td>FedRAMP-Moderate data centers</td>
</tr>
</tbody>
</table>
<h3 id="read-the-jurisdiction-from-inside-a-durable-object">Read the jurisdiction from inside a Durable Object</h3>
<p>The jurisdiction of a Durable Object is available inside the object via <a href="/durable-objects/api/id/#jurisdiction"><code>ctx.id.jurisdiction</code></a>. The value is preserved across <code>toString()</code> and <code>idFromString()</code> round-trips and is also available inside <a href="/durable-objects/api/alarms/">alarm handlers</a> for alarms scheduled on 2026-03-15 or later, which makes it suitable for region-aware logic inside the Durable Object.</p>
<h2 id="provide-a-location-hint">Provide a location hint</h2>
<p>Durable Objects, as with any stateful API, will often add response latency as requests must be forwarded to the data center where the Durable Object, or state, is located.</p>
<p>Durable Objects do not currently change locations after they are created<sup>1</sup>. By default, a Durable Object is instantiated in a data center close to where the initial <code>get()</code> request is made. This may not be in the same data center that the <code>get()</code> request is made from, but in most cases, it will be in close proximity.</p>
<aside class="nb-aside caution">
<h3 class="nb-aside-title" id="initial-requests-to-durable-objects">Initial requests to Durable Objects</h3>
@markup("md", "content/.markup/bodies/8154.md")
</aside>
<p>Location hints are the mechanism provided to specify the location that a Durable Object should be located regardless of where the initial <code>get()</code> request comes from.</p>
<p>To manually create Durable Objects in another location, provide an optional <code>locationHint</code> parameter to <code>get()</code>. Only the first call to <code>get()</code> for a particular Object will respect the hint.</p>
<pre tabindex="0"><code class="language-js">let durableObjectStub = OBJECT_NAMESPACE.get(id, { locationHint: &quot;enam&quot; });&#10;</code></pre>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/8153.md")
</aside>
<h3 id="supported-locations-1">Supported locations</h3>
<table>
<thead>
<tr>
<th>Parameter</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td>wnam</td>
<td>Western North America</td>
</tr>
<tr>
<td>enam</td>
<td>Eastern North America</td>
</tr>
<tr>
<td>sam</td>
<td>South America <sup>2</sup></td>
</tr>
<tr>
<td>weur</td>
<td>Western Europe</td>
</tr>
<tr>
<td>eeur</td>
<td>Eastern Europe</td>
</tr>
<tr>
<td>apac</td>
<td>Asia-Pacific</td>
</tr>
<tr>
<td>apac-ne</td>
<td>Northeast Asia-Pacific <sup>3</sup></td>
</tr>
<tr>
<td>apac-se</td>
<td>Southeast Asia-Pacific <sup>3</sup></td>
</tr>
<tr>
<td>oc</td>
<td>Oceania</td>
</tr>
<tr>
<td>afr</td>
<td>Africa <sup>2</sup></td>
</tr>
<tr>
<td>me</td>
<td>Middle East <sup>2</sup></td>
</tr>
</tbody>
</table>
<p><sup>1</sup> Dynamic relocation of existing Durable Objects is planned for the
future.</p>
<p><sup>2</sup> Durable Objects currently do not spawn in this location. Instead,
the Durable Object will spawn in a nearby location which does support Durable
Objects. For example, Durable Objects hinted to South America spawn in Eastern
North America instead.</p>
<p><sup>3</sup> <code>apac-ne</code> (Northeast Asia-Pacific) and <code>apac-se</code> (Southeast
Asia-Pacific) are narrower sub-regions within <code>apac</code> (Asia-Pacific). Prefer
<code>apac</code> for general Asia-Pacific placement. Choose <code>apac-ne</code> or <code>apac-se</code> only
when your users are concentrated in the northeast or southeast of the region and
you want to minimize latency for them.</p>
<h2 id="additional-resources">Additional resources</h2>
<ul>
<li>You can find our more about where Durable Objects are located using the website: <a href="https://where.durableobjects.live/">Where Durable Objects Live</a>.</li>
</ul>
