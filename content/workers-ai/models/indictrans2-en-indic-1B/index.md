<img src="/assets/upstream/images/workers-ai/meta.svg" alt="Meta logo" width="48" height="48">

<h1 id="indictrans2-en-indic-1b">indictrans2-en-indic-1B</h1>

<p><code>@cf/ai4bharat/indictrans2-en-indic-1B</code></p>

IndicTrans2 is the first open-source transformer-based multilingual NMT model that supports high-quality translations across all the 22 scheduled Indic languages

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Translation</td></tr>
<tr><th>Unit pricing</th><td>USD 0.342 per M input tokens, USD 0.342 per M output tokens</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

<pre><code class="language-ts">export default {
  async fetch(request, env) {
    const input = await request.json();
    const response = await env.AI.run(&quot;@cf/ai4bharat/indictrans2-en-indic-1B&quot;, input);
    return Response.json(response);
  },
} satisfies ExportedHandler&lt;Env&gt;;</code></pre>

<pre><code class="language-ts">const response = await env.AI.run(&quot;@cf/ai4bharat/indictrans2-en-indic-1B&quot;, { translation: input });</code></pre>

<pre><code class="language-sh">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run/@cf/ai4bharat/indictrans2-en-indic-1B -H &quot;Authorization: Bearer $CLOUDFLARE_AUTH_TOKEN&quot;</code></pre>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>text</code></td><td>string or array</td><td>Required. Input text to translate. Can be a single string or a list of strings.</td></tr><tr><td><code>target_language</code></td><td>string</td><td>Required. Target langauge to translate to Default: hin_Deva; Values: asm_Beng, awa_Deva, ben_Beng, bho_Deva, brx_Deva, doi_Deva, eng_Latn, gom_Deva, gon_Deva, guj_Gujr, hin_Deva, hne_Deva, kan_Knda, kas_Arab, kas_Deva, kha_Latn, lus_Latn, mag_Deva, mai_Deva, mal_Mlym, mar_Deva, mni_Beng, mni_Mtei, npi_Deva, ory_Orya, pan_Guru, san_Deva, sat_Olck, snd_Arab, snd_Deva, tam_Taml, tel_Telu, urd_Arab, unr_Deva</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>translations</code></td><td>array</td><td>Required. Translated texts</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/workers-ai/models/indictrans2-en-indic-1B/schema-input.json)
- [Output schema](/workers-ai/models/indictrans2-en-indic-1B/schema-output.json)

