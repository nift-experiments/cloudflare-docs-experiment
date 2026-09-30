<p><a href="https://www.langchain.com/">LangChain</a> is the most popular framework for building AI applications powered by large language models (LLMs).</p>
<p>LangChain publishes multiple Python packages. The following are provided by the Workers runtime:</p>
<ul>
<li><a href="https://pypi.org/project/langchain/"><code>langchain</code></a> (version <code>0.1.8</code>)</li>
<li><a href="https://pypi.org/project/langchain-core/"><code>langchain-core</code></a> (version <code>0.1.25</code>)</li>
<li><a href="https://pypi.org/project/langchain-openai/"><code>langchain-openai</code></a> (version <code>0.0.6</code>)</li>
</ul>
<h2 id="get-started">Get Started</h2>
<p>Clone the <code>cloudflare/python-workers-examples</code> repository and run the LangChain example:</p>
<pre><code class="language-bash">git clone https://github.com/cloudflare/python-workers-examples&#10;cd python-workers-examples/langchain&#10;uv run pywrangler dev&#10;</code></pre>
<h3 id="example-code">Example code</h3>
<pre><code class="language-python">from workers import WorkerEntrypoint, Response&#10;from langchain_core.prompts import PromptTemplate&#10;from langchain_openai import OpenAI&#10;&#10;class Default(WorkerEntrypoint):&#10;    async def fetch(self, request):&#10;        prompt = PromptTemplate.from_template(&quot;Complete the following sentence: I am a {profession} and &quot;)&#10;        llm = OpenAI(api_key=self.env.API_KEY)&#10;        chain = prompt | llm&#10;&#10;        res = await chain.ainvoke({&quot;profession&quot;: &quot;electrician&quot;})&#10;        return Response(res.split(&quot;.&quot;)[0].strip())&#10;</code></pre>
