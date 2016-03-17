<html>
<body>
<h1>Работа с картинки</h1>
<p>За целта на задачата двумерен масив от пиксели  ще наричаме изображение. Всеки
пиксел ще бъде кортеж с три елемента <a href="https://bg.wikipedia.org/wiki/RGB"><code>(Red, Green,&#x000A;Blue)</code></a>, които ще определят цвета му. Вашата
задача е да напишете следните функции за обработка на снимки:</p>

<h3>rotate_left</h3>

<p>Приема като аргумент изображение и връща същото изображение завъртяно 90
градуса наляво</p>

<p><img src="https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda_rotate_left.jpg" alt="Завъртяна на ляво панда"></p>

<h3>rotate_right</h3>

<p>Аналогично на <code>rotate_left</code>, но завърта изображението надясно</p>

<p><img src="https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda_rotate_right.jpg" alt="Завъртяна на дясно панда"></p>

<h3>invert</h3>

<p>Приема като аргумент изображение и връща неговият негатив, т.е. изображение, в
което всеки пиксел е обърнат (взима се допълнението му до бялото, например
<code>(100, 155, 15)</code> се преобразува до <code>(155, 100, 240)</code>.</p>

<p><img src="https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda_invert.jpg" alt="Негатив на панда"></p>

<h3>lighten</h3>

<p>Приема два аргумента - изображение и реално число между <code>0</code> и <code>1</code>. Връща
изображението изсветлено с коефициент реалното число. Изсветляването се случва
пиксел по пиксел като всеки от тях се изсвелява по начинът показан по-долу.</p>

<p>Ако реалното число е <code>0.5</code> и пикселът, който искаме да преобразуваме е <code>(90,&#x000A;60, 90)</code>:</p>

<p><code>(90, 60, 90) -&gt; (90 + 0.5*(255 - 90), 60 + 0.5*(255 - 60), 90 + 0.5*(255 - 90))</code></p>

<p><img src="https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda_lighten.jpg" alt="Светла панда"></p>

<h3>darken</h3>

<p>Приема два аргумента - изображение и реално число между <code>0</code> и <code>1</code>. Връща
изображението потъмнено с коефициент реалното число. Затъмняването се случва
пиксел по пиксел като всеки от тях се потъмнява по начинът показан по-долу.</p>


<p>Ако реалното число е <code>0.5</code> и пикселът, който искаме да преобразуваме е <code>(90,&#x000A;60, 90)</code>:</p>

<p><code>(90, 60, 90) -&gt; (90 - 0.5*(90 - 0), 60 - 0.5*(60 - 0), 90 - 0.5*(90 - 0))</code></p>

<p><img src="https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/panda_darken.jpg" alt="Тъмна панда"></p>

<h3>create_histogram</h3>

<p>Функцията приема като аргумент изображението и връща хистограма по всеки от
трите цвята. Хистограмата ни трябва да представлява речник с три ключа:</p>

<ul>
<li><code>'red'</code></li>
<li><code>'green'</code></li>
<li><code>'blue'</code></li>
</ul>


<p>Всеки ключ се асоциира с речник с ключове от 0 до 255. Стойността на ключа <code>i</code>
в речника асоцииран с <code>'red'</code> показва колко пъти стойността <code>i</code> се среща като
стойност на червеното измежду пикселите в изображението.</p>

<p>Хистограмата на нашата панда изглежда така:</p>

<p><img src="https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/histogram.png" alt="Хистограма на панда"></p>

<h2>Визуализация</h2>

<p>За да ви в по-лесно да прецените коректността на вашите домашни, сме ви
подготвили малък скрипт, който да генерира изображения.</p>


<ol>
<li>Инсталирайте <code>Pillow</code>: <code>pip install Pillow</code>
</li>
<li>Инсталирайте <code>matplotlib</code>: <code>pip install matplotlib</code> или http://matplotlib.org/users/installing.html</li>
<li>Кръстете файла с вашето решение <code>solution.py</code>
</li>
<li>В същата директория поставете <a href="https://raw.githubusercontent.com/fmi/python-homework/master/2016/01/render.py"><code>render.py</code></a>
</li>
<li>Изпълнете командата <code>python render.py panda.jpg darken 0.7</code>. Това ще изпълни
вашата имплементация на <code>darken()</code>, върху изображението <code>panda.jpg</code> (в
същата директория) и ще подаде <code>0.5</code> като аргумент.</li>
<li>Аналогично:

<ul>
<li><code>python render.py panda.jpg rotate_left</code></li>
<li><code>python render.py panda.jpg rotate_right</code></li>
<li><code>python render.py panda.jpg lighten 0.5</code></li>
<li><code>python render.py panda.jpg create_histogram</code></li>
</ul>
</li>
</ol>


<h2>Забележки:</h2>

<ul>
<li>Функциите <strong>не</strong> трябва да променят подадените им стойности!</li>
<li>
<strong>Не</strong> трябва да валидирате подадените данни. Ние няма да тестваме с невалидни данни.</li>
<li>Имате право да дефинирате и други функции, освен описаните по-горе задължителни такива.</li>
</ul>


</div>

</div>
<footer>
<a href="#">Някои права запазени</a>
</footer>
</div>
<script>

</body>
</html>
