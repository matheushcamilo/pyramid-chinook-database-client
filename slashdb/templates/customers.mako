<!-- customer_list.mako -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer List</title>
</head>
<body>
    <h1>Customer List</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Company</th>
                <th>Address</th>
                <th>City</th>
                <th>State</th>
                <th>Country</th>
                <th>Postal Code</th>
                <th>Phone</th>
                <th>Fax</th>
                <th>Email</th>
                <th>Support Rep ID</th>
            </tr>
        </thead>
        <tbody>
            % for customer in items:
                <tr>
                    <td>${customer.CustomerId}</td>
                    <td>${customer.FirstName}</td>
                    <td>${customer.LastName}</td>
                    <td>${customer.Company}</td>
                    <td>${customer.Address}</td>
                    <td>${customer.City}</td>
                    <td>${customer.State}</td>
                    <td>${customer.Country}</td>
                    <td>${customer.PostalCode}</td>
                    <td>${customer.Phone}</td>
                    <td>${customer.Fax}</td>
                    <td>${customer.Email}</td>
                    <td>${customer.SupportRepId}</td>
                </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>
