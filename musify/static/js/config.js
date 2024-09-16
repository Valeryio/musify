
// Configure the share button
let shareBtn = document.querySelector(".header__cta");
let sharedLink = shareBtn.getAttribute("data-link")

shareBtn.addEventListener("click", (e) => {
  shareBtn.innerHTML = "Copied!";

  updateBtnStatus = setInterval(() => {
    shareBtn.innerHTML = "Share";
  }, 800);

  updateButton = clearInterval();
})


// async function to copuy content
const copyContent = async (content)  => {
  try {
    await navigator.clipboard.writeText(content);
  } catch (err) {
    console.error("Failed to copy!")
  }
}
