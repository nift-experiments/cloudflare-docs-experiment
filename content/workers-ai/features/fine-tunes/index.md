<p>Learn how to use Workers AI to get fine-tuned inference.</p>
<div class="nb-feature">
@markup("md", "content/.markup/bodies/15826.md")
</div>
<hr />
<h2 id="what-is-fine-tuning">What is fine-tuning?</h2>
<p>Fine-tuning is a general term for modifying an AI model by continuing to train it with additional data. The goal of fine-tuning is to increase the probability that a generation is similar to your dataset. Training a model from scratch is not practical for many use cases given how expensive and time consuming they can be to train. By fine-tuning an existing pre-trained model, you benefit from its capabilities while also accomplishing your desired task.</p>
<p><a href="https://arxiv.org/abs/2106.09685">Low-Rank Adaptation</a> (LoRA) is a specific fine-tuning method that can be applied to various model architectures, not just LLMs. It is common that the pre-trained model weights are directly modified or fused with additional fine-tune weights in traditional fine-tuning methods. LoRA, on the other hand, allows for the fine-tune weights and pre-trained model to remain separate, and for the pre-trained model to remain unchanged. The end result is that you can train models to be more accurate at specific tasks, such as generating code, having a specific personality, or generating images in a specific style.</p>
