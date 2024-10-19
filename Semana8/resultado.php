<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $serie = htmlspecialchars($_POST["serie"]);
            echo "<p>Tu serie preferida es: <strong><em style='color: red;'>$serie</em></strong></p>";
        } else {
            echo "<p>Por favor, regresa al formulario e ingresa una serie.</p>";
        }
    ?>
</body>
</html>
