<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Playlists</title>
</head>
<body>
    <h1>$Playlists</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
            </tr>
        </thead>
        <tbody>
            % for playlist in items:
                <tr>
                    <td>${playlist.PlaylistId}</td>
                    <td>${playlist.Name}</td>
                </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>
