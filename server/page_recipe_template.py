from re import template


page_template= """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Recipes</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  </head>
    <body>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
        <div class="container-fluid p-5 bg-primary text-white text-center">
            <h1>{}</h1>
            <p>by Agata Malczyk</p>
        </div>
        <div class="container mt-5">
            <div class="row">
                 <div class="col-sm-4">
                    <img src="{}" width="300" height="300" alt="">
                </div>
                <div class="col-sm-4">
                    <h2>składniki</h2><hr>
                    <ul>
                        <li>składnik 1</li>
                        <li>składnik 2</li>
                        <li>składnik 3</li>
                    </ul>   
                </div>
            </div>
            <div class="row">
                <a href="/">back</a>       
            </div>
        </div>
        
        
    </body>
</html>
"""