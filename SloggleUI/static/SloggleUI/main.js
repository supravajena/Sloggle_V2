function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

// for signup modal

const signupForm = document.getElementById("signupForm");
const hireFreelancerButton = document.getElementById("hireFreelancerButton");
const beFreelancerButton = document.getElementById("beFreelancerButton");
const signupCancelButton = document.getElementById("signupCancelButton");

hireFreelancerButton.addEventListener("click", function () {
  signupForm.classList.remove("d-none");
  hireFreelancerButton.classList.add("d-none");
  beFreelancerButton.classList.add("d-none");
});

beFreelancerButton.addEventListener("click", function () {
  signupForm.classList.remove("d-none");
  hireFreelancerButton.classList.add("d-none");
  beFreelancerButton.classList.add("d-none");
});

signupCancelButton.addEventListener("click", function() {
  signupForm.classList.add("d-none");
  hireFreelancerButton.classList.remove("d-none");
  beFreelancerButton.classList.remove("d-none");
});