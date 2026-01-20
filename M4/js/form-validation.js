// ================================
// FORM VALIDATION WITH REGEX
// ================================

// Form and inputs
const form = document.getElementById('contactForm');

const nameInput = document.getElementById('name');
const phoneInput = document.getElementById('phone');
const emailInput = document.getElementById('email');
const messageInput = document.getElementById('message');

// Regex patterns
const nameRegex = /^[A-Za-zÀ-ÿ\s]{3,30}$/;
const phoneRegex = /^[0-9]{9}$/;
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// ================================
// VALIDATION FUNCTIONS
// ================================

function setValid(input) {
  const formGroup = input.parentElement;
  formGroup.classList.remove('invalid');
  formGroup.classList.add('valid');
}

function setInvalid(input) {
  const formGroup = input.parentElement;
  formGroup.classList.remove('valid');
  formGroup.classList.add('invalid');
}

function validateName() {
  if (nameRegex.test(nameInput.value.trim())) {
    setValid(nameInput);
    return true;
  } else {
    setInvalid(nameInput);
    return false;
  }
}

function validatePhone() {
  if (phoneRegex.test(phoneInput.value.trim())) {
    setValid(phoneInput);
    return true;
  } else {
    setInvalid(phoneInput);
    return false;
  }
}

function validateEmail() {
  if (emailRegex.test(emailInput.value.trim())) {
    setValid(emailInput);
    return true;
  } else {
    setInvalid(emailInput);
    return false;
  }
}

function validateMessage() {
  if (messageInput.value.trim().length >= 10) {
    setValid(messageInput);
    return true;
  } else {
    setInvalid(messageInput);
    return false;
  }
}

// ================================
// REAL-TIME VALIDATION
// ================================

nameInput.addEventListener('input', validateName);
phoneInput.addEventListener('input', validatePhone);
emailInput.addEventListener('input', validateEmail);
messageInput.addEventListener('input', validateMessage);

// ================================
// FORM SUBMIT
// ================================

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const isNameValid = validateName();
  const isPhoneValid = validatePhone();
  const isEmailValid = validateEmail();
  const isMessageValid = validateMessage();

  if (isNameValid && isPhoneValid && isEmailValid && isMessageValid) {
    alert('Formulari validat correctament');
    form.reset();

    document.querySelectorAll('.form-group').forEach(group => {
      group.classList.remove('valid');
    });
  }
});
