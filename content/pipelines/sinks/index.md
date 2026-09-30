<p>Sinks define destinations for your data in Cloudflare Pipelines. They support writing to <a href="/r2-data-catalog/">R2 Data Catalog</a> as Apache Iceberg tables or to <a href="/r2/">R2</a> as raw JSON or Parquet files.</p>
<p>Sinks provide exactly-once delivery guarantees, ensuring events are never duplicated or dropped. They can be configured to write files frequently for low-latency ingestion or to write larger, less frequent files for better query performance.</p>
<h2 id="learn-more">Learn more</h2>
<p><a class="nb-card nb-link-card" href="/pipelines/sinks/manage-sinks/"><h3 id="card-manage-sinks-pipelines-sinks-manage-sinks">Manage sinks</h3><p>Create, configure, and delete sinks using Wrangler or the API.</p></a></p>
<p><a class="nb-card nb-link-card" href="/pipelines/sinks/available-sinks/"><h3 id="card-available-sinks-pipelines-sinks-available-sinks">Available sinks</h3><p>Learn about supported sink destinations and their configuration options.</p></a></p>
