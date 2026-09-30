<h2 id="formatdatetime">formatDateTime</h2>
<p>Usage:</p>
<pre><code class="language-sql">formatDateTime(&lt;datetime expression&gt;, &lt;format string&gt;[, &lt;timezone string&gt;])&#10;</code></pre>
<p><code>formatDateTime</code> prints a datetime as a string according to a provided format string. Refer to
<a href="https://clickhouse.com/docs/en/sql-reference/functions/date-time-functions/#formatdatetime">ClickHouse's documentation</a>
for a list of supported formatting options.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- prints the current YYYY-MM-DD in UTC&#10;formatDateTime(now(), &#x27;%Y-%m-%d&#x27;)&#10;&#10;&#45;- prints YYYY-MM-DD in the datetime&#x27;s timezone&#10;formatDateTime(&lt;a datetime with a timezone&gt;, &#x27;%Y-%m-%d&#x27;)&#10;formatDateTime(toDateTime(&#x27;2022-12-01 16:17:00&#x27;, &#x27;America/New_York&#x27;), &#x27;%Y-%m-%d&#x27;)&#10;&#10;&#45;- prints YYYY-MM-DD in UTC&#10;formatDateTime(&lt;a datetime with a timezone&gt;, &#x27;%Y-%m-%d&#x27;, &#x27;Etc/UTC&#x27;)&#10;formatDateTime(toDateTime(&#x27;2022-12-01 16:17:00&#x27;, &#x27;America/New_York&#x27;), &#x27;%Y-%m-%d&#x27;, &#x27;Etc/UTC&#x27;)&#10;</code></pre>
<h2 id="now">now</h2>
<p>Usage:</p>
<pre><code class="language-sql">now()&#10;</code></pre>
<p>Returns the current time as a DateTime.</p>
<h2 id="today">today <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">today()&#10;</code></pre>
<p>Returns the current date as a <code>Date</code>.</p>
<h2 id="todatetime">toDateTime</h2>
<p>Usage:</p>
<pre><code class="language-sql">toDateTime(&lt;expression&gt;[, &#x27;timezone string&#x27;])&#10;</code></pre>
<p><code>toDateTime</code> converts an expression to a datetime. This function does not support ISO 8601-style timezones; if your time is not in UTC then you must provide the timezone using the second optional argument.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- double1 contains a unix timestamp in seconds&#10;toDateTime(double1)&#10;&#10;&#45;- blob1 contains an datetime in the format &#x27;YYYY-MM-DD hh:mm:ss&#x27;&#10;toDateTime(blob1)&#10;&#10;&#45;- literal values:&#10;toDateTime(355924804) -- unix timestamp&#10;toDateTime(&#x27;355924804&#x27;) -- string containing unix timestamp&#10;toDateTime(&#x27;1981-04-12 12:00:04&#x27;) -- string with datetime in &#x27;YYYY-MM-DD hh:mm:ss&#x27; format&#10;&#10;&#45;- interpret a date relative to New York time&#10;toDateTime(&#x27;2022-12-01 16:17:00&#x27;, &#x27;America/New_York&#x27;)&#10;</code></pre>
<h2 id="toyear">toYear <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toYear(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toYear</code> returns the year of a datetime.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 2025&#10;toYear(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;</code></pre>
<h2 id="tomonth">toMonth <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toMonth(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toMonth</code> returns the year of a datetime.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 10&#10;toMonth(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;</code></pre>
<h2 id="todayofweek">toDayOfWeek <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toDayOfWeek(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toDayOfWeek</code> takes a datetime and returns its numerical day of the week.</p>
<p>Returns <code>1</code> to indicate Monday, <code>2</code> to indicate Tuesday, and so on.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 1 for Monday 27th October 2025&#10;toDayOfWeek(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;&#10;&#45;- returns the number 2 for Tuesday 28th October 2025&#10;toDayOfWeek(toDateTime(&#x27;2025-10-28 00:00:00&#x27;))&#10;&#10;&#45;- returns the number 7 for Sunday 2nd November 2025&#10;toDayOfWeek(toDateTime(&#x27;2025-11-02 00:00:00&#x27;))&#10;</code></pre>
<h2 id="todayofmonth">toDayOfMonth <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toDayOfMonth(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toDayOfMonth</code> returns the day of the month from a datetime.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 27&#10;toDayOfMonth(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;</code></pre>
<h2 id="tohour">toHour <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toHour(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toHour</code> returns the hour of the day from a datetime.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 9&#10;toHour(toDateTime(&#x27;2025-10-27 09:11:13&#x27;))&#10;</code></pre>
<h2 id="tominute">toMinute <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toMinute(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toMinute</code> returns the minute of the hour from a datetime.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 11&#10;toMinute(toDateTime(&#x27;2025-10-27 09:11:13&#x27;))&#10;</code></pre>
<h2 id="tosecond">toSecond <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toSecond(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toSecond</code> returns the second of the minute from a datetime.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 13&#10;toSecond(toDateTime(&#x27;2025-10-27 09:11:13&#x27;))&#10;</code></pre>
<h2 id="tounixtimestamp">toUnixTimestamp</h2>
<p>Usage:</p>
<pre><code class="language-sql">toUnixTimestamp(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toUnixTimestamp</code> converts a datetime into an integer unix timestamp.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- get the current unix timestamp&#10;toUnixTimestamp(now())&#10;</code></pre>
<h2 id="tostartofinterval">toStartOfInterval</h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfInterval(&lt;datetime&gt;, INTERVAL &#x27;&lt;n&gt;&#x27; &lt;unit&gt;[, &lt;timezone string&gt;])&#10;</code></pre>
<p><code>toStartOfInterval</code> rounds down a datetime to the nearest offset of a provided interval. This can
be useful for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round the current time down to the nearest 15 minutes&#10;toStartOfInterval(now(), INTERVAL &#x27;15&#x27; MINUTE)&#10;&#10;&#45;- round a timestamp down to the day&#10;toStartOfInterval(timestamp, INTERVAL &#x27;1&#x27; DAY)&#10;&#10;&#45;- count the number of datapoints filed in each hourly window&#10;SELECT&#10;  toStartOfInterval(timestamp, INTERVAL &#x27;1&#x27; HOUR) AS hour,&#10;  sum(_sample_interval) AS count&#10;FROM your_dataset&#10;GROUP BY hour&#10;ORDER BY hour ASC&#10;</code></pre>
<h2 id="tostartofyear">toStartOfYear <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfYear(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfYear</code> rounds down a datetime to the nearest start of year. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-01-01 00:00:00&#10;toStartOfYear(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;</code></pre>
<h2 id="tostartofmonth">toStartOfMonth <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfMonth(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfMonth</code> rounds down a datetime to the nearest start of month. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-10-01 00:00:00&#10;toStartOfMonth(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;</code></pre>
<h2 id="tostartofweek">toStartOfWeek <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfWeek(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfWeek</code> rounds down a datetime to the start of the week. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Treats Monday as the first day of the week.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a time on a Monday down to Monday 2025-10-27 00:00:00&#10;toStartOfWeek(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;&#10;&#45;- round a time on a Wednesday down to Monday 2025-10-27 00:00:00&#10;toStartOfWeek(toDateTime(&#x27;2025-10-29 00:00:00&#x27;))&#10;</code></pre>
<h2 id="tostartofday">toStartOfDay <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfDay(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfDay</code> rounds down a datetime to the nearest start of day. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-10-27 00:00:00&#10;toStartOfDay(toDateTime(&#x27;2025-10-27 00:00:00&#x27;))&#10;</code></pre>
<h2 id="tostartofhour">toStartOfHour <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfHour(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfHour</code> rounds down a datetime to the nearest start of hour. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-10-27 16:00:00&#10;toStartOfHour(toDateTime(&#x27;2025-10-27 16:55:25&#x27;))&#10;</code></pre>
<h2 id="tostartoffifteenminutes">toStartOfFifteenMinutes <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfFifteenMinutes(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfFifteenMinutes</code> rounds down a datetime to the nearest fifteen minutes. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-10-27 16:45:00&#10;toStartOfFifteenMinutes(toDateTime(&#x27;2025-10-27 16:55:25&#x27;))&#10;</code></pre>
<h2 id="tostartoftenminutes">toStartOfTenMinutes <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfTenMinutes(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfTenMinutes</code> rounds down a datetime to the nearest ten minutes. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-10-27 16:50:00&#10;toStartOfTenMinutes(toDateTime(&#x27;2025-10-27 16:55:25&#x27;))&#10;</code></pre>
<h2 id="tostartoffiveminutes">toStartOfFiveMinutes <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfFiveMinutes(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfFiveMinutes</code> rounds down a datetime to the nearest five minutes. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-10-27 16:55:00&#10;toStartOfFiveMinutes(toDateTime(&#x27;2025-10-27 16:55:25&#x27;))&#10;</code></pre>
<h2 id="tostartofminute">toStartOfMinute <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toStartOfMinute(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toStartOfMinute</code> rounds down a datetime to the nearest minute. This can be useful
for grouping data into equal-sized time ranges.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- round a timestamp down to 2025-10-27 16:55:00&#10;toStartOfMinute(toDateTime(&#x27;2025-10-27 16:55:25&#x27;))&#10;</code></pre>
<h2 id="toyyyymm">toYYYYMM <span class="nb-badge">New</span></h2>
<p>Usage:</p>
<pre><code class="language-sql">toYYYYMM(&lt;datetime&gt;)&#10;</code></pre>
<p><code>toYYYYMM</code> returns a number representing year and month of a datetime.
For instance a datetime on <code>2025-05-03</code> would return the number <code>202505</code>.</p>
<p>Examples:</p>
<pre><code class="language-sql">&#45;- returns the number 202510&#10;toYYYYMM(toDateTime(&#x27;2025-10-27 16:55:25&#x27;))&#10;</code></pre>
