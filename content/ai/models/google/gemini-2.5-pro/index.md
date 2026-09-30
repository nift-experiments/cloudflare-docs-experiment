<img src="/assets/upstream/images/workers-ai/google.svg" alt="Google logo" width="48" height="48">

<h1 id="gemini-2-5-pro">Gemini 2.5 Pro</h1>

<p><code>google/gemini-2.5-pro</code></p>

Google's most capable Gemini 2.5 model with strong reasoning, thinking support, and a 1M token context window.

<div class="table-scroll"><table><tbody>
<tr><th>Task</th><td>Text Generation</td></tr>
<tr><th>Context window</th><td>1,000,000 tokens</td></tr>
<tr><th>Terms</th><td><a href="https://ai.google.dev/gemini-api/terms">Model terms</a></td></tr>
<tr><th>Unit pricing</th><td>Input tokens (per 1M): 1.25, Output tokens (per 1M): 10, Cached input tokens (per 1M): 0.125</td></tr>
</tbody></table></div>

<h2 id="usage">Usage</h2>

Basic generateContent request

<section class="model-example"><strong>Simple Question</strong>
<p>Basic generateContent request</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Of course! The three laws of thermodynamics are fundamental principles in physics that describe the relationships between heat, energy, and work.\n\nHere they are, explained from a simple \&quot;catchphrase\&quot; summary to a more detailed breakdown.\n\n***\n\n### A Quick Summary (The \&quot;Gambling\&quot; Analogy)\n\nA popular, easy way to remember the laws is to think of them in terms of a game:\n\n1.  **First Law:** You can&#x27;t win. (You can&#x27;t get more energy out than you put in.)\n2.  **Second Law:** You can&#x27;t break even. (You can&#x27;t even get back the energy you put in, in a perfectly useful form.)\n3.  **Third Law:** You can&#x27;t quit the game. (You can&#x27;t reach absolute zero and stop all energy.)\n\n***\n\n### The Detailed Explanation\n\nBefore the three main laws, it&#x27;s helpful to understand the **Zeroth Law**, which was formulated after the others but is more fundamental.\n\n#### The Zeroth Law of Thermodynamics: Defines Temperature\n*   **Simple Statement:** Objects in thermal equilibrium are at the same temperature.\n*   **Explanation:** If two systems are each in thermal equilibrium with a third system, then they are also in thermal equilibrium with each other. This law sounds obvious, but it&#x27;s what makes thermometers work. When you put a thermometer in a cup of coffee, the thermometer and coffee reach thermal equilibrium. If you then use that thermometer on another cup and it gives the same reading, you know both cups are the same temperature without them ever having touched.\n\n---\n\n### 1. The First Law of Thermodynamics: Conservation of Energy\n\n*   **Simple Statement:** Energy cannot be created or destroyed, only converted from one form to another.\n*   **Explanation:** This is the thermodynamic version of the law of conservation of energy. It means that the total energy in a closed system is constant. If you add energy to a system (e.g., by heating it), that energy doesn&#x27;t disappear. It either increases the system&#x27;s internal energy (making it hotter) or is used by the system to do work on its surroundings (like a piston moving). You can&#x27;t get free energy out of nothing.\n*   **Everyday Example:** When you eat food, the chemical energy stored in the food is converted by your body into thermal energy (to keep you warm) and kinetic energy (to move your muscles). The energy isn&#x27;t created; it&#x27;s just transformed.\n\n---\n\n### 2. The Second Law of Thermodynamics: The Increase of Entropy\n\n*   **Simple Statement:** The total entropy (disorder) of the universe always increases over time.\n*   **Explanation:** This is arguably the most profound of the laws. It states that natural processes tend to move towards a state of greater disorder or randomness (entropy). Heat will always spontaneously flow from a hotter object to a colder object, never the other way around. This flow increases the overall entropy because the energy becomes more spread out and less \&quot;organized.\&quot; Because of this law, no energy transfer is 100% efficient; some energy is always lost as waste heat, increasing the overall disorder of the universe.\n*   **Everyday Example:** A hot cup of coffee will always cool down to room temperature. The concentrated heat (an ordered state) will spread out into the cooler, larger room (a more disordered state). You will never see a room-temperature cup of coffee spontaneously become hot by drawing heat from the air. Similarly, an ice cube melts in a warm room, moving from an ordered crystal structure to a disordered liquid.\n\n---\n\n### 3. The Third Law of Thermodynamics: Absolute Zero is Unreachable\n\n*   **Simple Statement:** The entropy of a system approaches a minimum value as the temperature approaches absolute zero. It is impossible to reach absolute zero in a finite number of steps.\n*   **Explanation:** Absolute zero (0 Kelvin or -273.15\u00b0C / -459.67\u00b0F) is the theoretical temperature at which all particle motion would completely stop. The Third Law states that as you get colder and closer to this temperature, the entropy of a perfect crystal becomes zero. However, the law also implies that it&#x27;s physically impossible to ever reach absolute zero. Each step you take to cool a system gets you closer, but the effort required to remove the next bit of heat increases exponentially. You can get incredibly close, but you can never take that final step to get there.\n*   **Everyday Example:** This law is less intuitive in daily life as it deals with extreme cold. But you can think of it like trying to create a perfect vacuum by pumping all the air out of a container. With each pump, you remove a fraction of the remaining air, so you get closer and closer to a perfect vacuum but never fully achieve it because there will always be *some* molecules left. Reaching absolute zero is a similar process of diminishing returns.\n\n| Law | Simple Statement | Key Concept |\n| :--- | :--- | :--- |\n| **Zeroth** | Defines temperature. | Thermal Equilibrium |\n| **First** | Energy is conserved. | Conservation of Energy |\n| **Second**| Disorder (entropy) increases. | Entropy &amp; The Arrow of Time |\n| **Third** | Absolute zero is unreachable. | Absolute Zero &amp; Minimum Entropy |&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.3830967711048414,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Of course! The three laws of thermodynamics are fundamental principles in physics that describe the relationships between heat, energy, and work.\n\nHere they are, explained from a simple \&quot;catchphrase\&quot; summary to a more detailed breakdown.\n\n***\n\n### A Quick Summary (The \&quot;Gambling\&quot; Analogy)\n\nA popular, easy way to remember the laws is to think of them in terms of a game:\n\n1.  **First Law:** You can&#x27;t win. (You can&#x27;t get more energy out than you put in.)\n2.  **Second Law:** You can&#x27;t break even. (You can&#x27;t even get back the energy you put in, in a perfectly useful form.)\n3.  **Third Law:** You can&#x27;t quit the game. (You can&#x27;t reach absolute zero and stop all energy.)\n\n***\n\n### The Detailed Explanation\n\nBefore the three main laws, it&#x27;s helpful to understand the **Zeroth Law**, which was formulated after the others but is more fundamental.\n\n#### The Zeroth Law of Thermodynamics: Defines Temperature\n*   **Simple Statement:** Objects in thermal equilibrium are at the same temperature.\n*   **Explanation:** If two systems are each in thermal equilibrium with a third system, then they are also in thermal equilibrium with each other. This law sounds obvious, but it&#x27;s what makes thermometers work. When you put a thermometer in a cup of coffee, the thermometer and coffee reach thermal equilibrium. If you then use that thermometer on another cup and it gives the same reading, you know both cups are the same temperature without them ever having touched.\n\n---\n\n### 1. The First Law of Thermodynamics: Conservation of Energy\n\n*   **Simple Statement:** Energy cannot be created or destroyed, only converted from one form to another.\n*   **Explanation:** This is the thermodynamic version of the law of conservation of energy. It means that the total energy in a closed system is constant. If you add energy to a system (e.g., by heating it), that energy doesn&#x27;t disappear. It either increases the system&#x27;s internal energy (making it hotter) or is used by the system to do work on its surroundings (like a piston moving). You can&#x27;t get free energy out of nothing.\n*   **Everyday Example:** When you eat food, the chemical energy stored in the food is converted by your body into thermal energy (to keep you warm) and kinetic energy (to move your muscles). The energy isn&#x27;t created; it&#x27;s just transformed.\n\n---\n\n### 2. The Second Law of Thermodynamics: The Increase of Entropy\n\n*   **Simple Statement:** The total entropy (disorder) of the universe always increases over time.\n*   **Explanation:** This is arguably the most profound of the laws. It states that natural processes tend to move towards a state of greater disorder or randomness (entropy). Heat will always spontaneously flow from a hotter object to a colder object, never the other way around. This flow increases the overall entropy because the energy becomes more spread out and less \&quot;organized.\&quot; Because of this law, no energy transfer is 100% efficient; some energy is always lost as waste heat, increasing the overall disorder of the universe.\n*   **Everyday Example:** A hot cup of coffee will always cool down to room temperature. The concentrated heat (an ordered state) will spread out into the cooler, larger room (a more disordered state). You will never see a room-temperature cup of coffee spontaneously become hot by drawing heat from the air. Similarly, an ice cube melts in a warm room, moving from an ordered crystal structure to a disordered liquid.\n\n---\n\n### 3. The Third Law of Thermodynamics: Absolute Zero is Unreachable\n\n*   **Simple Statement:** The entropy of a system approaches a minimum value as the temperature approaches absolute zero. It is impossible to reach absolute zero in a finite number of steps.\n*   **Explanation:** Absolute zero (0 Kelvin or -273.15\u00b0C / -459.67\u00b0F) is the theoretical temperature at which all particle motion would completely stop. The Third Law states that as you get colder and closer to this temperature, the entropy of a perfect crystal becomes zero. However, the law also implies that it&#x27;s physically impossible to ever reach absolute zero. Each step you take to cool a system gets you closer, but the effort required to remove the next bit of heat increases exponentially. You can get incredibly close, but you can never take that final step to get there.\n*   **Everyday Example:** This law is less intuitive in daily life as it deals with extreme cold. But you can think of it like trying to create a perfect vacuum by pumping all the air out of a container. With each pump, you remove a fraction of the remaining air, so you get closer and closer to a perfect vacuum but never fully achieve it because there will always be *some* molecules left. Reaching absolute zero is a similar process of diminishing returns.\n\n| Law | Simple Statement | Key Concept |\n| :--- | :--- | :--- |\n| **Zeroth** | Defines temperature. | Thermal Equilibrium |\n| **First** | Energy is conserved. | Conservation of Energy |\n| **Second**| Disorder (entropy) increases. | Entropy &amp; The Arrow of Time |\n| **Third** | Absolute zero is unreachable. | Absolute Zero &amp; Minimum Entropy |&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:08.655096Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-pro&quot;,
    &quot;responseId&quot;: &quot;sAvxafj9J8aA9LsP4fWlkAs&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 1127,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 1127
        }
      ],
      &quot;promptTokenCount&quot;: 8,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 8
        }
      ],
      &quot;thoughtsTokenCount&quot;: 1631,
      &quot;totalTokenCount&quot;: 2766,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-pro&#x27;,
  { contents: [{ parts: [{ text: &#x27;What are the three laws of thermodynamics?&#x27; }], role: &#x27;user&#x27; }] },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-2.5-pro&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;What are the three laws of thermodynamics?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ]
  }
}&#x27;</code></pre>
</section>

<h2 id="examples">Examples</h2>

<section class="model-example"><strong>With System Instruction</strong>
<p>Using a system instruction to set context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;How do I read a JSON file in Python?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0.3
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
        }
      ]
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Of course! Reading a JSON file in Python is a common task, and the built-in `json` module makes it very straightforward.\n\nHere is the most common and recommended way to do it.\n\n### The Short &amp; Sweet Answer\n\nUse the `json.load()` function along with a `with open()` context manager.\n\n```python\nimport json\n\n# The name of your JSON file\nfilename = &#x27;data.json&#x27;\n\n# Use a &#x27;with&#x27; statement for safe file handling\nwith open(filename, &#x27;r&#x27;) as file:\n    # Load the JSON data from the file into a Python object\n    data = json.load(file)\n\n# Now &#x27;data&#x27; is a Python dictionary (or list) that you can work with\nprint(\&quot;Successfully loaded JSON data!\&quot;)\nprint(data)\n\n# Example of accessing data\nprint(\&quot;\\nAccessing specific data:\&quot;)\nprint(\&quot;Name:\&quot;, data[&#x27;name&#x27;])\nprint(\&quot;First skill:\&quot;, data[&#x27;skills&#x27;][0])\n```\n\n---\n\n### Step-by-Step Explanation\n\nLet&#x27;s break down the code above with a complete, runnable example.\n\n#### 1. Create a Sample JSON File\n\nFirst, let&#x27;s create a JSON file to read. Save the following content in a file named `data.json` in the same directory as your Python script.\n\n**`data.json`**\n```json\n{\n  \&quot;name\&quot;: \&quot;Alex\&quot;,\n  \&quot;id\&quot;: 12345,\n  \&quot;is_active\&quot;: true,\n  \&quot;email\&quot;: null,\n  \&quot;skills\&quot;: [\n    \&quot;Python\&quot;,\n    \&quot;Data Analysis\&quot;,\n    \&quot;Machine Learning\&quot;\n  ],\n  \&quot;projects\&quot;: {\n    \&quot;project_a\&quot;: \&quot;In Progress\&quot;,\n    \&quot;project_b\&quot;: \&quot;Completed\&quot;\n  }\n}\n```\n&gt; **Note:** JSON requires double quotes `\&quot;` for all keys and string values. Single quotes `&#x27;` will cause an error.\n\n#### 2. Write the Python Script\n\nNow, let&#x27;s look at the Python code in detail.\n\n**`read_file.py`**\n```python\n# Step 1: Import the json module\n# This module is built into Python, so no installation is needed.\nimport json\n\n# Step 2: Open the JSON file for reading\n# The &#x27;with&#x27; statement is highly recommended because it automatically\n# handles closing the file, even if errors occur.\n# &#x27;r&#x27; stands for \&quot;read mode\&quot;.\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as f:\n    \n    # Step 3: Load the data using json.load()\n    # The json.load() function reads from a file-like object (f),\n    # parses the JSON data, and converts it into a Python object.\n    data = json.load(f)\n\n# Step 4: Work with your new Python object\n# The &#x27;data&#x27; variable now holds the content of the JSON file.\n# JSON objects are converted to Python dictionaries.\n# JSON arrays are converted to Python lists.\n\nprint(\&quot;The data type is:\&quot;, type(data))\nprint(\&quot;---\&quot;)\nprint(\&quot;Full data:\&quot;, data)\nprint(\&quot;---\&quot;)\n\n# You can now access the data just like any other Python dictionary\nprint(\&quot;User&#x27;s name:\&quot;, data[&#x27;name&#x27;])\nprint(\&quot;User&#x27;s skills:\&quot;, data[&#x27;skills&#x27;])\n\n# Loop through the list of skills\nprint(\&quot;\\nSkills:\&quot;)\nfor skill in data[&#x27;skills&#x27;]:\n    print(\&quot;-\&quot;, skill)\n```\n\n#### How JSON Types Map to Python Types\n\nWhen you use `json.load()`, the data is converted as follows:\n\n| JSON | Python |\n| :--- | :--- |\n| object | `dict` |\n| array | `list` |\n| string | `str` |\n| number (int) | `int` |\n| number (real) | `float` |\n| `true` | `True` |\n| `false` | `False` |\n| `null` | `None` |\n\n---\n\n### Common Issues and Solutions\n\n1.  **`FileNotFoundError`**: This happens if Python can&#x27;t find your file.\n    *   **Solution**: Make sure the file name is spelled correctly and the file is in the same directory as your script. If it&#x27;s in a different directory, provide the full or relative path (e.g., `&#x27;data/my_file.json&#x27;`).\n\n2.  **`json.JSONDecodeError`**: This means your file is not valid JSON.\n    *   **Solution**: Check your `.json` file for syntax errors. The most common mistakes are:\n        *   Using single quotes (`&#x27;`) instead of double quotes (`\&quot;`).\n        *   Having a trailing comma after the last item in an object or list.\n        *   Missing commas between elements.\n\n3.  **Character Encoding Issues**: If your file contains special characters (like `\u00e9` or `\u00fc`), you might get a `UnicodeDecodeError`.\n    *   **Solution**: Specify the encoding when opening the file. UTF-8 is the most common and is standard for JSON.\n    ```python\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n        data = json.load(file)\n    ```\n\n### Reading a JSON String vs. a JSON File\n\nIt&#x27;s important to know the difference between `json.load()` and `json.loads()`.\n\n*   `json.load()`: Reads from a **file object**.\n*   `json.loads()`: Reads from a **string**. (The &#x27;s&#x27; stands for \&quot;string\&quot;).\n\n**Example using `json.loads()`:**\n\n```python\nimport json\n\njson_string = \&quot;\&quot;\&quot;\n{\n  \&quot;name\&quot;: \&quot;Brenda\&quot;,\n  \&quot;city\&quot;: \&quot;New York\&quot;\n}\n\&quot;\&quot;\&quot;\n\n# Load data from the string\ndata = json.loads(json_string)\n\nprint(data[&#x27;city&#x27;])  # Output: New York\n```&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -0.18925412299094185,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Of course! Reading a JSON file in Python is a common task, and the built-in `json` module makes it very straightforward.\n\nHere is the most common and recommended way to do it.\n\n### The Short &amp; Sweet Answer\n\nUse the `json.load()` function along with a `with open()` context manager.\n\n```python\nimport json\n\n# The name of your JSON file\nfilename = &#x27;data.json&#x27;\n\n# Use a &#x27;with&#x27; statement for safe file handling\nwith open(filename, &#x27;r&#x27;) as file:\n    # Load the JSON data from the file into a Python object\n    data = json.load(file)\n\n# Now &#x27;data&#x27; is a Python dictionary (or list) that you can work with\nprint(\&quot;Successfully loaded JSON data!\&quot;)\nprint(data)\n\n# Example of accessing data\nprint(\&quot;\\nAccessing specific data:\&quot;)\nprint(\&quot;Name:\&quot;, data[&#x27;name&#x27;])\nprint(\&quot;First skill:\&quot;, data[&#x27;skills&#x27;][0])\n```\n\n---\n\n### Step-by-Step Explanation\n\nLet&#x27;s break down the code above with a complete, runnable example.\n\n#### 1. Create a Sample JSON File\n\nFirst, let&#x27;s create a JSON file to read. Save the following content in a file named `data.json` in the same directory as your Python script.\n\n**`data.json`**\n```json\n{\n  \&quot;name\&quot;: \&quot;Alex\&quot;,\n  \&quot;id\&quot;: 12345,\n  \&quot;is_active\&quot;: true,\n  \&quot;email\&quot;: null,\n  \&quot;skills\&quot;: [\n    \&quot;Python\&quot;,\n    \&quot;Data Analysis\&quot;,\n    \&quot;Machine Learning\&quot;\n  ],\n  \&quot;projects\&quot;: {\n    \&quot;project_a\&quot;: \&quot;In Progress\&quot;,\n    \&quot;project_b\&quot;: \&quot;Completed\&quot;\n  }\n}\n```\n&gt; **Note:** JSON requires double quotes `\&quot;` for all keys and string values. Single quotes `&#x27;` will cause an error.\n\n#### 2. Write the Python Script\n\nNow, let&#x27;s look at the Python code in detail.\n\n**`read_file.py`**\n```python\n# Step 1: Import the json module\n# This module is built into Python, so no installation is needed.\nimport json\n\n# Step 2: Open the JSON file for reading\n# The &#x27;with&#x27; statement is highly recommended because it automatically\n# handles closing the file, even if errors occur.\n# &#x27;r&#x27; stands for \&quot;read mode\&quot;.\nwith open(&#x27;data.json&#x27;, &#x27;r&#x27;) as f:\n    \n    # Step 3: Load the data using json.load()\n    # The json.load() function reads from a file-like object (f),\n    # parses the JSON data, and converts it into a Python object.\n    data = json.load(f)\n\n# Step 4: Work with your new Python object\n# The &#x27;data&#x27; variable now holds the content of the JSON file.\n# JSON objects are converted to Python dictionaries.\n# JSON arrays are converted to Python lists.\n\nprint(\&quot;The data type is:\&quot;, type(data))\nprint(\&quot;---\&quot;)\nprint(\&quot;Full data:\&quot;, data)\nprint(\&quot;---\&quot;)\n\n# You can now access the data just like any other Python dictionary\nprint(\&quot;User&#x27;s name:\&quot;, data[&#x27;name&#x27;])\nprint(\&quot;User&#x27;s skills:\&quot;, data[&#x27;skills&#x27;])\n\n# Loop through the list of skills\nprint(\&quot;\\nSkills:\&quot;)\nfor skill in data[&#x27;skills&#x27;]:\n    print(\&quot;-\&quot;, skill)\n```\n\n#### How JSON Types Map to Python Types\n\nWhen you use `json.load()`, the data is converted as follows:\n\n| JSON | Python |\n| :--- | :--- |\n| object | `dict` |\n| array | `list` |\n| string | `str` |\n| number (int) | `int` |\n| number (real) | `float` |\n| `true` | `True` |\n| `false` | `False` |\n| `null` | `None` |\n\n---\n\n### Common Issues and Solutions\n\n1.  **`FileNotFoundError`**: This happens if Python can&#x27;t find your file.\n    *   **Solution**: Make sure the file name is spelled correctly and the file is in the same directory as your script. If it&#x27;s in a different directory, provide the full or relative path (e.g., `&#x27;data/my_file.json&#x27;`).\n\n2.  **`json.JSONDecodeError`**: This means your file is not valid JSON.\n    *   **Solution**: Check your `.json` file for syntax errors. The most common mistakes are:\n        *   Using single quotes (`&#x27;`) instead of double quotes (`\&quot;`).\n        *   Having a trailing comma after the last item in an object or list.\n        *   Missing commas between elements.\n\n3.  **Character Encoding Issues**: If your file contains special characters (like `\u00e9` or `\u00fc`), you might get a `UnicodeDecodeError`.\n    *   **Solution**: Specify the encoding when opening the file. UTF-8 is the most common and is standard for JSON.\n    ```python\n    with open(&#x27;data.json&#x27;, &#x27;r&#x27;, encoding=&#x27;utf-8&#x27;) as file:\n        data = json.load(file)\n    ```\n\n### Reading a JSON String vs. a JSON File\n\nIt&#x27;s important to know the difference between `json.load()` and `json.loads()`.\n\n*   `json.load()`: Reads from a **file object**.\n*   `json.loads()`: Reads from a **string**. (The &#x27;s&#x27; stands for \&quot;string\&quot;).\n\n**Example using `json.loads()`:**\n\n```python\nimport json\n\njson_string = \&quot;\&quot;\&quot;\n{\n  \&quot;name\&quot;: \&quot;Brenda\&quot;,\n  \&quot;city\&quot;: \&quot;New York\&quot;\n}\n\&quot;\&quot;\&quot;\n\n# Load data from the string\ndata = json.loads(json_string)\n\nprint(data[&#x27;city&#x27;])  # Output: New York\n```&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;STOP&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:08.614146Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-pro&quot;,
    &quot;responseId&quot;: &quot;sAvxaYK-JZmA6tkPxraQ6Qg&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 1292,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 1292
        }
      ],
      &quot;promptTokenCount&quot;: 20,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 20
        }
      ],
      &quot;thoughtsTokenCount&quot;: 1582,
      &quot;totalTokenCount&quot;: 2894,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-pro&#x27;,
  {
    contents: [{ parts: [{ text: &#x27;How do I read a JSON file in Python?&#x27; }], role: &#x27;user&#x27; }],
    generationConfig: { temperature: 0.3 },
    systemInstruction: {
      parts: [{ text: &#x27;You are a helpful coding assistant specializing in Python.&#x27; }],
    },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-2.5-pro&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;How do I read a JSON file in Python?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;temperature&quot;: 0.3
    },
    &quot;systemInstruction&quot;: {
      &quot;parts&quot;: [
        {
          &quot;text&quot;: &quot;You are a helpful coding assistant specializing in Python.&quot;
        }
      ]
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Multi-turn Conversation</strong>
<p>Continuing a conversation with context</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Yes, what are some good places to stop?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 2048
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;Of course! The drive from San Francisco to Los Angeles offers two very different experiences, depending on&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -5.178282888312089,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;Of course! The drive from San Francisco to Los Angeles offers two very different experiences, depending on&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;MAX_TOKENS&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:34.916567Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-pro&quot;,
    &quot;responseId&quot;: &quot;ygvxadf4N5TIodAPqsDhyQk&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 19,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 19
        }
      ],
      &quot;promptTokenCount&quot;: 64,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 64
        }
      ],
      &quot;thoughtsTokenCount&quot;: 477,
      &quot;totalTokenCount&quot;: 560,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-pro&#x27;,
  {
    contents: [
      {
        parts: [{ text: &#x27;I need help planning a road trip from San Francisco to Los Angeles.&#x27; }],
        role: &#x27;user&#x27;,
      },
      {
        parts: [
          {
            text: &quot;I&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;,
          },
        ],
        role: &#x27;model&#x27;,
      },
      { parts: [{ text: &#x27;Yes, what are some good places to stop?&#x27; }], role: &#x27;user&#x27; },
    ],
    generationConfig: { maxOutputTokens: 2048 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-2.5-pro&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I need help planning a road trip from San Francisco to Los Angeles.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;I&#x27;\&#x27;&#x27;d be happy to help! The drive is about 380 miles and takes roughly 5-6 hours. Would you like suggestions for scenic routes or interesting stops along the way?&quot;
          }
        ],
        &quot;role&quot;: &quot;model&quot;
      },
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Yes, what are some good places to stop?&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 2048
    }
  }
}&#x27;</code></pre>
</section>

<section class="model-example"><strong>Creative Writing</strong>
<p>Higher temperature for creative output</p>
<pre><code class="language-json">{
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 1500,
      &quot;temperature&quot;: 0.8
    }
  },
  &quot;output&quot;: {
    &quot;text&quot;: &quot;The stale, metallic tang of blood was the first&quot;
  },
  &quot;raw_response&quot;: {
    &quot;candidates&quot;: [
      {
        &quot;avgLogprobs&quot;: -7.117010498046875,
        &quot;content&quot;: {
          &quot;parts&quot;: [
            {
              &quot;text&quot;: &quot;The stale, metallic tang of blood was the first&quot;
            }
          ],
          &quot;role&quot;: &quot;model&quot;
        },
        &quot;finishReason&quot;: &quot;MAX_TOKENS&quot;
      }
    ],
    &quot;createTime&quot;: &quot;2026-04-28T19:34:36.902347Z&quot;,
    &quot;gatewayMetadata&quot;: {
      &quot;keySource&quot;: &quot;BYOK&quot;
    },
    &quot;modelVersion&quot;: &quot;gemini-2.5-pro&quot;,
    &quot;responseId&quot;: &quot;zAvxacuJN-fHodAP8o2RyQ4&quot;,
    &quot;usageMetadata&quot;: {
      &quot;candidatesTokenCount&quot;: 10,
      &quot;candidatesTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 10
        }
      ],
      &quot;promptTokenCount&quot;: 13,
      &quot;promptTokensDetails&quot;: [
        {
          &quot;modality&quot;: &quot;TEXT&quot;,
          &quot;tokenCount&quot;: 13
        }
      ],
      &quot;thoughtsTokenCount&quot;: 286,
      &quot;totalTokenCount&quot;: 309,
      &quot;trafficType&quot;: &quot;ON_DEMAND&quot;
    }
  }
}</code></pre>
<pre><code class="language-typescript">const response = await env.AI.run(
  &#x27;google/gemini-2.5-pro&#x27;,
  {
    contents: [
      {
        parts: [{ text: &#x27;Write a short story opening about a detective finding an unusual clue.&#x27; }],
        role: &#x27;user&#x27;,
      },
    ],
    generationConfig: { maxOutputTokens: 1500, temperature: 0.8 },
  },
)
console.log(response)</code></pre>
<pre><code class="language-bash">curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/run \
  --header &quot;Authorization: Bearer $CLOUDFLARE_API_TOKEN&quot; \
  --header &quot;Content-Type: application/json&quot; \
  --data &#x27;{
  &quot;model&quot;: &quot;google/gemini-2.5-pro&quot;,
  &quot;input&quot;: {
    &quot;contents&quot;: [
      {
        &quot;parts&quot;: [
          {
            &quot;text&quot;: &quot;Write a short story opening about a detective finding an unusual clue.&quot;
          }
        ],
        &quot;role&quot;: &quot;user&quot;
      }
    ],
    &quot;generationConfig&quot;: {
      &quot;maxOutputTokens&quot;: 1500,
      &quot;temperature&quot;: 0.8
    }
  }
}&#x27;</code></pre>
</section>

<h2 id="parameters">Parameters</h2>

<h3 id="input">Input</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>contents</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].role</code></td><td>string</td><td>Values: user, model</td></tr><tr><td><code>contents[].parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>contents[].parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>systemInstruction</code></td><td>object</td><td></td></tr><tr><td><code>systemInstruction.parts</code></td><td>array</td><td>Required.</td></tr><tr><td><code>systemInstruction.parts[].text</code></td><td>string</td><td></td></tr><tr><td><code>generationConfig</code></td><td>object</td><td></td></tr><tr><td><code>generationConfig.temperature</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topP</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.topK</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.maxOutputTokens</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.candidateCount</code></td><td>number</td><td></td></tr><tr><td><code>generationConfig.stopSequences</code></td><td>array</td><td></td></tr><tr><td><code>generationConfig.responseMimeType</code></td><td>string</td><td></td></tr><tr><td><code>safetySettings</code></td><td>array</td><td></td></tr><tr><td><code>safetySettings[].category</code></td><td>string</td><td>Required.</td></tr><tr><td><code>safetySettings[].threshold</code></td><td>string</td><td>Required.</td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>toolConfig</code></td><td>object</td><td></td></tr><tr><td><code>messages</code></td><td>array</td><td>Required.</td></tr><tr><td><code>messages[].role</code></td><td>string</td><td>Required. Values: system, developer, user, assistant, tool</td></tr><tr><td><code>messages[].content</code></td><td>string or null or array</td><td></td></tr><tr><td><code>temperature</code></td><td>number</td><td>Minimum: 0; Maximum: 2</td></tr><tr><td><code>max_tokens</code></td><td>number</td><td></td></tr><tr><td><code>max_completion_tokens</code></td><td>number</td><td></td></tr><tr><td><code>top_p</code></td><td>number</td><td>Minimum: 0; Maximum: 1</td></tr><tr><td><code>frequency_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>presence_penalty</code></td><td>number</td><td>Minimum: -2; Maximum: 2</td></tr><tr><td><code>stream</code></td><td>boolean</td><td></td></tr><tr><td><code>stream_options</code></td><td>object</td><td></td></tr><tr><td><code>stream_options.include_usage</code></td><td>boolean</td><td></td></tr><tr><td><code>tools</code></td><td>array</td><td></td></tr><tr><td><code>tool_choice</code></td><td>object</td><td></td></tr><tr><td><code>response_format</code></td><td>object</td><td></td></tr><tr><td><code>modalities</code></td><td>array</td><td></td></tr><tr><td><code>audio</code></td><td>object</td><td></td></tr><tr><td><code>audio.voice</code></td><td>string</td><td>Values: alloy, ash, ballad, coral, echo, sage, shimmer, verse</td></tr><tr><td><code>audio.format</code></td><td>string</td><td>Values: wav, mp3, flac, opus, pcm16</td></tr><tr><td><code>reasoning_effort</code></td><td>['string', 'null']</td><td>Optional reasoning control; availability and accepted values are model-dependent.</td></tr></tbody></table></div>

<h3 id="output">Output</h3>

<div class="table-scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td><code>candidates</code></td><td>array</td><td></td></tr><tr><td><code>usageMetadata</code></td><td>object</td><td></td></tr><tr><td><code>usageMetadata.promptTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.candidatesTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>usageMetadata.totalTokenCount</code></td><td>number</td><td></td></tr><tr><td><code>modelVersion</code></td><td>string</td><td></td></tr><tr><td><code>id</code></td><td>string</td><td>Required.</td></tr><tr><td><code>object</code></td><td>string</td><td>Required.</td></tr><tr><td><code>created</code></td><td>number</td><td>Required.</td></tr><tr><td><code>model</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices</code></td><td>array</td><td>Required.</td></tr><tr><td><code>choices[].index</code></td><td>number</td><td>Required.</td></tr><tr><td><code>choices[].message</code></td><td>object</td><td>Required.</td></tr><tr><td><code>choices[].message.role</code></td><td>string</td><td>Required.</td></tr><tr><td><code>choices[].message.content</code></td><td>['string', 'null']</td><td></td></tr><tr><td><code>choices[].message.tool_calls</code></td><td>array or null</td><td></td></tr><tr><td><code>choices[].message.audio</code></td><td>object or null</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.id</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.data</code></td><td>string</td><td></td></tr><tr><td><code>choices[].message.audio.expires_at</code></td><td>number</td><td></td></tr><tr><td><code>choices[].message.audio.transcript</code></td><td>string</td><td></td></tr><tr><td><code>choices[].finish_reason</code></td><td>['string', 'null']</td><td>Required.</td></tr><tr><td><code>usage</code></td><td>object</td><td></td></tr><tr><td><code>usage.prompt_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.completion_tokens</code></td><td>number</td><td>Required.</td></tr><tr><td><code>usage.total_tokens</code></td><td>number</td><td>Required.</td></tr></tbody></table></div>

<h2 id="api-schemas-raw">API Schemas (Raw)</h2>

- [Input schema](/ai/models/google/gemini-2.5-pro/schema-input.json)
- [Output schema](/ai/models/google/gemini-2.5-pro/schema-output.json)

