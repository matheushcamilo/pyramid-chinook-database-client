<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Album List</title>
</head>
<body>
    <h1>Album List</h1>
    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Artist</th>
                <!-- Add more column headers as needed -->
            </tr>
        </thead>
        <tbody>
            % for album in items:
            <tr>
                <td><a href="/album/${album.AlbumId}">${album.Title}</a></td>
                <td>${album.Artist.Name}</td>
                <!-- Add more album attributes as needed -->
            </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>
