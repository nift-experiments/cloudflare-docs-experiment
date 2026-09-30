<p>Workers written in Python are executed by <a href="https://pyodide.org/en/stable/index.html">Pyodide</a>.</p>
<p>Pyodide is a port of CPython to WebAssembly — for the most part it behaves identically to <a href="https://github.com/python">CPython</a> (the reference implementation of Python — commonly referred to as just &quot;Python&quot;).
The majority of the CPython test suite passes when run against Pyodide. For the most part, you shouldn't need to worry about differences in behavior.</p>
<p>The full <a href="https://docs.python.org/3/library/index.html">Python Standard Library</a> is available in Python Workers, with the following exceptions:</p>
<h2 id="excluded-modules">Excluded modules</h2>
<p>The following modules are not available in Python Workers:</p>
<ul>
<li>curses</li>
<li>dbm</li>
<li>ensurepip</li>
<li>fcntl</li>
<li>grp</li>
<li>idlelib</li>
<li>lib2to3</li>
<li>msvcrt</li>
<li>pwd</li>
<li>resource</li>
<li>syslog</li>
<li>termios</li>
<li>tkinter</li>
<li>turtle.py</li>
<li>turtledemo</li>
<li>venv</li>
<li>winreg</li>
<li>winsound</li>
</ul>
<p>The following modules can be imported, but are not functional due to the limitations of the WebAssembly VM.</p>
<ul>
<li>multiprocessing</li>
<li>threading</li>
</ul>
<p>The following are present but cannot be imported due to a dependency on the termios package which has been removed:</p>
<ul>
<li>pty</li>
<li>tty</li>
</ul>
<h2 id="modules-with-limited-functionality">Modules with limited functionality</h2>
<ul>
<li><code>decimal</code>: The decimal module has C (_decimal) and Python (_pydecimal) implementations
with the same functionality. Only the C implementation is available (compiled to WebAssembly)</li>
<li><code>pydoc</code>: Help messages for Python builtins are not available</li>
<li><code>webbrowser</code>: The original webbrowser module is not available.</li>
</ul>
<h2 id="in-memory-filesystem">In-memory filesystem</h2>
<p>Python Workers have access to an ephemeral, in-memory filesystem. You can read and write files using standard Python file I/O (for example, <code>open()</code>, <code>pathlib.Path</code>), but all data is <strong>lost when the Worker isolate is destroyed</strong>. The filesystem is not shared between different isolate instances.</p>
<p>This can be useful for temporary file operations, but should not be relied upon for persistent storage. Use <a href="/kv/">KV</a>, <a href="/r2/">R2</a>, or <a href="/durable-objects/">Durable Objects</a> for durable storage.</p>
