<p><a href="https://github.com/cloudflare/workers-py?tab=readme-ov-file#pywrangler">Pywrangler</a> is a CLI tool for managing packages and Python Workers.
It is meant as a wrapper for wrangler that sets up a full environment for you, including bundling your packages into
your worker bundle on deployment.</p>
<p>To get started, create a pyproject.toml file with the following contents:</p>
<pre><code class="language-toml">[project]&#10;name = &quot;YourProjectName&quot;&#10;version = &quot;0.1.0&quot;&#10;description = &quot;Add your description here&quot;&#10;requires-python = &quot;&gt;=3.13&quot;&#10;dependencies = [&#10;    &quot;fastapi&quot;&#10;]&#10;&#10;[dependency-groups]&#10;dev = [&#10;	&quot;workers-py&quot;,&#10;	&quot;workers-runtime-sdk&quot;&#10;]&#10;</code></pre>
<p>The above will allow your worker to depend on the <a href="https://fastapi.tiangolo.com/">FastAPI</a> package.</p>
<p>To run the worker locally:</p>
<pre><code>uv run pywrangler dev&#10;</code></pre>
<p>To deploy your worker:</p>
<pre><code>uv run pywrangler deploy&#10;</code></pre>
<p>Your dependencies will get bundled with your worker automatically on deployment.</p>
<p>The <code>pywrangler</code> CLI also supports all commands supported by the <code>wrangler</code> tool, for the full list of commands run <code>uv run pywrangler --help</code>.</p>
<h2 id="supported-libraries">Supported Libraries</h2>
<p>Python Workers support pure and <a href="https://peps.python.org/pep-0783/">PyEmscripten</a> Python packages on <a href="https://pypi.org/">PyPI</a>.
Additionally, Python Workers support packages that are included in <a href="https://pyodide.org/en/stable/usage/packages-in-pyodide.html">Pyodide</a>.</p>
<p>WebAssembly support for Python packages is still in early stages, and some packages may not yet be available as PyEmscripten wheels on PyPI.
If a package you would like to use is not yet available, we encourage you to reach out to the package maintainers and request PyEmscripten wheels.
You can also start a thread in the <a href="https://github.com/cloudflare/workerd/discussions/categories/python-packages">Python Packages Discussions</a>
on the Cloudflare Workers Runtime GitHub repository — we would be happy to help you communicate with package maintainers.</p>
