

paypal.Buttons({
    // Sets up the transaction when a payment button is clicked
    createOrder: (data, actions) => {

      let donationAmount = document.getElementById("donationAmount").innerText;
      return actions.order.create({
        purchase_units: [{
          amount: {
            value: donationAmount // Can also reference a variable or function
          }
        }]
      });
    },
    // Finalize the transaction after payer approval
    onApprove: (data, actions) => {
      return actions.order.capture().then(function(orderData) {
        // Successful capture! For dev/demo purposes:
        //console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
        //const transaction = orderData.purchase_units[0].payments.captures[0];
        //alert(`Transaction ${transaction.status}: ${transaction.id}\n\nSee console for all available details`);
        // When ready to go live, remove the alert and show a success message within this page. For example:
        // const element = document.getElementById('paypal-button-container');
        // element.innerHTML = '<h3>Thank you for your payment!</h3>';
        // Or go to another URL:  actions.redirect('thank_you.html');


        fetch('http://127.0.0.1:8000/Donate/', {
          method: "POST",
          headers: {
            "Content-Type" : "application/json",
            "X-CSRFToken" : getCookie("csrftoken"),
          },
          mode: "same-origin",
          body: JSON.stringify({
            firstName : document.getElementById("first-name").value,
            lastName: document.getElementById("last-name").value,
            email: document.getElementById("email-address").value,
            phoneNumber: document.getElementById("phone-number").value,
            amount: orderData.purchase_units[0].amount.value,
            cause: document.getElementById("cause").value,
          }),
        }).then(response => response.json())
        .then(data =>{
          location.href = "/";
        })
        .catch(error =>{
          console.error(error);
        });
      });
      
    }

  }).render('#paypal-button-container');

function getCookie(name) {
  if (!document.cookie) {
    return null;
  }

  const xsrfCookies = document.cookie.split(';')
    .map(c => c.trim())
    .filter(c => c.startsWith(name + '='));

  if (xsrfCookies.length === 0) {
    return null;
  }
  return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}