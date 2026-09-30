<p><em>Cloudflare Pipelines scalar function implementations are based on
<a href="https://arrow.apache.org/datafusion/">Apache DataFusion</a> (via <a href="https://www.arroyo.dev/">Arroyo</a>) and these docs are derived from
the DataFusion function reference.</em></p>
<h2 id="date-bin"><code>date_bin</code></h2>
<p>Calculates time intervals and returns the start of the interval nearest to the specified timestamp.
Use <code>date_bin</code> to downsample time series data by grouping rows into time-based &quot;bins&quot; or &quot;windows&quot;
and applying an aggregate or selector function to each window.</p>
<p>For example, if you &quot;bin&quot; or &quot;window&quot; data into 15 minute intervals, an input
timestamp of <code>2023-01-01T18:18:18Z</code> will be updated to the start time of the 15
minute bin it is in: <code>2023-01-01T18:15:00Z</code>.</p>
<pre><code>date_bin(interval, expression, origin-timestamp)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>interval</strong>: Bin interval.</li>
<li><strong>expression</strong>: Time expression to operate on.
Can be a constant, column, or function.</li>
<li><strong>origin-timestamp</strong>: Optional. Starting point used to determine bin boundaries. If not specified
defaults <code>1970-01-01T00:00:00Z</code> (the UNIX epoch in UTC).</li>
</ul>
<p>The following intervals are supported:</p>
<ul>
<li>nanoseconds</li>
<li>microseconds</li>
<li>milliseconds</li>
<li>seconds</li>
<li>minutes</li>
<li>hours</li>
<li>days</li>
<li>weeks</li>
<li>months</li>
<li>years</li>
<li>century</li>
</ul>
<h2 id="date-trunc"><code>date_trunc</code></h2>
<p>Truncates a timestamp value to a specified precision.</p>
<pre><code>date_trunc(precision, expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li>
<p><strong>precision</strong>: Time precision to truncate to.
The following precisions are supported:</p>
<ul>
<li>year / YEAR</li>
<li>quarter / QUARTER</li>
<li>month / MONTH</li>
<li>week / WEEK</li>
<li>day / DAY</li>
<li>hour / HOUR</li>
<li>minute / MINUTE</li>
<li>second / SECOND</li>
</ul>
</li>
<li>
<p><strong>expression</strong>: Time expression to operate on.
Can be a constant, column, or function.</p>
</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>datetrunc</li>
</ul>
<h2 id="datetrunc"><code>datetrunc</code></h2>
<p><em>Alias of <a href="#date_trunc">date_trunc</a>.</em></p>
<h2 id="date-part"><code>date_part</code></h2>
<p>Returns the specified part of the date as an integer.</p>
<pre><code>date_part(part, expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li>
<p><strong>part</strong>: Part of the date to return.
The following date parts are supported:</p>
<ul>
<li>year</li>
<li>quarter <em>(emits value in inclusive range [1, 4] based on which quartile of the year the date is in)</em></li>
<li>month</li>
<li>week <em>(week of the year)</em></li>
<li>day <em>(day of the month)</em></li>
<li>hour</li>
<li>minute</li>
<li>second</li>
<li>millisecond</li>
<li>microsecond</li>
<li>nanosecond</li>
<li>dow <em>(day of the week)</em></li>
<li>doy <em>(day of the year)</em></li>
<li>epoch <em>(seconds since Unix epoch)</em></li>
</ul>
</li>
<li>
<p><strong>expression</strong>: Time expression to operate on.
Can be a constant, column, or function.</p>
</li>
</ul>
<p><strong>Aliases</strong></p>
<ul>
<li>datepart</li>
</ul>
<h2 id="datepart"><code>datepart</code></h2>
<p><em>Alias of <a href="#date_part">date_part</a>.</em></p>
<h2 id="extract"><code>extract</code></h2>
<p>Returns a sub-field from a time value as an integer.</p>
<pre><code>extract(field FROM source)&#10;</code></pre>
<p>Equivalent to calling <code>date_part('field', source)</code>. For example, these are equivalent:</p>
<pre><code class="language-sql">extract(day FROM &#x27;2024-04-13&#x27;::date)&#10;date_part(&#x27;day&#x27;, &#x27;2024-04-13&#x27;::date)&#10;</code></pre>
<p>See <a href="#date_part">date_part</a>.</p>
<h2 id="make-date"><code>make_date</code></h2>
<p>Make a date from year/month/day component parts.</p>
<pre><code>make_date(year, month, day)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>year</strong>: Year to use when making the date.
Can be a constant, column or function, and any combination of arithmetic operators.</li>
<li><strong>month</strong>: Month to use when making the date.
Can be a constant, column or function, and any combination of arithmetic operators.</li>
<li><strong>day</strong>: Day to use when making the date.
Can be a constant, column or function, and any combination of arithmetic operators.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select make_date(2023, 1, 31);&#10;&#43;-------------------------------------------+&#10;| make_date(Int64(2023),Int64(1),Int64(31)) |&#10;&#43;-------------------------------------------+&#10;| 2023-01-31                                |&#10;&#43;-------------------------------------------+&#10;&gt; select make_date(&#x27;2023&#x27;, &#x27;01&#x27;, &#x27;31&#x27;);&#10;&#43;-----------------------------------------------+&#10;| make_date(Utf8(&quot;2023&quot;),Utf8(&quot;01&quot;),Utf8(&quot;31&quot;)) |&#10;&#43;-----------------------------------------------+&#10;| 2023-01-31                                    |&#10;&#43;-----------------------------------------------+&#10;</code></pre>
<h2 id="to-char"><code>to_char</code></h2>
<p>Returns a string representation of a date, time, timestamp or duration based
on a <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a>. Unlike the PostgreSQL equivalent of this function
numerical formatting is not supported.</p>
<pre><code>to_char(expression, format)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to operate on.
Can be a constant, column, or function that results in a
date, time, timestamp or duration.</li>
<li><strong>format</strong>: A <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a> string to use to convert the expression.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; &gt; select to_char(&#x27;2023-03-01&#x27;::date, &#x27;%d-%m-%Y&#x27;);&#10;&#43;----------------------------------------------+&#10;| to_char(Utf8(&quot;2023-03-01&quot;),Utf8(&quot;%d-%m-%Y&quot;)) |&#10;&#43;----------------------------------------------+&#10;| 01-03-2023                                   |&#10;&#43;----------------------------------------------+&#10;</code></pre>
<p><strong>Aliases</strong></p>
<ul>
<li>date_format</li>
</ul>
<h2 id="to-timestamp"><code>to_timestamp</code></h2>
<p>Converts a value to a timestamp (<code>YYYY-MM-DDT00:00:00Z</code>).
Supports strings, integer, unsigned integer, and double types as input.
Strings are parsed as RFC3339 (e.g. '2023-07-20T05:44:00') if no [Chrono formats] are provided.
Integers, unsigned integers, and doubles are interpreted as seconds since the unix epoch (<code>1970-01-01T00:00:00Z</code>).
Returns the corresponding timestamp.</p>
<p>Note: <code>to_timestamp</code> returns <code>Timestamp(Nanosecond)</code>. The supported range for integer input is between <code>-9223372037</code> and <code>9223372036</code>.
Supported range for string input is between <code>1677-09-21T00:12:44.0</code> and <code>2262-04-11T23:47:16.0</code>. Please use <code>to_timestamp_seconds</code>
for the input outside of supported bounds.</p>
<pre><code>to_timestamp(expression[, ..., format_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>format_n</strong>: Optional <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a> strings to use to parse the expression. Formats will be tried in the order
they appear with the first successful one being returned. If none of the formats successfully parse the expression
an error will be returned.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select to_timestamp(&#x27;2023-01-31T09:26:56.123456789-05:00&#x27;);&#10;&#43;-----------------------------------------------------------+&#10;| to_timestamp(Utf8(&quot;2023-01-31T09:26:56.123456789-05:00&quot;)) |&#10;&#43;-----------------------------------------------------------+&#10;| 2023-01-31T14:26:56.123456789                             |&#10;&#43;-----------------------------------------------------------+&#10;&gt; select to_timestamp(&#x27;03:59:00.123456789 05-17-2023&#x27;, &#x27;%c&#x27;, &#x27;%+&#x27;, &#x27;%H:%M:%S%.f %m-%d-%Y&#x27;);&#10;&#43;--------------------------------------------------------------------------------------------------------+&#10;| to_timestamp(Utf8(&quot;03:59:00.123456789 05-17-2023&quot;),Utf8(&quot;%c&quot;),Utf8(&quot;%+&quot;),Utf8(&quot;%H:%M:%S%.f %m-%d-%Y&quot;)) |&#10;&#43;--------------------------------------------------------------------------------------------------------+&#10;| 2023-05-17T03:59:00.123456789                                                                          |&#10;&#43;--------------------------------------------------------------------------------------------------------+&#10;</code></pre>
<h2 id="to-timestamp-millis"><code>to_timestamp_millis</code></h2>
<p>Converts a value to a timestamp (<code>YYYY-MM-DDT00:00:00.000Z</code>).
Supports strings, integer, and unsigned integer types as input.
Strings are parsed as RFC3339 (e.g. '2023-07-20T05:44:00') if no <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a>s are provided.
Integers and unsigned integers are interpreted as milliseconds since the unix epoch (<code>1970-01-01T00:00:00Z</code>).
Returns the corresponding timestamp.</p>
<pre><code>to_timestamp_millis(expression[, ..., format_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>format_n</strong>: Optional <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a> strings to use to parse the expression. Formats will be tried in the order
they appear with the first successful one being returned. If none of the formats successfully parse the expression
an error will be returned.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select to_timestamp_millis(&#x27;2023-01-31T09:26:56.123456789-05:00&#x27;);&#10;&#43;------------------------------------------------------------------+&#10;| to_timestamp_millis(Utf8(&quot;2023-01-31T09:26:56.123456789-05:00&quot;)) |&#10;&#43;------------------------------------------------------------------+&#10;| 2023-01-31T14:26:56.123                                          |&#10;&#43;------------------------------------------------------------------+&#10;&gt; select to_timestamp_millis(&#x27;03:59:00.123456789 05-17-2023&#x27;, &#x27;%c&#x27;, &#x27;%+&#x27;, &#x27;%H:%M:%S%.f %m-%d-%Y&#x27;);&#10;&#43;---------------------------------------------------------------------------------------------------------------+&#10;| to_timestamp_millis(Utf8(&quot;03:59:00.123456789 05-17-2023&quot;),Utf8(&quot;%c&quot;),Utf8(&quot;%+&quot;),Utf8(&quot;%H:%M:%S%.f %m-%d-%Y&quot;)) |&#10;&#43;---------------------------------------------------------------------------------------------------------------+&#10;| 2023-05-17T03:59:00.123                                                                                       |&#10;&#43;---------------------------------------------------------------------------------------------------------------+&#10;</code></pre>
<h2 id="to-timestamp-micros"><code>to_timestamp_micros</code></h2>
<p>Converts a value to a timestamp (<code>YYYY-MM-DDT00:00:00.000000Z</code>).
Supports strings, integer, and unsigned integer types as input.
Strings are parsed as RFC3339 (e.g. '2023-07-20T05:44:00') if no <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a>s are provided.
Integers and unsigned integers are interpreted as microseconds since the unix epoch (<code>1970-01-01T00:00:00Z</code>)
Returns the corresponding timestamp.</p>
<pre><code>to_timestamp_micros(expression[, ..., format_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>format_n</strong>: Optional <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a> strings to use to parse the expression. Formats will be tried in the order
they appear with the first successful one being returned. If none of the formats successfully parse the expression
an error will be returned.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select to_timestamp_micros(&#x27;2023-01-31T09:26:56.123456789-05:00&#x27;);&#10;&#43;------------------------------------------------------------------+&#10;| to_timestamp_micros(Utf8(&quot;2023-01-31T09:26:56.123456789-05:00&quot;)) |&#10;&#43;------------------------------------------------------------------+&#10;| 2023-01-31T14:26:56.123456                                       |&#10;&#43;------------------------------------------------------------------+&#10;&gt; select to_timestamp_micros(&#x27;03:59:00.123456789 05-17-2023&#x27;, &#x27;%c&#x27;, &#x27;%+&#x27;, &#x27;%H:%M:%S%.f %m-%d-%Y&#x27;);&#10;&#43;---------------------------------------------------------------------------------------------------------------+&#10;| to_timestamp_micros(Utf8(&quot;03:59:00.123456789 05-17-2023&quot;),Utf8(&quot;%c&quot;),Utf8(&quot;%+&quot;),Utf8(&quot;%H:%M:%S%.f %m-%d-%Y&quot;)) |&#10;&#43;---------------------------------------------------------------------------------------------------------------+&#10;| 2023-05-17T03:59:00.123456                                                                                    |&#10;&#43;---------------------------------------------------------------------------------------------------------------+&#10;</code></pre>
<h2 id="to-timestamp-nanos"><code>to_timestamp_nanos</code></h2>
<p>Converts a value to a timestamp (<code>YYYY-MM-DDT00:00:00.000000000Z</code>).
Supports strings, integer, and unsigned integer types as input.
Strings are parsed as RFC3339 (e.g. '2023-07-20T05:44:00') if no [Chrono formats] are provided.
Integers and unsigned integers are interpreted as nanoseconds since the unix epoch (<code>1970-01-01T00:00:00Z</code>).
Returns the corresponding timestamp.</p>
<pre><code>to_timestamp_nanos(expression[, ..., format_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>format_n</strong>: Optional <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a> strings to use to parse the expression. Formats will be tried in the order
they appear with the first successful one being returned. If none of the formats successfully parse the expression
an error will be returned.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select to_timestamp_nanos(&#x27;2023-01-31T09:26:56.123456789-05:00&#x27;);&#10;&#43;-----------------------------------------------------------------+&#10;| to_timestamp_nanos(Utf8(&quot;2023-01-31T09:26:56.123456789-05:00&quot;)) |&#10;&#43;-----------------------------------------------------------------+&#10;| 2023-01-31T14:26:56.123456789                                   |&#10;&#43;-----------------------------------------------------------------+&#10;&gt; select to_timestamp_nanos(&#x27;03:59:00.123456789 05-17-2023&#x27;, &#x27;%c&#x27;, &#x27;%+&#x27;, &#x27;%H:%M:%S%.f %m-%d-%Y&#x27;);&#10;&#43;--------------------------------------------------------------------------------------------------------------+&#10;| to_timestamp_nanos(Utf8(&quot;03:59:00.123456789 05-17-2023&quot;),Utf8(&quot;%c&quot;),Utf8(&quot;%+&quot;),Utf8(&quot;%H:%M:%S%.f %m-%d-%Y&quot;)) |&#10;&#43;--------------------------------------------------------------------------------------------------------------+&#10;| 2023-05-17T03:59:00.123456789                                                                                |&#10;&#43;---------------------------------------------------------------------------------------------------------------+&#10;</code></pre>
<h2 id="to-timestamp-seconds"><code>to_timestamp_seconds</code></h2>
<p>Converts a value to a timestamp (<code>YYYY-MM-DDT00:00:00.000Z</code>).
Supports strings, integer, and unsigned integer types as input.
Strings are parsed as RFC3339 (e.g. '2023-07-20T05:44:00') if no <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a>s are provided.
Integers and unsigned integers are interpreted as seconds since the unix epoch (<code>1970-01-01T00:00:00Z</code>).
Returns the corresponding timestamp.</p>
<pre><code>to_timestamp_seconds(expression[, ..., format_n])&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
<li><strong>format_n</strong>: Optional <a href="https://docs.rs/chrono/latest/chrono/format/strftime/index.html">Chrono format</a> strings to use to parse the expression. Formats will be tried in the order
they appear with the first successful one being returned. If none of the formats successfully parse the expression
an error will be returned.</li>
</ul>
<p><strong>Example</strong></p>
<pre><code>&gt; select to_timestamp_seconds(&#x27;2023-01-31T09:26:56.123456789-05:00&#x27;);&#10;&#43;-------------------------------------------------------------------+&#10;| to_timestamp_seconds(Utf8(&quot;2023-01-31T09:26:56.123456789-05:00&quot;)) |&#10;&#43;-------------------------------------------------------------------+&#10;| 2023-01-31T14:26:56                                               |&#10;&#43;-------------------------------------------------------------------+&#10;&gt; select to_timestamp_seconds(&#x27;03:59:00.123456789 05-17-2023&#x27;, &#x27;%c&#x27;, &#x27;%+&#x27;, &#x27;%H:%M:%S%.f %m-%d-%Y&#x27;);&#10;&#43;----------------------------------------------------------------------------------------------------------------+&#10;| to_timestamp_seconds(Utf8(&quot;03:59:00.123456789 05-17-2023&quot;),Utf8(&quot;%c&quot;),Utf8(&quot;%+&quot;),Utf8(&quot;%H:%M:%S%.f %m-%d-%Y&quot;)) |&#10;&#43;----------------------------------------------------------------------------------------------------------------+&#10;| 2023-05-17T03:59:00                                                                                            |&#10;&#43;----------------------------------------------------------------------------------------------------------------+&#10;</code></pre>
<h2 id="from-unixtime"><code>from_unixtime</code></h2>
<p>Converts an integer to RFC3339 timestamp format (<code>YYYY-MM-DDT00:00:00.000000000Z</code>).
Integers and unsigned integers are interpreted as nanoseconds since the unix epoch (<code>1970-01-01T00:00:00Z</code>)
return the corresponding timestamp.</p>
<pre><code>from_unixtime(expression)&#10;</code></pre>
<p><strong>Arguments</strong></p>
<ul>
<li><strong>expression</strong>: Expression to operate on.
Can be a constant, column, or function, and any combination of arithmetic operators.</li>
</ul>
<h2 id="now"><code>now</code></h2>
<p>Returns the UTC timestamp at pipeline start.</p>
<p>The now() return value is determined at query compilation time, and will be constant across the execution
of the pipeline.</p>
