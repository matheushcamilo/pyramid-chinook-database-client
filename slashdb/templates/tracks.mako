<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Track List</title>
</head>
<body>
    <h1>Track List</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Album Id</th>
                <th>Media Type Id</th>
                <th>Genre Id</th>
                <th>Composer</th>
                <th>Milliseconds</th>
                <th>Bytes</th>
                <th>Unit Price</th>
            </tr>
        </thead>
        <tbody>
            % for track in items:
                <tr>
                    <td>${track.TrackId}</td>
                    <td>${track.Name}</td>
                    <td>${track.AlbumId}</td>
                    <td>${track.MediaTypeId}</td>
                    <td>${track.GenreId}</td>
                    <td>${track.Composer or 'N/A'}</td>
                    <td>${track.Milliseconds}</td>
                    <td>${track.Bytes}</td>
                    <td>${track.UnitPrice}</td>
                </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>
