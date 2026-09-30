<p>Tiered Cache uses the size of the Cloudflare network to reduce requests to customer origins by dramatically increasing cache hit ratios. With data centers around the world, Cloudflare caches content very close to end users. However, if a piece of content is not in cache, the Cloudflare edge data centers must contact the origin server to receive the cacheable content.</p>
<p>Tiered Cache works by dividing Cloudflare’s data centers into a hierarchy of lower-tiers and upper-tiers. If content is not cached in lower-tier data centers (generally the ones closest to a visitor), the lower-tier must ask an upper-tier to see if it has the content. If the upper-tier does not have the content, only the upper-tier can ask the origin for content. This practice improves bandwidth efficiency by limiting the number of data centers that can ask the origin for content, which reduces origin load and makes websites more cost-effective to operate.</p>
<p>Additionally, Tiered Cache concentrates connections to origin servers so they come from a small number of data centers rather than the full set of network locations. This results in fewer open connections using server resources.</p>
<p>To enable Tiered Cache, refer to <a href="/cache/how-to/tiered-cache/#enable-tiered-cache">Enable Tiered Cache</a>.</p>
<h2 id="tiered-cache-topology">Tiered Cache Topology</h2>
<p>Cloudflare allows you to select your cache topology so that you have control over how your origin connects to Cloudflare’s data centers. This will help ensure higher cache hit ratios, fewer origin connections, and a reduction of Internet latency. Below you can find details about the options we have available.</p>
<h3 id="smart-tiered-cache">Smart Tiered Cache</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield">Smart Shield</h3>
@markup("md", "content/.markup/bodies/3807.md")
</aside>
<p>Smart Tiered Cache dynamically selects the single closest upper tier for each of your website’s origins with no configuration required, using our in-house performance and routing data. Cloudflare collects latency data for each request to an origin, and uses the latency data to determine how well any upper-tier data center is connected with an origin. As a result, Cloudflare can select the data center with the lowest latency to be the upper-tier for an origin.</p>
<h4 id="public-cloud-origins">Public cloud origins</h4>
<p>Origins hosted on public cloud providers (AWS, GCP, Azure, or Oracle Cloud) often use <a href="https://www.cloudflare.com/en-gb/learning/cdn/glossary/anycast-network/">anycast</a> or regional unicast networking, which prevents Smart Tiered Cache from determining the origin location through latency probing alone. To solve this, you can set a <strong>cloud region hint</strong> that tells Smart Tiered Cache which cloud provider and region your origin is in. Smart Tiered Cache then selects a primary upper-tier data center close to that cloud region, plus a fallback in a different location for resilience. To set up a cloud region hint, refer to <a href="/cache/how-to/tiered-cache/#set-a-cloud-region-hint">Set a cloud region hint</a>.</p>
<h4 id="load-balancing-interaction">Load Balancing interaction</h4>
<p>While Smart Tiered Cache selects one Upper Tier per origin, when using Load Balancing, Smart Tiered Cache will select the single best Upper Tier for the entire <a href="/load-balancing/understand-basics/load-balancing-components/#pools">Load Balancing Pool</a>.</p>
<h4 id="caveats">Caveats</h4>
<p>You need to be careful when updating your origin IPs/DNS records while Smart Tiered Cache is enabled. Depending on the changes made, it may cause the existing assigned upper tiers to change, resulting in an increased <code>MISS</code> rate as cache is refilled in the new upper tiers. If the origin is switched to a network behind anycast, it will significantly reduce the effectiveness of Smart Tiered Cache unless you set a <a href="/cache/how-to/tiered-cache/#set-a-cloud-region-hint">cloud region hint</a>.</p>
<h3 id="generic-global-tiered-cache">Generic Global Tiered Cache</h3>
<p>Generic Global topology allows for all of Cloudflare’s global data centers to serve as a network of upper-tiers. This topology may help reduce the long tail latencies for far-away visitors.</p>
<h3 id="regional-tiered-cache">Regional Tiered Cache</h3>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="smart-shield-1">Smart Shield</h3>
@markup("md", "content/.markup/bodies/3806.md")
</aside>
<p>Regional Tiered Cache provides an additional layer of caching for customers who have a global traffic footprint and want to serve content faster by avoiding network latency when there is a cache <code>MISS</code> in a lower-tier, resulting in an upper-tier fetch in a data center located far away.</p>
<p>Regional Tiered Cache instructs Cloudflare to check a regional hub data center near the lower tier before going to the upper tier that may be outside of the region.</p>
<p>This can help improve performance for <strong>Smart</strong> and <strong>Custom Tiered Cache</strong> topologies with upper-tiers in one or two regions. Regional Tiered Cache is not beneficial for customers with many upper tiers in many regions like Generic Global Tiered Cache.</p>
<h3 id="custom-tiered-cache">Custom Tiered Cache</h3>
<p>Custom Tiered cache allows Enterprise customers to work with their account team to set a custom topology that fits your specific needs, for instance you have close upper tiers or you have a unique traffic pattern. If you want a custom topology, please engage your account team.</p>
<h2 id="availability">Availability</h2>
<table>
<thead>
<tr>
<th></th>
<th>Free</th>
<th>Pro</th>
<th>Business</th>
<th>Enterprise</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tiered Cache</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Smart Topology</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Generic Global Topology</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Regional Tiered Cache</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr>
<td>Custom Topology</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>
<h2 id="bandwidth-alliance">Bandwidth Alliance</h2>
<p>Enterprise customers can override Bandwidth Alliance configuration with Tiered Cache. For all other users, the Bandwidth Alliance takes precedence. Tiered Cache is still a valuable option to enable because the Bandwidth Alliance may not always be an available option, and in those instances, the Tiered Cache configuration will be used.</p>
<h2 id="enable-tiered-cache">Enable Tiered Cache</h2>
<p>You can enable Tiered Cache in the dashboard or via API.</p>
<h3 id="enable-tiered-cache-in-the-dashboard">Enable Tiered Cache in the dashboard</h3>
<ol>
<li>In the Cloudflare dashboard, go to the <strong>Tiered Cache</strong> page.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>From <strong>Tiered Cache</strong>, toggle the button to <strong>enabled</strong>.</li>
<li>In <strong>Tiered Cache Topology</strong>, you can control how your origin connects to Cloudflare’s data centers. You can select:
<ul>
<li><strong>Upper Tier Cache</strong> - You have the option to choose between Smart or Generic Global Tiered Cache Topology.</li>
<li><strong>Middle Tier Cache</strong> -  If you have selected Smart or Custom Tiered Cache Topology, you can now enable Regional Tiered Cache.</li>
<li><strong>Custom Tiered Cache</strong> - Allows you to work with Cloudflare’s support team to set a custom topology that fits your specific needs.</li>
<li><strong>Disable Tiered Cache</strong>.</li>
</ul>
</li>
</ol>
<p><img src="/assets/upstream/images/cache/tiered_cache_topology.png" alt="Tiered Cache Topology dashboard" /></p>
<h3 id="enable-tiered-cache-via-api">Enable Tiered Cache via API</h3>
<p>To enable Tiered Cache via API use the following cURL example:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/argo/tiered_caching \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;value&quot;: &quot;on&quot;&#10;}&#x27;</code></pre>
<p>You can also configure Tiered Cache Topology via API, for instance:</p>
<details class="nb-details"><summary>Enable Smart Tiered Cache</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3808.md")
</div></details>
<details class="nb-details"><summary>Enable Regional Tiered Cache</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/3809.md")
</div></details>
<p>For more API examples and configuration options for Tiered Cache, refer to the <a href="/api/resources/argo/subresources/tiered_caching/methods/get/">API documentation</a>.</p>
<h3 id="set-a-cloud-region-hint">Set a cloud region hint</h3>
<p>If your origin is hosted on a public cloud provider, set a cloud region hint so Smart Tiered Cache can select the optimal upper tier for your cloud region. For background on why this is needed, refer to <a href="/cache/how-to/tiered-cache/#smart-tiered-cache">Public cloud origins</a>.</p>
<p>Cloud region hints are available on all plan types (Free, Pro, Business, and Enterprise) at no additional cost. Supported providers: AWS, GCP, Azure, and Oracle Cloud.</p>
<h4 id="set-a-cloud-region-hint-in-the-dashboard">Set a cloud region hint in the dashboard</h4>
<ol>
<li>Go to <strong>Caching</strong> &gt; <strong>Tiered Cache</strong> &gt; <strong>Origin Configuration</strong>.</li>
</ol>
<div class="nb-dash-button"></div>
<ol start="2">
<li>Find your origin IP or hostname and select <strong>Set Region Hint</strong>.</li>
<li>Select your cloud provider and region (for example, <code>aws:us-east-1</code> or <code>gcp:europe-west1</code>).</li>
</ol>
<h4 id="list-supported-cloud-regions-via-api">List supported cloud regions via API</h4>
<p>To see all available cloud providers and regions, use the supported regions endpoint:</p>
<pre class="nb-api-request"><code class="language-bash">curl --request GET \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cache/origin_cloud_regions/supported_regions \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot;</code></pre>
<h4 id="set-a-cloud-region-hint-via-api">Set a cloud region hint via API</h4>
<pre class="nb-api-request"><code class="language-bash">curl --request PATCH \&#10;  --url https://api.cloudflare.com/client/v4/zones/{zone_id}/cache/origin_cloud_regions \&#10;  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \&#10;  --data &#x27;{&#10;  &quot;ip&quot;: &quot;203.0.113.1&quot;,&#10;  &quot;vendor&quot;: &quot;aws&quot;,&#10;  &quot;region&quot;: &quot;us-east-1&quot;&#10;}&#x27;</code></pre>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3805.md")
</aside>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/3804.md")
</aside>
