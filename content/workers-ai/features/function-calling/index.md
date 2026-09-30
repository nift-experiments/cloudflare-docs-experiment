<p>Function calling enables people to take Large Language Models (LLMs) and use the model response to execute functions or interact with external APIs. The developer usually defines a set of functions and the required input schema for each function, which we call <code>tools</code>. The model then intelligently understands when it needs to do a tool call, and it returns a JSON output which the user needs to feed to another function or API.</p>
<p>In essence, function calling allows you to perform actions with LLMs by executing code or making additional API calls.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/Id5oKCa__IA" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<h2 id="how-can-i-use-function-calling">How can I use function calling?</h2>
<p>Workers AI has <a href="/workers-ai/features/function-calling/embedded/">embedded function calling</a> which allows you to execute function code alongside your inference calls. We have a package called <a href="https://www.npmjs.com/package/@cloudflare/ai-utils"><code>@cloudflare/ai-utils</code></a> to help facilitate this, which we have open-sourced on <a href="https://github.com/cloudflare/ai-utils">Github</a>.</p>
<p>For industry-standard function calling, take a look at the documentation on <a href="/workers-ai/features/function-calling/traditional/">Traditional Function Calling</a>.</p>
<p>To show you the value of embedded function calling, take a look at the example below that compares traditional function calling with embedded function calling. Embedded function calling allowed us to cut down the lines of code from 77 to 31.</p>
<div class="nb-tabs" data-nb-tabs><div role="tablist" aria-label="Options" data-nb-tabs-list></div><div data-nb-tabs-panels>
@input("content/.markup/bodies/15821.md")
</div></div>
<h2 id="what-models-support-function-calling">What models support function calling?</h2>
<p>There are open-source models which have been fine-tuned to do function calling. When browsing our <a href="/workers-ai/models/">model catalog</a>, look for models with the function calling property beside it. For example, <a href="/workers-ai/models/hermes-2-pro-mistral-7b/">@hf/nousresearch/hermes-2-pro-mistral-7b</a> is a fine-tuned variant of Mistral 7B that you can use for function calling.</p>
