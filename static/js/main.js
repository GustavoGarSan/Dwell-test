window.onload = function() {
    let errorCount = 0;
    let purchaseForm = document.getElementById('purchaseForm');

    if (purchaseForm) {
        purchaseForm.onsubmit = function(event) {
            event.preventDefault();
            let max_purchases = parseInt(purchaseForm.getAttribute('data'));
            if (localStorage.getItem('purchaseCount')) {
                let counter = parseInt(localStorage.getItem('purchaseCount'));
                if (counter < max_purchases) {
                    counter = counter + 1;
                    localStorage.setItem('purchaseCount', counter);
                    purchaseForm.submit();
                } else {
                    console.log("You cannot buy more than 10 tickets");
                    if (errorCount == 0) {
                        let errorMsg = document.createElement("p");
                        let text = document.createTextNode("You cannot buy more than 10 tickets"); 
                        errorMsg.appendChild(text); // <p>TEST TEXT</p>
                        purchaseForm.parentNode.insertBefore(errorMsg, purchaseForm.nextSibling);
                        errorCount = errorCount + 1;
                    }
                    return;
                }
            } else {
                localStorage.setItem('purchaseCount', 1);
                purchaseForm.submit();
            }
        }
    }
}

