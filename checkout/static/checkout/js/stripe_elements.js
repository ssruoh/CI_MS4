var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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

// Handle form submission

var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({
        'disabled': true
    });
    $('#checkout-button').attr('disabled', true);
    $('#checkout-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span role="alert">
                ${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#checkout-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({
                'disabled': false
            });
            $('#checkout-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});