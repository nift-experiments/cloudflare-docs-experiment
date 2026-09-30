<p>Cloudflare has data centers in <a href="https://www.cloudflare.com/network/">hundreds of cities worldwide</a>. Health checks do not run from every single of these data centers as this would result in numerous requests to your servers. Instead, you are able to choose between one and thirteen regions from which to run health checks. Cloudflare will run Health Checks from three data centers in each region that you select.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/9014.md")
</aside>
<p>The Internet is not the same everywhere around the world and your users may not have the same experience on your application according to where they are. Running Health Checks from different regions lets you know the health of your application from the point of view of the Cloudflare network in each of these regions.</p>
<p>Analytics are presented at two levels:</p>
<ul>
<li>Regional Aggregates: Combined results from the three data centers within a specific region.</li>
<li>Global Aggregates: Total results across all configured regions and data centers.</li>
</ul>
<p>In the event log, entries are labeled by region or as <strong>Global</strong>. We do not provide granular data for individual data centers.</p>
<p>If you select multiple regions or choose <strong>All Regions</strong> (Business and Enterprise Only), you may increase traffic to your servers. Each region sends individual health checks from three data centers.</p>
