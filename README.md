<h1>Contador de monedas</h1>

<p>Por medio de procesamiento de imagenes, se realiza el conteo de unas monedas en una fotografia</p>
<p>Se utliza las librerias opencv para el procesamiento y numpy para las operaciones matematicas</p>
<p>El procedimiento es:</p>
<li>
  <p>1.Redimensionar la imagen</p>
  <p>2.Aplicar escala de grises</p>
  <p>3.Aplicar la funcion de cv2 filtro de Gauss</p>
  <p>4.Aplicar la funcion de cv2 Canny</p>
  <p>5.Se determina el contorno de cada moneda (COP) y se saca su área para posteriomente realizar su sumatoria.</p>
  <p>6.Se muestra el valor total de la suma de las monedas</p>
</li>
