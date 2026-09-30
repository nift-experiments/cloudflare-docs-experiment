<p>You can connect a Cloudflare Worker to get data from Google BigQuery and pass it to Workers AI, to run AI Models, powered by serverless GPUs. This will allow you to enhance data with AI-generated responses, such as detecting the sentiment score of some text or generating tags for an article. This document describes a simple way to get started if you are looking to give Workers AI a try and see how the <a href="/workers-ai/models/">new and different AI models</a> would perform with your data hosted in BigQuery.</p>
<h2 id="user-based-approach">User-based approach</h2>
<p>This version of the integration is aimed at workflows that require interaction with users to fetch data or generate ad-hoc reports.</p>
<p><img src="/assets/upstream/images/reference-architecture/bigquery-workers-ai/user-based-architecture.svg" alt="Figure 1: Ingesting Google BigQuery Data into Workers AI (user-based)" title="Figure 1: Ingesting Google BigQuery Data into Workers AI (user-based)" /></p>
<ol>
<li>A user makes a request to a <a href="https://workers.cloudflare.com/">Worker</a> endpoint. (Which can optionally incorporate <a href="/cloudflare-one/access-controls/policies/">Access</a> in front of it to authenticate users).</li>
<li>Worker fetches <a href="/workers/configuration/secrets/">securely stored</a> Google Cloud Platform service account information such as service key and generates a JSON Web Token to issue an authenticated API request to BigQuery.</li>
<li>Worker receives the data from BigQuery and <a href="/workers-ai/guides/tutorials/using-bigquery-with-workers-ai/#6-format-results-from-the-query">transforms it into a format</a> that will make it easier to iterate when interacting with Workers AI.</li>
<li>Using its <a href="/workers-ai/configuration/bindings/">native integration</a> with Workers AI, the Worker forwards the data from BigQuery which is then run against one of Cloudflare's hosted AI models.</li>
<li>The original data retrieved from BigQuery alongside the AI-generated information is returned to the user as a response to the request initiated in step 1.</li>
</ol>
<h2 id="cron-triggered-approach">Cron-triggered approach</h2>
<p>For periodic or longer workflows, you may opt for a batch approach. This diagram also explores more products where you can use the data ingested from BigQuery. It relies on <a href="/workers/configuration/cron-triggers/">Cron Triggers</a>, which are built into the Developer Platform and available for free when using Workers to schedule initialization of workloads.</p>
<p><img src="/assets/upstream/images/reference-architecture/bigquery-workers-ai/scheduled-based-architecture.svg" alt="Figure 2: Ingesting Google BigQuery Data into Workers AI (cron-triggered)" title="Figure 2: Ingesting Google BigQuery Data into Workers AI (cron-triggered)" /></p>
<ol>
<li><a href="/workers/configuration/cron-triggers/">A Cron Trigger</a> invokes the Worker without any user interaction.</li>
<li>Worker fetches <a href="/workers/configuration/secrets/">securely stored</a> Google Cloud Platform service account information such as service key and generates a JSON Web Token to issue an authenticated API request to BigQuery.</li>
<li>Worker receives the data from BigQuery and <a href="/workers-ai/guides/tutorials/using-bigquery-with-workers-ai/#6-format-results-from-the-query">transforms it into a format</a> that will make it easier to iterate when interacting with Workers AI.</li>
<li>Using its <a href="/workers-ai/configuration/bindings/">native integration</a> with Workers AI, the Worker forwards the data from BigQuery to generate some content related to it.</li>
<li>Optionally, you can store the BigQuery data and the AI-generated data in a variety of different Cloudflare services.
<ul>
<li>Into <a href="/d1/">D1</a>, a SQL database.</li>
<li>If in step four you used Workers AI to generate embeddings, you can store them in <a href="/vectorize/">Vectorize</a>. To learn more about this type of solution, please consider reviewing the reference architecture diagram on <a href="/reference-architecture/diagrams/ai/ai-rag/">Retrieval Augmented Generation</a>.</li>
<li>To <a href="/kv/">Workers KV</a> if the output of your data will be stored and consumed in a key/value fashion.</li>
<li>If you prefer to save the data fetched from BigQuery and Workers AI into objects (such as images, files, JSONs), you can use <a href="/r2/">R2</a>, our egress-free object storage to do so.</li>
</ul>
</li>
<li>You can set up an integration so a system or a user gets notified whenever a new result is available or if an error occurs. It's also worth mentioning that Workers by themselves can already provide additional <a href="/workers/observability/">observability</a>.
<ul>
<li>Sending an email with all the data retrieved and generated in the previous step is possible using <a href="/email-service/api/send-emails/workers-api/">Email Routing</a>.</li>
<li>Since Workers allows you to issue HTTP requests, you can notify a webhook or API endpoint once the process finishes or if there's an error.</li>
</ul>
</li>
</ol>
<h2 id="related-resources">Related resources</h2>
<ul>
<li><a href="/workers-ai/guides/tutorials/using-bigquery-with-workers-ai/">Tutorial: Using BigQuery with Workers AI</a></li>
<li><a href="/workers-ai/get-started/workers-wrangler/">Workers AI: Get Started</a></li>
<li><a href="/workers/configuration/secrets/">Workers: Secrets</a></li>
<li><a href="/workers/runtime-apis/handlers/scheduled/">Workers: Cron Triggers</a></li>
<li><a href="/email-service/api/send-emails/workers-api/">Email Routing</a></li>
<li><a href="https://cloud.google.com/iam/docs/service-accounts-create#iam-service-accounts-create-console">Create a GCP service account</a></li>
<li><a href="https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console">Create a GCP service account key</a></li>
<li><a href="/reference-architecture/diagrams/ai/ai-rag/">Retrieval Augmented Generation (RAG) Reference Architecture</a></li>
<li><a href="/vectorize/">Vectorize</a></li>
<li><a href="/kv/">Workers KV</a></li>
<li><a href="/r2/">R2</a></li>
<li><a href="/d1/">D1</a></li>
</ul>
