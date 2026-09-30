<p>Specify model or provider fallbacks with your <a href="/ai-gateway/usage/universal/">Universal endpoint</a> to handle request failures and ensure reliability.</p>
<p>Cloudflare can trigger your fallback provider in response to <a href="#request-failures">request errors</a> or <a href="/ai-gateway/configuration/request-handling#request-timeouts">predetermined request timeouts</a>. The <a href="#response-headercf-aig-step">response header <code>cf-aig-step</code></a> indicates which step successfully processed the request.</p>
<h2 id="request-failures">Request failures</h2>
<p>By default, Cloudflare triggers your fallback if a model request returns an error.</p>
<h3 id="example">Example</h3>
<p>In the following example, a request first goes to the <a href="/workers-ai/">Workers AI</a> Inference API. If the request fails, it falls back to OpenAI. The response header <code>cf-aig-step</code> indicates which provider successfully processed the request.</p>
<ol>
<li>Sends a request to Workers AI Inference API.</li>
<li>If that request fails, proceeds to OpenAI.</li>
</ol>
<pre><code class="language-mermaid">graph TD&#10;    A[AI Gateway] --&gt; B[Request to Workers AI Inference API]&#10;    B --&gt;|Success| C[Return Response]&#10;    B --&gt;|Failure| D[Request to OpenAI API]&#10;    D --&gt; E[Return Response]&#10;</code></pre>
<br />
<p>You can add as many fallbacks as you need, just by adding another object in the array.</p>
<pre><code class="language-bash">curl https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id} \&#10;  &#45;-header &#x27;Content-Type: application/json&#x27; \&#10;  &#45;-data &#x27;[&#10;  {&#10;    &quot;provider&quot;: &quot;workers-ai&quot;,&#10;    &quot;endpoint&quot;: &quot;@cf/meta/llama-3.1-8b-instruct&quot;,&#10;    &quot;headers&quot;: {&#10;      &quot;Authorization&quot;: &quot;Bearer {cloudflare_token}&quot;,&#10;      &quot;Content-Type&quot;: &quot;application/json&quot;&#10;    },&#10;    &quot;query&quot;: {&#10;      &quot;messages&quot;: [&#10;        {&#10;          &quot;role&quot;: &quot;system&quot;,&#10;          &quot;content&quot;: &quot;You are a friendly assistant&quot;&#10;        },&#10;        {&#10;          &quot;role&quot;: &quot;user&quot;,&#10;          &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;      ]&#10;    }&#10;  },&#10;  {&#10;    &quot;provider&quot;: &quot;openai&quot;,&#10;    &quot;endpoint&quot;: &quot;chat/completions&quot;,&#10;    &quot;headers&quot;: {&#10;      &quot;Authorization&quot;: &quot;Bearer {open_ai_token}&quot;,&#10;      &quot;Content-Type&quot;: &quot;application/json&quot;&#10;    },&#10;    &quot;query&quot;: {&#10;      &quot;model&quot;: &quot;gpt-4o-mini&quot;,&#10;      &quot;stream&quot;: true,&#10;      &quot;messages&quot;: [&#10;        {&#10;          &quot;role&quot;: &quot;user&quot;,&#10;          &quot;content&quot;: &quot;What is Cloudflare?&quot;&#10;        }&#10;      ]&#10;    }&#10;  }&#10;]&#x27;&#10;</code></pre>
<h2 id="response-header-cf-aig-step">Response header(cf-aig-step)</h2>
<p>When using the <a href="/ai-gateway/usage/universal/">Universal endpoint</a> with fallbacks, the response header <code>cf-aig-step</code> indicates which model successfully processed the request by returning the step number. This header provides visibility into whether a fallback was triggered and which model ultimately processed the response.</p>
<ul>
<li><code>cf-aig-step:0</code> – The first (primary) model was used successfully.</li>
<li><code>cf-aig-step:1</code> – The request fell back to the second model.</li>
<li><code>cf-aig-step:2</code> – The request fell back to the third model.</li>
<li>Subsequent steps – Each fallback increments the step number by 1.</li>
</ul>
