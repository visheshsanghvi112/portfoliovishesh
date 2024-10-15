document.addEventListener("DOMContentLoaded", function () {
    const amountInput = document.getElementById("amount");
    const termInput = document.getElementById("term");
    const frequencyInput = document.getElementById("frequency");
    const paymentSpan = document.getElementById("payment");
    const calculateBtn = document.getElementById("calculate-btn");
    const amountError = document.getElementById("amount-error");
    const termError = document.getElementById("term-error");

    calculateBtn.addEventListener("click", function () {
        const amount = parseFloat(amountInput.value);
        const term = parseInt(termInput.value);
        const frequency = frequencyInput.value;

        let isValid = true;

        // Validate amount
        if (isNaN(amount) || amount <= 0) {
            isValid = false;
            amountError.textContent = "Please enter a valid loan amount";
        } else {
            amountError.textContent = "";
        }

        // Validate term
        if (isNaN(term) || term <= 0) {
            isValid = false;
            termError.textContent = "Please enter a valid loan term";
        } else {
            termError.textContent = "";
        }

        // Calculate payment if inputs are valid
        if (isValid) {
            let payment = 0;
            if (frequency === "monthly") {
                payment = calculateMonthlyPayment(amount, term);
            } else if (frequency === "biweekly") {
                payment = calculateBiweeklyPayment(amount, term);
            }
            paymentSpan.textContent = "$" + payment.toFixed(2);
        } else {
            paymentSpan.textContent = "";
        }
    });

    function calculateMonthlyPayment(amount, term) {
        // Add your calculation logic for monthly payment here
        return amount * 0.05 * Math.pow(1.05, term) / (Math.pow(1.05, term) - 1);
    }

    function calculateBiweeklyPayment(amount, term) {
        // Add your calculation logic for biweekly payment here
        return amount * 0.05 * Math.pow(1.05, term / 26) / (Math.pow(1.05, term / 26) - 1);
    }
});
