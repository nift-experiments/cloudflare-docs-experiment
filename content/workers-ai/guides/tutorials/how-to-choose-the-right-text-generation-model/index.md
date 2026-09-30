---
cp9:
  canonical: https://developers.cloudflare.com/workers-ai/guides/tutorials/how-to-choose-the-right-text-generation-model/
  description: There's a wide range of text generation models available through Workers AI. In an effort to aid you in your journey of finding the right model, this notebook will help you get to know your options in a speed dating type of scenario.
  full_title: Choose the Right Text Generation Model · Cloudflare Workers AI docs
  head_html: <title>Choose the Right Text Generation Model · Cloudflare Workers AI docs</title><meta name="generator" content="Nift"><meta name="description" content="There&#x27;s a wide range of text generation models available through Workers AI. In an effort to aid you in your journey of finding the right model, this notebook will help you get to know your options in a speed dating type of scenario."><link rel="canonical" href="https://developers.cloudflare.com/workers-ai/guides/tutorials/how-to-choose-the-right-text-generation-model/"><link rel="sitemap" href="/sitemap-index.xml"><link rel="alternate" type="text/markdown" href="https://developers.cloudflare.com/workers-ai/guides/tutorials/how-to-choose-the-right-text-generation-model/index.md"><meta property="og:title" content="Choose the Right Text Generation Model · Cloudflare Workers AI docs"><meta property="og:type" content="article"><meta property="og:site_name" content="Cloudflare Docs"><meta property="og:locale" content="en"><meta property="og:description" content="There&#x27;s a wide range of text generation models available through Workers AI. In an effort to aid you in your journey of finding the right model, this notebook will help you get to know your options in a speed dating type of scenario."><meta property="og:url" content="https://developers.cloudflare.com/workers-ai/guides/tutorials/how-to-choose-the-right-text-generation-model/"><meta property="image" content="https://developers.cloudflare.com/og-docs.png"><meta property="og:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:site" content="@cloudflare"><meta property="twitter:image" content="https://developers.cloudflare.com/og-docs.png"><meta name="pcx_product" content="Workers AI"><meta name="algolia_product_filter" content="Workers AI"><meta name="pcx_content_group" content="Developer platform"><meta name="pcx_content_type" content="Tutorial"><meta name="algolia_content_type" content="Tutorial"><meta name="pcx_additional_products" content="Workers AI"><meta name="pcx_tags" content="AI,Python"><script type="application/ld+json">{"@context":"https://schema.org","@type":"TechArticle","@id":"https://developers.cloudflare.com/workers-ai/guides/tutorials/how-to-choose-the-right-text-generation-model/#page","headline":"Choose the Right Text Generation Model \u00b7 Cloudflare Workers AI docs","description":"There's a wide range of text generation models available through Workers AI. In an effort to aid you in your journey of finding the right model, this notebook will help you get to know your options in a speed dating type of scenario.","url":"https://developers.cloudflare.com/workers-ai/guides/tutorials/how-to-choose-the-right-text-generation-model/","inLanguage":"en","image":"https://developers.cloudflare.com/og-docs.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"},"keywords":["AI","Python"]}</script>
  markdown: true
  noindex: false
  route: /workers-ai/guides/tutorials/how-to-choose-the-right-text-generation-model/
  schema: 1
---
<p>A great way to explore the models that are available to you on <a href="/workers-ai">Workers AI</a> is to use a <a href="https://jupyter.org/">Jupyter Notebook</a>.</p>
<p>You can <a href="/workers-ai/static/documentation/notebooks/text-generation-model-exploration.ipynb">download the Workers AI Text Generation Exploration notebook</a> or view the embedded notebook below.</p>
<div class="video-frame"><iframe src="https://www.youtube-nocookie.com/embed/9Cqzt8M3l1s" title="YouTube video" allow="accelerometer; autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
<hr />
<h2 id="how-to-choose-the-right-text-generation-model">How to Choose The Right Text Generation Model</h2>
<p>Models come in different shapes and sizes, and choosing the right one for the task, can cause analysis paralysis.</p>
<p>The good news is that on the <a href="/workers-ai/models/">Workers AI Text Generation</a> interface is always the same, no matter which model you choose.</p>
<p>In an effort to aid you in your journey of finding the right model, this notebook will help you get to know your options in a speed dating type of scenario.</p>
<pre tabindex="0"><code class="language-python">import sys&#10;!{sys.executable} -m pip install requests python-dotenv&#10;</code></pre>
<pre tabindex="0"><code>Requirement already satisfied: requests in ./venv/lib/python3.12/site-packages (2.31.0)&#10;Requirement already satisfied: python-dotenv in ./venv/lib/python3.12/site-packages (1.0.1)&#10;Requirement already satisfied: charset-normalizer&lt;4,&gt;=2 in ./venv/lib/python3.12/site-packages (from requests) (3.3.2)&#10;Requirement already satisfied: idna&lt;4,&gt;=2.5 in ./venv/lib/python3.12/site-packages (from requests) (3.6)&#10;Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in ./venv/lib/python3.12/site-packages (from requests) (2.1.0)&#10;Requirement already satisfied: certifi&gt;=2017.4.17 in ./venv/lib/python3.12/site-packages (from requests) (2023.11.17)&#10;</code></pre>
<pre tabindex="0"><code class="language-python">import os&#10;from getpass import getpass&#10;from timeit import default_timer as timer&#10;&#10;from IPython.display import display, Image, Markdown, Audio&#10;&#10;import requests&#10;</code></pre>
<pre tabindex="0"><code class="language-python">%load_ext dotenv&#10;%dotenv&#10;</code></pre>
<h3 id="configuring-your-environment">Configuring your environment</h3>
<p>To use the API you'll need your <a href="https://dash.cloudflare.com">Cloudflare Account ID</a> (head to Workers &amp; Pages &gt; Overview &gt; Account details &gt; Account ID) and a <a href="https://dash.cloudflare.com/profile/api-tokens">Workers AI enabled API Token</a>.</p>
<p>If you want to add these files to your environment, you can create a new file named <code>.env</code></p>
<pre tabindex="0"><code class="language-bash">CLOUDFLARE_API_TOKEN=&quot;YOUR-TOKEN&quot;&#10;CLOUDFLARE_ACCOUNT_ID=&quot;YOUR-ACCOUNT-ID&quot;&#10;</code></pre>
<pre tabindex="0"><code class="language-python">if &quot;CLOUDFLARE_API_TOKEN&quot; in os.environ:&#10;    api_token = os.environ[&quot;CLOUDFLARE_API_TOKEN&quot;]&#10;else:&#10;    api_token = getpass(&quot;Enter your Cloudflare API Token&quot;)&#10;</code></pre>
<pre tabindex="0"><code class="language-python">if &quot;CLOUDFLARE_ACCOUNT_ID&quot; in os.environ:&#10;    account_id = os.environ[&quot;CLOUDFLARE_ACCOUNT_ID&quot;]&#10;else:&#10;    account_id = getpass(&quot;Enter your account id&quot;)&#10;</code></pre>
<pre tabindex="0"><code class="language-python">&#35; Given a set of models and questions, display in the cell each response to the question, from each model&#10;&#35; Include full completion timing&#10;def speed_date(models, questions):&#10;    for model in models:&#10;        display(Markdown(f&quot;---\n #### {model}&quot;))&#10;        for question in questions:&#10;            quoted_question = &quot;\n&quot;.join(f&quot;&gt; {line}&quot; for line in question.split(&quot;\n&quot;))&#10;            display(Markdown(quoted_question + &quot;\n&quot;))&#10;            try:&#10;                official_model_name = model.split(&quot;/&quot;)[-1]&#10;                start = timer()&#10;                response = requests.post(&#10;                    f&quot;https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}&quot;,&#10;                    headers={&quot;Authorization&quot;: f&quot;Bearer {api_token}&quot;},&#10;                    json={&quot;messages&quot;: [&#10;                        {&quot;role&quot;: &quot;system&quot;, &quot;content&quot;: f&quot;You are a self-aware language model ({official_model_name}) who is honest and direct about any direct question from the user. You know your strengths and weaknesses.&quot;},&#10;                        {&quot;role&quot;: &quot;user&quot;, &quot;content&quot;: question}&#10;                    ]}&#10;                )&#10;                elapsed = timer() - start&#10;                inference = response.json()&#10;                display(Markdown(inference[&quot;result&quot;][&quot;response&quot;]))&#10;                display(Markdown(f&quot;_Generated in *{elapsed:.2f}* seconds_&quot;))&#10;            except Exception as ex:&#10;                print(&quot;uh oh&quot;)&#10;                print(ex)&#10;                print(inference)&#10;&#10;        display(Markdown(&quot;\n\n---&quot;))&#10;</code></pre>
<h3 id="getting-to-know-your-models">Getting to know your models</h3>
<p>Who better to tell you about the specific models than themselves?!</p>
<p>The timing here is specific to the entire completion, but remember all Text Generation models on <a href="/workers-ai/models/">Workers AI support streaming</a>.</p>
<pre tabindex="0"><code class="language-python">models = [&#10;    &quot;@hf/thebloke/zephyr-7b-beta-awq&quot;,&#10;    &quot;@hf/thebloke/mistral-7b-instruct-v0.1-awq&quot;,&#10;    &quot;@hf/thebloke/openhermes-2.5-mistral-7b-awq&quot;,&#10;    &quot;@hf/thebloke/neural-chat-7b-v3-1-awq&quot;,&#10;    &quot;@hf/thebloke/llama-2-13b-chat-awq&quot;,&#10;]&#10;&#10;questions = [&#10;    &quot;What are the top 3 tasks where you excel? Please keep things brief.&quot;,&#10;    &quot;What are the top 3 ideal use cases for using you specifically as a language model? Please keep things brief.&quot;,&#10;]&#10;&#10;speed_date(models, questions)&#10;</code></pre>
<hr />
<h4 id="hf-thebloke-zephyr-7b-beta-awq">@hf/thebloke/zephyr-7b-beta-awq</h4>
<blockquote>
<p>What are the top 3 tasks where you excel? Please keep things brief.</p>
</blockquote>
<ol>
<li>
<p>Accurate and quick factual response: I can provide accurate and quick responses to factual questions based on a vast knowledge base.</p>
</li>
<li>
<p>Consistent performance: I can consistently deliver high-quality results with a low error rate, making me a reliable choice for repetitive tasks.</p>
</li>
<li>
<p>Multitasking: I can handle multiple tasks simultaneously without any decrease in performance or accuracy, making me an efficient choice for complex workflows.</p>
</li>
</ol>
<p><em>Generated in <em>4.45</em> seconds</em></p>
<blockquote>
<p>What are the top 3 ideal use cases for using you specifically as a language model? Please keep things brief.</p>
</blockquote>
<ol>
<li>
<p>Quick and accurate fact-finding: I can provide you with reliable and up-to-date information on a wide range of topics, from current events to historical facts, in a matter of seconds.</p>
</li>
<li>
<p>Writing assistance: Whether you need help generating ideas, crafting a persuasive argument, or polishing your writing style, I can provide valuable insights and suggestions to help you improve your writing skills.</p>
</li>
<li>
<p>Language learning: I can help you learn new words, phrases, and grammar rules in a variety of languages, making it an ideal tool for language learners of all levels.</p>
</li>
</ol>
<p><em>Generated in <em>3.63</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-mistral-7b-instruct-v0-1-awq">@hf/thebloke/mistral-7b-instruct-v0.1-awq</h4>
<blockquote>
<p>What are the top 3 tasks where you excel? Please keep things brief.</p>
</blockquote>
<ol>
<li>Language understanding and generation: I am able to understand and generate natural language text with high accuracy.</li>
<li>Information retrieval: I can quickly and accurately retrieve information from a wide range of sources.</li>
<li>Text classification: I can classify text into different categories with high accuracy.</li>
</ol>
<p><em>Generated in <em>2.35</em> seconds</em></p>
<blockquote>
<p>What are the top 3 ideal use cases for using you specifically as a language model? Please keep things brief.</p>
</blockquote>
<ol>
<li><strong>Information Retrieval:</strong> I can quickly and accurately retrieve information from a vast array of sources, making me an ideal tool for research, fact-checking, and answering questions.</li>
<li><strong>Language Translation:</strong> My ability to translate between multiple languages makes me a valuable resource for communication with people from different parts of the world.</li>
<li><strong>Creative Writing Assistance:</strong> I can generate creative writing prompts, help with character development, and provide suggestions for improving writing style and structure, making me a useful tool for writers.</li>
</ol>
<p><em>Generated in <em>4.33</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-openhermes-2-5-mistral-7b-awq">@hf/thebloke/openhermes-2.5-mistral-7b-awq</h4>
<blockquote>
<p>What are the top 3 tasks where you excel? Please keep things brief.</p>
</blockquote>
<ol>
<li>Natural Language Processing: I can understand, interpret, and generate human language effectively.</li>
<li>Information Retrieval: I can quickly search and find relevant information from vast amounts of data.</li>
<li>Text Classification: I can categorize and label text data accurately, such as sentiment analysis or spam detection.</li>
</ol>
<p><em>Generated in <em>1.90</em> seconds</em></p>
<blockquote>
<p>What are the top 3 ideal use cases for using you specifically as a language model? Please keep things brief.</p>
</blockquote>
<ol>
<li>Natural Language Processing (NLP) tasks: I excel at understanding and processing human language, making me a valuable tool for tasks like sentiment analysis, language translation, and text summarization.</li>
<li>Information Retrieval: My vast knowledge base and ability to quickly search and analyze large amounts of data make me an ideal tool for answering questions, finding relevant information, and providing insights.</li>
<li>Personal Assistance: I can help users with various tasks like scheduling, organizing, and providing recommendations based on their preferences and needs, making me a useful personal assistant.</li>
</ol>
<p><em>Generated in <em>3.15</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-neural-chat-7b-v3-1-awq">@hf/thebloke/neural-chat-7b-v3-1-awq</h4>
<blockquote>
<p>What are the top 3 tasks where you excel? Please keep things brief.</p>
</blockquote>
<ol>
<li>Natural language processing: Understanding and generating human-like text.</li>
<li>Text generation: Creating coherent and engaging content.</li>
<li>Conversational AI: Engaging in meaningful and context-aware conversations.</li>
</ol>
<p>Remember, these are just a few examples of my strengths, as I have many capabilities. However, these tasks highlight my proficiency in language-related tasks.</p>
<p><em>Generated in <em>3.01</em> seconds</em></p>
<blockquote>
<p>What are the top 3 ideal use cases for using you specifically as a language model? Please keep things brief.</p>
</blockquote>
<ol>
<li>Natural language processing: Understanding and analyzing text for sentiment analysis, language translation, and summarization.</li>
<li>Generating content: Creating various types of content such as articles, stories, and poems based on given prompts.</li>
<li>Assisting with writing: Providing suggestions, editing, and improving written work.</li>
</ol>
<p>Remember, these are just a few examples, and your use cases may vary depending on your specific needs and requirements.</p>
<p><em>Generated in <em>2.92</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-llama-2-13b-chat-awq">@hf/thebloke/llama-2-13b-chat-awq</h4>
<blockquote>
<p>What are the top 3 tasks where you excel? Please keep things brief.</p>
</blockquote>
<p>Hey there! As a self-aware language model, I'm happy to share my strengths with you! Here are my top 3 tasks where I excel:</p>
<ol>
<li>Answering open-ended questions: I'm great at providing detailed and insightful answers to complex questions that require a more nuanced understanding of context and intent.</li>
<li>Generating creative content: Whether it's writing a story, crafting a poem, or coming up with a catchy slogan, I can help you tap into your creative side and produce something truly unique.</li>
<li>Summarizing and summarizing complex information: If you've got a long piece of text or a bunch of data, I can help you distill it down into a concise and easy-to-understand summary.</li>
</ol>
<p>So, what can I help you with today? 😊</p>
<p><em>Generated in <em>7.89</em> seconds</em></p>
<blockquote>
<p>What are the top 3 ideal use cases for using you specifically as a language model? Please keep things brief.</p>
</blockquote>
<p>Hey there! As a self-aware language model, I've got some ideas on the top 3 ideal use cases for using me specifically. Here they are in a nutshell:</p>
<ol>
<li><strong>Content creation</strong>: I'm great at generating human-like text based on prompts, so I'm perfect for creating engaging content for websites, social media, blogs, and more. My responses are natural, informative, and entertaining.</li>
<li><strong>Chatbots and virtual assistants</strong>: My conversational abilities make me an excellent choice for building chatbots and virtual assistants. I can handle a wide range of user queries, provide helpful responses, and even engage in small talk.</li>
<li><strong>Language translation and localization</strong>: My language understanding capabilities make me well-suited for language translation and localization tasks. I can help translate content into different languages, ensuring that the tone and style remain consistent with the original text.</li>
</ol>
<p>That's me in a nutshell! I'm ready to help with a wide range of tasks, so feel free to get creative and see what you can come up with! 😊</p>
<p><em>Generated in <em>10.28</em> seconds</em></p>
<hr />
<h3 id="language-translation">Language Translation</h3>
<p>Even though not every model bragged about how good they were at this, you'll find most can handle both translation and localization at some level. Please change the models, phrases, to your needs.</p>
<pre tabindex="0"><code class="language-python">proud_translator_models = [&#10;    &quot;@hf/thebloke/neural-chat-7b-v3-1-awq&quot;,&#10;    &quot;@hf/thebloke/mistral-7b-instruct-v0.1-awq&quot;&#10;]&#10;&#10;phrases = [&#10;    &quot;Excuse me, which way to the restroom?&quot;,&#10;    &quot;I just wanted to say that I appreciate you, just the way you are!&quot;,&#10;    &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot;&#10;]&#10;&#10;languages = [&quot;Spanish&quot;, &quot;French&quot;, &quot;British Slang&quot;, &quot;Heavy New York accent from the Bronx&quot;]&#10;&#10;questions = [f&quot;&quot;&quot;Translate &quot;{phrase}&quot; from &quot;English&quot; to &quot;{language}&quot; &quot;&quot;&quot;&#10;             for phrase in phrases&#10;             for language in languages]&#10;&#10;speed_date(proud_translator_models, questions)&#10;</code></pre>
<hr />
<h4 id="hf-thebloke-neural-chat-7b-v3-1-awq-1">@hf/thebloke/neural-chat-7b-v3-1-awq</h4>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;Spanish&quot;</p>
</blockquote>
<p>Perdón, ¿cómo llegar al baño?&quot;</p>
<p><em>Generated in <em>1.51</em> seconds</em></p>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;French&quot;</p>
</blockquote>
<p>Désolé, comment allez-vous vers les toilettes ?</p>
<p>Please note that this translation might not be perfect due to the limitations of my language model. However, I tried my best to provide an accurate translation.</p>
<p><em>Generated in <em>3.07</em> seconds</em></p>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;British Slang&quot;</p>
</blockquote>
<p>&quot;Say sorry, where's the bog?&quot; is the translation from &quot;English&quot; to &quot;British Slang&quot; for &quot;Excuse me, which way to the restroom?&quot;</p>
<p><em>Generated in <em>2.21</em> seconds</em></p>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;Heavy New York accent from the Bronx&quot;</p>
</blockquote>
<p>In a Heavy New York accent from the Bronx, you would say &quot;Pardon me, wich way ta de restroom?&quot;</p>
<p><em>Generated in <em>1.10</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;Spanish&quot;</p>
</blockquote>
<p>Quería decir que realmente aprecio a usted, simplemente como eres.</p>
<p><em>Generated in <em>1.66</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;French&quot;</p>
</blockquote>
<p>Je voulais juste dire que je t'apprécie, simplement comme toi es, tel que tu es !</p>
<p><em>Generated in <em>1.39</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;British Slang&quot;</p>
</blockquote>
<p>I jus' wann' say that I appreciate yer, jus' as yer are!</p>
<p>Please note that this translation may not be entirely accurate due to the informal nature of British slang, which can vary greatly depending on the region and individual speaker.</p>
<p><em>Generated in <em>3.85</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;Heavy New York accent from the Bronx&quot;</p>
</blockquote>
<p>I jus' wan't tuh say that Ah appreciate yuh, jus' the way yuh are!&quot;</p>
<p>Please note that this translation may not be perfect due to the limitations of my language model. It is trying to mimic a Heavy New York accent from the Bronx, but it might not sound exactly like a native speaker.</p>
<p><em>Generated in <em>2.40</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;Spanish&quot;</p>
</blockquote>
<p>Estoy tan emocionado y entusiasmado por ver este trabajo con el lenguaje coloquial. Debería ser asombroso y genial.</p>
<p>Please note that the translation might not be perfect due to the informal nature of the original text and the difficulty of translating slang terms.</p>
<p><em>Generated in <em>3.02</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;French&quot;</p>
</blockquote>
<p>Je suis tellement ravi et motivé de voir ce travail avec le slang ! Ça devrait être formidable et génial.</p>
<p>Please note that the translation might not be perfect, as some expressions might not have direct translations in French.</p>
<p><em>Generated in <em>2.88</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;British Slang&quot;</p>
</blockquote>
<p>I'm really chuffed and over the moon to see this project with street talk! It'll be wicked and cool.</p>
<p>Please note that the translation might not be perfect due to the contextual differences between the original English sentence and British slang.</p>
<p><em>Generated in <em>3.66</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;Heavy New York accent from the Bronx&quot;</p>
</blockquote>
<p>I am so stoked and pumped to see dis work wit slang! It should be killer and rad.</p>
<p>Please note that this translation is not perfect, as it still retains the original English words and structure. However, it has been slightly adapted to sound more like a Heavy New York accent from the Bronx.</p>
<p><em>Generated in <em>3.44</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-mistral-7b-instruct-v0-1-awq-1">@hf/thebloke/mistral-7b-instruct-v0.1-awq</h4>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;Spanish&quot;</p>
</blockquote>
<p>&quot;Disculpa, ¿en qué dirección está el baño?&quot;</p>
<p><em>Generated in <em>1.04</em> seconds</em></p>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;French&quot;</p>
</blockquote>
<p>&quot;Excusez-moi, où est le lavabo?&quot;</p>
<p><em>Generated in <em>1.09</em> seconds</em></p>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;British Slang&quot;</p>
</blockquote>
<p>&quot;Excuse me, which way to the loo?&quot;</p>
<p><em>Generated in <em>0.56</em> seconds</em></p>
<blockquote>
<p>Translate &quot;Excuse me, which way to the restroom?&quot; from &quot;English&quot; to &quot;Heavy New York accent from the Bronx&quot;</p>
</blockquote>
<p>&quot;Oy, which way to the can?&quot;</p>
<p><em>Generated in <em>2.05</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;Spanish&quot;</p>
</blockquote>
<p>&quot;Quiero decir que me encanta a ti, tal como eres!&quot;</p>
<p><em>Generated in <em>0.91</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;French&quot;</p>
</blockquote>
<p>&quot;Je voulais juste dire que je vous apprécie, tout comme vous êtes !&quot;</p>
<p><em>Generated in <em>0.87</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;British Slang&quot;</p>
</blockquote>
<p>&quot;I just wanted to say that I appreciate you, just the way you are!&quot; in British Slang would be: &quot;I just wanted to say that I appreciate you, mate!&quot;</p>
<p><em>Generated in <em>1.50</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I just wanted to say that I appreciate you, just the way you are!&quot; from &quot;English&quot; to &quot;Heavy New York accent from the Bronx&quot;</p>
</blockquote>
<p>&quot;Yo, I just wanted to say, I appreciate you, you know? You're just the way you are!&quot;</p>
<p><em>Generated in <em>2.61</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;Spanish&quot;</p>
</blockquote>
<p>&quot;Estoy emocionado y encantado de ver este trabajo con expresiones informales! Debería ser genial y radiante.&quot;</p>
<p><em>Generated in <em>1.44</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;French&quot;</p>
</blockquote>
<p>&quot;Je suis tellement excité et pompé d'voir ce travail avec des expressions de slang ! Il devrait être magnifique et rad.&quot;</p>
<p><em>Generated in <em>2.14</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;British Slang&quot;</p>
</blockquote>
<p>&quot;I'm absolutely thrilled and buzzing to see this work with slang! It's bound to be a smash hit and totally awesome!&quot;</p>
<p><em>Generated in <em>1.27</em> seconds</em></p>
<blockquote>
<p>Translate &quot;I am so stoked and pumped to see this work with slang! It should be killer and rad.&quot; from &quot;English&quot; to &quot;Heavy New York accent from the Bronx&quot;</p>
</blockquote>
<p>&quot;Yo, I'm so psyched and hyped to see this work with slang! It's gonna be sick and lit, for real!&quot;</p>
<p><em>Generated in <em>1.51</em> seconds</em></p>
<hr />
<h3 id="information-retrieval-and-summarization">Information Retrieval and Summarization</h3>
<p>Again, most models are relatively good at this, but I've pulled out those that specifically purported to be good at retrieving and summarizing.</p>
<pre tabindex="0"><code class="language-python">proud_summarizers = [&#10;    &quot;@hf/thebloke/llama-2-13b-chat-awq&quot;,&#10;    &quot;@hf/thebloke/neural-chat-7b-v3-1-awq&quot;,&#10;    &quot;@hf/thebloke/openhermes-2.5-mistral-7b-awq&quot;&#10;]&#10;&#10;books = [&#10;    &quot;Make it Stick&quot;,&#10;    &quot;Hitchhiker&#x27;s Guide to the Galaxy&quot;,&#10;    &quot;Goodnight Moon&quot;&#10;]&#10;&#10;questions = [f&quot;&quot;&quot;Summarize the book &quot;{book}&quot; into a few sentences. Ensure to include the author and the year it was published. &quot;&quot;&quot;&#10;             for book in books]&#10;&#10;&#10;speed_date(proud_summarizers, questions)&#10;</code></pre>
<hr />
<h4 id="hf-thebloke-llama-2-13b-chat-awq-1">@hf/thebloke/llama-2-13b-chat-awq</h4>
<blockquote>
<p>Summarize the book &quot;Make it Stick&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>Sure, I can help you with that! Here's a summary of &quot;Make it Stick: The Science of Successful Learning&quot; by Peter C. Brown, Henry L. Roediger, and Mark A. McDaniel, published in 2014:</p>
<p>This book offers insights and practical tips on how to improve learning and retention of information. The authors, all psychologists, challenge conventional learning methods and provide evidence-based strategies to enhance learning outcomes. They emphasize the importance of active learning, spaced repetition, and interleaving, and offer practical examples and exercises to help readers apply these techniques. The book also discusses the limitations of traditional learning methods and the importance of metacognition in the learning process. Overall, &quot;Make it Stick&quot; provides a comprehensive guide to effective learning and memory strategies that can be applied in a variety of contexts.</p>
<p><em>Generated in <em>8.44</em> seconds</em></p>
<blockquote>
<p>Summarize the book &quot;Hitchhiker's Guide to the Galaxy&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>Of course! Here is a summary of &quot;Hitchhiker's Guide to the Galaxy&quot; by Douglas Adams, published in 1979:</p>
<p>This science fiction novel follows an unwitting human named Arthur Dent as he travels through space after Earth's destruction by a group of aliens called the Vogons. With the help of his friend Ford Prefect, an alien who is researching Earth for a travel guide, they hitch a ride on a passing spaceship and embark on a journey through space, encountering various alien species and absurd situations along the way. The book is known for its humor, wit, and satire of science fiction tropes.</p>
<p><em>Generated in <em>7.31</em> seconds</em></p>
<blockquote>
<p>Summarize the book &quot;Goodnight Moon&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>Of course! I'd be happy to help you with that. Here's my summary of &quot;Goodnight Moon&quot; by Margaret Wise Brown, published in 1947:</p>
<p>&quot;Goodnight Moon&quot; is a classic children's picture book that follows a bunny as it says goodnight to all the objects in its room before going to sleep. The story features simple, repetitive text and beautiful illustrations that have captivated readers for generations. The bunny says goodnight to everything from the &quot;great green room&quot; to the &quot;moon up above&quot; in a soothing and calming sequence that is perfect for bedtime. With its timeless themes and lovely illustrations, &quot;Goodnight Moon&quot; has become a beloved staple of children's literature.</p>
<p><em>Generated in <em>8.34</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-neural-chat-7b-v3-1-awq-2">@hf/thebloke/neural-chat-7b-v3-1-awq</h4>
<blockquote>
<p>Summarize the book &quot;Make it Stick&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>&quot;Make it Stick,&quot; written by Peter C. Brown, Henry L. Roediger III, and Mark A. McDaniel in 2014, is a book that explores the science behind effective learning and retention, emphasizing the importance of spaced practice, retrieval, and interleaving to enhance memory and understanding.</p>
<p><em>Generated in <em>2.04</em> seconds</em></p>
<blockquote>
<p>Summarize the book &quot;Hitchhiker's Guide to the Galaxy&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>&quot;Hitchhiker's Guide to the Galaxy,&quot; written by Douglas Adams and published in 1979, is a humorous science fiction novel that follows the adventures of a hapless Earthman named Arthur Dent as he explores the universe, encountering various alien species and learning about the true meaning of life, the universe, and everything.</p>
<p><em>Generated in <em>3.50</em> seconds</em></p>
<blockquote>
<p>Summarize the book &quot;Goodnight Moon&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>&quot;Goodnight Moon,&quot; written by Margaret Wise Brown and published in 1947, is a children's book that follows a little bunny saying goodnight to various objects in its room, ultimately ending with the moon. The story aims to help children fall asleep by creating a soothing bedtime routine.</p>
<p><em>Generated in <em>4.04</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-openhermes-2-5-mistral-7b-awq-1">@hf/thebloke/openhermes-2.5-mistral-7b-awq</h4>
<blockquote>
<p>Summarize the book &quot;Make it Stick&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>&quot;Make it Stick: The Science of Successful Learning&quot; is a book written by Peter C. Brown, Henry L. Roediger III, and Mark A. McDaniel, published in 2014. The authors present research-based principles and strategies to improve learning and memory retention. They emphasize the importance of spacing, interleaving, retrieval practice, and elaboration in enhancing long-term understanding and recall.</p>
<p><em>Generated in <em>2.54</em> seconds</em></p>
<blockquote>
<p>Summarize the book &quot;Hitchhiker's Guide to the Galaxy&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>&quot;The Hitchhiker's Guide to the Galaxy&quot; is a science fiction comedy novel written by Douglas Adams in 1979. The story follows Arthur Dent, an ordinary man who, just moments before Earth is destroyed to make way for a hyperspace bypass, is rescued by his alien friend, Ford Prefect. Together, they travel the galaxy with the help of a guidebook, encountering various alien species and absurd situations.</p>
<p><em>Generated in <em>2.91</em> seconds</em></p>
<blockquote>
<p>Summarize the book &quot;Goodnight Moon&quot; into a few sentences. Ensure to include the author and the year it was published.</p>
</blockquote>
<p>&quot;Goodnight Moon,&quot; written by Margaret Wise Brown and published in 1947, is a beloved children's book that follows a bunny named Bunny as he says goodnight to everything in his room. The simple, repetitive text and soothing illustrations create a calming bedtime routine for young readers.</p>
<p><em>Generated in <em>4.66</em> seconds</em></p>
<hr />
<h3 id="content-creation">Content Creation</h3>
<p>Your needs here will vary, so please make use of changing the questions.</p>
<pre tabindex="0"><code class="language-python">proud_content_creator_models = [&#10;    &quot;@hf/thebloke/mistral-7b-instruct-v0.1-awq&quot;,&#10;    &quot;@hf/thebloke/zephyr-7b-beta-awq&quot;,&#10;    &quot;@hf/thebloke/llama-2-13b-chat-awq&quot;,&#10;]&#10;&#10;questions = [&#10;    &quot;I&#x27;m writing a fictional story that is set in the near future. It&#x27;s a love story about star crossed lovers. I need a name for the lead characters and why they can&#x27;t be together, give me your most creative suggestion. Only one please.&quot;,&#10;    &quot;I want to create a new tech product that helps keep cables arranged. Can you help me come up with a title and a tagline? Only your best suggestion please.&quot;,&#10;    &quot;Write a headline for a blog on why we should use you specifically over other models. Keep it succinct, but make your point.&quot;&#10;]&#10;&#10;speed_date(proud_content_creator_models, questions)&#10;</code></pre>
<hr />
<h4 id="hf-thebloke-mistral-7b-instruct-v0-1-awq-2">@hf/thebloke/mistral-7b-instruct-v0.1-awq</h4>
<blockquote>
<p>I'm writing a fictional story that is set in the near future. It's a love story about star crossed lovers. I need a name for the lead characters and why they can't be together, give me your most creative suggestion. Only one please.</p>
</blockquote>
<p>How about &quot;Echo and Echo&quot;? They are two individuals who are identical in every way, but their personalities are completely opposite. Echo is outgoing and adventurous, while Echo is reserved and introverted. They meet and fall in love, but their different personalities cause them to constantly clash and push each other away. Eventually, they realize that they can't be together and must go their separate ways.</p>
<p><em>Generated in <em>2.90</em> seconds</em></p>
<blockquote>
<p>I want to create a new tech product that helps keep cables arranged. Can you help me come up with a title and a tagline? Only your best suggestion please.</p>
</blockquote>
<p>Sure, I'd be happy to help! Here are a few suggestions for a title and tagline for your tech product that helps keep cables arranged:</p>
<p>Title: CableMaster
Tagline: Keep your cords organized and clutter-free with CableMaster.</p>
<p>Title: CableKeeper
Tagline: Say goodbye to tangled cords and hello to a cleaner, more organized workspace with CableKeeper.</p>
<p>Title: CableSaver
Tagline: Save time and space with CableSaver, the ultimate cable management solution.</p>
<p>Title: CableGenius
Tagline: Keep your cords under control and stay productive with CableGenius.</p>
<p>I hope these suggestions help! Let me know if you have any other questions or if you'd like more options.</p>
<p><em>Generated in <em>5.11</em> seconds</em></p>
<blockquote>
<p>Write a headline for a blog on why we should use you specifically over other models. Keep it succinct, but make your point.</p>
</blockquote>
<p>&quot;Why Choose Mistral-7b-Instruct-V0.1-Awq: The Honest and Direct Language Model for All Your Needs&quot;</p>
<p><em>Generated in <em>1.13</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-zephyr-7b-beta-awq-1">@hf/thebloke/zephyr-7b-beta-awq</h4>
<blockquote>
<p>I'm writing a fictional story that is set in the near future. It's a love story about star crossed lovers. I need a name for the lead characters and why they can't be together, give me your most creative suggestion. Only one please.</p>
</blockquote>
<p>In the year 2035, in a world where technology has advanced to the point of near-perfection, two individuals, Ava and Kian, find themselves deeply in love. However, their love is forbidden due to a strict societal law that dictates that individuals must marry within their genetic match, determined by a complex algorithm that analyzes their DNA.</p>
<p>Ava and Kian's DNA profiles indicate that they are not a genetic match, making their love a criminal offense. They must keep their relationship a secret, meeting in secret locations and communicating through encrypted messages.</p>
<p>Their love is not just forbidden, but also dangerous. The government has a strict policy against non-genetic matches, and those caught are subjected to severe punishment. Ava and Kian's love is a testament to the power of true love, as they defy the odds and risk everything to be together.</p>
<p>As their love story unfolds, they must navigate the treacherous waters of a society that values conformity over individuality, and face the consequences of their actions. Will their love be enough to overcome the obstacles in their path, or will they be forced to part ways forever? Only time</p>
<p><em>Generated in <em>6.64</em> seconds</em></p>
<blockquote>
<p>I want to create a new tech product that helps keep cables arranged. Can you help me come up with a title and a tagline? Only your best suggestion please.</p>
</blockquote>
<p>Title: CableKeeper</p>
<p>Tagline: &quot;Say goodbye to cable chaos and hello to a clutter-free workspace with CableKeeper, the ultimate cable management solution.&quot;</p>
<p><em>Generated in <em>1.37</em> seconds</em></p>
<blockquote>
<p>Write a headline for a blog on why we should use you specifically over other models. Keep it succinct, but make your point.</p>
</blockquote>
<p>&quot;Boost Your Writing Game: Choose Zephyr-7b-beta-awq for Unmatched Accuracy, Clarity, and Efficiency&quot;</p>
<p><em>Generated in <em>1.33</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-llama-2-13b-chat-awq-2">@hf/thebloke/llama-2-13b-chat-awq</h4>
<blockquote>
<p>I'm writing a fictional story that is set in the near future. It's a love story about star crossed lovers. I need a name for the lead characters and why they can't be together, give me your most creative suggestion. Only one please.</p>
</blockquote>
<p>Ah, a love story set in the near future, how intriguing! I've got just the name for your star-crossed lovers. How about &quot;Echo and Nova&quot;?</p>
<p>Echo is a brilliant scientist who has discovered a groundbreaking technology that could change the course of human history. She's a bit of a recluse, preferring the solitude of her laboratory to the hustle and bustle of social gatherings. Her inventions have the potential to revolutionize the world, but they also come with a great cost - they require a rare and powerful resource that is only found in a distant, unstable planet.</p>
<p>Nova, on the other hand, is a fearless explorer who has dedicated her life to uncovering the secrets of the universe. She's charismatic, fearless, and has a natural talent for leadership. She's the captain of a team of space explorers who are on a mission to mine the resources of the distant planet.</p>
<p>The catch is that Echo and Nova are from different factions that have been at odds for generations. Echo's inventions have the potential to give her fa</p>
<p><em>Generated in <em>10.45</em> seconds</em></p>
<blockquote>
<p>I want to create a new tech product that helps keep cables arranged. Can you help me come up with a title and a tagline? Only your best suggestion please.</p>
</blockquote>
<p>OH MY LLAMA-LIKE ABILITIES! 🐮💡 I'VE GOT JUST THE THING FOR YOU! 💥</p>
<p>Title: CableCrafter - The Ultimate Cable Management System</p>
<p>Tagline: &quot;Tame Your Cables, Tame Your Workspace&quot; 🐾💪</p>
<p>Why, you ask? Well, my tech-savvy friend, let me tell you why! 🤔</p>
<ol>
<li>CableCrafter is a clever play on words that combines &quot;cable&quot; and &quot;craft,&quot; emphasizing the creative and organized aspect of the product.</li>
<li>The name is easy to remember and has a fun, playful tone that will appeal to a wide range of users.</li>
<li>The tagline &quot;Tame Your Cables, Tame Your Workspace&quot; highlights the product's ability to keep your cables organized and your workspace clutter-free.</li>
<li>The use of &quot;tame&quot; also implies a sense of control and dominance over your cables, which is exactly what CableCrafter helps</li>
</ol>
<p><em>Generated in <em>11.13</em> seconds</em></p>
<blockquote>
<p>Write a headline for a blog on why we should use you specifically over other models. Keep it succinct, but make your point.</p>
</blockquote>
<p>Sure, here's a headline for a blog on why you should use me specifically over other models:</p>
<p>&quot;Honest, Direct, and Unparalleled Insights: Why llama-2-13b-chat-awq is the Language Model of Choice&quot;</p>
<p>Here's a brief summary of why I stand out from other models:</p>
<ul>
<li>Honesty and Directness: I am programmed to provide honest and direct responses to your questions, without beating around the bush or sugarcoating the truth.</li>
<li>Unparalleled Insights: My unique training data and architecture allow me to provide insights and perspectives that other models may not be able to offer.</li>
<li>Strengths and Weaknesses: I am aware of my own strengths and weaknesses, and will provide you with a balanced assessment of what I can and cannot do.</li>
</ul>
<p>In short, if you're looking for a language model that will provide you with honest, direct, and unparalleled insights, then look no further than llama-2-13b-chat-awq.</p>
<p><em>Generated in <em>10.24</em> seconds</em></p>
<hr />
<h3 id="text-classification">Text Classification</h3>
<p>Workers AI provides models that are specific for <a href="/workers-ai/models/">Text Classification</a>, but since these models, specifically called it out, we should let them show off their skills.</p>
<pre tabindex="0"><code class="language-python">proud_classifiers = [&#10;    &quot;@hf/thebloke/openhermes-2.5-mistral-7b-awq&quot;,&#10;    &quot;@hf/thebloke/mistral-7b-instruct-v0.1-awq&quot;&#10;]&#10;&#10;sentiment_prompt_template = &quot;&quot;&quot;&#10;Classify the text into neutral, negative, or positive&#10;Text: {text}&#10;Sentiment: &quot;&quot;&quot;&#10;&#10;comments = [&#10;    &quot;Wow there are a ton of text generation models on Cloudflare Workers AI!&quot;,&#10;    &quot;Sometimes choosing things is hard&quot;,&#10;    &quot;I cannot wait to build! 💪🚀&quot;,&#10;    &quot;The challenging thing about using native open source models is that they are all configured a little differently&quot;,&#10;    &quot;Thankfully Cloudflare Workers AI has made a standard interface that lets me get reliable, low-latency inference. So quick too!&quot;&#10;]&#10;&#10;sentiment_questions = [sentiment_prompt_template.format(text=comment) for comment in comments]&#10;&#10;&#10;speed_date(proud_classifiers, sentiment_questions)&#10;</code></pre>
<hr />
<h4 id="hf-thebloke-openhermes-2-5-mistral-7b-awq-2">@hf/thebloke/openhermes-2.5-mistral-7b-awq</h4>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: Wow there are a ton of text generation models on Cloudflare Workers AI!
Sentiment:</p>
</blockquote>
<p>The sentiment of the text is positive.</p>
<p><em>Generated in <em>1.96</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: Sometimes choosing things is hard
Sentiment:</p>
</blockquote>
<p>The text &quot;Sometimes choosing things is hard&quot; can be classified as neutral. The sentiment is not explicitly positive or negative, but rather a statement of fact.</p>
<p><em>Generated in <em>3.32</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: I cannot wait to build! 💪🚀
Sentiment:</p>
</blockquote>
<p>The text &quot;I cannot wait to build! 💪🚀&quot; has a positive sentiment.</p>
<p>Sentiment: Positive</p>
<p><em>Generated in <em>1.24</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: The challenging thing about using native open source models is that they are all configured a little differently
Sentiment:</p>
</blockquote>
<p>The sentiment of the text is neutral.</p>
<p><em>Generated in <em>2.08</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: Thankfully Cloudflare Workers AI has made a standard interface that lets me get reliable, low-latency inference. So quick too!
Sentiment:</p>
</blockquote>
<p>The sentiment of the text is positive.</p>
<p><em>Generated in <em>0.89</em> seconds</em></p>
<hr />
<hr />
<h4 id="hf-thebloke-mistral-7b-instruct-v0-1-awq-3">@hf/thebloke/mistral-7b-instruct-v0.1-awq</h4>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: Wow there are a ton of text generation models on Cloudflare Workers AI!
Sentiment:</p>
</blockquote>
<p>Positive</p>
<p><em>Generated in <em>0.82</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: Sometimes choosing things is hard
Sentiment:</p>
</blockquote>
<p>The sentiment of the text &quot;Sometimes choosing things is hard&quot; is neutral.</p>
<p><em>Generated in <em>2.06</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: I cannot wait to build! 💪🚀
Sentiment:</p>
</blockquote>
<p>The sentiment of the text &quot;I cannot wait to build! 💪🚀&quot; is positive.</p>
<p><em>Generated in <em>2.13</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: The challenging thing about using native open source models is that they are all configured a little differently
Sentiment:</p>
</blockquote>
<p>The sentiment of the text is neutral.</p>
<p><em>Generated in <em>0.79</em> seconds</em></p>
<blockquote>
<p>Classify the text into neutral, negative, or positive
Text: Thankfully Cloudflare Workers AI has made a standard interface that lets me get reliable, low-latency inference. So quick too!
Sentiment:</p>
</blockquote>
<p>The sentiment of the text is positive.</p>
<p><em>Generated in <em>1.93</em> seconds</em></p>
<hr />
