<p>In this tutorial you will learn how to:</p>
<ul>
<li><strong>Transcribe large audio files:</strong> Use the <a href="/workers-ai/models/whisper-large-v3-turbo/">Whisper-large-v3-turbo</a> model from Cloudflare Workers AI to perform automatic speech recognition (ASR) or translation.</li>
<li><strong>Handle large files:</strong> Split large audio files into smaller chunks for processing, which helps overcome memory and execution time limitations.</li>
<li><strong>Deploy using Cloudflare Workers:</strong> Create a scalable, low‑latency transcription pipeline in a serverless environment.</li>
</ul>
<h2 id="1-create-a-new-cloudflare-worker-project">1: Create a new Cloudflare Worker project</h2>
<ol>
<li>Sign up for a <a href="https://dash.cloudflare.com/sign-up/workers-and-pages">Cloudflare account</a>.</li>
<li>Install <a href="https://docs.npmjs.com/downloading-and-installing-node-js-and-npm"><code>Node.js</code></a>.</li>
</ol>
<details class="nb-details"><summary>Node.js version manager</summary><div class="nb-details-body">
@markup("md", "content/.markup/bodies/15846.md")
</div></details>
<p>You will create a new Worker project using the <code>create-cloudflare</code> CLI (C3). <a href="https://github.com/cloudflare/workers-sdk/tree/main/packages/create-cloudflare">C3</a> is a command-line tool designed to help you set up and deploy new applications to Cloudflare.</p>
<p>Create a new project named <code>whisper-tutorial</code> by running:</p>
<div class="nb-package-managers" data-nb-pm><div role="tablist" aria-label="Package manager"><button type="button" role="tab" data-nb-pm-tab aria-selected="true" tabindex="0">npm</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">yarn</button><button type="button" role="tab" data-nb-pm-tab aria-selected="false" tabindex="-1">pnpm</button></div><div role="tabpanel" data-nb-pm-panel><pre><code data-nb-pm-code>npm create cloudflare@latest -- whisper-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="npm create cloudflare@latest -- whisper-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>yarn create cloudflare whisper-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="yarn create cloudflare whisper-tutorial" aria-label="Copy to clipboard">Copy</button></div><div role="tabpanel" data-nb-pm-panel hidden><pre><code data-nb-pm-code>pnpm create cloudflare@latest whisper-tutorial</code></pre><button type="button" data-nb-pm-copy data-nb-command="pnpm create cloudflare@latest whisper-tutorial" aria-label="Copy to clipboard">Copy</button></div></div>
<p>Running <code>npm create cloudflare@latest</code> will prompt you to install the <a href="https://www.npmjs.com/package/create-cloudflare"><code>create-cloudflare</code> package</a>, and lead you through setup. C3 will also install <a href="/workers/wrangler/">Wrangler</a>, the Cloudflare Developer Platform CLI.</p>
<p>For setup, select the following options:</p>
<ul>
<li>For <em>What would you like to start with?</em>, choose <code>Hello World example</code>.</li>
<li>For <em>Which template would you like to use?</em>, choose <code>Worker only</code>.</li>
<li>For <em>Which language do you want to use?</em>, choose <code>TypeScript</code>.</li>
<li>For <em>Do you want to use git for version control?</em>, choose <code>Yes</code>.</li>
<li>For <em>Do you want to deploy your application?</em>, choose <code>No</code> (we will be making some changes before deploying).</li>
</ul>
<p>This will create a new <code>whisper-tutorial</code> directory. Your new <code>whisper-tutorial</code> directory will include:</p>
<ul>
<li>A <code>&quot;Hello World&quot;</code> <a href="/workers/get-started/guide/#3-write-code">Worker</a> at <code>src/index.ts</code>.</li>
<li>A <a href="/workers/wrangler/configuration/"><code>wrangler.jsonc</code></a> configuration file.</li>
</ul>
<p>Go to your application directory:</p>
<pre><code class="language-sh">cd whisper-tutorial&#10;</code></pre>
<h2 id="2-connect-your-worker-to-workers-ai"><ol start="2">
<li>Connect your Worker to Workers AI</li>
</ol></h2>
<p>You must create an AI binding for your Worker to connect to Workers AI. <a href="/workers/runtime-apis/bindings/">Bindings</a> allow your Workers to interact with resources, like Workers AI, on the Cloudflare Developer Platform.</p>
<p>To bind Workers AI to your Worker, add the following to the end of your Wrangler configuration file:</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15847.md")
</div>
<p>Your binding is <a href="/workers/reference/migrate-to-module-workers/#bindings-in-es-modules-format">available in your Worker code</a> on <a href="/workers/runtime-apis/handlers/fetch/"><code>env.AI</code></a>.</p>
<h2 id="3-configure-wrangler"><ol start="3">
<li>Configure Wrangler</li>
</ol></h2>
<p>In your wrangler file, add or update the following settings to enable Node.js APIs and polyfills (with a compatibility date of 2024‑09‑23 or later):</p>
<div class="nb-wrangler-config">
@markup("md", "content/.markup/bodies/15848.md")
</div>
<h2 id="4-handle-large-audio-files-with-chunking"><ol start="4">
<li>Handle large audio files with chunking</li>
</ol></h2>
<p>Replace the contents of your <code>src/index.ts</code> file with the following integrated code. This sample demonstrates how to:</p>
<p>(1) Extract an audio file URL from the query parameters.</p>
<p>(2) Fetch the audio file while explicitly following redirects.</p>
<p>(3) Split the audio file into smaller chunks (such as, 1 MB chunks).</p>
<p>(4) Transcribe each chunk using the Whisper-large-v3-turbo model via the Cloudflare AI binding.</p>
<p>(5) Return the aggregated transcription as plain text.</p>
<pre><code class="language-ts">import { Buffer } from &quot;node:buffer&quot;;&#10;import type { Ai } from &quot;workers-ai&quot;;&#10;&#10;export interface Env {&#10;	AI: Ai;&#10;	// If needed, add your KV namespace for storing transcripts.&#10;	// MY_KV_NAMESPACE: KVNamespace;&#10;}&#10;&#10;/**&#10; &#42; Fetches the audio file from the provided URL and splits it into chunks.&#10; &#42; This function explicitly follows redirects.&#10; &#42;&#10; &#42; @param audioUrl - The URL of the audio file.&#10; &#42; @returns An array of ArrayBuffers, each representing a chunk of the audio.&#10; &#42;/&#10;async function getAudioChunks(audioUrl: string): Promise&lt;ArrayBuffer[]&gt; {&#10;	const response = await fetch(audioUrl, { redirect: &quot;follow&quot; });&#10;	if (!response.ok) {&#10;		throw new Error(`Failed to fetch audio: ${response.status}`);&#10;	}&#10;	const arrayBuffer = await response.arrayBuffer();&#10;&#10;	// Example: Split the audio into 1MB chunks.&#10;	const chunkSize = 1024 * 1024; // 1MB&#10;	const chunks: ArrayBuffer[] = [];&#10;	for (let i = 0; i &lt; arrayBuffer.byteLength; i += chunkSize) {&#10;		const chunk = arrayBuffer.slice(i, i + chunkSize);&#10;		chunks.push(chunk);&#10;	}&#10;	return chunks;&#10;}&#10;&#10;/**&#10; &#42; Transcribes a single audio chunk using the Whisper‑large‑v3‑turbo model.&#10; &#42; The function converts the audio chunk to a Base64-encoded string and&#10; &#42; sends it to the model via the AI binding.&#10; &#42;&#10; &#42; @param chunkBuffer - The audio chunk as an ArrayBuffer.&#10; &#42; @param env - The Cloudflare Worker environment, including the AI binding.&#10; &#42; @returns The transcription text from the model.&#10; &#42;/&#10;async function transcribeChunk(&#10;	chunkBuffer: ArrayBuffer,&#10;	env: Env,&#10;): Promise&lt;string&gt; {&#10;	const base64 = Buffer.from(chunkBuffer, &quot;binary&quot;).toString(&quot;base64&quot;);&#10;	const res = await env.AI.run(&quot;@cf/openai/whisper-large-v3-turbo&quot;, {&#10;		audio: base64,&#10;		// Optional parameters (uncomment and set if needed):&#10;		// task: &quot;transcribe&quot;,   // or &quot;translate&quot;&#10;		// language: &quot;en&quot;,&#10;		// vad_filter: &quot;false&quot;,&#10;		// initial_prompt: &quot;Provide context if needed.&quot;,&#10;		// prefix: &quot;Transcription:&quot;,&#10;	});&#10;	return res.text; // Assumes the transcription result includes a &quot;text&quot; property.&#10;}&#10;&#10;/**&#10; &#42; The main fetch handler. It extracts the &#x27;url&#x27; query parameter, fetches the audio,&#10; &#42; processes it in chunks, and returns the full transcription.&#10; &#42;/&#10;export default {&#10;	async fetch(&#10;		request: Request,&#10;		env: Env,&#10;		ctx: ExecutionContext,&#10;	): Promise&lt;Response&gt; {&#10;		// Extract the audio URL from the query parameters.&#10;		const { searchParams } = new URL(request.url);&#10;		const audioUrl = searchParams.get(&quot;url&quot;);&#10;&#10;		if (!audioUrl) {&#10;			return new Response(&quot;Missing &#x27;url&#x27; query parameter&quot;, { status: 400 });&#10;		}&#10;&#10;		// Get the audio chunks.&#10;		const audioChunks: ArrayBuffer[] = await getAudioChunks(audioUrl);&#10;		let fullTranscript = &quot;&quot;;&#10;&#10;		// Process each chunk and build the full transcript.&#10;		for (const chunk of audioChunks) {&#10;			try {&#10;				const transcript = await transcribeChunk(chunk, env);&#10;				fullTranscript += transcript + &quot;\n&quot;;&#10;			} catch (error) {&#10;				fullTranscript += &quot;[Error transcribing chunk]\n&quot;;&#10;			}&#10;		}&#10;&#10;		return new Response(fullTranscript, {&#10;			headers: { &quot;Content-Type&quot;: &quot;text/plain&quot; },&#10;		});&#10;	},&#10;} satisfies ExportedHandler&lt;Env&gt;;&#10;</code></pre>
<h2 id="5-deploy-your-worker"><ol start="5">
<li>Deploy your Worker</li>
</ol></h2>
<ol>
<li>
<p><strong>Run the Worker locally:</strong></p>
<p>Use wrangler's development mode to test your Worker locally:</p>
</li>
</ol>
<pre><code class="language-sh">npx wrangler dev&#10;</code></pre>
<p>Open your browser and go to <a href="http://localhost:8787">http://localhost:8787</a>, or use curl:</p>
<pre><code class="language-sh">curl &quot;http://localhost:8787?url=https://raw.githubusercontent.com/your-username/your-repo/main/your-audio-file.mp3&quot;&#10;</code></pre>
<p>Replace the URL query parameter with the direct link to your audio file. (For GitHub-hosted files, ensure you use the raw file URL.)</p>
<ol start="2">
<li>
<p><strong>Deploy the Worker:</strong></p>
<p>Once testing is complete, deploy your Worker with:</p>
</li>
</ol>
<pre><code class="language-sh">npx wrangler deploy&#10;</code></pre>
<ol start="3">
<li>
<p><strong>Test the deployed Worker:</strong></p>
<p>After deployment, test your Worker by passing the audio URL as a query parameter:</p>
</li>
</ol>
<pre><code class="language-sh">curl &quot;https://&lt;your-worker-subdomain&gt;.workers.dev?url=https://raw.githubusercontent.com/your-username/your-repo/main/your-audio-file.mp3&quot;&#10;</code></pre>
<p>Make sure to replace <code>&lt;your-worker-subdomain&gt;</code>, <code>your-username</code>, <code>your-repo</code>, and <code>your-audio-file.mp3</code> with your actual details.</p>
<p>If successful, the Worker will return a transcript of the audio file:</p>
<pre><code class="language-sh">This is the transcript of the audio...&#10;</code></pre>
