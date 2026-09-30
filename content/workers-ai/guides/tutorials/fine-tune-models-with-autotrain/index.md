<p>Fine tuning an AI model gives you the opportunity to add additional training data to the model. Workers AI allows for <a href="/workers-ai/features/fine-tunes/loras/">Low-Rank Adaptation, LoRA, adapters</a> that will allow you to finetune our models.</p>
<p>In this tutorial, we will explore how to create our own LoRAs. We will focus on <a href="https://huggingface.co/docs/autotrain/llm_finetuning">LLM Finetuning using AutoTrain</a>.</p>
<h2 id="1-create-a-csv-file-with-your-training-data"><ol>
<li>Create a CSV file with your training data</li>
</ol></h2>
<p>Start by creating a CSV, Comma Separated Values, file. This file will only have one column named <code>text</code>. Set the header by adding the word <code>text</code> on a line by itself.</p>
<p>Now you need to figure out what you want to add to your model.</p>
<p>Example formats are below:</p>
<pre><code class="language-text">&#35;## Human: What is the meaning of life? ### Assistant: 42.&#10;</code></pre>
<p>If your training row contains newlines, you should wrap it with quotes.</p>
<pre><code class="language-text">&quot;human: What is the meaning of life? \n bot: 42.&quot;&#10;</code></pre>
<p>Different models, like Mistral, will provide a specific <a href="https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1#instruction-format">chat template/instruction format</a></p>
<pre><code class="language-text">&lt;s&gt;[INST] What is the meaning of life? [/INST] 42&lt;/s&gt;&#10;</code></pre>
<h2 id="2-configure-the-huggingface-autotrain-advanced-notebook"><ol start="2">
<li>Configure the HuggingFace Autotrain Advanced Notebook</li>
</ol></h2>
<p>Open the <a href="https://colab.research.google.com/github/huggingface/autotrain-advanced/blob/main/colabs/AutoTrain_LLM.ipynb">HuggingFace Autotrain Advanced Notebook</a></p>
<p>In order to give your AutoTrain ample memory, you will need to need to choose a different Runtime. From the menu at the top of the Notebook choose Runtime &gt; Change Runtime Type. Choose A100.</p>
<aside class="nb-aside note">
@markup("md", "content/.markup/bodies/15845.md")
</aside>
<p>The notebook contains a few interactive sections that we will need to change.</p>
<h3 id="project-config">Project Config</h3>
<p>Modify the following fields</p>
<ul>
<li><strong>project_name</strong>: Choose a descriptive name for you to remember later</li>
<li><strong>model_name</strong>: Choose from the one of the official HuggingFace base models that we support:
<ul>
<li><code>mistralai/Mistral-7B-Instruct-v0.2</code></li>
<li><code>google/gemma-2b-it</code></li>
<li><code>google/gemma-7b-it</code></li>
<li><code>meta-llama/llama-2-7b-chat-hf</code></li>
</ul>
</li>
</ul>
<h3 id="optional-section-push-to-hub">Optional Section: Push to Hub</h3>
<p>Although not required to use AutoTrain, creating a <a href="https://huggingface.co/join">HuggingFace account</a> will help you keep your finetune artifacts in a handy repository for you to refer to later.</p>
<p>If you do not perform the HuggingFace setup you can still download your files from the Notebook.</p>
<p>Follow the instructions <a href="https://colab.research.google.com/github/huggingface/autotrain-advanced/blob/main/colabs/AutoTrain_LLM.ipynb">in the notebook</a> to create an account and token if necessary.</p>
<h3 id="section-hyperparameters">Section: Hyperparameters</h3>
<p>We only need to change a few of these fields to ensure things work on Cloudflare Workers AI.</p>
<ul>
<li><strong>quantization</strong>: Change the drop down to <code>none</code></li>
<li><strong>lora-r</strong>: Change the value to <code>8</code></li>
</ul>
<aside class="nb-aside caution">
@markup("md", "content/.markup/bodies/15844.md")
</aside>
<h2 id="3-upload-your-csv-file-to-the-notebook"><ol start="3">
<li>Upload your CSV file to the Notebook</li>
</ol></h2>
<p>Notebooks have a folder structure which you can access by clicking the folder icon on the left hand navigation bar.</p>
<p>Create a folder named data.</p>
<p>You can drag your CSV file into the notebook.</p>
<p>Ensure that it is named <strong>train.csv</strong></p>
<h2 id="4-execute-the-notebook"><ol start="4">
<li>Execute the Notebook</li>
</ol></h2>
<p>In the Notebook menu, choose Runtime &gt; Run All.</p>
<p>It will run through each cell of the notebook, first doing installations, then configuring and running your AutoTrain session.</p>
<p>This might take some time depending on the size of your train.csv file.</p>
<p>If you encounter the following error, it is caused by an Out of Memory error. You might want to change your runtime to a bigger GPU backend.</p>
<pre><code class="language-bash">subprocess.CalledProcessError: Command &#x27;[&#x27;/usr/bin/python3&#x27;, &#x27;-m&#x27;, &#x27;autotrain.trainers.clm&#x27;, &#x27;--training_config&#x27;, &#x27;blog-instruct/training_params.json&#x27;]&#x27; died with &lt;Signals.SIGKILL: 9&gt;.&#10;</code></pre>
<h2 id="5-download-the-lora"><ol start="5">
<li>Download The LoRA</li>
</ol></h2>
<h3 id="optional-huggingface">Optional: HuggingFace</h3>
<p>If you pushed to HuggingFace you will find your new model card that you named in <strong>project_name</strong> above. Your model card is private by default. Navigate to the files and download the files listed below.</p>
<h3 id="notebook">Notebook</h3>
<p>In your Notebook you can also find the needed files. A new folder that matches your <strong>project_name</strong> will be there.</p>
<p>Download the following files:</p>
<ul>
<li><code>adapter_model.safetensors</code></li>
<li><code>adapter_config.json</code></li>
</ul>
<h2 id="6-update-adapter-config"><ol start="6">
<li>Update Adapter Config</li>
</ol></h2>
<p>You need to add one line to your <code>adapter_config.json</code> that you downloaded.</p>
<p><code>&quot;model_type&quot;: &quot;mistral&quot;</code></p>
<p>Where <code>model_type</code> is the architecture. Current valid values are <code>mistral</code>, <code>gemma</code>, and <code>llama</code>.</p>
<h2 id="7-upload-the-fine-tune-to-your-cloudflare-account"><ol start="7">
<li>Upload the Fine Tune to your Cloudflare Account</li>
</ol></h2>
<p>Now that you have your files, you can add them to your account.</p>
<p>You can either use the <a href="/workers-ai/features/fine-tunes/loras/">REST API or Wrangler</a>.</p>
<h2 id="8-use-your-fine-tune-in-your-generations"><ol start="8">
<li>Use your Fine Tune in your Generations</li>
</ol></h2>
<p>After you have your new fine tune all set up, you are ready to <a href="/workers-ai/features/fine-tunes/loras/#running-inference-with-loras">put it to use in your inference requests</a>.</p>
