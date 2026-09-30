<p>This guide will instruct you through:</p>
<ul>
<li>Creating your first <a href="/r2/buckets/">R2 bucket</a> and enabling its <a href="/r2-data-catalog/">data catalog</a>.</li>
<li>Creating an <a href="/r2/api/tokens/">API token</a> needed for query engines to authenticate with your data catalog.</li>
<li>Using <a href="https://py.iceberg.apache.org/">PyIceberg</a> to create your first Iceberg table in a <a href="https://marimo.io/">marimo</a> Python notebook.</li>
<li>Using <a href="https://py.iceberg.apache.org/">PyIceberg</a> to load sample data into your table and query it.</li>
</ul>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/558.md")
</div></details>
<h2 id="1-create-an-r2-bucket-and-enable-the-data-catalog"><ol>
<li>Create an R2 bucket and enable the data catalog</li>
</ol></h2>
<div class="nb-tabs" data-nb-tabs data-nb-sync-key="CLIvDash"><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/563.md")
</div></div>
<h2 id="2-create-an-api-token"><ol start="2">
<li>Create an API token</li>
</ol></h2>
<p>Iceberg clients (including <a href="https://py.iceberg.apache.org/">PyIceberg</a>) must authenticate to the catalog with an <a href="/r2/api/tokens/">R2 API token</a> that has both R2 and catalog permissions.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/564.md")
</div>
<h2 id="3-install-uv"><ol start="3">
<li>Install uv</li>
</ol></h2>
<p>You need to install a Python package manager. In this guide, use <a href="https://docs.astral.sh/uv/">uv</a>. If you do not already have uv installed, follow the <a href="https://docs.astral.sh/uv/getting-started/installation/">installing uv guide</a>.</p>
<h2 id="4-install-marimo-and-set-up-your-project-with-uv"><ol start="4">
<li>Install marimo and set up your project with uv</li>
</ol></h2>
<p>We will use <a href="https://github.com/marimo-team/marimo">marimo</a> as a Python notebook.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/565.md")
</div>
<h2 id="5-create-a-python-notebook-to-interact-with-the-data-warehouse"><ol start="5">
<li>Create a Python notebook to interact with the data warehouse</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/566.md")
</div>
<p>In the Python notebook above, you:</p>
<ol>
<li>Connect to your catalog.</li>
<li>Create the <code>default</code> namespace.</li>
<li>Create a simple PyArrow table.</li>
<li>Create (or load) the <code>people</code> table in the <code>default</code> namespace.</li>
<li>Append sample data to the table.</li>
<li>Print the contents of the table.</li>
<li>(Optional) Drop the <code>people</code> table we created for this tutorial.</li>
</ol>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/r2-data-catalog/manage-catalogs/"><h3 id="card-managing-catalogs-r2-data-catalog-manage-catalogs">Managing catalogs</h3><p>Enable or disable R2 Data Catalog on your bucket, retrieve configuration details, and authenticate your Iceberg engine.</p></a></p>
<p><a class="nb-card nb-link-card" href="/r2-data-catalog/config-examples/"><h3 id="card-connect-to-iceberg-engines-r2-data-catalog-config-examples">Connect to Iceberg engines</h3><p>Find detailed setup instructions for Apache Spark and other common query engines.</p></a></p>
