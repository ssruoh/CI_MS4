var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

/* Slightly altered styling from https://stripe.com/en-nl/payments/elements */
var style = {
    base: {
        color: '#000',
        fontSize: '16px',
        fontFamily: '"Assistant", sans-serif',
        fontSmoothing: 'antialiased',
        '::placeholder': {
            color: '#CFD7DF',
        },
    },
    invalid: {
        color: '#dc3545',
        ':focus': {
            color: '#dc3545',
        },
    },
};

var card = elements.create('card', {
    style: style
});

card.mount('#card-element');

// Card element validation error handling
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span role="alert">
                ${event.error.message}
            </span>
        `
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});