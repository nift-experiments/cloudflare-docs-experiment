<p>In this tutorial, you will learn how to import a database into D1 using the <a href="/api/resources/d1/subresources/database/methods/import/">REST API</a>.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/7271.md")
</div></details>
<h2 id="1-create-a-d1-api-token"><ol>
<li>Create a D1 API token</li>
</ol></h2>
<p>To use REST APIs, you need to generate an API token to authenticate your API requests. You can do this through the Cloudflare dashboard.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7272.md")
</div>
<ul>
<li>Refer to <a href="/fundamentals/api/get-started/create-token/">Create API token</a> for more information on creating API tokens through the Cloudflare dashboard.</li>
<li>Refer to <a href="/fundamentals/api/how-to/create-via-api/">Create tokens via API</a> for more information on creating API tokens through API.</li>
</ul>
<h2 id="2-create-the-target-table"><ol start="2">
<li>Create the target table</li>
</ol></h2>
<p>You must have an existing D1 table which matches the schema of the data you wish to import.</p>
<p>This tutorial uses the following:</p>
<ul>
<li>A database called <code>d1-import-tutorial</code>.</li>
<li>A table called <code>TargetD1Table</code></li>
<li>Within <code>TargetD1Table</code>, three columns called <code>id</code>, <code>text</code>, and <code>date_added</code>.</li>
</ul>
<p>To create the table, follow these steps:</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7273.md")
</div>
<h2 id="3-create-an-index-js-file"><ol start="3">
<li>Create an <code>index.js</code> file</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7274.md")
</div>
<h2 id="4-generate-example-data-optional"><ol start="4">
<li>Generate example data (optional)</li>
</ol></h2>
<p>In practice, you may already have the data you wish to import to a D1 database.</p>
<p>This tutorial generates example data to demonstrate the import process.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7275.md")
</div>
<h2 id="5-generate-the-sql-command"><ol start="5">
<li>Generate the SQL command</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7276.md")
</div>
<h2 id="6-import-the-data-to-d1"><ol start="6">
<li>Import the data to D1</li>
</ol></h2>
<p>The import process consists of four steps:</p>
<ol>
<li><strong>Init upload</strong>: This step initializes the upload process. It sends the hash of the SQL command to the D1 API and receives an upload URL.</li>
<li><strong>Upload to R2</strong>: This step uploads the SQL command to the upload URL.</li>
<li><strong>Start ingestion</strong>: This step starts the ingestion process.</li>
<li><strong>Polling</strong>: This step polls the import process until it completes.</li>
</ol>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7277.md")
</div>
<h2 id="7-write-the-final-code"><ol start="7">
<li>Write the final code</li>
</ol></h2>
<p>In the previous steps, you have created functions to execute various processes involved in importing data into D1. The final code executes those functions to import the example data into the target D1 table.</p>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7278.md")
</div>
<h2 id="8-run-the-code"><ol start="8">
<li>Run the code</li>
</ol></h2>
<div class="nb-steps">
@markup("md", "content/.markup/bodies/7279.md")
</div>
<p>You will now see your target D1 table populated with the example data.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/7269.md")
</aside>
<h2 id="summary">Summary</h2>
<p>By completing this tutorial, you have</p>
<ol>
<li>Created an API token.</li>
<li>Created a target database and table.</li>
<li>Generated example data.</li>
<li>Created SQL command for the example data.</li>
<li>Imported your example data into the D1 target table using REST API.</li>
</ol>
