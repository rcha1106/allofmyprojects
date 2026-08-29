Public Class Form1

    Private Sub btnCalculate_Click(sender As Object, e As EventArgs) Handles btnCalculate.Click

        Dim customerName As String = ""
        Dim businessName As String = ""
        Dim spaceType As String = ""
        Dim weeks As Integer = 0

        Call ReadInputs(customerName, businessName, spaceType, weeks)

        If customerName = "" Then
            Exit Sub
        End If

        If businessName = "" Then
            Exit Sub
        End If

        If spaceType = "" Then
            Exit Sub
        End If

        If weeks <= 0 Then
            Exit Sub
        End If

        If weeks > 15 Then
            Exit Sub
        End If

        Dim weeklyRate As Decimal = 0
        Dim rentalCost As Decimal = 0
        Dim discount As Decimal = 0
        Dim subtotal As Decimal = 0
        Dim tax As Decimal = 0
        Dim finalTotal As Decimal = 0

        Call CalculateRental(spaceType, weeks, weeklyRate, rentalCost, discount, subtotal, tax, finalTotal)

        Call DisplayResults(rentalCost, discount, subtotal, tax, finalTotal)

    End Sub

    Private Sub ReadInputs(ByRef customerName As String, ByRef businessName As String, ByRef spaceType As String, ByRef weeks As Integer)

        customerName = txtCustomerName.Text
        businessName = txtBusinessName.Text
        spaceType = cbSpaceType.Text
        weeks = numNumberofWeeks.Value

        If customerName = "" Then
            MessageBox.Show("Please enter the customer name.")
            Exit Sub
        End If

        If businessName = "" Then
            MessageBox.Show("Please enter the business name.")
            Exit Sub
        End If

        If spaceType = "" Then
            MessageBox.Show("Please select a space type.")
            Exit Sub
        End If

        If weeks <= 0 Then
            MessageBox.Show("Number of weeks must be greater than 0.")
            Exit Sub
        End If

        If weeks > 15 Then
            MessageBox.Show("Number of weeks cannot be greater than 15.")
            Exit Sub
        End If

    End Sub

    Private Sub CalculateRental(spaceType As String, weeks As Integer, ByRef weeklyRate As Decimal, ByRef rentalCost As Decimal, ByRef discount As Decimal, ByRef subtotal As Decimal, ByRef tax As Decimal, ByRef finalTotal As Decimal)

        If spaceType = "Single Space - $100/Week" Then
            weeklyRate = 100
        ElseIf spaceType = "Double Space - $180/Week" Then
            weeklyRate = 180
        ElseIf spaceType = "Food Truck Space - $200/Week" Then
            weeklyRate = 200
        End If

        rentalCost = weeklyRate * weeks

        If weeks > 10 Then
            discount = rentalCost * 0.05
        End If

        subtotal = rentalCost - discount
        tax = subtotal * 0.1
        finalTotal = subtotal + tax

    End Sub

    Private Sub DisplayResults(rentalCost As Decimal, discount As Decimal, subtotal As Decimal, tax As Decimal, finalTotal As Decimal)

        lblRentalCostShow.Text = rentalCost
        lblDiscountShow.Text = discount
        lblSubtotalShow.Text = subtotal
        lblTaxShow.Text = tax
        lblFinalCostShow.Text = finalTotal

    End Sub

    Private Sub btnClear_Click(sender As Object, e As EventArgs) Handles btnClear.Click

        txtCustomerName.Text = ""
        txtBusinessName.Text = ""
        cbSpaceType.Text = ""

        numNumberofWeeks.Value = 1

        lblRentalCostShow.Text = ""
        lblDiscountShow.Text = ""
        lblSubtotalShow.Text = ""
        lblTaxShow.Text = ""
        lblFinalCostShow.Text = ""

    End Sub

    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click

        Close()

    End Sub

End Class