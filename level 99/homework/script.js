

const cardNumberInput = document.querySelector('input[placeholder="e.g. 1234 5678 9123 0000"]');
const cardHolderInput = document.querySelector('input[placeholder="e.g. Jane Appleseed"]');
const expMonthInput = document.querySelector('input[placeholder="MM"]');
const expYearInput = document.querySelector('input[placeholder="YY"]');
const cvcInput = document.querySelector('input[placeholder="e.g. 123"]');
const confirmButton = document.querySelector('button');

const cardNumberDisplay = document.querySelector('.card-number');
const cardHolderDisplay = document.querySelector('.card-name');
const cardExpDisplay = document.querySelector('.card-exp');
const cardCvcDisplay = document.querySelector('.card-cvc');


cardNumberInput.addEventListener('input', () => {
  cardNumberDisplay.textContent = cardNumberInput.value || '0000 0000 0000 0000';
});

cardHolderInput.addEventListener('input', () => {
  cardHolderDisplay.textContent = cardHolderInput.value || 'JANE APPLESEED';
});

expMonthInput.addEventListener('input', updateExpDate);
expYearInput.addEventListener('input', updateExpDate);

function updateExpDate() {
  const mm = expMonthInput.value || '00';
  const yy = expYearInput.value || '00';
  cardExpDisplay.textContent = `${mm}/${yy}`;
}

cvcInput.addEventListener('input', () => {
  cardCvcDisplay.textContent = cvcInput.value || '000';
});


confirmButton.addEventListener('click', (e) => {
  e.preventDefault();
  const errors = [];

  if (!cardHolderInput.value.trim()) errors.push('Cardholder name is required.');
  if (!/^\d{16}$/.test(cardNumberInput.value.replace(/\s/g, ''))) errors.push('Card number must be 16 digits.');
  if (!/^\d{2}$/.test(expMonthInput.value)) errors.push('Expiration month must be 2 digits.');
  if (!/^\d{2}$/.test(expYearInput.value)) errors.push('Expiration year must be 2 digits.');
  if (!/^\d{3}$/.test(cvcInput.value)) errors.push('CVC must be 3 digits.');

  if (errors.length > 0) {
    alert('Please fix the following errors:\n' + errors.join('\n'));
  } else {
    alert('Card submitted successfully!');
  }
});


