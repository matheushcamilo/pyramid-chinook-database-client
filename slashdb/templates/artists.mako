<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$Artist List</title>
</head>
<body>
    <h1>$Artist List</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
            </tr>
        </thead>
        <tbody>
            % for artist in items:
                <tr>
                    <td>${artist.ArtistId}</td>
                    <td>${artist.Name}</td>
                </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>
