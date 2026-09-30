<p>Workers AI is now Generally Available. We've updated our rate limits to reflect this.</p>
<p>Note that model inferences in local mode using Wrangler will also count towards these limits. Beta models may have lower rate limits while we work on performance and scale.</p>
<aside class="nb-aside note">
<h3 class="nb-aside-title" id="custom-requirements">Custom requirements</h3>
@markup("md", "content/.markup/bodies/15806.md")
</aside>
<p>Rate limits are default per task type, with some per-model limits defined as follows:</p>
<h2 id="rate-limits-by-task-type">Rate limits by task type</h2>
<h3 id="automatic-speech-recognition-workers-ai-models"><a href="/workers-ai/models/">Automatic Speech Recognition</a></h3>
<ul>
<li>720 requests per minute</li>
</ul>
<h3 id="image-classification-workers-ai-models"><a href="/workers-ai/models/">Image Classification</a></h3>
<ul>
<li>3000 requests per minute</li>
</ul>
<h3 id="image-to-text-workers-ai-models"><a href="/workers-ai/models/">Image-to-Text</a></h3>
<ul>
<li>720 requests per minute</li>
</ul>
<h3 id="object-detection-workers-ai-models"><a href="/workers-ai/models/">Object Detection</a></h3>
<ul>
<li>3000 requests per minute</li>
</ul>
<h3 id="summarization-workers-ai-models"><a href="/workers-ai/models/">Summarization</a></h3>
<ul>
<li>1500 requests per minute</li>
</ul>
<h3 id="text-classification-workers-ai-models"><a href="/workers-ai/models/">Text Classification</a></h3>
<ul>
<li>2000 requests per minute</li>
</ul>
<h3 id="text-embeddings-workers-ai-models"><a href="/workers-ai/models/">Text Embeddings</a></h3>
<ul>
<li>3000 requests per minute</li>
<li><a href="/workers-ai/models/bge-large-en-v1.5/">@cf/baai/bge-large-en-v1.5</a> is 1500 requests per minute</li>
</ul>
<h3 id="text-generation-workers-ai-models"><a href="/workers-ai/models/">Text Generation</a></h3>
<ul>
<li>300 requests per minute, unless the model requires the Workers Paid plan</li>
</ul>
<h4 id="paid-models">Paid models</h4>
<p>The following limits apply per account, per model to any model that requires the <a href="/workers/platform/pricing/#workers">Workers Paid plan</a> — each model page states whether it does. These models are the only models that do not receive the default limit:</p>
<table>
<thead>
<tr>
<th>Billing</th>
<th>Rate limit</th>
</tr>
</thead>
<tbody>
<tr>
<td>Standard Workers AI billing</td>
<td>20 requests per minute</td>
</tr>
<tr>
<td>Prepaid AI Gateway credits</td>
<td>50 requests per minute</td>
</tr>
</tbody>
</table>
<p>To receive the elevated limit, load <a href="/ai-gateway/features/unified-billing/">prepaid AI Gateway credits</a> and set the gateway's <a href="/ai-gateway/configuration/manage-gateway/#configure-workers-ai-billing">Workers AI billing setting</a> to <strong>Unified billing</strong>. These limits are designed for typical agentic and coding workloads, where requests to frontier models can take longer to complete.</p>
<h3 id="text-to-image-workers-ai-models"><a href="/workers-ai/models/">Text-to-Image</a></h3>
<ul>
<li>720 requests per minute</li>
<li><a href="/workers-ai/models/stable-diffusion-v1-5-img2img/">@cf/runwayml/stable-diffusion-v1-5-img2img</a> is 1500 requests per minute</li>
</ul>
<h3 id="translation-workers-ai-models"><a href="/workers-ai/models/">Translation</a></h3>
<ul>
<li>720 requests per minute</li>
</ul>
