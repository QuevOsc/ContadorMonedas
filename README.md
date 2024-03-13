<h1>Contador de monedas</h1>

<p>Por medio de procesamiento de imagenes, se realiza el conteo de unas monedas en una fotografia</p>
<p>Se utliza las librerias opencv para el procesamiento y numpy para las operaciones matematicas</p>
<p>El procedimiento es:</p>

<li>Redimensionar la imagen</li>
<li>Aplicar escala de grises</li>
<li>Aplicar la funcion de cv2 filtro de Gauss</li>
<li>Aplicar la funcion de cv2 Canny</li>
<li>Se determina el contorno de cada moneda (COP) y se saca su área para posteriomente realizar su sumatoria.</li>
<li>Se muestra el valor total de la suma de las monedas</li>

