<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Invoices</title>
</head>
<body>
    <h1>$Invoices</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Customer ID</th>
                <th>Invoice Date</th>
                <th>Billing Address</th>
                <th>Billing City</th>
                <th>Billing State</th>
                <th>Billing Country</th>
                <th>Billing Postal Code</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            % for invoice in items:
                <tr>
                    <td>${invoice.InvoiceId}</td>
                    <td>${invoice.CustomerId}</td>
                    <td>${invoice.InvoiceDate}</td>
                    <td>${invoice.BillingAddress}</td>
                    <td>${invoice.BillingCity}</td>
                    <td>${invoice.BillingState}</td>
                    <td>${invoice.BillingCountry}</td>
                    <td>${invoice.BillingPostalCode}</td>
                    <td>${invoice.Total}</td>
                </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>
